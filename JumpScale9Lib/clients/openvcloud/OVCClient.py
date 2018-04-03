import time
import jwt
import jose.jwt
from paramiko.ssh_exception import BadAuthenticationType
from js9 import j

from .Account import Account
from .Machine import Machine
from .Space import Space

# NEED: pip3 install python-jose


TEMPLATE = """
address = ""
port = 443
jwt_ = ""
location = ""
account = ""
space = ""
"""

# appkey_ = ""


JSConfigBase = j.tools.configmanager.base_class_config


class OVCClient(JSConfigBase):

    def __init__(self, instance, data=None, parent=None, interactive=False):
        if not data:
            data = {}

        JSConfigBase.__init__(self, instance=instance, data=data, parent=parent,
                              template=TEMPLATE, interactive=interactive)
        self._api = None
        self._jwt_expire_timestamp = None

        if not self.config.data.get("location"):
            if len(self.locations) == 1:
                self.config.data_set("location", self.locations[0]["locationCode"])
                self.config.save()

    def jwt_refresh(self):
        '''
        Refresh jwt token is expired or expires within 300s
        '''

        if not self._jwt_expire_timestamp and self.config.data.get('jwt_'):
            #means there is a jwt token specified, need to see if it did not expire yet
            self._jwt_expire_timestamp = j.clients.itsyouonline.jwt_expire_timestamp(self.config.data['jwt_'])

        if self._jwt_expire_timestamp and self._jwt_expire_timestamp - 300 < time.time():
            if j.tools.configmanager.sandbox_check():
                if j.tools.configmanager.interactive:
                    print("Get your jwt client (in another shell, not in this sandbox)")
                    print("DO:  js9 'print(j.clients.itsyouonline.default.jwt)'")
                    jwt=j.tools.console.askString("give your jwt code, you got from the other shell:")
                    self.config.data_set('jwt_', jwt)
                    self.config.save()
                    self._jwt_expire_timestamp = j.clients.itsyouonline.jwt_expire_timestamp(jwt)
                    return
                raise j.exceptions.Input("please refresh your jwt token in your openvcloud config.\n")
            token = j.clients.itsyouonline.refresh_jwt_token(self.config.data['jwt_'], validity=3600)
            self.config.data_set('jwt_', token)
            self.config.save()
            self._jwt_expire_timestamp = j.clients.itsyouonline.jwt_expire_timestamp(token)

    @property
    def api(self):
        self.jwt_refresh()

        if self._api is None:

            self._config_check()

            # before using api refresh jwt token if needed
            self.jwt_refresh()

            self._api = j.clients.portal.get(data={'ip': self.config.data.get("address"),
                                                   'port': self.config.data.get("port")}, interactive=False)
            # patch handle the case where the connection dies because of inactivity
            self.__patch_portal_client(self._api)
            self.__login()
            self._api.load_swagger(group='cloudapi')
        return self._api

    def _config_check(self):
        """
        check the configuration if not what you want the class will barf & show you where it went wrong
        """

        def urlClean(url):
            url = url.lower()
            url = url.strip()
            if url.startswith("http"):
                url = url.split("//")[1].rstrip("/")
            if "/" in url:
                url = url.split("/")[0]
            self.logger.info("Get OpenvCloud client on URL: %s" % url)
            return url

        self.config.data_set("address", urlClean(self.config.data["address"]))

        if self.config.data["address"].strip() == "":
            raise RuntimeError(
                "please specify address to OpenvCloud server (address) e.g. se-gen-1.demo.greenitglobe.com")

        if not self.config.data["jwt_"].strip():
            self.config.data = {"jwt_": j.clients.itsyouonline.default.jwt}


        # if not self.config.data.get("login"):
        #     raise RuntimeError("login cannot be empty")

    def __patch_portal_client(self, api):
        # try to relogin in the case the connection is dead because of
        # inactivity
        origcall = api.__call__

        def patch_call(that, *args, **kwargs):
            from JumpScale9Lib.clients.portal.PortalClient import ApiError
            try:
                return origcall(that, *args, **kwargs)
            except ApiError as e:
                if e.response.status_code == 419:
                    self.__login()
                    return origcall(that, *args, **kwargs)
                raise

        api.__call__ = patch_call

    def __login(self):
        jwt = self.config.data.get("jwt_")
        payload = jose.jwt.get_unverified_claims(jwt)
        # if payload['exp'] < time.time():
        #     j.clients.itsyouonline.reset()
        #     # Regenerate jwt after resetting the expired one
        #     self.config.data = {"jwt_": j.clients.itsyouonline.default.jwt}
        self.api._session.headers['Authorization'] = 'bearer {}'.format(jwt)
        self._login = '{}@{}'.format(payload['username'], payload['iss'])

    @property
    def accounts(self):
        ovc_accounts = self.api.cloudapi.accounts.list()
        accounts = list()
        for account in ovc_accounts:
            accounts.append(Account(self, account))
        return accounts

    @property
    def locations(self):
        return self.api.cloudapi.locations.list()

    def account_get(self, name="", create=True,
                    maxMemoryCapacity=-1, maxVDiskCapacity=-1, maxCPUCapacity=-1, maxNASCapacity=-1,
                    maxNetworkOptTransfer=-1, maxNetworkPeerTransfer=-1, maxNumPublicIP=-1):
        """
        Returns the OpenvCloud account with the given name, and in case it doesn't exist yet the account will be created.

        Args:
            - name (required): name of the account to lookup or create if it doesn't exist yet, e.g. "myaccount"
            - create (defaults to True): if set to True the account is created in case it doesn't exist yet
            - maxMemoryCapacity (defaults to -1: unlimited): available memory in GB for all virtual machines in the account
            - maxVDiskCapacity (defaults to -1: unlimited): available disk capacity in GiB for all virtual disks in the account
            - maxCPUCapacity (defaults to -1: unlimited): total number of available virtual CPU core that can be used by the virtual machines in the account
            - maxNASCapacity (defaults to -1: unlimited): not implemented
            - maxNetworkOptTransfer (defaults to -1: unlimited): not implemented
            - maxNetworkPeerTransfer (defaults to -1: unlimited): not implemented
            - maxNumPublicIP (defaults to -1: unlimited): number of external IP addresses that can be used in the account

        Raises: KeyError if account doesn't exist, and create argument was set to False
        """
        if name == "":
            name = self.config.data["account"]
        if not name:
            raise RuntimeError("name needs to be specified in account in config or on method.")
        for account in self.accounts:
            if account.model['name'] == name:
                return account
        else:
            if create is False:
                raise KeyError("No account with name \"%s\" found" % name)
            self.api.cloudbroker.account.create(username=self.login,
                                                name=name,
                                                maxMemoryCapacity=maxMemoryCapacity,
                                                maxVDiskCapacity=maxVDiskCapacity,
                                                maxCPUCapacity=maxCPUCapacity,
                                                maxNASCapacity=maxNASCapacity,
                                                maxNetworkOptTransfer=maxNetworkOptTransfer,
                                                maxNetworkPeerTransfer=maxNetworkPeerTransfer,
                                                maxNumPublicIP=maxNumPublicIP)
            return self.account_get(name, False)

    def space_get(self,
                  accountName="",
                  spaceName="",
                  location="",
                  createSpace=True,
                  maxMemoryCapacity=-1,
                  maxVDiskCapacity=-1,
                  maxCPUCapacity=-1,
                  maxNASCapacity=-1,
                  maxNetworkOptTransfer=-1,
                  maxNetworkPeerTransfer=-1,
                  maxNumPublicIP=-1,
                  externalnetworkId=None):
        """
        Returns the OpenvCloud space with the given account_name, space_name, space_location and in case the account doesn't exist yet it will be created.

        Args:
            - accountName (required): name of the account to lookup, e.g. "myaccount"
            - spaceName (required): name of the cloud space to lookup or create if it doesn't exist yet, e.g. "myvdc"
            - location (only required when cloud space needs to be created): location when the cloud space needs to be created
            - createSpace (defaults to True): if set to True the account is created in case it doesn't exist yet
            - maxMemoryCapacity (defaults to -1: unlimited): available memory in GB for all virtual machines in the cloud space
            - maxVDiskCapacity (defaults to -1: unlimited): available disk capacity in GiB for all virtual disks in the cloud space
            - maxCPUCapacity (defaults to -1: unlimited): total number of available virtual CPU core that can be used by the virtual machines in the cloud space
            - maxNASCapacity (defaults to -1: unlimited): not implemented
            - maxNetworkOptTransfer (defaults to -1: unlimited): not implemented
            - maxNetworkPeerTransfer (defaults to -1: unlimited): not implemented
            - maxNumPublicIP (defaults to -1: unlimited): number of external IP addresses that can be used in the cloud space
        """

        if location == "":
            location = self.config.data["location"]

        if spaceName == "":
            spaceName = self.config.data["space"]

        if not spaceName:
            raise RuntimeError("name needs to be specified in account in config or on method.")


        account = self.account_get(name=accountName, create=False)
        if account:
            return account.space_get(name=spaceName,
                                     create=createSpace,
                                     location=location,
                                     maxMemoryCapacity=maxMemoryCapacity,
                                     maxVDiskCapacity=maxVDiskCapacity,
                                     maxCPUCapacity=maxCPUCapacity,
                                     maxNASCapacity=maxNASCapacity,
                                     maxNetworkOptTransfer=maxNetworkOptTransfer,
                                     maxNetworkPeerTransfer=maxNetworkPeerTransfer,
                                     maxNumPublicIP=maxNumPublicIP,
                                     externalnetworkId=externalnetworkId
                                     )
        else:
            raise j.exceptions.RuntimeError(
                "Could not find account with name %s" % accountName)

    def get_available_images(self, cloudspaceId=None, accountId=None):
        """
        lists all available images for a cloud space

        Args:
            - cloudspaceId (optional): cloud space Id
            - accountId (optional): account Id
        """
        return self.api.cloudapi.images.list(cloudspaceId=cloudspaceId, accountId=accountId)

    @property
    def login(self):
        return self._login

    def __repr__(self):
        return "OpenvCloud client:\n%s" % self.config

    __str__ = __repr__
