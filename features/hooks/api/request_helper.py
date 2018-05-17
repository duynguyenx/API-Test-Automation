import json
import logging

import requests

from conf.environment_setup import EnvSetup
from features.hooks.api import constants


class RequestHelper(object):
    logger = logging.getLogger(__name__)

    @staticmethod
    def print_response_json(request):
        RequestHelper.logger.debug('Response code: %s', request.status_code)
        if request.status_code != constants.RESPONSE_CODE_SUCCESSFUL_NO_CONTENT:
            RequestHelper.logger.debug(u'''Response json:
                {json}'''.format(json=request.json()))

    @staticmethod
    def send_post_request(session, end_point, data=''):
        url = EnvSetup.API_HOST + end_point
        RequestHelper.logger.debug(u'''Sending POST request
            URL  = {url}
            Data = {data}'''.format(url=url, data=data))
        headers = session.get_auth_token()
        headers.update({'content-type': 'application/json'})
        response = requests.post(url, headers=headers, data=json.dumps(data))
        RequestHelper.print_response_json(response)
        return response

    @staticmethod
    def send_patch_request(session, end_point, data=None):
        url = EnvSetup.API_HOST + end_point
        RequestHelper.logger.debug(u'''Sending PATCH request
            URL  = {url}
            Data = {data}'''.format(url=url, data=data))
        headers = session.get_auth_token()
        headers.update({'content-type': 'application/json'})
        if data:
            response = requests.patch(url, headers=headers, data=json.dumps(data))
        else:
            response = requests.patch(url, headers=headers)
        RequestHelper.print_response_json(response)
        return response

    @staticmethod
    def send_delete_request(session, end_point, data=None):
        url = EnvSetup.API_HOST + end_point
        RequestHelper.logger.debug(u'''Sending DELETE request
            URL  = {url}'''.format(url=url))
        if data:
            response = requests.delete(url, headers=session.get_auth_token(), data=json.dumps(data))
        else:
            response = requests.delete(url, headers=session.get_auth_token())

        RequestHelper.print_response_json(response)
        return response

    @staticmethod
    def send_get_request(session, end_point, data=None):
        url = EnvSetup.API_HOST + end_point
        RequestHelper.logger.debug(u'''Sending GET request
            URL  = {url}'''.format(url=url))
        if data:
            response = requests.get(url, headers=session.get_auth_token())
        else:
            response = requests.get(url, headers=session.get_auth_token(), data=data)
        RequestHelper.print_response_json(response)
        return response

    @staticmethod
    def is_object_in_response_list(request, attribute_name, attribute_value):
        for element in request.json():
            element_value = element[attribute_name]
            if element_value == attribute_value:
                return True
        return False

    @staticmethod
    def is_valid_url(session, endpoint):
        response = RequestHelper.send_get_request(session, endpoint)
        if response.status_code not in (constants.RESPONSE_CODE_SUCCESSFUL,
                                        constants.RESPONSE_CODE_SUCCESSFUL_NO_CONTENT):
            return False
        return True
