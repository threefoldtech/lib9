from js9 import j

from . import typchk
JSBASE = j.application.jsbase_get_class()


class AggregatorManager(JSBASE):
    _query_chk = typchk.Checker({
        'key': typchk.Or(str, typchk.IsNone()),
        'tags': typchk.Map(str, str),
    })

    def __init__(self, client):
        self._client = client
        JSBASE.__init__(self)

    def query(self, key=None, **tags):
        """
        Query zero-os aggregator for current state object of monitored metrics.

        Note: ID is returned as part of the key (if set) to avoid conflict with similar metrics that
        has same key. For example, a cpu core nr can be the id associated with 'machine.CPU.percent'
        so we can return all values for all the core numbers in the same dict.

        U can filter on the ID as a tag
        :example:
            self.query(key=key, id=value)

        :param key: metric key (ex: machine.memory.ram.available)
        :param tags: optional tags filter
        :return: dict of {
            'key[/id]': state object
        }

        @QUESTION how do we know which keys are available?
        @QUESTION what do we monitor?

        """
        args = {
            'key': key,
            'tags': tags,
        }
        self._query_chk.check(args)

        return self._client.json('aggregator.query', args)
