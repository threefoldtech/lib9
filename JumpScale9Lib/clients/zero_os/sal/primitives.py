from js9 import j
from .VM import VM, ZeroOSVM, ZDBDisk


BASEFLIST = 'https://hub.gig.tech/gig-bootable/{}.flist'
ZEROOSFLIST = "https://hub.gig.tech/gig-bootable/zero-os-bootable.flist"

class Primitives:
    def __init__(self, node):
        self.node = node

    def create_virtual_machine(self, name, type_):
        """
        Create virtual machine

        :param name: Name of virtual machine
        :type name: str
        :param type_: Type of vm this defines the template to be used check 
                      https://hub.gig.tech/gig-bootable

                      eg: ubuntu:16.04, zero-os:master
        """
        templatename, _, version = type_.partition(':')
        kwargs = {'name': name, 'node': self.node}
        if templatename == 'zero-os':
            version = version or 'master'
            ipxeurl = 'https://bootstrap.gig.tech/ipxe/{}/0/development'.format(version)
            klass = ZeroOSVM
            kwargs['flist'] = ZEROOSFLIST
            kwargs['ipxe_url'] = ipxeurl
        elif templatename == 'ubuntu':
            version = version or 'lts'
            flistname = '{}:{}'.format(templatename, version)
            kwargs['flist'] = BASEFLIST.format(flistname)
            klass = VM
        else:
            raise RuntimeError('Invalid VM type {}'.format(type_))
        return klass(**kwargs)

    def create_disk(self, name, zdb, mountpoint=None, filesystem='ext4', size=10):
        """
        Create a disk on zdb and create filesystem

        :param name: Name of the disk/namespace in zdb
        :type name: str
        :param zdb: zerodb sal object
        :type zerodb ZeroDB sal object
        :param filesystem: Filesystem to create on the disk
        :type filesystem: str
        :param size: Size of the disk in GiB
        :type size: int
        """
        return ZDBDisk(zdb, name, mountpoint, filesystem, size)

    def create_gateway(self, name):
        """
        Create gateway object

        To deploy gatewy invoke .deploy method

        :param name: Name of the gateway
        :type name: str
        :return: Gateway object
        :rtype: Gateway object
        """
        return self.node.gateways.get(name)

    def drop_gateway(self, name):
        """
        Drop/delete a gateway

        :param name: Name of the gateway
        :type name: str
        """
        self.node.gateways.get(name).stop()

    def drop_virtual_machine(self, name):
        """
        Drop/delete a virtual machine

        :param name: Name of the vm
        :type name: str
        """
        self.node.hypervisor.get(name).destroy()

    def create_zerodb(self, name, path=None, mode='user', sync=False, admin='', node_port=9900):
        """
        Create zerodb object

        To deploy zerodb invoke .deploy method

        :param name: Name of the zerodb
        :type name: str
        :param path: path zerodb stores data on
        :type path: str
        :param mode: zerodb running mode
        :type mode: str
        :param sync: zerodb sync
        :type sync: bool
        :param admin: zerodb admin password
        :type admin: str

        :return: Zerodb object
        :rtype: Zerodb object
        """
        return self.node.zerodbs.create(name, path=path, mode=mode, sync=sync, admin=admin, node_port=node_port)

    def drop_zerodb(self, name):
        """
        Drop/delete a zerodb

        :param name: Name of the zerodb
        :type name: str
        """
        self.node.zerodbs.get(name).stop()

    def from_json(self, type_, json):
        """
        Load primitive from json string

        :param type_: Type of primitive
        :type type_: str
        :param json: json string
        :type json: str
        :return: primitive object
        :rtype: mixed
        """
        data = j.data.serializer.json.loads(json)
        return self.from_dict(type_, data)

    def from_dict(self, type_, data):
        """
        Load primitive from data dict

        :param type_: Type of primitive
        :type type_: str
        :param data: dict object
        :type data: dict
        :return: primitive object
        :rtype: mixed
        """
        if type_ == 'gateway':
            gw = self.create_gateway(data['hostname'])
            gw.from_dict(data)
            return gw
        elif type_ == 'vm':
            if data.get('ipxeUrl'):
                vm = ZeroOSVM(self.node, data['name'])
            else:
                vm = VM(self.node, data['name'])
            vm.from_dict(data)
            return vm
        elif type_ == 'zerodb':
            zdb = self.create_zerodb(data['name'])
            zdb.from_dict(data)
            return zdb
        raise RuntimeError('Unkown type {}, supported types are gateway, vm and zerodb'.format(type_))
