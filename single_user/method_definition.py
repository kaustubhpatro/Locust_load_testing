import csv
import json
import os
import random
import string
from cnvrgp import Cnvrg
import sys

sys.path.append(os.getcwd())
from common.env_details import Env
from common.payloads import payload_create_workspace, payload_create_experiment, payload_create_webservice, \
    payload_create_stream, payload_create_batch, payload_voila_app, payload_shiny_app, payload_dash_app


def signup(self):
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    email = username + '@test12.com'
    password = 'Tftus@123'
    url = "" + Env + "/api/v2/users/"
    payload = "{\n  \"data\": {\n    \"type\": \"user\",\n    \"attributes\": {\n      \"email\": \"" + email + "\",\n      \"username\": \"" + username + "\",\n      \"password\": \"" + password + "\"\n    }\n  }\n}"
    headers = {'Content-Type': 'application/json', 'User-Agent': 'cnvrg/0.3.2', 'Authorization': 'bearer None'}
    self.client.post(url, headers=headers, data=payload, name="signup: " + url)
    print("Email: ", email)
    return [username, email, password]


def sign(self):
    with open('data.csv', 'r') as csv_file:  # Open the file in read mode
        csv_reader = csv.reader(csv_file)  # use dictreader method to reade the file in dictionary
        data = list(csv_reader)
        u = data[0][0]
        e = data[0][1]
        p = data[0][2]
    return u, e, p


def sign_in(self, u, e, p):
    url = "" + Env + "/api/v2/users/sign_in"
    payload = "{\n  \"username\": \"" + e + "\",\n  \"password\": \"" + p + "\",\n  \"user\": {\n    \"username\": \"" + u + "\"\n  }\n}"
    headers = {'Content-Type': 'application/json', 'User-Agent': 'cnvrg/0.3.2', 'Authorization': 'bearer None'}
    response = self.client.post(url, headers=headers, data=payload, name="sign_in: " + url)
    jwt = (json.loads(response.text)['meta']['jwt'])
    # print("jwt: ", jwt)
    return jwt


def create_organization(self, jwt, u):
    organization = u
    url = "" + Env + "/api/v2/organizations"
    payload = "{\"title\": \"" + organization + "\"}"
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json'}
    self.client.post(url, headers=headers, data=payload, name="create_organization: " + url)


def file_upload(self, e, p, u):
    cnvrg = Cnvrg(domain=Env, email=e, password=p, organization=u, suppress_exceptions=False)
    myproj = cnvrg.projects.get("testproject")
    myproj.put_files(
        ['predict.py', 'app.py', 'app.R', 'basics.ipynb', 'experiment.py', 'experiment.rb', 'testendpoint.py'])


def create_dataset(self, jwt, u):
    url = "" + Env + "/api/v2/" + u + "/datasets/"
    payload = "{\n    \"data\": \n    {\n        \"type\": \"dataset\",\n        \"attributes\":\n            {\n     " \
              "           \"title\": \"dataset1\", \"category\": \"general\"\n            }\n    }\n\n} "
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + jwt}
    self.client.post(url, headers=headers, data=payload, name="create_dataset: " + url)


def get_dataset(self, jwt, u):
    url = "" + Env + "/api/v2/" + u + "/datasets/"
    payload = {}
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + jwt, 'User-Agent': 'cnvrg/0.3.2'}
    self.client.get(url, headers=headers, data=payload, name="dataset info :" + url)


def create_project(self, jwt, u):
    url = "" + Env + "/api/v2/" + u + "/projects?example&title=testproject"
    payload = "{\n  \"data\": {\n    \"type\": \"project\",\n    \"attributes\": {\n      \"title\": " \
              "\"testproject\"\n    }\n  }\n} "
    headers = {'Content-Type': 'application/json', 'User-Agent': 'cnvrg/0.3.2', 'Authorization': 'Bearer ' + jwt}
    self.client.post(url, headers=headers, data=payload, name="create_project: " + url)


def get_project(self, jwt, u):
    url = ""+Env+"/api/v2/"+u+"/projects/"
    payload = {}
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer '+jwt}
    self.client.get(url, headers=headers, data=payload, name="Project info: "+url)


