"""
Auto-generated class for Repository
"""
from .User import User
from datetime import datetime
from six import string_types

from . import client_support


class Repository(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type clone_url: str
        :type created_at: datetime
        :type default_branch: str
        :type description: str
        :type empty: bool
        :type fork: bool
        :type forks_count: int
        :type full_name: str
        :type html_url: str
        :type id: int
        :type mirror: bool
        :type name: str
        :type open_issues_count: int
        :type owner: User
        :rtype: Repository
        """

        return Repository(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Repository'
        data = json or kwargs

        # set attributes
        data_types = [string_types]
        self.clone_url = client_support.set_property('clone_url', data, data_types, False, [], False, False, class_name)
        data_types = [datetime]
        self.created_at = client_support.set_property(
            'created_at', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.default_branch = client_support.set_property(
            'default_branch', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.description = client_support.set_property(
            'description', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.empty = client_support.set_property('empty', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.fork = client_support.set_property('fork', data, data_types, False, [], False, False, class_name)
        data_types = [int]
        self.forks_count = client_support.set_property(
            'forks_count', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.full_name = client_support.set_property('full_name', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.html_url = client_support.set_property('html_url', data, data_types, False, [], False, False, class_name)
        data_types = [int]
        self.id = client_support.set_property('id', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.mirror = client_support.set_property('mirror', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.name = client_support.set_property('name', data, data_types, False, [], False, False, class_name)
        data_types = [int]
        self.open_issues_count = client_support.set_property(
            'open_issues_count', data, data_types, False, [], False, False, class_name)
        data_types = [User]
        self.owner = client_support.set_property('owner', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
