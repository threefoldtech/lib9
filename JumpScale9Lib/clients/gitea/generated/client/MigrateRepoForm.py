"""
Auto-generated class for MigrateRepoForm
"""
from six import string_types

from . import client_support


class MigrateRepoForm(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type auth_password: str
        :type auth_username: str
        :type clone_addr: str
        :type description: str
        :type mirror: bool
        :type private: bool
        :type repo_name: str
        :type uid: int
        :rtype: MigrateRepoForm
        """

        return MigrateRepoForm(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'MigrateRepoForm'
        data = json or kwargs

        # set attributes
        data_types = [string_types]
        self.auth_password = client_support.set_property(
            'auth_password', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.auth_username = client_support.set_property(
            'auth_username', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.clone_addr = client_support.set_property(
            'clone_addr', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.description = client_support.set_property(
            'description', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.mirror = client_support.set_property('mirror', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.private = client_support.set_property('private', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.repo_name = client_support.set_property('repo_name', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.uid = client_support.set_property('uid', data, data_types, False, [], False, True, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)