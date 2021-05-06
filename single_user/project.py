from locust import HttpUser, between, task

from single_user.method_definition import sign_in, create_project, sign


class Project(HttpUser):
    wait_time = between(1, 2.5)
    to_run = True

    @task
    def project(self):
        if self.to_run:
            u, e, p = sign(self)
            jwt = sign_in(self, u, e, p)
            create_project(self, jwt, u)
            self.to_run = False
