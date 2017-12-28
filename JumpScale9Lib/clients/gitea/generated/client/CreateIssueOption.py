"""
Auto-generated class for CreateIssueOption
"""
from six import string_types

from . import client_support


class CreateIssueOption(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type assignee: str
        :type body: str
        :type closed: bool
        :type labels: list[int]
        :type milestone: int
        :type title: str
        :rtype: CreateIssueOption
        """

        return CreateIssueOption(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'CreateIssueOption'
        data = json or kwargs

        # set attributes
        data_types = [string_types]
        self.assignee = client_support.set_property('assignee', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.body = client_support.set_property('body', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.closed = client_support.set_property('closed', data, data_types, False, [], False, False, class_name)
        data_types = [int]
        self.labels = client_support.set_property('labels', data, data_types, False, [], True, False, class_name)
        data_types = [int]
        self.milestone = client_support.set_property('milestone', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.title = client_support.set_property('title', data, data_types, False, [], False, True, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
