from django.test import TestCase
from github import Github
# 9aad62e349becabce8e02e4ffd88d74012272f97
github = Github(base_url="https://api.github.com", login_or_token="9aad62e349becabce8e02e4ffd88d74012272f97")

print(github)

for repo in github.get_user().get_repos():
    print(repo.name)

