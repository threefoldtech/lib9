"""
Auto-generated class for PRBranchInfo
"""
from .Repository import Repository
from six import string_types

from . import client_support


class PRBranchInfo(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type label: str
        :type ref: str
        :type repo: Repository
        :type repo_id: int
        :type sha: str
        :rtype: PRBranchInfo
        """

        return PRBranchInfo(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'PRBranchInfo'
        data = json or kwargs

        # set attributes
        data_types = [string_types]
        self.label = client_support.set_property('label', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.ref = client_support.set_property('ref', data, data_types, False, [], False, False, class_name)
        data_types = [Repository]
        self.repo = client_support.set_property('repo', data, data_types, False, [], False, False, class_name)
        data_types = [int]
        self.repo_id = client_support.set_property('repo_id', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.sha = client_support.set_property('sha', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
