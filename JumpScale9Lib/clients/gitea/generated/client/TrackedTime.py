"""
Auto-generated class for TrackedTime
"""
from datetime import datetime

from . import client_support


class TrackedTime(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type created: datetime
        :type id: int
        :type issue_id: int
        :type time: int
        :type user_id: int
        :rtype: TrackedTime
        """

        return TrackedTime(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'TrackedTime'
        data = json or kwargs

        # set attributes
        data_types = [datetime]
        self.created = client_support.set_property('created', data, data_types, False, [], False, False, class_name)
        data_types = [int]
        self.id = client_support.set_property('id', data, data_types, False, [], False, False, class_name)
        data_types = [int]
        self.issue_id = client_support.set_property('issue_id', data, data_types, False, [], False, False, class_name)
        data_types = [int]
        self.time = client_support.set_property('time', data, data_types, False, [], False, False, class_name)
        data_types = [int]
        self.user_id = client_support.set_property('user_id', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
