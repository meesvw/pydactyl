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

    """
    User endpoints
    """
    def get_users(self):
        return request('GET', self.url + 'users/', headers=self.headers).json()['data']

    def get_user(self, user_id: int):
        return request('GET', self.url + 'users/' + str(user_id), headers=self.headers).json()

    def get_users_external(self, external_id: str):
        return request('GET', self.url + 'users/external/' + external_id, headers=self.headers)

    def update_user(
            self,
            user_id: int,
            email: str = None,
            username: str = None,
            first_name: str = None,
            last_name: str = None,
            admin: bool = False,
            password: str = None
    ):
        payload = {}

        if email:
            payload['email'] = email

        if username:
            payload['username'] = username

        if first_name:
            payload['first_name'] = first_name

        if last_name:
            payload['last_name'] = last_name

        if admin:
            payload['root_admin'] = True

        if password:
            payload['password'] = password

        return request('PATCH', self.url + 'users/' + str(user_id), data=dumps(payload), headers=self.headers)

    def delete_user(self, user_id: int):
        return request('DELETE', self.url + 'users/' + str(user_id), headers=self.headers).json()

    def create_user(
            self, email: str, username: str, first_name: str, last_name: str, admin: bool = False, password: str = None
    ):
        payload = {
            "email": email,
            "username": username,
            "first_name": first_name,
            "last_name": last_name
        }

        if password:
            payload['password'] = password

        if admin:
            payload['root_admin'] = True

        return request('POST', self.url + 'users', data=dumps(payload), headers=self.headers).json()

    """
    Nodes endpoints
    """
    def get_nodes(self):
        return request('GET', self.url + 'nodes', headers=self.headers).json()

    def get_node_configuration(self, node_id: int):
        return request('GET', self.url + 'nodes/' + str(node_id) + '/configuration', headers=self.headers).json()

    def create_node(
            self,
            name: str,
            location_id: int,
            fqdn: str,
            memory: int,
            disk: int,
            scheme: str = "https",
            memory_overallocate: int = 0,
            disk_overallocate: int = 0,
            upload_size: int = 100,
            daemon_sftp: int = 2022,
            daemon_listen: int = 8080
    ):
        payload = {
            "name": name,
            "location_id": location_id,
            "fqdn": fqdn,
            "scheme": scheme,
            "memory": memory,
            "memory_overallocate": memory_overallocate,
            "disk": disk,
            "disk_overallocate": disk_overallocate,
            "upload_size": upload_size,
            "daemon_sftp": daemon_sftp,
            "daemon_listen": daemon_listen
        }
        return request('POST', self.url + 'nodes', data=dumps(payload), headers=self.headers).json()

    def update_node(
            self,
            name: str,
            location_id: int,
            fqdn: str,
            memory: int,
            disk: int,
            scheme: str = "https",
            memory_overallocate: int = 0,
            disk_overallocate: int = 0,
            upload_size: int = 100,
            daemon_sftp: int = 2022,
            daemon_listen: int = 8080
    ):
        payload = {
            "name": name,
            "location_id": location_id,
            "fqdn": fqdn,
            "scheme": scheme,
            "memory": memory,
            "memory_overallocate": memory_overallocate,
            "disk": disk,
            "disk_overallocate": disk_overallocate,
            "upload_size": upload_size,
            "daemon_sftp": daemon_sftp,
            "daemon_listen": daemon_listen
        }
        return request('PATCH', self.url + 'nodes', data=dumps(payload), headers=self.headers).json()

    def delete_node(self, node_id: int):
        return request('DELETE', self.url + 'nodes/' + str(node_id), headers=self.headers)

    def get_node_allocations(self, node_id: int):
        return request('GET', self.url + 'nodes/' + str(node_id) + '/allocations', headers=self.headers).json()

    """
    Location endpoints
    """
    def get_locations(self):
        return request('GET', self.url + 'locations', headers=self.headers).json()

    def get_location(self, location_id: int):
        return request('GET', self.url + 'locations/' + str(location_id), headers=self.headers).json()

    def create_location(self, short: str, long: str = None):
        payload = {"short": short}

        if long:
            payload['long'] = long

        return request(
            'POST', self.url + 'locations', data=dumps(payload), headers=self.headers
        ).json()

    def update_location(self, location_id: int, short: str, long: str = None):
        payload = {"short": short}

        if long:
            payload['long'] = long

        return request(
            'PATCH', self.url + 'locations/' + str(location_id), data=dumps(payload), headers=self.headers
        ).json()

    def delete_location(self, location_id: int):
        return request('DELETE', self.url + 'locations/' + str(location_id), headers=self.headers)

    """
    Database endpoints
    """
    def get_server_databases(self, server_id: int):
        return request('GET', self.url + 'servers/' + str(server_id) + '/databases', headers=self.headers).json()

    def get_server_database(self, server_id: int, database_id: int):
        return request(
            'GET', self.url + 'servers/' + str(server_id) + '/databases/' + str(database_id), headers=self.headers
        )

    # not finished
    def create_server_database(self, server_id: int, database_id: int):
        payload = {}
        return

    def reset_server_database(self, server_id: int, database_id: int):
        return request(
            'POST',
            self.url + 'servers/' + str(server_id) + '/databases/' + str(database_id) + '/reset-password',
            headers=self.headers
        )

    def delete_server_database(self, server_id: int, database_id: int):
        return request(
            'DELETE', self.url + 'servers/' + str(server_id) + '/databases/' + str(database_id), headers=self.headers
        )

    """
    Server endpoints
    """
    def get_servers(self):
        return request('GET', self.url + 'servers', headers=self.headers).json()

    def get_server(self, server_id: int):
        return request('GET', self.url + 'servers/' + str(server_id), headers=self.headers).json()

    def get_server_external(self, external_id: str):
        return request('GET', self.url + 'servers/external/' + external_id)

    # not finished
    def update_server_details(
            self, user_id: int, server_id: int, name: str, external_id: str = None, description: str = None
    ):
        payload = {}
        return request(
            'PATCH', self.url + 'servers/' + str(server_id) + '/details', data=dumps(payload), headers=self.headers
        )

    # not finished
    def update_server_build(self):
        return

    # not finished
    def create_server(
            self,
            user_id: int,
            name: str,
            nest_id: int,
            egg_id: int,
            docker_image: str,
            startup: str,
            environment: dict,
            default_allocation: int
    ):
        payload = {
            "name": name,
            "user": user_id,
            "nest": nest_id,
            "egg": egg_id,
            "docker_image": docker_image,
            "startup": startup,
            "environment": environment,
            "limits": {
                "memory": 1024,
                "swap": 0,
                "disk": 1024,
                "io": 500,
                "cpu": 200
            },
            "feature_limits": {
                "databases": 0,
                "backups": 0
            },
            "allocation": {
                "default": default_allocation
            }
        }
        return request('POST', self.url + 'servers/', data=dumps(payload), headers=self.headers).json()

    def suspend_server(self, server_id: int):
        return request('POST', self.url + 'servers/' + str(server_id) + '/suspend', headers=self.headers)

    def unsuspend_server(self, server_id: int):
        return request('POST', self.url + 'servers/' + str(server_id) + '/unsuspend', headers=self.headers)

    def reinstall_server(self, server_id: int):
        return request('POST', self.url + 'servers/' + str(server_id) + '/reinstall', headers=self.headers)

    def delete_server(self, server_id: int):
        return request('DELETE', self.url + 'servers/' + str(server_id), headers=self.headers)

    def force_delete_server(self, server_id: int):
        return request('DELETE', self.url + 'servers/' + str(server_id) + '/force', headers=self.headers)

    """
    Nest endpoints
    """
    def get_nests(self):
        return request('GET', self.url + 'nests', headers=self.headers).json()

    def get_nest(self, nest_id: int):
        return request('GET', self.url + 'nests/' + str(nest_id), headers=self.headers).json()

    def get_nest_eggs(self, nest_id: int):
        return request('GET', self.url + 'nests/' + str(nest_id) + '/eggs', headers=self.headers).json()

    def get_nest_egg(self, nest_id: int, egg_id: int):
        return request('GET', self.url + 'nests/' + str(nest_id) + '/eggs/' + str(egg_id), headers=self.headers).json()
