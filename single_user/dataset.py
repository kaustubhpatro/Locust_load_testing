from locust import HttpUser, between, task

from single_user.method_definition import sign_in, create_dataset, sign, get_dataset


class Dataset(HttpUser):
    wait_time = between(1, 2.5)
    to_run = True

    @task
    def dataset(self):
        if self.to_run:
            u, e, p = sign(self)
            jwt = sign_in(self, u, e, p)
            create_dataset(self, jwt, u)
            get_dataset(self, jwt, u)
            self.to_run = False
