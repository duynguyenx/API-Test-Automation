import os


class EnvSetup(object):
    API_HOST = os.getenv('API_URL', 'http://api_host:port')