from datetime import datetime


class DataHelper:

    @staticmethod
    def get_unique_string_by_time():
        return datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
