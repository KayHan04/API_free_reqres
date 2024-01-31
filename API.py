import requests
import json


class Testclass:

    def __init__(self):
        self.base_url = 'https://reqres.in'

    def get_list_users(self) -> json:
        res = requests.get(self.base_url + '/api/users?page=2')
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def get_single_user(self) -> json:
        res = requests.get(self.base_url + '/api/users?page=2')
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def get_not_found_user(self) -> json:
        res = requests.get(self.base_url + '/api/users/23')
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def get_list(self) -> json:
        res = requests.get(self.base_url + '/api/unknown')
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def get_single(self) -> json:
        res = requests.get(self.base_url + '/api/unknowm/2')
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def get_single_not_found(self) -> json:
        res = requests.get(self.base_url + '/api/unknowm/23')
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def post_create_user(self) -> json:
        data = {"name": 'morpheus',
                "job": 'leader'}
        res = requests.post(self.base_url + '/api/users', data=data)
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def put_update_user(self) -> json:
        data = {
            "name": "morpheus",
            "job": "zion resident"
        }
        res = requests.post(self.base_url + '/api/users/2', data=data)
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def patch_update_user(self) -> json:
        data = {
            "name": "morpheus",
            "job": "zion resident"
        }
        res = requests.patch(self.base_url + '/api/users/2', data=data)
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def delete_user(self) -> json:
        res = requests.delete(self.base_url + '/api/users')
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def post_register(self) -> json:
        data = {"email": "eve.holt@reqres.in",
                "password": "pistol"
                }
        res = requests.post(self.base_url + '/api/register', data=data)
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def post_register_unsuccessful(self) -> json:
        data = {"email": "eve.holt@reqres.in"
                }
        res = requests.post(self.base_url + '/api/register', data=data)
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def post_login_successful(self) -> json:
        data = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        res = requests.post(self.base_url + '/api/login', data=data)
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def post_login_unsuccessful(self) -> json:
        data = {
            "email": "peter@klaven"
        }
        res = requests.post(self.base_url + '/api/login', data=data)
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault

    def get_delayed(self) -> json:
        res = requests.get(self.base_url + "/api/users?delay=3")
        status = res.status_code
        resault = ""
        try:
            resault = res.json()
        except json.decoder.JSONDecodeError:
            resault = res.text
        return status, resault
