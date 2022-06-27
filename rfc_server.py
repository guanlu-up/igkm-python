from typing import Union
import requests


class RFC(object):
    """与usb服务的通信"""

    def __init__(self, url=None):
        localhost = "http://localhost:5000/rfc"
        self.url = url or localhost

    def __call__(self, params: Union[dict, None] = None):
        return self.request(params=params)

    @property
    def default_headers(self):
        return {
            'Content-Type': 'application/json',
        }

    @staticmethod
    def _error_response(status_code, result_message="server error", result=0):
        return {
            "resultCode": status_code,
            "resultMsg": result_message,
            "result": result,
        }

    def request(self, params: Union[dict, None] = None):
        """ 向USB服务发送键盘指令
        :return:
        """
        params = params or {}
        headers = self.default_headers
        try:
            response = requests.request(
                "POST", self.url, headers=headers, json=params, timeout=(3, 30))
            if response.status_code == 200:
                return response.json()
            return self._error_response(response.status_code)
        except Exception as error:
            return self._error_response(500, str(error))
