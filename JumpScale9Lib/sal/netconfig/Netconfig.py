from js9 import j
import netaddr
import time

# MAYBE WE SHOULD STANDARDISE ON ARCH LINUX & USE SYSTEMDNETWORKING


class Netconfig:
    """
    Helps you to configure the network.
    """

    def __init__(self):
        self.__jslocation__ = "j.sal.netconfig"
        self.root = j.tools.path.get("/")
        self._executor = j.tools.executorLocal
        self._interfaceChanged = False
        self.log = j.logger.get("j.sal.netconfig")

    def chroot(self, root):
        """
        choose another root to manipulate the config files
        @param root str: new root path for config files.
        """
        self.root = j.tools.path.get(root)
        if not self.root.exists():
            raise j.exceptions.RuntimeError("Cannot find root for netconfig:%s" % root)
        # set base files
        for item in ["etc/network/interfaces", "etc/resolv.conf"]:
            j.sal.fs.touch(j.sal.fs.joinPaths(self.root, item))

    def interfaces_shutdown(self, excludes=[]):
        """
        find all interfaces and shut them all down with ifdown
        this is to remove all networking things going on
        @param excludes list: excluded interfaces.
        """
        excludes.append("lo")
        for nic in j.sal.nettools.getNics():
            if nic not in excludes:
                cmd = "ifdown %s --force" % nic
                print("shutdown:%s" % nic)
                self._executor.execute(cmd, die=False)

    def _getInterfacePath(self):
        path = j.sal.fs.joinPaths(self.root, "etc/network/interfaces")
        if not path.exists():
            raise j.exceptions.RuntimeError("Could not find network interface path: %s" % path)
        return path

    def _backup(self, path):
        path = j.tools.path.get(path)
        backuppath = path + ".backup"
        counter = 1
        while backuppath.exists():
            counter += 1
            backuppath = path + ".backup.%s" % counter
        path.copyfile(backuppath)

    def interfaces_reset(self, shutdown=False):
        """
        empty config of /etc/network/interfaces
        @param shutdown bool: shutsdown the network.
        """
        if shutdown:
            self.interfaces_shutdown()
        path = j.tools.path.get(self._getInterfacePath())
        self._backup(path)
        path.write_text("auto lo\n\n")

    def interface_remove(self, dev, apply=True):
        """
        Remove an interface.
        """
        path = self._getInterfacePath()
        ed = j.tools.code.getTextFileEditor(path)
        ed.removeSection(dev)

        if apply:
            self.interfaces_apply()

    # TODO: need to check this works
    def interface_remove_ipaddr(self, network="192.168.1"):
        for item in j.sal.nettools.getNetworkInfo():
            for ip in item["ip"]:
                if ip.startswith(network):
                    # remove ip addr from this interface
                    cmd = "ip addr flush dev %s" % item["name"]
                    print(cmd)
                    j.sal.process.execute(cmd)

    def nameserver_set(self, addr):
        """
        Set nameserver
        @param addr string: nameserver address.
        resolvconf will be disabled
        """
        cmd = "resolvconf --disable-updates"
        self._executor.execute(cmd)
        C = "nameserver %s\n" % addr
        path = self.root.joinpath("etc/resolv.conf")
        if not path.exists():
            raise j.exceptions.RuntimeError("Could not find resolv.conf path: '%s'" % path)
        path.write_text(C)

    def hostname_set(self, hostname):
        """
        change hostname
        @param hostname str: new hostname.
        """
        hostnameFile = j.tools.path.get('/etc/hostname')
        hostnameFile.write_text(hostname, append=False)
        cmd = 'hostname %s' % hostname
        self._executor.execute(cmd)

    def interface_configure_dhcp(self, dev="eth0", apply=True):
        """
        Configure interface to use dhcp
        @param dev str: interface name.
        """
        return self.interface_configure(dev=dev, dhcp=True, apply=apply)

    def interface_configure_dhcp_bridge(self, dev="eth0", bridgedev=None, apply=True):
        return self.interface_configure(dev=dev, dhcp=True, apply=apply, bridgedev=bridgedev)

    def interface_configure(self, dev, ipaddr=None, bridgedev=None, gw=None, dhcp=False, apply=True):
        """
        ipaddr in form of 192.168.10.2/24 (can be list)
        gateway in form of 192.168.10.254
        """
        if dhcp:
            C = """
            auto $int
            iface $int inet dhcp
            """

        else:
            C = """
            auto $int
            iface $int inet static

            """
        C = j.data.text.strip(C)

        if bridgedev is not None:
            C += "    bridge_fd 0\n"
            C += "    bridge_maxwait 0\n"

        if ipaddr is not None:
            if dhcp:
                raise j.exceptions.RuntimeError("cannot specify ipaddr & dhcp")
            C += "    address $ip\n"
            C += "    netmask $mask\n"
            C += "    network $net\n"
        else:
            C = C.replace("static", "manual")

        if bridgedev is not None:
            C += "       bridge_ports %s\n" % bridgedev
        # else:
        #     C+="       bridge_ports none\n"

        if gw is not None:
            C += "       gateway %s" % gw

        #         future="""
        #        #broadcast <broadcast IP here, e.g. 192.168.1.255>
        #        # dns-* options are implemented by the resolvconf package, if installed
        #        #dns-nameservers <name server IP address here, e.g. 192.168.1.1>
        #        #dns-search your.search.domain.here

        # """

        path = self._getInterfacePath()
        ed = j.tools.code.getTextFileEditor(path)
        ed.setSection(dev, C)

        ip = netaddr.IPNetwork(ipaddr)
        C = C.replace("$ip", str(ip.ip))
        C = C.replace("$mask", str(ip.netmask))
        C = C.replace("$net", str(ip.network))

        C = C.replace("$int", dev)

        path = self._getInterfacePath()
        ed = j.tools.code.getTextFileEditor(path)
        ed.setSection(dev, C)

        if apply:
            self.interfaces_restart(dev)
            if dhcp:
                print("refresh dhcp")
                self._executor.execute("dhclient %s" % dev)

    # def interface_configure_bridge(self,dev,bridgedev,apply=False):
    #     self.enableInterfaceBridge(dev=dev,bridgedev=bridgedev,apply=apply)

    def interfaces_restart(self, dev=None):
        """
        Restart an interface
        @param dev str: interface name.
        """
        if dev is None:
            for nic in j.sal.nettools.getNics():
                cmd = "ifdown %s --force" % nic
                print("shutdown:%s" % nic)
                self._executor.execute(cmd, die=False)
        else:
            self.logger.info("restart:%s" % dev)
            cmd = "ifdown %s" % dev
            self._executor.execute(cmd)
            cmd = "ifup %s" % dev
            self._executor.execute(cmd)

    def proxy_enable(self):
        maincfg = j.config.getConfig('main')
        if 'proxy' in maincfg:
            import os
            import urllib.request
            import urllib.error
            import urllib.parse
            proxycfg = maincfg['proxy']
            proxyserver = proxycfg['server']
            params = ""
            proxyuser = proxycfg.get('user')
            if proxyuser:
                params += proxyuser
                proxypassword = proxycfg.get('password')
                if proxypassword:
                    params += ":%s" % proxypassword
                params += "@"
            params += proxyserver
            if j.core.platformtype.myplatform.isunix:
                os.environ['http_proxy'] = proxyserver
            proxy_support = urllib.request.ProxyHandler()
            opener = urllib.request.build_opener(proxy_support)
            urllib.request.install_opener(opener)

    def interface_remove_ipaddr(self, network="192.168.1"):
        for item in j.sal.nettools.getNetworkInfo():
            for ip in item["ip"]:
                if ip.startswith(network):
                    # remove ip addr from this interface
                    cmd = "ip addr flush dev %s" % item["name"]
                    print(cmd)
                    j.sal.process.execute(cmd)

    def interface_configure_dhcp_waitdown(self, interface="eth0", ipaddr=None, gw=None, mask=24, config=True):
        """
        Bringing all bridges down and set specified interface with an IP address or on dhcp if no IP address, is provided
        @param config if True then will be stored in linux configuration files
        """
        import pynetlinux

        j.sal.netconfig.interfaces_reset(True)

        if ipaddr is None or gw is None:
            raise j.exceptions.Input("Cannot configure network when ipaddr or gw not specified", "net.config")

        if pynetlinux.brctl.findbridge("brpub") is not None:
            print("found brpub, will try to bring down.")
            i = pynetlinux.brctl.findbridge("brpub")
            i.down()
            counter = 0
            while i.is_up() and counter < 10:
                i.down()
                time.sleep(1)
                counter += 1
                print("waiting for bridge:brpub to go down")

        i = pynetlinux.ifconfig.findif(interface)
        if i is not None:
            print("found %s, will try to bring down." % interface)
            i.down()
            counter = 0
            while i.is_up() and counter < 10:
                i.down()
                time.sleep(1)
                counter += 1
                print("waiting for interface:%s to go down" % interface)

        print("set ipaddr:%s" % ipaddr)
        i.set_ip(ipaddr)
        print("set mask:%s" % mask)
        i.set_netmask(mask)
        print("bring interface up")
        i.up()

        while i.is_up() is False:
            i.up()
            time.sleep(1)
            print("waiting for interface:%s to go up" % interface)

        print("interface:%s up" % interface)

        print("check can reach default gw:%s" % gw)
        if not j.sal.nettools.pingMachine(gw):
            j.events.opserror_critical(
                "Cannot get to default gw, network configuration did not succeed for %s %s/%s -> %s" %
                (interface, ipaddr, mask, gw))
        print("gw reachable")

        self.resetDefaultGateway(gw)
        print("default gw up:%s" % gw)

    def interface_configure_dhcp_waitdown2(self, interface="eth0"):
        """
        this will bring all bridges down and set specified interface on dhcp (dangerous)
        """
        # @TODO:
        #     QUESTION why 2 functions almost the same, very confusing
        import pynetlinux

        self.reset(True)

        for br in pynetlinux.brctl.list_bridges():
            counter = 0
            while br.is_up() and counter < 10:
                br.down()
                time.sleep(1)
                counter += 1
                print("waiting for bridge:%s to go down" % br.name)

        i = pynetlinux.ifconfig.findif(interface)
        if i is not None:
            print("found %s, will try to bring down." % interface)
            i.down()
            counter = 0
            while i.is_up() and counter < 10:
                i.down()
                time.sleep(1)
                counter += 1
                print("waiting for interface:%s to go down" % interface)

            cmd = "ip addr flush dev %s" % interface
            j.sal.process.execute(cmd)

        self.interface_configure_dhcp(dev=interface, apply=True)

        print("check interface up")
        while i.is_up() is False:
            i.up()
            time.sleep(1)
            print("waiting for interface:%s to go up" % interface)

        print("interface:%s up" % interface)

        print("check can reach 8.8.8.8")
        if not j.sal.nettools.pingMachine("8.8.8.8"):
            j.events.opserror_critical(
                "Cannot get to public dns, network configuration did not succeed for %s (dhcp)" % (interface))
        print("8.8.8.8 reachable")
        print("network config done.")

    def interface_configure_bridge_safe(self, interface=None, ipaddr=None, gw=None, mask=None):
        """
        will in a safe way configure bridge brpub
        if available and has ip addr to go to internet then nothing will happen
        otherwise system will try in a safe way set this ipaddr, this is a dangerous operation

        if ipaddr is None then will look for existing config on interface and use that one to configure the bridge
        """
        import pynetlinux
        if ipaddr is None or mask is None or interface is None:
            print("get default network config for main interface")
            interface2, ipaddr2 = self.getDefaultIPConfig()
            if interface is None:
                interface = str(interface2)
                print("interface found:%s" % interface)
            if ipaddr is None:
                ipaddr = ipaddr2
                print("ipaddr found:%s" % ipaddr)

        if interface == "brpub":
            gw = pynetlinux.route.get_default_gw()
            if not j.sal.nettools.pingMachine(gw, pingtimeout=2):
                raise j.exceptions.RuntimeError(
                    "cannot continue to execute on bridgeConfigResetPub, gw was not reachable.")
            # this means the default found interface is already brpub, so can leave here
            return

        i = pynetlinux.ifconfig.Interface(interface)

        try:
            i.mac
        except IOError as e:
            if e.errno == 19:
                raise j.exceptions.RuntimeError("Did not find interface: %s" % interface)
            else:
                raise

        if ipaddr is None:
            raise j.exceptions.RuntimeError("Did not find ipaddr: %s" % ipaddr)

        if mask is None:
            mask = i.get_netmask()
            print("mask found:%s" % mask)

        if gw is None:
            gw = pynetlinux.route.get_default_gw()
            print("gw found:%s" % gw)

        if gw is None:
            raise j.exceptions.RuntimeError("Did not find gw: %s" % gw)

        if not j.sal.nettools.pingMachine(gw, pingtimeout=2):
            raise j.exceptions.RuntimeError("cannot continue to execute on bridgeConfigResetPub, gw was not reachable.")
        print("gw can be reached")

        if self.bridgeExists("brpub"):
            br = pynetlinux.brctl.findbridge("brpub")
            br.down()
            cmd = "brctl delbr brpub"
            j.sal.process.execute(cmd)

        try:
            import netaddr
            n = netaddr.IPNetwork("%s/%s" % (ipaddr, mask))
            self.removeNetworkFromInterfaces(str(n.network.ipv4()))

            # bring all other brdiges down
            for br in pynetlinux.brctl.list_bridges():
                counter = 0
                while br.is_up() and counter < 10:
                    br.down()
                    time.sleep(1)
                    counter += 1
                    print("waiting for bridge:%s to go down" % br.name)

            # bring own interface down
            i = pynetlinux.ifconfig.findif(interface)
            if i is not None:
                print("found %s, will try to bring down." % interface)
                i.down()
                counter = 0
                while i.is_up() and counter < 10:
                    i.down()
                    time.sleep(1)
                    counter += 1
                    print("waiting for interface:%s to go down" % interface)

                cmd = "ip addr flush dev %s" % interface
                j.sal.process.execute(cmd)

            j.sal.process.execute("sudo stop network-manager", showout=False, die=False)
            j.sal.fs.writeFile("/etc/init/network-manager.override", "manual")

            j.sal.netconfig.interfaces_reset()

            j.sal.netconfig.nameserver_set("8.8.8.8")

        except Exception as e:
            print("error in bridgeConfigResetPub:'%s'" % e)

        return interface, ipaddr, mask, gw
