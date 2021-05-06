import os
import time

from locust import HttpUser, between, task
import sys

sys.path.append(os.getcwd())
from single_user.method_definition import sign_in, create_experiment, stop_experiment, sign, delete_experiment


class Experiment(HttpUser):
    wait_time = between(1, 2.5)
    to_run = True

    @task
    def experiment(self):
        if self.to_run:
            u, e, p = sign(self)
            jwt = sign_in(self, u, e, p)
            time.sleep(40)
            slug = create_experiment(self, jwt, u)
            time.sleep(30)
            stop_experiment(self, jwt, slug, u)
            delete_experiment(self, jwt, slug, u)
            self.to_run = False
