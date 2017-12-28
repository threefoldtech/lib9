
from . import
from .Branch import Branch
from .Comment import Comment
from .DeployKey import DeployKey
from .Issue import Issue
from .Label import Label
from .Milestone import Milestone
from .PullRequest import PullRequest
from .Release import Release
from .Repository import Repository
from .SearchResults import SearchResults
from .Status import Status
from .TrackedTime import TrackedTime
from .WatchInfo import WatchInfo
from .api_response import APIResponse
from .unhandled_api_error import UnhandledAPIError
from .unmarshall_error import UnmarshallError


class ReposService:
    def __init__(self, client):
        self.client = client

    def repoMigrate(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        Migrate a remote git repository
        It is method for POST /repos/migrate
        """
        uri = self.client.base_url + "/repos/migrate"
        resp = self.client.post(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 201:
                return APIResponse(data=Repository(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def repoSearch(self, headers=None, query_params=None, content_type="application/json"):
        """
        Search for repositories
        It is method for GET /repos/search
        """
        uri = self.client.base_url + "/repos/search"
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return APIResponse(data=SearchResults(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def repoGetArchive(self, filepath, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Get an archive of a repository
        It is method for GET /repos/{owner}/{repo}/archive/{filepath}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/archive/" + filepath
        return self.client.get(uri, None, headers, query_params, content_type)

    def repoGetBranch(self, branch, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        List a repository's branches
        It is method for GET /repos/{owner}/{repo}/branches/{branch}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/branches/" + branch
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return APIResponse(data=Branch(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def repoListBranches(self, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        List a repository's branches
        It is method for GET /repos/{owner}/{repo}/branches
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/branches"
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

    def repoDeleteCollaborator(
            self,
            collaborator,
            repo,
            owner,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        Delete a collaborator from a repository
        It is method for DELETE /repos/{owner}/{repo}/collaborators/{collaborator}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/collaborators/" + collaborator
        return self.client.delete(uri, None, headers, query_params, content_type)

    def repoCheckCollaborator(
            self,
            collaborator,
            repo,
            owner,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        Check if a user is a collaborator of a repository
        It is method for GET /repos/{owner}/{repo}/collaborators/{collaborator}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/collaborators/" + collaborator
        return self.client.get(uri, None, headers, query_params, content_type)

    def repoAddCollaborator(
            self,
            data,
            collaborator,
            repo,
            owner,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        Add a collaborator to a repository
        It is method for PUT /repos/{owner}/{repo}/collaborators/{collaborator}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/collaborators/" + collaborator
        return self.client.put(uri, data, headers, query_params, content_type)

    def repoListCollaborators(self, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        List a repository's collaborators
        It is method for GET /repos/{owner}/{repo}/collaborators
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/collaborators"
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

    def repoGetCombinedStatusByRef(
            self,
            ref,
            repo,
            owner,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        Get a commit's combined status, by branch/tag/commit reference
        It is method for GET /repos/{owner}/{repo}/commits/{ref}/statuses
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/commits/" + ref + "/statuses"
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return APIResponse(data=Status(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def repoGetEditorConfig(
            self,
            filepath,
            repo,
            owner,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        Get the EditorConfig definitions of a file in a repository
        It is method for GET /repos/{owner}/{repo}/editorconfig/{filepath}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/editorconfig/" + filepath
        return self.client.get(uri, None, headers, query_params, content_type)

    def listForks(self, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        List a repository's forks
        It is method for GET /repos/{owner}/{repo}/forks
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/forks"
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

    def createFork(self, data, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Fork a repository
        It is method for POST /repos/{owner}/{repo}/forks
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/forks"
        resp = self.client.post(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 202:
                return APIResponse(data=Repository(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def repoGetHook(self, id, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Get a hook
        It is method for GET /repos/{owner}/{repo}/hooks/{id}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/hooks/" + id
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

    def repoEditHook(self, data, id, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Edit a hook in a repository
        It is method for PATCH /repos/{owner}/{repo}/hooks/{id}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/hooks/" + id
        resp = self.client.patch(uri, data, headers, query_params, content_type)
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

    def repoListHooks(self, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        List the hooks in a repository
        It is method for GET /repos/{owner}/{repo}/hooks
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/hooks"
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

    def repoCreateHook(self, data, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Create a hook
        It is method for POST /repos/{owner}/{repo}/hooks
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/hooks"
        resp = self.client.post(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 201:
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

    def issueGetComments(self, index, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        List all comments on an issue
        It is method for GET /repos/{owner}/{repo}/issue/{index}/comments
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/issue/" + index + "/comments"
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

    def issueRemoveLabel(
            self,
            id,
            index,
            repo,
            owner,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        Remove a label from an issue
        It is method for DELETE /repos/{owner}/{repo}/issue/{index}/labels/{id}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/issue/" + index + "/labels/" + id
        return self.client.delete(uri, None, headers, query_params, content_type)

    def issueClearLabels(self, index, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Remove all labels from an issue
        It is method for DELETE /repos/{owner}/{repo}/issue/{index}/labels
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/issue/" + index + "/labels"
        return self.client.delete(uri, None, headers, query_params, content_type)

    def issueAddLabel(self, data, index, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Add a label to an issue
        It is method for POST /repos/{owner}/{repo}/issue/{index}/labels
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/issue/" + index + "/labels"
        resp = self.client.post(uri, data, headers, query_params, content_type)
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

    def issueReplaceLabels(
            self,
            data,
            index,
            repo,
            owner,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        Replace an issue's labels
        It is method for PUT /repos/{owner}/{repo}/issue/{index}/labels
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/issue/" + index + "/labels"
        resp = self.client.put(uri, data, headers, query_params, content_type)
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

    def issueDeleteComment(self, id, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Delete a comment
        It is method for DELETE /repos/{owner}/{repo}/issues/comments/{id}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/issues/comments/" + id
        return self.client.delete(uri, None, headers, query_params, content_type)

    def issueEditComment(self, data, id, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Edit a comment
        It is method for PATCH /repos/{owner}/{repo}/issues/comments/{id}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/issues/comments/" + id
        resp = self.client.patch(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return APIResponse(data=Comment(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def issueGetRepoComments(self, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        List all comments in a repository
        It is method for GET /repos/{owner}/{repo}/issues/comments
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/issues/comments"
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

    def issueGetIssue(self, id, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Get an issue by id
        It is method for GET /repos/{owner}/{repo}/issues/{id}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/issues/" + id
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return APIResponse(data=Issue(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def issueEditIssue(self, data, id, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Edit an issue
        It is method for PATCH /repos/{owner}/{repo}/issues/{id}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/issues/" + id
        resp = self.client.patch(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 201:
                return APIResponse(data=Issue(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def issueDeleteCommentDeprecated(
            self,
            id,
            index,
            repo,
            owner,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        Delete a comment
        It is method for DELETE /repos/{owner}/{repo}/issues/{index}/comments/{id}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/issues/" + index + "/comments/" + id
        return self.client.delete(uri, None, headers, query_params, content_type)

    def issueEditCommentDeprecated(
            self,
            data,
            id,
            index,
            repo,
            owner,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        Edit a comment
        It is method for PATCH /repos/{owner}/{repo}/issues/{index}/comments/{id}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/issues/" + index + "/comments/" + id
        resp = self.client.patch(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return APIResponse(data=Comment(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def issueCreateComment(
            self,
            data,
            index,
            repo,
            owner,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        Add a comment to an issue
        It is method for POST /repos/{owner}/{repo}/issues/{index}/comments
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/issues/" + index + "/comments"
        resp = self.client.post(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 201:
                return APIResponse(data=Comment(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def issueGetLabels(self, index, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Get an issue's labels
        It is method for GET /repos/{owner}/{repo}/issues/{index}/labels
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/issues/" + index + "/labels"
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

    def issueTrackedTimes(self, index, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        List an issue's tracked times
        It is method for GET /repos/{owner}/{repo}/issues/{index}/times
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/issues/" + index + "/times"
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

    def issueAddTime(self, data, index, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Add a tracked time to a issue
        It is method for POST /repos/{owner}/{repo}/issues/{index}/times
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/issues/" + index + "/times"
        resp = self.client.post(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return APIResponse(data=TrackedTime(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def issueListIssues(self, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        List a repository's issues
        It is method for GET /repos/{owner}/{repo}/issues
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/issues"
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

    def issueCreateIssue(self, data, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Create an issue
        It is method for POST /repos/{owner}/{repo}/issues
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/issues"
        resp = self.client.post(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 201:
                return APIResponse(data=Issue(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def repoDeleteKey(self, id, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Delete a key from a repository
        It is method for DELETE /repos/{owner}/{repo}/keys/{id}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/keys/" + id
        return self.client.delete(uri, None, headers, query_params, content_type)

    def repoGetKey(self, id, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Get a repository's key by id
        It is method for GET /repos/{owner}/{repo}/keys/{id}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/keys/" + id
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return APIResponse(data=DeployKey(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def repoListKeys(self, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        List a repository's keys
        It is method for GET /repos/{owner}/{repo}/keys
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/keys"
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

    def repoCreateKey(self, data, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Add a key to a repository
        It is method for POST /repos/{owner}/{repo}/keys
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/keys"
        resp = self.client.post(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 201:
                return APIResponse(data=DeployKey(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def issueDeleteLabel(self, id, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Delete a label
        It is method for DELETE /repos/{owner}/{repo}/labels/{id}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/labels/" + id
        return self.client.delete(uri, None, headers, query_params, content_type)

    def issueGetLabel(self, id, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Get a single label
        It is method for GET /repos/{owner}/{repo}/labels/{id}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/labels/" + id
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return APIResponse(data=Label(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def issueEditLabel(self, data, id, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Update a label
        It is method for PATCH /repos/{owner}/{repo}/labels/{id}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/labels/" + id
        resp = self.client.patch(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return APIResponse(data=Label(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def issueListLabels(self, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Get all of a repository's labels
        It is method for GET /repos/{owner}/{repo}/labels
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/labels"
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

    def issueCreateLabel(self, data, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Create a label
        It is method for POST /repos/{owner}/{repo}/labels
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/labels"
        resp = self.client.post(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 201:
                return APIResponse(data=Label(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def issueDeleteMilestone(self, id, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Delete a milestone
        It is method for DELETE /repos/{owner}/{repo}/milestones/{id}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/milestones/" + id
        return self.client.delete(uri, None, headers, query_params, content_type)

    def issueGetMilestone(self, id, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Get a milestone
        It is method for GET /repos/{owner}/{repo}/milestones/{id}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/milestones/" + id
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return APIResponse(data=Milestone(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def issueEditMilestone(
            self,
            data,
            id,
            repo,
            owner,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        Update a milestone
        It is method for PATCH /repos/{owner}/{repo}/milestones/{id}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/milestones/" + id
        resp = self.client.patch(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return APIResponse(data=Milestone(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def issueGetMilestones(self, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Get all of a repository's milestones
        It is method for GET /repos/{owner}/{repo}/milestones
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/milestones"
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

    def issueCreateMilestone(self, data, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Create a milestone
        It is method for POST /repos/{owner}/{repo}/milestones
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/milestones"
        resp = self.client.post(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 201:
                return APIResponse(data=Milestone(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def repoMirrorSync(self, data, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Sync a mirrored repository
        It is method for POST /repos/{owner}/{repo}/mirror-sync
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/mirror-sync"
        return self.client.post(uri, data, headers, query_params, content_type)

    def repoPullRequestIsMerged(
            self,
            index,
            repo,
            owner,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        Check if a pull request has been merged
        It is method for GET /repos/{owner}/{repo}/pulls/{index}/merge
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/pulls/" + index + "/merge"
        return self.client.get(uri, None, headers, query_params, content_type)

    def repoMergePullRequest(
            self,
            data,
            index,
            repo,
            owner,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        Merge a pull request
        It is method for POST /repos/{owner}/{repo}/pulls/{index}/merge
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/pulls/" + index + "/merge"
        return self.client.post(uri, data, headers, query_params, content_type)

    def repoGetPullRequest(self, index, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Get a pull request
        It is method for GET /repos/{owner}/{repo}/pulls/{index}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/pulls/" + index
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return APIResponse(data=PullRequest(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def repoEditPullRequest(
            self,
            data,
            index,
            repo,
            owner,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        Update a pull request
        It is method for PATCH /repos/{owner}/{repo}/pulls/{index}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/pulls/" + index
        resp = self.client.patch(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 201:
                return APIResponse(data=PullRequest(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def repoListPullRequests(self, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        List a repo's pull requests
        It is method for GET /repos/{owner}/{repo}/pulls
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/pulls"
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

    def repoCreatePullRequest(
            self,
            data,
            repo,
            owner,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        Create a pull request
        It is method for POST /repos/{owner}/{repo}/pulls
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/pulls"
        resp = self.client.post(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 201:
                return APIResponse(data=PullRequest(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def repoGetRawFile(self, filepath, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Get a file from a repository
        It is method for GET /repos/{owner}/{repo}/raw/{filepath}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/raw/" + filepath
        return self.client.get(uri, None, headers, query_params, content_type)

    def repoDeleteRelease(self, id, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Delete a release
        It is method for DELETE /repos/{owner}/{repo}/releases/{id}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/releases/" + id
        return self.client.delete(uri, None, headers, query_params, content_type)

    def repoEditRelease(self, data, id, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Update a release
        It is method for PATCH /repos/{owner}/{repo}/releases/{id}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/releases/" + id
        resp = self.client.patch(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return APIResponse(data=Release(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def repoCreateRelease(self, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Create a release
        It is method for GET /repos/{owner}/{repo}/releases
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/releases"
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 201:
                return APIResponse(data=Release(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def repoListStargazers(self, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        List a repo's stargazers
        It is method for GET /repos/{owner}/{repo}/stargazers
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/stargazers"
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

    def repoListStatuses(self, sha, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Get a commit's statuses
        It is method for GET /repos/{owner}/{repo}/statuses/{sha}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/statuses/" + sha
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

    def repoCreateStatus(
            self,
            data,
            sha,
            repo,
            owner,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        Create a commit status
        It is method for POST /repos/{owner}/{repo}/statuses/{sha}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/statuses/" + sha
        resp = self.client.post(uri, data, headers, query_params, content_type)
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

    def repoListSubscribers(self, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        List a repo's watchers
        It is method for GET /repos/{owner}/{repo}/subscribers
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/subscribers"
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

    def userCurrentDeleteSubscription(
            self,
            repo,
            owner,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        Unwatch a repo
        It is method for DELETE /repos/{owner}/{repo}/subscription
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/subscription"
        return self.client.delete(uri, None, headers, query_params, content_type)

    def userCurrentCheckSubscription(
            self,
            repo,
            owner,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        Check if the current user is watching a repo
        It is method for GET /repos/{owner}/{repo}/subscription
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/subscription"
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return APIResponse(data=WatchInfo(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def userCurrentPutSubscription(
            self,
            data,
            repo,
            owner,
            headers=None,
            query_params=None,
            content_type="application/json"):
        """
        Watch a repo
        It is method for PUT /repos/{owner}/{repo}/subscription
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/subscription"
        resp = self.client.put(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return APIResponse(data=WatchInfo(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def userTrackedTimes(self, tracker, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        List a user's tracked times in a repo
        It is method for GET /repos/{owner}/{repo}/times/{tracker}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/times/" + tracker
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

    def repoTrackedTimes(self, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        List a repo's tracked times
        It is method for GET /repos/{owner}/{repo}/times
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo + "/times"
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

    def repoDelete(self, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Delete a repository
        It is method for DELETE /repos/{owner}/{repo}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo
        return self.client.delete(uri, None, headers, query_params, content_type)

    def repoGet(self, repo, owner, headers=None, query_params=None, content_type="application/json"):
        """
        Get a repository
        It is method for GET /repos/{owner}/{repo}
        """
        uri = self.client.base_url + "/repos/" + owner + "/" + repo
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return APIResponse(data=Repository(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def repoDeleteHook(self, user, repo, id, headers=None, query_params=None, content_type="application/json"):
        """
        Delete a hook in a repository
        It is method for DELETE /repos/{user}/{repo}/hooks/{id}
        """
        uri = self.client.base_url + "/repos/" + user + "/" + repo + "/hooks/" + id
        return self.client.delete(uri, None, headers, query_params, content_type)
