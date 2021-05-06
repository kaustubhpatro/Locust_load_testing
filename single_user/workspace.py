import os
import time

from locust import HttpUser, between, task
import sys

sys.path.append(os.getcwd())
from single_user.method_definition import sign_in, create_workspace, stop_workspace, sign, delete_workspace, get_workspace


class Workspace(HttpUser):
    wait_time = between(1, 2.5)
    to_run = True

    @task
    def workspace(self):
        if self.to_run:
            u, e, p = sign(self)
            jwt = sign_in(self, u, e, p)
            time.sleep(40)
            slug = create_workspace(self, jwt, u)
            get_workspace(self, jwt, slug, u)
            stop_workspace(self, jwt, slug, u)
            delete_workspace(self, jwt, slug, u)
            self.to_run = False
