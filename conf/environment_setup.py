import os


class EnvSetup:
    API_HOST = os.getenv('API_HOST', 'https://unsplash.com/napi')
    API_USER_HARD_TOKEN = os.getenv('API_TOKEN', 'Bearer 6c5803fe24f515379cbcea562ba2e9f890543ea28d850ffb64fc3e951724ffc3')