# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

"""
Auto-generated class for ServiceFilter
"""

from . import client_support
from js9 import j
JSBASE = j.application.jsbase_get_class()


class ServiceFilter(object, JSBASE):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :rtype: ServiceFilter
        """

        return ServiceFilter(**kwargs)

    def __init__(self, json=None, **kwargs):
        JSBASE.__init__(self)
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'ServiceFilter'
        data = json or kwargs

        # set attributes

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
