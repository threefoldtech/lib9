"""
Auto-generated class for Eco
"""
from six import string_types

from . import client_support


class Eco(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type _limit: int
        :type _traceback: str
        :type appname: str
        :type category: str
        :type closetime: int
        :type code: str
        :type data: dict
        :type epoch: int
        :type errormessage: str
        :type errormessagePub: str
        :type exceptionclassname: str
        :type funcfilename: str
        :type funclinenr: int
        :type funcname: str
        :type guid: str
        :type jid: int
        :type lasttime: int
        :type level: int
        :type masterjid: int
        :type occurrences: int
        :type pid: int
        :type state: str
        :type tags: str
        :type type: str
        :type uniquekey: str
        :rtype: Eco
        """

        return Eco(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Eco'
        data = json or kwargs

        # set attributes
        data_types = [int]
        self._limit = client_support.set_property('_limit', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self._traceback = client_support.set_property(
            '_traceback', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.appname = client_support.set_property('appname', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.category = client_support.set_property('category', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.closetime = client_support.set_property('closetime', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.code = client_support.set_property('code', data, data_types, False, [], False, True, class_name)
        data_types = [dict]
        self.data = client_support.set_property('data', data, data_types, False, [], False, False, class_name)
        data_types = [int]
        self.epoch = client_support.set_property('epoch', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.errormessage = client_support.set_property(
            'errormessage', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.errormessagePub = client_support.set_property(
            'errormessagePub', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.exceptionclassname = client_support.set_property(
            'exceptionclassname', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.funcfilename = client_support.set_property(
            'funcfilename', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.funclinenr = client_support.set_property(
            'funclinenr', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.funcname = client_support.set_property('funcname', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.guid = client_support.set_property('guid', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.jid = client_support.set_property('jid', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.lasttime = client_support.set_property('lasttime', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.level = client_support.set_property('level', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.masterjid = client_support.set_property('masterjid', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.occurrences = client_support.set_property(
            'occurrences', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.pid = client_support.set_property('pid', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.state = client_support.set_property('state', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.tags = client_support.set_property('tags', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.type = client_support.set_property('type', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.uniquekey = client_support.set_property('uniquekey', data, data_types, False, [], False, True, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
