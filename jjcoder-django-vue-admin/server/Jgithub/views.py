from django.shortcuts import render
from rest_framework.views import APIView
from django.conf import settings
from github import Github


class GithubAuth(object):
    locals().update(settings.GITHUB)

    def authToken(self, base_url, token):
        github = Github(base_url=base_url, login_or_token=token)
        return github