def create_workspace(self, jwt, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows"
    payload = payload_create_workspace
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json'}
    response = self.client.post(url, headers=headers, data=payload, name="create_workspace: " + url)
    slug = (json.loads(response.text)['data']['attributes']['slug'])
    return slug


def get_workspace(self, jwt, slug, u):
    url = ""+Env+"/api/v2/"+u+"/projects/testproject/workflows/"+slug
    payload = {}
    headers = {'Authorization': 'Bearer '+jwt}
    self.client.get(url, headers=headers, data=payload, name="Workspace info: "+url)


def stop_workspace(self, jwt, slug, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows/stop_workflows"
    payload = "{\n  \"data\": {\n    \"type\": \"user\",\n    \"attributes\": {\n      \"workflow_slugs\": [\"" + slug + "\"],\n      \"sync\": \"False\"\n    }\n  }\n} "
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json', 'User-Agent': 'cnvrg/0.3.2'}
    self.client.post(url, headers=headers, data=payload, name="stop_workspace: " + url)


def create_experiment(http_user, jwt, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows"
    payload = payload_create_experiment
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json'}
    response = http_user.client.post(url, headers=headers, data=payload, name="create_experiment: " + url)
    slug = (json.loads(response.text)['data']['attributes']['slug'])
    return slug


def get_experiment(self, jwt, slug, u):
    url = ""+Env+"/api/v2/"+u+"/projects/testproject/workflows/"+slug
    payload = {}
    headers = {'Authorization': 'Bearer '+jwt}
    self.client.get(url, headers=headers, data=payload, name="Experiment info: "+url)


def stop_experiment(self, jwt, slug, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows/stop_workflows"
    payload = "{\"data\":{\"attributes\":{\"workflow_slugs\":[\"" + slug + "\"],\"sync\":false}}}"
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json', 'User-Agent': 'cnvrg/0.3.2'}
    self.client.post(url, headers=headers, data=payload, name="stop_experiment: " + url)


def create_webservice(self, jwt, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows"
    payload = payload_create_webservice
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json'}
    response = self.client.post(url, headers=headers, data=payload, name="create_webservice: " + url)
    slug = (json.loads(response.text)['data']['attributes']['slug'])
    return slug


def get_webservice(self, jwt, slug, u):
    url = ""+Env+"/api/v2/"+u+"/projects/testproject/workflows/"+slug
    payload = {}
    headers = {'Authorization': 'Bearer '+jwt}
    self.client.get(url, headers=headers, data=payload, name="webservice info: "+url)


def stop_webservice(self, jwt, slug, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows/stop_workflows"
    payload = "{\"data\":{\"attributes\":{\"workflow_slugs\":[\"" + slug + "\"],\"sync\":false}}}"
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json'}
    self.client.post(url, headers=headers, data=payload, name="stop_webservice: " + url)


def create_stream(self, jwt, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows"
    payload = payload_create_stream
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json'}
    response = self.client.post(url, headers=headers, data=payload, name="create_stream: " + url)
    slug = (json.loads(response.text)['data']['attributes']['slug'])
    return slug


def get_stream(self, jwt, slug, u):
    url = ""+Env+"/api/v2/"+u+"/projects/testproject/workflows/"+slug
    payload = {}
    headers = {'Authorization': 'Bearer '+jwt}
    self.client.get(url, headers=headers, data=payload, name="Stream info: "+url)


def stop_stream(self, jwt, slug, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows/stop_workflows"
    payload = "{\"data\":{\"attributes\":{\"workflow_slugs\":[\"" + slug + "\"],\"sync\":false}}}"
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json'}
    self.client.post(url, headers=headers, data=payload, name="stop_stream: " + url)


def create_batch(self, jwt, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows"
    payload = payload_create_batch
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json'}
    response = self.client.post(url, headers=headers, data=payload, name="create_batch: " + url)
    slug = (json.loads(response.text)['data']['attributes']['slug'])
    return slug


def get_batch(self, jwt, slug, u):
    url = ""+Env+"/api/v2/"+u+"/projects/testproject/workflows/"+slug
    payload = {}
    headers = {'Authorization': 'Bearer '+jwt}
    self.client.get(url, headers=headers, data=payload, name="Batch info: "+url)


def stop_batch(self, jwt, slug, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows/stop_workflows"
    payload = "{\"data\":{\"attributes\":{\"workflow_slugs\":[\"" + slug + "\"],\"sync\":false}}}"
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json'}
    self.client.post(url, headers=headers, data=payload, name="stop_batch: " + url)


def create_voila(self, jwt, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows"
    payload = payload_voila_app
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json'}
    response = self.client.post(url, headers=headers, data=payload, name="create_voila: " + url)
    slug = (json.loads(response.text)['data']['attributes']['slug'])
    return slug


def get_voila(self, jwt, slug, u):
    url = ""+Env+"/api/v2/"+u+"/projects/testproject/workflows/"+slug
    payload = {}
    headers = {'Authorization': 'Bearer '+jwt}
    self.client.get(url, headers=headers, data=payload, name="Voila info: "+url)


def stop_voila(self, jwt, slug, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows/stop_workflows"
    payload = "{\"data\":{\"attributes\":{\"workflow_slugs\":[\"" + slug + "\"],\"sync\":false}}}"
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json'}
    self.client.post(url, headers=headers, data=payload, name="stop_voila: " + url)


def create_shiny(self, jwt, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows"
    payload = payload_shiny_app
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json'}
    response = self.client.post(url, headers=headers, data=payload, name="create_shiny: " + url)
    slug = (json.loads(response.text)['data']['attributes']['slug'])
    return slug


def get_shiny(self, jwt, slug, u):
    url = ""+Env+"/api/v2/"+u+"/projects/testproject/workflows/"+slug
    payload = {}
    headers = {'Authorization': 'Bearer '+jwt}
    self.client.get(url, headers=headers, data=payload, name="Shiny info: "+url)


def stop_shiny(self, jwt, slug, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows/stop_workflows"
    payload = "{\"data\":{\"attributes\":{\"workflow_slugs\":[\"" + slug + "\"],\"sync\":false}}}"
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json'}
    self.client.post(url, headers=headers, data=payload, name="stop_shiny: " + url)


def create_dash(self, jwt, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows"
    payload = payload_dash_app
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json'}
    response = self.client.post(url, headers=headers, data=payload, name="create_dash: " + url)
    slug = (json.loads(response.text)['data']['attributes']['slug'])
    return slug


def get_dash(self, jwt, slug, u):
    url = ""+Env+"/api/v2/"+u+"/projects/testproject/workflows/"+slug
    payload = {}
    headers = {'Authorization': 'Bearer '+jwt}
    self.client.get(url, headers=headers, data=payload, name="Dash info: "+url)


def stop_dash(self, jwt, slug, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows/stop_workflows"
    payload = "{\"data\":{\"attributes\":{\"workflow_slugs\":[\"" + slug + "\"],\"sync\":false}}}"
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json'}
    self.client.post(url, headers=headers, data=payload, name="stop_dash: " + url)


def delete_workspace(self, jwt, slug, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows/delete_workflows"
    payload = "{\"data\":{\"attributes\":{\"workflow_slugs\":[\"" + slug + "\"]}}}"
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json'}
    self.client.post(url, headers=headers, data=payload, name="delete_workspace: " + url)


def delete_experiment(self, jwt, slug, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows/delete_workflows"
    payload = "{\"data\":{\"attributes\":{\"workflow_slugs\":[\"" + slug + "\"]}}}"
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json'}
    self.client.post(url, headers=headers, data=payload, name="delete_experiment: " + url)


def delete_webservice(self, jwt, slug, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows/delete_workflows"
    payload = "{\"data\":{\"attributes\":{\"workflow_slugs\":[\"" + slug + "\"]}}}"
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json'}
    self.client.post(url, headers=headers, data=payload, name="delete_webservice: " + url)


def delete_stream(self, jwt, slug, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows/delete_workflows"
    payload = "{\"data\":{\"attributes\":{\"workflow_slugs\":[\"" + slug + "\"]}}}"
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json'}
    self.client.post(url, headers=headers, data=payload, name="delete_stream: " + url)


def delete_batch(self, jwt, slug, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows/delete_workflows"
    payload = "{\"data\":{\"attributes\":{\"workflow_slugs\":[\"" + slug + "\"]}}}"
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json'}
    self.client.post(url, headers=headers, data=payload, name="delete_batch: " + url)


def delete_voila(self, jwt, slug, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows/delete_workflows"
    payload = "{\"data\":{\"attributes\":{\"workflow_slugs\":[\"" + slug + "\"]}}}"
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json'}
    self.client.post(url, headers=headers, data=payload, name="delete_voila: " + url)


def delete_shiny(self, jwt, slug, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows/delete_workflows"
    payload = "{\"data\":{\"attributes\":{\"workflow_slugs\":[\"" + slug + "\"]}}}"
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json'}
    self.client.post(url, headers=headers, data=payload, name="delete_shiny: " + url)


def delete_dash(self, jwt, slug, u):
    url = "" + Env + "/api/v2/" + u + "/projects/testproject/workflows/delete_workflows"
    payload = "{\"data\":{\"attributes\":{\"workflow_slugs\":[\"" + slug + "\"]}}}"
    headers = {'Authorization': 'Bearer ' + jwt, 'Content-Type': 'application/json'}
    self.client.post(url, headers=headers, data=payload, name="delete_dash: " + url)



