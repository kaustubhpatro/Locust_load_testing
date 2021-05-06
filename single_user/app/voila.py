import os
import time

from locust import HttpUser, between, task
import sys

sys.path.append(os.getcwd())
from single_user.method_definition import sign_in, create_voila, stop_voila, sign, delete_voila


class Voila(HttpUser):
    wait_time = between(1, 2.5)
    to_run = True

    @task
    def voila(self):
        if self.to_run:
            u, e, p = sign(self)
            jwt = sign_in(self, u, e, p)
            # file_upload(self, e, p, u)
            time.sleep(40)
            slug = create_voila(self, jwt, u)
            time.sleep(30)
            stop_voila(self, jwt, slug, u)
            delete_voila(self, jwt, slug, u)
            self.to_run = False
