import os
import time

from locust import HttpUser, between, task
import sys

sys.path.append(os.getcwd())
from single_user.method_definition import sign_in, create_batch, stop_batch, sign, delete_batch


class Batch(HttpUser):
    wait_time = between(1, 2.5)
    to_run = True

    @task
    def batch(self):
        if self.to_run:
            u, e, p = sign(self)
            jwt = sign_in(self, u, e, p)
            # file_upload(self, e, p, u)
            time.sleep(40)
            slug = create_batch(self, jwt, u)
            stop_batch(self, jwt, slug, u)
            delete_batch(self, jwt, slug, u)
            self.to_run = False
