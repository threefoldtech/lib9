
from jumpscale import j
from pprint import pprint as print

from .ZdbConfig import ZdbConfig

JSConfigBase = j.tools.configmanager.base_class_configs


class ZdbConfigFactory(JSConfigBase):

    def __init__(self):
        self.__jslocation__ = "j.clients.zdb"
        JSConfigBase.__init__(self, ZdbConfig)
        self._tree = None

    def configure(self, instance="main", secrets="", addr="localhost", port=None,
                  adminsecret="", mode="user"):
        """

        :param instance:
        :param secrets: $ns:$secret,... or $secret which will be defaulf for all namespaces
        :param addr:
        :param port:
        :param adminsecret: the main secret
        :param mode: seq or user
        :return:
        """

        if port is None:
            raise ValueError("port cannot be None")

        data = {}
        data["addr"] = addr
        data["port"] = str(port)
        data["mode"] = str(mode)
        data["adminsecret_"] = adminsecret
        # is now multiple secrets or 1 default one, in future will be our own serializion lib (the schemas)
        data["secrets_"] = secrets
        return self.get(instance=instance, data=data)

    def testdb_server_start_client_get(self, reset=False, mode="seq"):
        """
        will start a ZDB server in tmux (will only start when not there yet or when reset asked for)
        erase all content
        and will return client to it

        """

        db = j.servers.zdb.configure(instance="test", adminsecret="123456", reset=reset, mode=mode)
        db.start()

        # if secrets only 1 secret then will be used for all namespaces
        cl = db.client_get(secrets="1234")
        return cl

    def test(self, reset=True):
        """
        js_shell 'j.clients.zdb.test(reset=True)'

        """

        cl = j.clients.zdb.testdb_server_start_client_get(reset=reset, mode="seq")

        cl1 = cl.namespace_new("test")
        cl1.test_seq()

        # TODO: *1 need to test the other modes as well
