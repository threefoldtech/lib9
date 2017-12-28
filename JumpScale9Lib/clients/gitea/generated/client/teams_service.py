
from . import
from .Team import Team
from .api_response import APIResponse
from .unhandled_api_error import UnhandledAPIError
from .unmarshall_error import UnmarshallError


class TeamsService:
    def __init__(self, client):
        self.client = client

    def orgAddTeamMember(self, username, id, headers=None, query_params=None, content_type="application/json"):
        """
        Remove a team member
        It is method for DELETE /teams/{id}/members/{username}
        """
        uri = self.client.base_url + "/teams/" + id + "/members/" + username
        return self.client.delete(uri, None, headers, query_params, content_type)

    def orgAddTeamMember(self, data, username, id, headers=None, query_params=None, content_type="application/json"):
        """
        Add a team member
        It is method for PUT /teams/{id}/members/{username}
        """
        uri = self.client.base_url + "/teams/" + id + "/members/" + username
        return self.client.put(uri, data, headers, query_params, content_type)

    def orgListTeamMembers(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        List a team's members
        It is method for GET /teams/{id}/members
        """
        uri = self.client.base_url + "/teams/" + id + "/members"
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                resps = []
                for elem in resp.json():
                    resps.append((elem))
                return APIResponse(data=resps, response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def orgAddTeamMember(self, org, repo, id, headers=None, query_params=None, content_type="application/json"):
        """
        This does not delete the repository, it only removes the repository from the team.
        It is method for DELETE /teams/{id}/repos/{org}/{repo}
        """
        uri = self.client.base_url + "/teams/" + id + "/repos/" + org + "/" + repo
        return self.client.delete(uri, None, headers, query_params, content_type)

    def orgAddTeamMember(self, data, org, repo, id, headers=None, query_params=None, content_type="application/json"):
        """
        Add a repository to a team
        It is method for PUT /teams/{id}/repos/{org}/{repo}
        """
        uri = self.client.base_url + "/teams/" + id + "/repos/" + org + "/" + repo
        return self.client.put(uri, data, headers, query_params, content_type)

    def orgListTeamRepos(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        List a team's repos
        It is method for GET /teams/{id}/repos
        """
        uri = self.client.base_url + "/teams/" + id + "/repos"
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                resps = []
                for elem in resp.json():
                    resps.append((elem))
                return APIResponse(data=resps, response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def orgDeleteTeam(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        Delete a team
        It is method for DELETE /teams/{id}
        """
        uri = self.client.base_url + "/teams/" + id
        return self.client.delete(uri, None, headers, query_params, content_type)

    def orgGetTeam(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        Get a team
        It is method for GET /teams/{id}
        """
        uri = self.client.base_url + "/teams/" + id
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return APIResponse(data=Team(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def orgEditTeam(self, data, id, headers=None, query_params=None, content_type="application/json"):
        """
        Edit a team
        It is method for PATCH /teams/{id}
        """
        uri = self.client.base_url + "/teams/" + id
        resp = self.client.patch(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return APIResponse(data=Team(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)
