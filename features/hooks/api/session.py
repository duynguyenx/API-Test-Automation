class Session(object):
    __auth_token = None

    def __init__(self, auth_token):
        self.__auth_token = auth_token

    def get_auth_token(self):
        return self.__auth_token