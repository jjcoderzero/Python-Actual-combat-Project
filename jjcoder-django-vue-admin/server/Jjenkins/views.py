from django.conf import settings
from django.shortcuts import HttpResponse
import json
import jenkins

print(settings.JENKINS)


class JenkinsAuth(object):
    def __init__(self, jenkinsConf=settings.JENKINS):
        self.url = jenkinsConf["jenkins_server_url"]
        self.username = jenkinsConf["user_id"]
        self.password = jenkinsConf["api_token"]

    def authToken(self):
        server = jenkins.Jenkins(url=self.url, username=self.username, password=self.password)
        return server


def job_name_info(request, job_name):
    auth = JenkinsAuth()
    server = auth.authToken()
    job_info = server.get_job_info(job_name)
    return HttpResponse(json.dumps(job_info), content_type="application/json")
