"""
Auto-generated class for EditReleaseOption
"""
from six import string_types

from . import client_support


class EditReleaseOption(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type body: str
        :type draft: bool
        :type name: str
        :type prerelease: bool
        :type tag_name: str
        :type target_commitish: str
        :rtype: EditReleaseOption
        """

        return EditReleaseOption(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'EditReleaseOption'
        data = json or kwargs

        # set attributes
        data_types = [string_types]
        self.body = client_support.set_property('body', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.draft = client_support.set_property('draft', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.name = client_support.set_property('name', data, data_types, False, [], False, False, class_name)
        data_types = [bool]
        self.prerelease = client_support.set_property(
            'prerelease', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.tag_name = client_support.set_property('tag_name', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.target_commitish = client_support.set_property(
            'target_commitish', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
