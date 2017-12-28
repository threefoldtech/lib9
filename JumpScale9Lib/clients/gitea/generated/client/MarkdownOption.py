"""
Auto-generated class for MarkdownOption
"""
from six import string_types

from . import client_support


class MarkdownOption(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type Context: str
        :type Mode: str
        :type Text: str
        :type Wiki: bool
        :rtype: MarkdownOption
        """

        return MarkdownOption(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'MarkdownOption'
        data = json or kwargs

        # set attributes
        data_types = [string_types]
        self.Context = client_support.set_property('Context', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.Mode = client_support.set_property('Mode', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.Text = client_support.set_property('Text', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.Wiki = client_support.set_property('Wiki', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
