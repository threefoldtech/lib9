
from .api_response import APIResponse
from .unhandled_api_error import UnhandledAPIError
from .unmarshall_error import UnmarshallError


class MarkdownService:
    def __init__(self, client):
        self.client = client

    def renderMarkdownRaw(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        Render raw markdown as HTML
        It is method for POST /markdown/raw
        """
        uri = self.client.base_url + "/markdown/raw"
        return self.client.post(uri, data, headers, query_params, content_type)

    def renderMarkdown(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        Render a markdown document as HTML
        It is method for POST /markdown
        """
        uri = self.client.base_url + "/markdown"
        return self.client.post(uri, data, headers, query_params, content_type)
