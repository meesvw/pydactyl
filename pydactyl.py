import asyncio
import aiohttp
from json import dumps


class Client:
    def __init__(self, url: str, api_key: str):
        self.url = url + '/api/client/'
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    """
    Account endpoints
    """
    async def account(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'account'
            return await (await session.get(url)).json()

    """
    Server endpoints
    """
    async def power(self, identifier: str, signal: str):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            payload = {'signal': signal}
            url = self.url + 'servers/' + identifier + '/power'
            return await (await session.post(url, data=dumps(payload))).json()


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
    async def get_users(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'users/'
            return await (await session.get(url)).json()

    async def get_user(self, user_id: int):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'users/' + str(user_id)
            return await (await session.get(url)).json()

    async def get_users_external(self, external_id: str):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'users/external/' + external_id
            return await (await session.get(url)).json()

    async def update_user(
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

        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'users/' + str(user_id)
            return await (await session.patch(url, data=dumps(payload))).json()

    async def delete_user(self, user_id: int):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'users/' + str(user_id)
            return await (await session.delete(url)).json()

    async def create_user(
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

        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'users'
            return await (await session.post(url, data=dumps(payload))).json()

    """
    Nodes endpoints
    """
    async def get_nodes(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'nodes'
            return await (await session.get(url)).json()

    async def get_node_configuration(self, node_id: int):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'nodes/' + str(node_id) + '/configuration'
            return await (await session.get(url)).json()

    async def create_node(
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

        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'nodes'
            return await (await session.post(url, data=dumps(payload))).json()

    async def update_node(
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
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'nodes'
            return await (await session.patch(url, data=dumps(payload))).json()

    # no aiohttp
    async def delete_node(self, node_id: int):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'nodes/' + str(node_id)
            return await session.delete(url)

    async def get_node_allocations(self, node_id: int):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'nodes/' + str(node_id) + '/allocations'
            return await (await session.get(url)).json()

    """
    Location endpoints
    """
    async def get_locations(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'locations'
            return await (await session.get(url)).json()

    async def get_location(self, location_id: int):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'locations/' + str(location_id)
            return await (await session.get(url)).json()

    async def create_location(self, short: str, long: str = None):
        payload = {"short": short}

        if long:
            payload['long'] = long

        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'locations'
            return await (await session.post(url, data=dumps(payload))).json()

    async def update_location(self, location_id: int, short: str, long: str = None):
        payload = {"short": short}

        if long:
            payload['long'] = long

        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'locations/' + str(location_id)
            return await (await session.patch(url, data=dumps(payload))).json()

    async def delete_location(self, location_id: int):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'locations/' + str(location_id)
            return await session.delete(url)

    """
    Database endpoints
    """
    async def get_server_databases(self, server_id: int):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'servers/' + str(server_id) + '/databases'
            return await (await session.get(url)).json()

    async def get_server_database(self, server_id: int, database_id: int):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'servers/' + str(server_id) + '/databases/' + str(database_id)
            return await (await session.get(url)).json()

    # not finished
    async def create_server_database(self, server_id: int, database_id: int):
        payload = {}
        return

    async def reset_server_database(self, server_id: int, database_id: int):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'servers/' + str(server_id) + '/databases/' + str(database_id) + '/reset-password'
            return await session.post(url)

    async def delete_server_database(self, server_id: int, database_id: int):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'servers/' + str(server_id) + '/databases/' + str(database_id)
            return await session.delete(url)

    """
    Server endpoints
    """
    async def get_servers(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'servers'
            return await (await session.get(url)).json()

    async def get_server(self, server_id: int):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'servers/' + str(server_id)
            return await (await session.get(url)).json()

    async def get_server_external(self, external_id: str):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'servers/external/' + external_id
            return await (await session.get(url)).json()

    # not finished no aiohttp
    async def update_server_details(
            self, user_id: int, server_id: int, name: str, external_id: str = None, description: str = None
    ):
        payload = {}
        # return request(
        #     'PATCH', self.url + 'servers/' + str(server_id) + '/details', data=dumps(payload), headers=self.headers
        # )
        return

    # not finished
    async def update_server_build(self):
        return

    # not finished
    async def create_server(
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
                "memory": 3072,
                "swap": 0,
                "disk": 1024,
                "io": 500,
                "cpu": 400,
                "oom_disabled": False
            },
            "feature_limits": {
                "databases": 0,
                "backups": 0
            },
            "allocation": {
                "default": default_allocation
            }
        }
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'servers/'
            return await (await session.post(url, data=dumps(payload))).json()

    async def suspend_server(self, server_id: int):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'servers/' + str(server_id) + '/suspend'
            return await session.post(url)

    async def unsuspend_server(self, server_id: int):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'servers/' + str(server_id) + '/unsuspend'
            return await session.post(url)

    async def reinstall_server(self, server_id: int):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'servers/' + str(server_id) + '/reinstall'
            return await session.post(url)

    async def delete_server(self, server_id: int):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'servers/' + str(server_id)
            return await session.delete(url)

    async def force_delete_server(self, server_id: int):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'servers/' + str(server_id) + '/force'
            return await session.delete(url)

    """
    Nest endpoints
    """
    async def get_nests(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'nests'
            return await (await session.get(url)).json()

    async def get_nest(self, nest_id: int):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'nests/' + str(nest_id)
            return await (await session.get(url)).json()

    async def get_nest_eggs(self, nest_id: int):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'nests/' + str(nest_id) + '/eggs'
            return await (await session.get(url)).json()

    async def get_nest_egg(self, nest_id: int, egg_id: int):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            url = self.url + 'nests/' + str(nest_id) + '/eggs/' + str(egg_id)
            return await (await session.get(url)).json()
