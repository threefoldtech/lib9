import redis
import uuid
import json
import textwrap
import shlex
import base64
import signal
import socket
import logging
import time
import sys
from js9 import j

from .Client import *

class KvmManager:
    _iotune_dict = {
        'totalbytessecset': typchk.Or(bool, typchk.Missing()),
        'totalbytessec': typchk.Or(int, typchk.Missing()),
        'readbytessecset': typchk.Or(bool, typchk.Missing()),
        'readbytessec': typchk.Or(int, typchk.Missing()),
        'writebytessecset': typchk.Or(bool, typchk.Missing()),
        'writebytessec': typchk.Or(int, typchk.Missing()),
        'totaliopssecset': typchk.Or(bool, typchk.Missing()),
        'totaliopssec': typchk.Or(int, typchk.Missing()),
        'readiopssecset': typchk.Or(bool, typchk.Missing()),
        'readiopssec': typchk.Or(int, typchk.Missing()),
        'writeiopssecset': typchk.Or(bool, typchk.Missing()),
        'writeiopssec': typchk.Or(int, typchk.Missing()),
        'totalbytessecmaxset': typchk.Or(bool, typchk.Missing()),
        'totalbytessecmax': typchk.Or(int, typchk.Missing()),
        'readbytessecmaxset': typchk.Or(bool, typchk.Missing()),
        'readbytessecmax': typchk.Or(int, typchk.Missing()),
        'writebytessecmaxset': typchk.Or(bool, typchk.Missing()),
        'writebytessecmax': typchk.Or(int, typchk.Missing()),
        'totaliopssecmaxset': typchk.Or(bool, typchk.Missing()),
        'totaliopssecmax': typchk.Or(int, typchk.Missing()),
        'readiopssecmaxset': typchk.Or(bool, typchk.Missing()),
        'readiopssecmax': typchk.Or(int, typchk.Missing()),
        'writeiopssecmaxset': typchk.Or(bool, typchk.Missing()),
        'writeiopssecmax': typchk.Or(int, typchk.Missing()),
        'totalbytessecmaxlengthset': typchk.Or(bool, typchk.Missing()),
        'totalbytessecmaxlength': typchk.Or(int, typchk.Missing()),
        'readbytessecmaxlengthset': typchk.Or(bool, typchk.Missing()),
        'readbytessecmaxlength': typchk.Or(int, typchk.Missing()),
        'writebytessecmaxlengthset': typchk.Or(bool, typchk.Missing()),
        'writebytessecmaxlength': typchk.Or(int, typchk.Missing()),
        'totaliopssecmaxlengthset': typchk.Or(bool, typchk.Missing()),
        'totaliopssecmaxlength': typchk.Or(int, typchk.Missing()),
        'readiopssecmaxlengthset': typchk.Or(bool, typchk.Missing()),
        'readiopssecmaxlength': typchk.Or(int, typchk.Missing()),
        'writeiopssecmaxlengthset': typchk.Or(bool, typchk.Missing()),
        'writeiopssecmaxlength': typchk.Or(int, typchk.Missing()),
        'sizeiopssecset': typchk.Or(bool, typchk.Missing()),
        'sizeiopssec': typchk.Or(int, typchk.Missing()),
        'groupnameset': typchk.Or(bool, typchk.Missing()),
        'groupname': typchk.Or(str, typchk.Missing()),
    }
    _media_dict = {
        'type': typchk.Or(
            typchk.Enum('disk', 'cdrom'),
            typchk.Missing()
        ),
        'url': str,
        'iotune': typchk.Or(
            _iotune_dict,
            typchk.Missing()
        )
    }
    _create_chk = j.tools.typechecker.get({
        'name': str,
        'media': typchk.Or([_media_dict], typchk.IsNone()),
        'flist': typchk.Or(str, typchk.IsNone()),
        'cpu': int,
        'memory': int,
        'nics': [{
            'type': typchk.Enum('default', 'bridge', 'vxlan', 'vlan'),
            'id': typchk.Or(str, typchk.Missing()),
            'hwaddr': typchk.Or(str, typchk.Missing()),
        }],
        'port': typchk.Or(
            typchk.Map(int, int),
            typchk.IsNone()
        ),
        'mount': typchk.Or(
            [{'source': str, 'target': str, 'readonly': typchk.Or(bool, typchk.Missing())}],
            typchk.IsNone(),
        )
    })

    _migrate_network_chk = j.tools.typechecker.get({
        'nics': [{
            'type': typchk.Enum('default', 'bridge', 'vxlan', 'vlan'),
            'id': typchk.Or(str, typchk.Missing()),
            'hwaddr': typchk.Or(str, typchk.Missing()),
        }],
        'port': typchk.Or(
            typchk.Map(int, int),
            typchk.IsNone()
        ),
        'uuid': str
    })

    _domain_action_chk = j.tools.typechecker.get({
        'uuid': str,
    })

    _man_disk_action_chk = j.tools.typechecker.get({
        'uuid': str,
        'media': _media_dict,
    })

    _man_nic_action_chk = j.tools.typechecker.get({
        'uuid': str,
        'type': typchk.Enum('default', 'bridge', 'vxlan', 'vlan'),
        'id': typchk.Or(str, typchk.IsNone()),
        'hwaddr': typchk.Or(str, typchk.IsNone()),
    })

    _migrate_action_chk = j.tools.typechecker.get({
        'uuid': str,
        'desturi': str,
    })

    _limit_disk_io_dict = {
        'uuid': str,
        'media': _media_dict,
    }

    _limit_disk_io_dict.update(_iotune_dict)

    _limit_disk_io_action_chk = j.tools.typechecker.get(_limit_disk_io_dict)

    def __init__(self, client):
        self._client = client

    def create(self, name, media=None, flist=None, cpu=2, memory=512, nics=None, port=None, mount=None, tags=None):
        """
        :param name: Name of the kvm domain
        :param media: (optional) array of media objects to attach to the machine, where the first object is the boot device
                      each media object is a dict of {url, type} where type can be one of 'disk', or 'cdrom', or empty (default to disk)
                      example: [{'url': 'nbd+unix:///test?socket=/tmp/ndb.socket'}, {'type': 'cdrom': '/somefile.iso'}
        :param flist: (optional) VM flist. A special bootable flist witch has a correct boot.yaml file
                     example: http://hub.gig.tech/azmy/ubuntu-zesty.flist
        :param cpu: number of vcpu cores
        :param memory: memory in MiB
        :param port: A dict of host_port: container_port pairs
                       Example:
                        `port={8080: 80, 7000:7000}`
                     Only supported if default network is used
        :param nics: Configure the attached nics to the container
                     each nic object is a dict of the format
                     {
                        'type': nic_type # default, bridge, vlan, or vxlan (note, vlan and vxlan only supported by ovs)
                        'id': id # depends on the type, bridge name (bridge type) zerotier network id (zertier type), the vlan tag or the vxlan id
                     }
        :param port: Configure port forwards to vm, this only works if default network nic is added. Is a dict of {host-port: guest-port}
        :param mount: A list of host shared folders in the format {'source': '/host/path', 'target': '/guest/path', 'readonly': True|False}

        :note: At least one media or an flist must be provided.
        :return: uuid of the virtual machine
        """

        if nics is None:
            nics = []

        args = {
            'name': name,
            'media': media,
            'cpu': cpu,
            'flist': flist,
            'memory': memory,
            'nics': nics,
            'port': port,
            'mount': mount,
        }
        self._create_chk.check(args)

        if media is None and flist is None:
            raise ValueError('need at least one boot media via media or an flist')

        return self._client.sync('kvm.create', args, tags=tags)

    def prepare_migration_target(self, uuid, nics=None, port=None, tags=None):
        """
        :param name: Name of the kvm domain that will be migrated
        :param port: A dict of host_port: container_port pairs
                       Example:
                        `port={8080: 80, 7000:7000}`
                     Only supported if default network is used
        :param nics: Configure the attached nics to the container
                     each nic object is a dict of the format
                     {
                        'type': nic_type # default, bridge, vlan, or vxlan (note, vlan and vxlan only supported by ovs)
                        'id': id # depends on the type, bridge name (bridge type) zerotier network id (zertier type), the vlan tag or the vxlan id
                     }
        :param uuid: uuid of machine to be migrated on old node
        :return:
        """

        if nics is None:
            nics = []

        args = {
            'nics': nics,
            'port': port,
            'uuid': uuid
        }
        self._migrate_network_chk.check(args)

        self._client.sync('kvm.prepare_migration_target', args, tags=tags)

    def destroy(self, uuid):
        """
        Destroy a kvm domain by uuid
        :param uuid: uuid of the kvm container (same as the used in create)
        :return:
        """
        args = {
            'uuid': uuid,
        }
        self._domain_action_chk.check(args)

        self._client.sync('kvm.destroy', args)

    def shutdown(self, uuid):
        """
        Shutdown a kvm domain by uuid
        :param uuid: uuid of the kvm container (same as the used in create)
        :return:
        """
        args = {
            'uuid': uuid,
        }
        self._domain_action_chk.check(args)

        self._client.sync('kvm.shutdown', args)

    def reboot(self, uuid):
        """
        Reboot a kvm domain by uuid
        :param uuid: uuid of the kvm container (same as the used in create)
        :return:
        """
        args = {
            'uuid': uuid,
        }
        self._domain_action_chk.check(args)

        self._client.sync('kvm.reboot', args)

    def reset(self, uuid):
        """
        Reset (Force reboot) a kvm domain by uuid
        :param uuid: uuid of the kvm container (same as the used in create)
        :return:
        """
        args = {
            'uuid': uuid,
        }
        self._domain_action_chk.check(args)

        self._client.sync('kvm.reset', args)

    def pause(self, uuid):
        """
        Pause a kvm domain by uuid
        :param uuid: uuid of the kvm container (same as the used in create)
        :return:
        """
        args = {
            'uuid': uuid,
        }
        self._domain_action_chk.check(args)

        self._client.sync('kvm.pause', args)

    def resume(self, uuid):
        """
        Resume a kvm domain by uuid
        :param uuid: uuid of the kvm container (same as the used in create)
        :return:
        """
        args = {
            'uuid': uuid,
        }
        self._domain_action_chk.check(args)

        self._client.sync('kvm.resume', args)

    def info(self, uuid):
        """
        Get info about a kvm domain by uuid
        :param uuid: uuid of the kvm container (same as the used in create)
        :return:
        """
        args = {
            'uuid': uuid,
        }
        self._domain_action_chk.check(args)

        return self._client.json('kvm.info', args)

    def infops(self, uuid):
        """
        Get info per second about a kvm domain by uuid
        :param uuid: uuid of the kvm container (same as the used in create)
        :return:
        """
        args = {
            'uuid': uuid,
        }
        self._domain_action_chk.check(args)

        return self._client.json('kvm.infops', args)

    def attach_disk(self, uuid, media):
        """
        Attach a disk to a machine
        :param uuid: uuid of the kvm container (same as the used in create)
        :param media: the media object to attach to the machine
                      media object is a dict of {url, and type} where type can be one of 'disk', or 'cdrom', or empty (default to disk)
                      examples: {'url': 'nbd+unix:///test?socket=/tmp/ndb.socket'}, {'type': 'cdrom': '/somefile.iso'}
        :return:
        """
        args = {
            'uuid': uuid,
            'media': media,
        }
        self._man_disk_action_chk.check(args)

        self._client.sync('kvm.attach_disk', args)

    def detach_disk(self, uuid, media):
        """
        Detach a disk from a machine
        :param uuid: uuid of the kvm container (same as the used in create)
        :param media: the media object to attach to the machine
                      media object is a dict of {url, and type} where type can be one of 'disk', or 'cdrom', or empty (default to disk)
                      examples: {'url': 'nbd+unix:///test?socket=/tmp/ndb.socket'}, {'type': 'cdrom': '/somefile.iso'}
        :return:
        """
        args = {
            'uuid': uuid,
            'media': media,
        }
        self._man_disk_action_chk.check(args)

        self._client.sync('kvm.detach_disk', args)

    def add_nic(self, uuid, type, id=None, hwaddr=None):
        """
        Add a nic to a machine
        :param uuid: uuid of the kvm container (same as the used in create)
        :param type: nic_type # default, bridge, vlan, or vxlan (note, vlan and vxlan only supported by ovs)
         param id: id # depends on the type, bridge name (bridge type) zerotier network id (zertier type), the vlan tag or the vxlan id
         param hwaddr: the hardware address of the nic
        :return:
        """
        args = {
            'uuid': uuid,
            'type': type,
            'id': id,
            'hwaddr': hwaddr,
        }
        self._man_nic_action_chk.check(args)

        return self._client.json('kvm.add_nic', args)

    def remove_nic(self, uuid, type, id=None, hwaddr=None):
        """
        Remove a nic from a machine
        :param uuid: uuid of the kvm container (same as the used in create)
        :param type: nic_type # default, bridge, vlan, or vxlan (note, vlan and vxlan only supported by ovs)
         param id: id # depends on the type, bridge name (bridge type) zerotier network id (zertier type), the vlan tag or the vxlan id
         param hwaddr: the hardware address of the nic
        :return:
        """
        args = {
            'uuid': uuid,
            'type': type,
            'id': id,
            'hwaddr': hwaddr,
        }
        self._man_nic_action_chk.check(args)

        return self._client.json('kvm.remove_nic', args)

    def limit_disk_io(self, uuid, media, totalbytessecset=False, totalbytessec=0, readbytessecset=False, readbytessec=0, writebytessecset=False,
                      writebytessec=0, totaliopssecset=False, totaliopssec=0, readiopssecset=False, readiopssec=0, writeiopssecset=False, writeiopssec=0,
                      totalbytessecmaxset=False, totalbytessecmax=0, readbytessecmaxset=False, readbytessecmax=0, writebytessecmaxset=False, writebytessecmax=0,
                      totaliopssecmaxset=False, totaliopssecmax=0, readiopssecmaxset=False, readiopssecmax=0, writeiopssecmaxset=False, writeiopssecmax=0,
                      totalbytessecmaxlengthset=False, totalbytessecmaxlength=0, readbytessecmaxlengthset=False, readbytessecmaxlength=0,
                      writebytessecmaxlengthset=False, writebytessecmaxlength=0, totaliopssecmaxlengthset=False, totaliopssecmaxlength=0,
                      readiopssecmaxlengthset=False, readiopssecmaxlength=0, writeiopssecmaxlengthset=False, writeiopssecmaxlength=0, sizeiopssecset=False,
                      sizeiopssec=0, groupnameset=False, groupname=''):
        """
        Remove a nic from a machine
        :param uuid: uuid of the kvm container (same as the used in create)
        :param media: the media to limit the diskio
        :return:
        """
        args = {
            'uuid': uuid,
            'media': media,
            'totalbytessecset': totalbytessecset,
            'totalbytessec': totalbytessec,
            'readbytessecset': readbytessecset,
            'readbytessec': readbytessec,
            'writebytessecset': writebytessecset,
            'writebytessec': writebytessec,
            'totaliopssecset': totaliopssecset,
            'totaliopssec': totaliopssec,
            'readiopssecset': readiopssecset,
            'readiopssec': readiopssec,
            'writeiopssecset': writeiopssecset,
            'writeiopssec': writeiopssec,
            'totalbytessecmaxset': totalbytessecmaxset,
            'totalbytessecmax': totalbytessecmax,
            'readbytessecmaxset': readbytessecmaxset,
            'readbytessecmax': readbytessecmax,
            'writebytessecmaxset': writebytessecmaxset,
            'writebytessecmax': writebytessecmax,
            'totaliopssecmaxset': totaliopssecmaxset,
            'totaliopssecmax': totaliopssecmax,
            'readiopssecmaxset': readiopssecmaxset,
            'readiopssecmax': readiopssecmax,
            'writeiopssecmaxset': writeiopssecmaxset,
            'writeiopssecmax': writeiopssecmax,
            'totalbytessecmaxlengthset': totalbytessecmaxlengthset,
            'totalbytessecmaxlength': totalbytessecmaxlength,
            'readbytessecmaxlengthset': readbytessecmaxlengthset,
            'readbytessecmaxlength': readbytessecmaxlength,
            'writebytessecmaxlengthset': writebytessecmaxlengthset,
            'writebytessecmaxlength': writebytessecmaxlength,
            'totaliopssecmaxlengthset': totaliopssecmaxlengthset,
            'totaliopssecmaxlength': totaliopssecmaxlength,
            'readiopssecmaxlengthset': readiopssecmaxlengthset,
            'readiopssecmaxlength': readiopssecmaxlength,
            'writeiopssecmaxlengthset': writeiopssecmaxlengthset,
            'writeiopssecmaxlength': writeiopssecmaxlength,
            'sizeiopssecset': sizeiopssecset,
            'sizeiopssec': sizeiopssec,
            'groupnameset': groupnameset,
            'groupname': groupname,
        }
        self._limit_disk_io_action_chk.check(args)

        self._client.sync('kvm.limit_disk_io', args)

    def migrate(self, uuid, desturi):
        """
        Migrate a vm to another node
        :param uuid: uuid of the kvm container (same as the used in create)
        :param desturi: the uri of the destination node
        :return:
        """
        args = {
            'uuid': uuid,
            'desturi': desturi,
        }
        self._migrate_action_chk.check(args)

        self._client.sync('kvm.migrate', args)

    def list(self):
        """
        List configured domains

        :return:
        """
        return self._client.json('kvm.list', {})

