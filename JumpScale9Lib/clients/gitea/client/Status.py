# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

"""
Auto-generated class for Status
"""
from .User import User
from datetime import datetime
from six import string_types

from . import client_support




class Status(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type context: string_types
        :type created_at: datetime
        :type creator: User
        :type description: string_types
        :type id: int
        :type status: string_types
        :type target_url: string_types
        :type updated_at: datetime
        :type url: string_types
        :rtype: Status
        """

        return Status(**kwargs)

    def __init__(self, json=None, **kwargs):
        pass
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Status'
        data = json or kwargs

        # set attributes
        data_types = [string_types]
        self.context = client_support.set_property('context', data, data_types, False, [], False, False, class_name)
        data_types = [datetime]
        self.created_at = client_support.set_property(
            'created_at', data, data_types, False, [], False, False, class_name)
        data_types = [User]
        self.creator = client_support.set_property('creator', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.description = client_support.set_property(
            'description', data, data_types, False, [], False, False, class_name)
        data_types = [int]
        self.id = client_support.set_property('id', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.status = client_support.set_property('status', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.target_url = client_support.set_property(
            'target_url', data, data_types, False, [], False, False, class_name)
        data_types = [datetime]
        self.updated_at = client_support.set_property(
            'updated_at', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.url = client_support.set_property('url', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
