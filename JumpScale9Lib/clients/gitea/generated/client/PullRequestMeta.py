"""
Auto-generated class for PullRequestMeta
"""
from datetime import datetime

from . import client_support


class PullRequestMeta(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type merged: bool
        :type merged_at: datetime
        :rtype: PullRequestMeta
        """

        return PullRequestMeta(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'PullRequestMeta'
        data = json or kwargs

        # set attributes
        data_types = [bool]
        self.merged = client_support.set_property('merged', data, data_types, False, [], False, False, class_name)
        data_types = [datetime]
        self.merged_at = client_support.set_property('merged_at', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
