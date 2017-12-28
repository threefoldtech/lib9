"""
Auto-generated class for PayloadCommit
"""
from .PayloadCommitVerification import PayloadCommitVerification
from .PayloadUser import PayloadUser
from datetime import datetime
from six import string_types

from . import client_support


class PayloadCommit(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type author: PayloadUser
        :type committer: PayloadUser
        :type id: str
        :type message: str
        :type timestamp: datetime
        :type url: str
        :type verification: PayloadCommitVerification
        :rtype: PayloadCommit
        """

        return PayloadCommit(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'PayloadCommit'
        data = json or kwargs

        # set attributes
        data_types = [PayloadUser]
        self.author = client_support.set_property('author', data, data_types, False, [], False, False, class_name)
        data_types = [PayloadUser]
        self.committer = client_support.set_property('committer', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.id = client_support.set_property('id', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.message = client_support.set_property('message', data, data_types, False, [], False, False, class_name)
        data_types = [datetime]
        self.timestamp = client_support.set_property('timestamp', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.url = client_support.set_property('url', data, data_types, False, [], False, False, class_name)
        data_types = [PayloadCommitVerification]
        self.verification = client_support.set_property(
            'verification', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
