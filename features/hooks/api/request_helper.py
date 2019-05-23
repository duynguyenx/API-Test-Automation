import requests
from conf.environment_setup import EnvSetup


class RequestHelper:

    @staticmethod
    def send_post_request(user_token, end_point, data=''):
        url = EnvSetup.API_HOST + end_point
        headers = {'Authorization': user_token}
        headers.update({'content-type': 'application/x-www-form-urlencoded'})
        response = requests.post(url, headers=headers, data=data)
        return response

    @staticmethod
    def send_delete_request(user_token, end_point, data=None):
        url = EnvSetup.API_HOST + end_point
        headers = {'Authorization': user_token}
        headers.update({'content-type': 'application/x-www-form-urlencoded'})
        if data:
            response = requests.delete(url, headers=headers, data=data)
        else:
            response = requests.delete(url, headers=headers)
        return response

    @staticmethod
    def send_get_request(user_token, end_point, data=None):
        url = EnvSetup.API_HOST + end_point
        headers = {'Authorization': user_token}
        headers.update({'content-type': 'application/x-www-form-urlencoded'})
        if data:
            response = requests.get(url, headers=headers, data=data)
        else:
            response = requests.get(url, headers=headers)
        return response
