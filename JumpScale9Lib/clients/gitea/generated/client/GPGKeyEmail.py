"""
Auto-generated class for GPGKeyEmail
"""
from six import string_types

from . import client_support


class GPGKeyEmail(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type email: str
        :type verified: bool
        :rtype: GPGKeyEmail
        """

        return GPGKeyEmail(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'GPGKeyEmail'
        data = json or kwargs

        # set attributes
        data_types = [string_types]
        self.email = client_support.set_property('email', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.verified = client_support.set_property('verified', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
