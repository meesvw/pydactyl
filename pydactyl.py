from requests import request
from json import dumps


class Application:
    def __init__(self, url: str, api_key: str):
        self.url = url + '/api/application/'
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def get_users(self):
        return request('GET', self.url + 'users/', headers=self.headers).json()['data']

    def get_user(self, user_id: int):
        return request('GET', self.url + 'users/' + str(user_id), headers=self.headers).json()

    # not finished
    def update_user(self, user_id: int):
        payload = {}
        return request('PATCH', self.url + 'users' + str(user_id), payload=dumps(payload), headers=self.headers)

    def delete_user(self, user_id: int):
        return request('DELETE', self.url + 'users/' + str(user_id), headers=self.headers).json()

    def create_user(
            self, email: str, username: str, first_name: str, last_name: str, admin: bool = False, password: str = None
    ):
        payload = {
            'email': email,
            'username': username,
            'first_name': first_name,
            'last_name': last_name
        }

        if password:
            payload['password'] = password

        if admin:
            payload['root_admin'] = True

        return request('POST', self.url + 'users', data=dumps(payload), headers=self.headers).json()
