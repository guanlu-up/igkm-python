import rfc_server


class BaseKeyboard(object):
    """键盘的模拟操作"""

    def __init__(self, server_url=None):
        self.server = rfc_server.RFC(server_url)

    @staticmethod
    def _request_params(function="", value=None, _type=None):
        if value is None or _type is None:
            return {"function": function}
        return {
            "function": function,
            "params": [{"value": value, "type": _type}]
        }

    def press_key_by_code(self, code):
        """ 根据键值来按下对应的键
        :param code: 键值; 整数类型,取值范围0-255
        :return: 1：按键成功; 0：按键失败,键无效或设备未执行;
        """
        params = self._request_params("PressKeyByValue", str(code), 0)
        response = self.server.request(params=params)
        return response["result"]

    def release_key_by_code(self, code):
        """ 根据键值来释放按下的键
        :param code: 键值; 整数类型,取值范围0-255
        :return: 1：释放成功; 0：释放失败,键无效或设备未执行;
        """
        params = self._request_params("ReleaseKeyByValue", str(code), 0)
        response = self.server.request(params=params)
        return response["result"]

    def press_and_release_key_by_code(self, code):
        """ 根据键值来按下对应的键并立即释放键
        :param code: 键值; 整数类型,取值范围0-255
        :return: 1：按键成功; 0：按键失败,键无效或设备未执行;
        """
        params = self._request_params("PressAndReleaseKeyByValue", str(code), 0)
        response = self.server.request(params=params)
        return response["result"]

    def press_key_by_name(self, name):
        """ 根据键名按下对应的键
        :param name: 键名
        :return: 1：按键成功; 0：按键失败,键无效或设备未执行;
        """
        params = self._request_params("PressKeyByName", str(name), 0)
        response = self.server.request(params=params)
        return response["result"]

    def release_key_by_name(self, name):
        """ 根据键名释放对应的键
        :param name: 键名
        :return: 1：释放成功; 0：释放失败,键无效或设备未执行;
        """
        params = self._request_params("ReleaseKeyByName", str(name), 0)
        response = self.server.request(params=params)
        return response["result"]

    def press_and_release_key_by_name(self, name):
        """ 根据键值来按下对应的键并立即释放键
        :param name: 键名
        :return: 1：按键成功; 0：按键失败,键无效或设备未执行;
        """
        params = self._request_params("PressAndReleaseKeyByName", str(name), 0)
        response = self.server.request(params=params)
        return response["result"]

    def is_key_pressed_by_name(self, name):
        """ 根据键名判断指定键是否按下
        :param name: 键名
        :return: 1：键被按下; 0：键没按下,键无效或设备未执行;
        """
        params = self._request_params("IsKeyPressedByName", str(name), 0)
        response = self.server.request(params=params)
        return response["result"]

    def release_all_key(self):
        """ 释放所有键盘被按下的键
        :return: 1：表示成功 0：表示失败
        """
        params = self._request_params("ReleaseAllKey")
        response = self.server.request(params=params)
        return response["result"]

    def input_string(self, text):
        """ 输入字符串,支持中英文及各种符号混合输入,可做到与大写锁定状态无关
        :param text: 要输入的字符串
        :return: int; 表示输入成功的字符串长度
        """
        params = self._request_params("InputString", text, 1)
        response = self.server.request(params=params)
        return response["result"]

    def get_keyboard_light(self):
        """ 获取所有键盘锁定（键盘灯）状态
        :return:
            大于0：表示有锁定（灯亮），具体含义请参考接口说明
            0：表示无锁定（灯全部熄灭）或设备未执行
        """
        params = self._request_params("GetKeyboardLight")
        response = self.server.request(params=params)
        return response["result"]

    def get_caps_lock(self):
        """ 获取CapsLock（大写锁定）状态
        :return: 1：表示锁定（灯亮）; 0：表示未锁定（灯灭）
        """
        params = self._request_params("GetCapsLock")
        response = self.server.request(params=params)
        return response["result"]

    def get_num_lock(self):
        """ 获取NumLock（数字键盘锁定）状态
        :return: 1：表示锁定（灯亮）; 0：表示未锁定（灯灭）
        """
        params = self._request_params("GetNumLock")
        response = self.server.request(params=params)
        return response["result"]

    def set_press_key_delay(self, min_delay, max_delay):
        """ 设置按键延时范围，用于PressAndReleaseKey接口按下与释放之间的随机延时;
        该功能无记忆，服务每次运行都要重新设置，否则将使用默认值
        :param min_delay:整数类型，最小延时时间，单位毫秒，默认30
        :param max_delay:整数类型，最大延时时间，单位毫秒，默认100
        :return: 1：表示成功; 0：表示失败
        """
        params = {
            "function": "SetPressKeyDelay",
            "params": [{"value": min_delay, "type": 0},
                       {"value": max_delay, "type": 0}]
        }
        response = self.server.request(params=params)
        return response["result"]

    def set_input_string_interval_time(self, min_delay, max_delay):
        """ 设置输入字符串的间隔时间范围，用于InputString接口输入每个字符时的随机时间;
        该功能无记忆，软件每次运行都要重新设置，否则将使用默认值
        :param min_delay:整数类型，最小延时时间，单位毫秒，默认60
        :param max_delay:整数类型，最大延时时间，单位毫秒，默认200
        :return: 1：表示成功; 0：表示失败
        """
        params = {
            "function": "SetInputStringIntervalTime",
            "params": [{"value": min_delay, "type": 0},
                       {"value": max_delay, "type": 0}]
        }
        response = self.server.request(params=params)
        return response["result"]

    def set_case_sensitive(self, discriminate):
        """ 设置按键时是否区分字母键的大小写，以及是否自动应用shift键;
        该功能无记忆，软件每次运行都要重新设置，否则将使用默认值
        :param discriminate:整数类型，1区分，0不区分，默认1
        :return: 1：表示成功; 0：表示失败
        """
        params = self._request_params("SetCaseSensitive", discriminate, 0)
        response = self.server.request(params=params)
        return response["result"]

