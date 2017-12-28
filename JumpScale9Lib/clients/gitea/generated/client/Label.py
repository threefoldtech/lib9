"""
Auto-generated class for Label
"""
from six import string_types

from . import client_support


class Label(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type color: str
        :type id: int
        :type name: str
        :type url: str
        :rtype: Label
        """

        return Label(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Label'
        data = json or kwargs

        # set attributes
        data_types = [string_types]
        self.color = client_support.set_property('color', data, data_types, False, [], False, False, class_name)
        data_types = [int]
        self.id = client_support.set_property('id', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.name = client_support.set_property('name', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.url = client_support.set_property('url', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
