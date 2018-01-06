"""
Auto-generated class for Error
"""
from six import string_types

from . import client_support


class Error(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type code: int
        :type message: str
        :type stack_trace: str
        :rtype: Error
        """

        return Error(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Error'
        data = json or kwargs

        # set attributes
        data_types = [int]
        self.code = client_support.set_property('code', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.message = client_support.set_property('message', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.stack_trace = client_support.set_property(
            'stack_trace', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
