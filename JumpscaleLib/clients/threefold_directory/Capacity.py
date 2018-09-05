# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

"""
Auto-generated class for Capacity
"""
from .Location import Location
from .ResourceUnits import ResourceUnits
from .client_support import Timestamp
from datetime import datetime
from six import string_types

from . import client_support


class Capacity(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type farmer_id: string_types
        :type location: Location
        :type node_id: string_types
        :type os_version: string_types
        :type reserved_resources: ResourceUnits
        :type robot_address: string_types
        :type total_resources: ResourceUnits
        :type uptime: int
        :type used_resources: ResourceUnits
        :rtype: Capacity
        """

        return Capacity(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Capacity'
        data = json or kwargs

        # set attributes
        data_types = [string_types]
        self.farmer_id = client_support.set_property('farmer_id', data, data_types, False, [], False, False, class_name)
        data_types = [Location]
        self.location = client_support.set_property('location', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.node_id = client_support.set_property('node_id', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.os_version = client_support.set_property(
            'os_version', data, data_types, False, [], False, True, class_name)
        data_types = [ResourceUnits]
        self.reserved_resources = client_support.set_property(
            'reserved_resources', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.robot_address = client_support.set_property(
            'robot_address', data, data_types, False, [], False, True, class_name)
        data_types = [ResourceUnits]
        self.total_resources = client_support.set_property(
            'total_resources', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.uptime = client_support.set_property('uptime', data, data_types, False, [], False, False, class_name)
        data_types = [Timestamp]
        self.updated = client_support.set_property('updated', data, data_types, False, [], False, False, class_name)
        # data_types = [datetime]
        # self.updated = client_support.set_property('updated', data, data_types, False, [], False, False, class_name)
        data_types = [ResourceUnits]
        self.used_resources = client_support.set_property(
            'used_resources', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)