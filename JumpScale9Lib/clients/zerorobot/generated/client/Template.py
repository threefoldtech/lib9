"""
Auto-generated class for Template
"""
from six import string_types

from . import client_support


class Template(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type account: str
        :type host: str
        :type name: str
        :type repository: str
        :type uid: str
        :type version: str
        :rtype: Template
        """

        return Template(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Template'
        data = json or kwargs

        # set attributes
        data_types = [string_types]
        self.account = client_support.set_property('account', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.host = client_support.set_property('host', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.name = client_support.set_property('name', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.repository = client_support.set_property(
            'repository', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.uid = client_support.set_property('uid', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.version = client_support.set_property('version', data, data_types, False, [], False, True, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
