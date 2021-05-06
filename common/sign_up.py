import csv

from locust import HttpUser, between, task

from single_user.method_definition import signup, sign, sign_in, create_project, file_upload, create_organization


class Signup(HttpUser):
    wait_time = between(1, 2.5)
    to_run = True

    @task
    def signup(self):
        if self.to_run:
            username, email, password = signup(self)
            with open('data.csv', mode='w') as data_file:
                employee_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                employee_writer.writerow([username, email, password])
            u, e, p = sign(self)
            jwt = sign_in(self, u, e, p)
            create_organization(self, jwt, u)
            create_project(self, jwt, u)
            file_upload(self, e, p, u)
            with open('data.csv', mode='w') as data_file:
                employee_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                employee_writer.writerow([u, e, p])
            self.to_run = False
