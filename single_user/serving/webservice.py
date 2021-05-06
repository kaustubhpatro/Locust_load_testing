import os
import time

from locust import HttpUser, between, task
import sys

sys.path.append(os.getcwd())
from single_user.method_definition import sign_in, create_webservice, stop_webservice, sign, delete_webservice


class Webservice(HttpUser):
    wait_time = between(1, 2.5)
    to_run = True

    @task
    def webservice(self):
        if self.to_run:
            u, e, p = sign(self)
            jwt = sign_in(self, u, e, p)
            # file_upload(self, e, p, u)
            time.sleep(40)
            slug = create_webservice(self, jwt, u)
            time.sleep(30)
            stop_webservice(self, jwt, slug, u)
            delete_webservice(self, jwt, slug, u)
            self.to_run = False
