from .grafana import Grafana
from jumpscale import j
# import JumpscaleLib.baselib.remote

JSBASE = j.application.jsbase_get_class()


class GrafanaFactory(JSBASE):

    def __init__(self):
        self.__jslocation__ = "j.zos_sal.grafana"
        JSBASE.__init__(self)

    def get(self, container, ip, port, url):
        """
        Get sal for Grafana

        Returns:
            the sal layer 
        """
        return Grafana(container, ip, port, url)
