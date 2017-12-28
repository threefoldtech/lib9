

class OrgsService:
    def __init__(self, client):
        self.client = client

    def orgDeleteHook(self, id, org, headers=None, query_params=None, content_type="application/json"):
        """
        Delete a hook
        It is method for DELETE /orgs/{org}/hooks/{id}
        """
        uri = self.client.base_url + "/orgs/" + org + "/hooks/" + id
        return self.client.delete(uri, None, headers, query_params, content_type)

    def orgGetHook(self, id, org, headers=None, query_params=None, content_type="application/json"):
        """
        Get a hook
        It is method for GET /orgs/{org}/hooks/{id}
        """
        uri = self.client.base_url + "/orgs/" + org + "/hooks/" + id
        return self.client.get(uri, None, headers, query_params, content_type)

    def orgEditHook(self, data, id, org, headers=None, query_params=None, content_type="application/json"):
        """
        Update a hook
        It is method for PATCH /orgs/{org}/hooks/{id}
        """
        uri = self.client.base_url + "/orgs/" + org + "/hooks/" + id
        return self.client.patch(uri, data, headers, query_params, content_type)

    def orgListHooks(self, org, headers=None, query_params=None, content_type="application/json"):
        """
        List an organization's webhooks
        It is method for GET /orgs/{org}/hooks
        """
        uri = self.client.base_url + "/orgs/" + org + "/hooks"
        return self.client.get(uri, None, headers, query_params, content_type)

    def orgCreateHook(self, data, org, headers=None, query_params=None, content_type="application/json"):
        """
        Create a hook
        It is method for POST /orgs/{org}/hooks
        """
        uri = self.client.base_url + "/orgs/" + org + "/hooks"
        return self.client.post(uri, data, headers, query_params, content_type)

    def orgDeleteMember(self, username, org, headers=None, query_params=None, content_type="application/json"):
        """
        Remove a member from an organization
        It is method for DELETE /orgs/{org}/members/{username}
        """
        uri = self.client.base_url + "/orgs/" + org + "/members/" + username
        return self.client.delete(uri, None, headers, query_params, content_type)

    def orgIsMember(self, username, org, headers=None, query_params=None, content_type="application/json"):
        """
        Check if a user is a member of an organization
        It is method for GET /orgs/{org}/members/{username}
        """
        uri = self.client.base_url + "/orgs/" + org + "/members/" + username
        return self.client.get(uri, None, headers, query_params, content_type)

    def orgListMembers(self, org, headers=None, query_params=None, content_type="application/json"):
        """
        List an organization's members
        It is method for GET /orgs/{org}/members
        """
        uri = self.client.base_url + "/orgs/" + org + "/members"
        return self.client.get(uri, None, headers, query_params, content_type)

    def orgConcealMember(self, username, org, headers=None, query_params=None, content_type="application/json"):
        """
        Conceal a user's membership
        It is method for DELETE /orgs/{org}/public_members/{username}
        """
        uri = self.client.base_url + "/orgs/" + org + "/public_members/" + username
        return self.client.delete(uri, None, headers, query_params, content_type)

    def orgIsPublicMember(self, username, org, headers=None, query_params=None, content_type="application/json"):
        """
        Check if a user is a public member of an organization
        It is method for GET /orgs/{org}/public_members/{username}
        """
        uri = self.client.base_url + "/orgs/" + org + "/public_members/" + username
        return self.client.get(uri, None, headers, query_params, content_type)

    def orgPublicizeMember(self, data, username, org, headers=None, query_params=None, content_type="application/json"):
        """
        Publicize a user's membership
        It is method for PUT /orgs/{org}/public_members/{username}
        """
        uri = self.client.base_url + "/orgs/" + org + "/public_members/" + username
        return self.client.put(uri, data, headers, query_params, content_type)

    def orgListPublicMembers(self, org, headers=None, query_params=None, content_type="application/json"):
        """
        List an organization's public members
        It is method for GET /orgs/{org}/public_members
        """
        uri = self.client.base_url + "/orgs/" + org + "/public_members"
        return self.client.get(uri, None, headers, query_params, content_type)

    def orgListRepos(self, org, headers=None, query_params=None, content_type="application/json"):
        """
        List an organization's repos
        It is method for GET /orgs/{org}/repos
        """
        uri = self.client.base_url + "/orgs/" + org + "/repos"
        return self.client.get(uri, None, headers, query_params, content_type)

    def orgListTeams(self, org, headers=None, query_params=None, content_type="application/json"):
        """
        List an organization's teams
        It is method for GET /orgs/{org}/teams
        """
        uri = self.client.base_url + "/orgs/" + org + "/teams"
        return self.client.get(uri, None, headers, query_params, content_type)

    def orgCreateTeam(self, data, org, headers=None, query_params=None, content_type="application/json"):
        """
        Create a team
        It is method for POST /orgs/{org}/teams
        """
        uri = self.client.base_url + "/orgs/" + org + "/teams"
        return self.client.post(uri, data, headers, query_params, content_type)

    def orgGet(self, org, headers=None, query_params=None, content_type="application/json"):
        """
        Get an organization
        It is method for GET /orgs/{org}
        """
        uri = self.client.base_url + "/orgs/" + org
        return self.client.get(uri, None, headers, query_params, content_type)

    def orgEdit(self, data, org, headers=None, query_params=None, content_type="application/json"):
        """
        Edit an organization
        It is method for PATCH /orgs/{org}
        """
        uri = self.client.base_url + "/orgs/" + org
        return self.client.patch(uri, data, headers, query_params, content_type)
