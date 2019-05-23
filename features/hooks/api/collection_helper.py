from features.hooks.api import constants
from features.hooks.api.request_helper import RequestHelper


class CollectionHelper:

    @staticmethod
    def create_company(user_token, request_payload):
        response = RequestHelper().send_post_request(user_token, constants.CREATE_COLLECTION, request_payload)
        return response
