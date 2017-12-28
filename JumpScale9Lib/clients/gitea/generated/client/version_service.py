
from .ServerVersion import ServerVersion
from .api_response import APIResponse
from .unhandled_api_error import UnhandledAPIError
from .unmarshall_error import UnmarshallError


class VersionService:
    def __init__(self, client):
        self.client = client

    def getVersion(self, headers=None, query_params=None, content_type="application/json"):
        """
        Returns the version of the Gitea application
        It is method for GET /version
        """
        uri = self.client.base_url + "/version"
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return APIResponse(data=ServerVersion(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)
