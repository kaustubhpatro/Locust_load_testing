import os
import time

from locust import HttpUser, between, task
import sys

sys.path.append(os.getcwd())
from single_user.method_definition import sign_in, create_dash, stop_dash, sign, delete_dash


class Dash(HttpUser):
    wait_time = between(1, 2.5)
    to_run = True

    @task
    def dash(self):
        if self.to_run:
            u, e, p = sign(self)
            jwt = sign_in(self, u, e, p)
            # file_upload(self, e, p, u)
            time.sleep(40)
            slug = create_dash(self, jwt, u)
            time.sleep(30)
            stop_dash(self, jwt, slug, u)
            delete_dash(self, jwt, slug, u)
            self.to_run = False
