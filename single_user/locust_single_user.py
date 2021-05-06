import os
import time

from locust import HttpUser, between, task, tag
import sys

sys.path.append(os.getcwd())
from single_user.method_definition import sign_in, create_stream, stop_stream, sign, delete_stream, \
    create_workspace, stop_workspace, delete_workspace, create_experiment, stop_experiment, delete_experiment, \
    create_dataset, create_project, create_webservice, stop_webservice, delete_webservice, create_batch, stop_batch, \
    delete_batch, create_voila, stop_voila, delete_voila, create_shiny, stop_shiny, delete_shiny, create_dash, \
    stop_dash, delete_dash


class SingleUser(HttpUser):
    wait_time = between(1, 2.5)
    to_run = True

    @task
    def single_user(self):
        if self.to_run:
            u, e, p = sign(self)
            jwt = sign_in(self, u, e, p)
            #  Dataset
            create_dataset(self, jwt, u)
            # Project
            create_project(self, jwt, u)
            #  Workspace
            time.sleep(40)
            slug = create_workspace(self, jwt, u)
            time.sleep(10)
            stop_workspace(self, jwt, slug, u)
            delete_workspace(self, jwt, slug, u)
            #  Experiment
            # time.sleep(40)
            slug = create_experiment(self, jwt, u)
            time.sleep(10)
            stop_experiment(self, jwt, slug, u)
            delete_experiment(self, jwt, slug, u)
            # Webservice
            # time.sleep(40)
            slug = create_webservice(self, jwt, u)
            time.sleep(10)
            stop_webservice(self, jwt, slug, u)
            delete_webservice(self, jwt, slug, u)
            # Stream
            # time.sleep(40)
            slug = create_stream(self, jwt, u)
            time.sleep(10)
            stop_stream(self, jwt, slug, u)
            delete_stream(self, jwt, slug, u)
            # Batch
            # time.sleep(40)
            slug = create_batch(self, jwt, u)
            stop_batch(self, jwt, slug, u)
            delete_batch(self, jwt, slug, u)
            # Voila
            # time.sleep(40)
            slug = create_voila(self, jwt, u)
            time.sleep(10)
            stop_voila(self, jwt, slug, u)
            delete_voila(self, jwt, slug, u)
            # Shiny
            # time.sleep(40)
            slug = create_shiny(self, jwt, u)
            time.sleep(10)
            stop_shiny(self, jwt, slug, u)
            delete_shiny(self, jwt, slug, u)
            # Dash
            # time.sleep(40)
            slug = create_dash(self, jwt, u)
            time.sleep(10)
            stop_dash(self, jwt, slug, u)
            delete_dash(self, jwt, slug, u)
            self.to_run = False
