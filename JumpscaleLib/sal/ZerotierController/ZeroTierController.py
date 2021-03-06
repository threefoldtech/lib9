from Jumpscale import j
import json
import requests
import netaddr

BASE_API = "http://127.0.0.1:9993"

# ZT EtherType constants as defined here: https://github.com/zerotier/ZeroTierOne/blob/master/node/Constants.hpp
ZT_ETHERTYPE_IPV4 = "0x0800"
ZT_ETHERTYPE_ARP = "0x0806"
ZT_ETHERTYPE_IPV6 = "0x86dd"
RULES = [
    {
        "etherType": int(ZT_ETHERTYPE_IPV4, 16),
        "not": True,
        "or": False,
        "type": "MATCH_ETHERTYPE",
    },
    {
        "etherType": int(ZT_ETHERTYPE_IPV6, 16),
        "not": True,
        "or": False,
        "type": "MATCH_ETHERTYPE",
    },
    {
        "etherType": int(ZT_ETHERTYPE_ARP, 16),
        "not": True,
        "or": False,
        "type": "MATCH_ETHERTYPE",
    },
    {"not": False, "or": False, "type": "ACTION_DROP"},
    {"not": False, "or": False, "type": "ACTION_ACCEPT"},
]


class APIError(Exception):
    def __init__(self, req):
        self.req = req

    @property
    def code(self):
        return self.req.status_code


class ZeroTierController:
    def __init__(self):
        self.__jslocation__ = "j.sal.zerotier_Controller"
        self.controller_status()

    def get_filepath(self):
        """Get filepath """
        return "/var/lib/zerotier-one"

    def _request(self, url, payload=None, method="get"):
        """Simple request wrapper
        Takes a couple of variables and wraps around the requests
        module
        Args:
            url: API URL
            method: Query method (default: {"get"})
            payload: JSON payload (default: {None})
        Returns:
            Dataset as result from query
            JSON Object
        """
        header = {"X-ZT1-Auth": self.auth_token}
        req = None
        if payload is not None:
            req = requests.post(BASE_API + url, headers=header, json=payload)
        elif method == "get":
            req = requests.get(BASE_API + url, headers=header)
        elif method == "delete":
            req = requests.delete(BASE_API + url, headers=header)

        if req.status_code == 200:
            return req.json()
        else:
            raise APIError(req)

    def controller_status(self):
        return self._request("/controller", {})

    @property
    def auth_token(self):
        """gets authentication 
        Automatically detect system and reads authtoken.secret
        to set authenticaiton headers used in request method
        """
        pubsecret = self.get_filepath() + "/authtoken.secret"
        with open(pubsecret, "r") as f:
            authtoken = f.read().strip()
        return authtoken

    @property
    def public_id(self):
        """gets public id 
        Automatically detect system and reads identity.public
        """
        with open(self.get_filepath() + "/identity.public", "r") as f:
            network_id = f.read().split(":")[0]
        return network_id

    def network_add(self, name, start_ip, end_ip, mask, private=True):
        """
        that generate network id  doesn't exist in the worldmap using your public id

        Arguments:
            name {string} -- A short name for the network
            start_ip {string} -- Starting IP address in range e.g. "10.136.0.10"
            end_ip {sring} -- Ending IP address in range e.g. "10.136.0.250" 
            mask {string} -- mask of the network e.g. "255.255.255.0"

        Keyword Arguments:
            private {boolean} -- make the network private or not using ( True or False ) (default: {True})

        Returns:
            [Json] -- your network id that generated 
        """

        cidr = netaddr.IPAddress(mask).netmask_bits()
        ip = netaddr.IPNetwork("{}/{}".format(start_ip, cidr))
        target = str(ip.cidr)
        url = "/controller/network/%s______?auth=%s" % (self.public_id, self.auth_token)

        ipAssignmentPools = [{"ipRangeStart": start_ip, "ipRangeEnd": end_ip}]
        routes = [{"target": target}]
        v4AssignMode = {"zt": True}

        return self._request(
            url,
            {
                "name": name,
                "ipAssignmentPools": ipAssignmentPools,
                "routes": routes,
                "v4AssignMode": v4AssignMode,
                "private": private,
                "rules": RULES,
            },
        )

    def network_delete(self, network_id):
        """
        delete the network_id
        """
        return self._request("/controller/network/" + network_id, method="delete")

    def network_info(self, network_id):
        """
        retutrn network info of spesific id
        """
        return self._request("/controller/network/" + network_id)

    def networks_list(self):
        """
        return all networks
        """

        return self._request("/controller/network")

    def member_authorize(self, network_id, zt_id):
        """
        authorize zt_id in your network_id
        """
        return self._request(
            "/controller/network/" + network_id + "/member/" + zt_id,
            {"authorized": "true"},
        )

    def member_deauthorize(self, network_id, zt_id):

        return self._request(
            "/controller/network/" + network_id + "/member/" + zt_id,
            {"authorized": "false"},
        )

    def member_list(self, network_id):
        ztids = self._request("/controller/network/" + network_id + "/member")
        return ztids

    def member_delete(self, network_id, zt_id):
        return self._request(
            "/controller/network/" + network_id + "/member/" + zt_id, method="delete"
        )

    def member_active_list(self, network_id):
        ztids = self._request("/controller/network/" + network_id + "/active")
        return ztids
