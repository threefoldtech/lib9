from js9 import j

JSBASE = j.application.jsbase_get_class()

class Def(JSBASE):
    """
    """

    def __init__(self, docsource, name):
        JSBASE.__init__(self)
        self.docsource = docsource
        self.name = j.data.text.strip_to_ascii_dense(name)
        self.docsite = self.docsource.docsite
        self.aliasses = []

    

    def __repr__(self):
        return "def:%s" % (self.name)

    __str__ = __repr__
