"""
Auto-generated class for CreatePullRequestOption
"""
from six import string_types

from . import client_support


class CreatePullRequestOption(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type assignee: str
        :type base: str
        :type body: str
        :type head: str
        :type labels: list[int]
        :type milestone: int
        :type title: str
        :rtype: CreatePullRequestOption
        """

        return CreatePullRequestOption(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'CreatePullRequestOption'
        data = json or kwargs

        # set attributes
        data_types = [string_types]
        self.assignee = client_support.set_property('assignee', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.base = client_support.set_property('base', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.body = client_support.set_property('body', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.head = client_support.set_property('head', data, data_types, False, [], False, False, class_name)
        data_types = [int]
        self.labels = client_support.set_property('labels', data, data_types, False, [], True, False, class_name)
        data_types = [int]
        self.milestone = client_support.set_property('milestone', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.title = client_support.set_property('title', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
