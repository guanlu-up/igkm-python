from typing import Union
import requests


class RFC(object):
    """与usb服务的通信"""

    def __init__(self, url=None):
        localhost = "http://localhost:5000"
        self.url = url or localhost

    def __call__(self, params: Union[dict, None] = None):
        return self.request(params=params)

    @property
    def default_headers(self):
        return {
            'Content-Type': 'application/json',
        }

    @staticmethod
    def _error_response(status_code, result_message="server error", result=""):
        return {
            "resultCode": status_code,
            "resultMsg": result_message,
            "result": result,
        }

    def request(self, params: Union[dict, None] = None):
        params = params or {}
        headers = self.default_headers
        try:
            response = requests.request(
                "POST", self.url, headers=headers, json=params, timeout=(3, 30))
            if response.status_code == 200:
                return response.json(), True
            return self._error_response(response.status_code), False
        except Exception as error:
            return self._error_response(500, str(error)), False
