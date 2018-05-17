import logging
import urlparse


class DataHelper(object):
    logger = logging.getLogger(__name__)

    @staticmethod
    def get_query_string_list(url):
        return dict(urlparse.parse_qsl(urlparse.urlsplit(url).query))
