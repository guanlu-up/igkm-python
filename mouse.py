import rfc_server


class Mouse(object):
    """鼠标的模拟操作"""

    def __init__(self, server_url=None):
        """接收应用服务的URL, 可以是远程也可以是本地,None则表示本地"""
        self.server = rfc_server.RFC(server_url)

    @staticmethod
    def _request_params(function="", value=None, _type=None):
        if value is None or _type is None:
            return {"function": function}
        return {
            "function": function,
            "params": [{"value": value, "type": _type}]
        }

    def press_mouse(self, code="1"):
        """ 按下鼠标键
        :param code: 鼠标键序号（1:左键 2:中键 3:右键）
        :return: 1:成功 0:失败
        """
        params = self._request_params("PressMouseButton", str(code), 0)
        response = self.server.request(params=params)
        return response["result"]

    def release_mouse(self, code="1"):
        """ 释放已按下的鼠标键
        :param code: 鼠标键序号（1:左键 2:中键 3:右键）
        :return: 1:成功 0:失败
        """
        params = self._request_params("ReleaseMouseButton", str(code), 0)
        response = self.server.request(params=params)
        return response["result"]

    def press_and_release_mouse(self, code="1"):
        """ 按下并释放鼠标键，按下的随机延时时间可通过SetPressMouseButtonDelay设置
        :param code: 鼠标键序号（1:左键 2:中键 3:右键）
        :return: 1:成功 0:失败
        """
        params = self._request_params("PressAndReleaseMouseButton", str(code), 0)
        response = self.server.request(params=params)
        return response["result"]

    def is_mouse_pressed(self, code="1"):
        """ 判断指定的鼠标键是否按下
        :param code: 鼠标键序号（1:左键 2:中键 3:右键）
        :return: 1：键已按下 0：键未按下
        """
        params = self._request_params("IsMouseButtonPressed", str(code), 0)
        response = self.server.request(params=params)
        return response["result"]

    def release_all_mouse(self):
        """ 释放所有鼠标按键
        :return: 1:成功 0:失败
        """
        params = self._request_params("ReleaseAllMouseButton")
        response = self.server.request(params=params)
        return response["result"]

    def move_mouse_to(self, x, y):
        """ 从当前位置移动鼠标到屏幕的指定坐标;
        屏幕左上角坐标为0,0，右下角坐标为屏幕分辨率值减1
        如800*600的屏幕分辨率有效坐标范围为0,0 ~ 799,599
        :param x:屏幕的X坐标，取值范围为正整数
        :param y:屏幕的Y坐标，取值范围为正整数
        :return: 1:成功 0:失败
        """
        params = {
            "function": "MoveMouseTo",
            "params": [{"value": str(x), "type": 0},
                       {"value": str(y), "type": 0}]
        }
        response = self.server.request(params=params)
        return response["result"]

    def move_mouse_relative(self, x, y):
        """ 从当前位置相对移动鼠标;
        :param x:水平移动距离，取值范围为-127 ~ +127，正数为向右移动，负数为向左移动
        :param y:垂直移动距离，取值范围为-127 ~ +127，正数为向下移动，负数为向上移动
        :return: 1:成功 0:失败
        """
        params = {
            "function": "MoveMouseRelative",
            "params": [{"value": str(x), "type": 0},
                       {"value": str(y), "type": 0}]
        }
        response = self.server.request(params=params)
        return response["result"]

    def move_mouse_wheel(self, distance):
        """ 移动鼠标滚轮;
        :param distance:鼠标滚轮移动距离，取值范围为-127 ~ +127，正数向上移动，负数向下移动
        :return: 1:成功 0:失败
        """
        params = self._request_params("MoveMouseWheel", str(distance), 0)
        response = self.server.request(params=params)
        return response["result"]

    def get_mouse_position(self):
        """ 获取鼠标(X, Y)坐标
        :return: (X, Y)
        """
        params = self._request_params("GetMousePosition")
        response = self.server.request(params=params)
        position = response["result"]
        if position:
            return position >> 16 & 0xFFFF, position & 0xFFFF
        return -1, -1

    def get_mouse_x(self):
        """ 获取鼠标X坐标
        :return: position
        """
        params = self._request_params("GetMouseX")
        response = self.server.request(params=params)
        return response["result"]

    def get_mouse_y(self):
        """ 获取鼠标Y坐标
        :return: position
        """
        params = self._request_params("GetMouseY")
        response = self.server.request(params=params)
        return response["result"]

    def set_mouse_position(self, x, y):
        """
        设置鼠标位置，该接口和MoveMouseTo不同，
        MoveMouseTo是从当前位置移动到指定坐标，
        该接口是先把鼠标移动到(0,0)位置，然后再从(0,0)位置移动到指定坐标，主要用于双机互联设备，
        无法确定鼠标当前的位置时也可以精确设定鼠标位置，调用该接口后被控端鼠标当前位置即为设定位置
        :param x: 屏幕的X坐标，取值范围为正整数
        :param y:屏幕的Y坐标，取值范围为正整数
        :return: 1:成功 0:失败
        """
        params = {
            "function": "SetMousePosition",
            "params": [{"value": str(x), "type": 0},
                       {"value": str(y), "type": 1}]
        }
        response = self.server.request(params=params)
        return response["result"]

    def set_press_mouse_delay(self, min_delay, max_delay):
        """ 设置鼠标按键延时;
        用于PressAndReleaseMouseButton接口的按下延随机延时时间
        该功能无记忆，软件每次运行都要重新设置，否则将使用默认值
        :param min_delay:最小延时时间，单位毫秒，默认30
        :param max_delay:最大延时时间，单位毫秒，默认100
        :return: 1:成功 0:失败
        """
        params = {
            "function": "SetPressMouseButtonDelay",
            "params": [{"value": str(min_delay), "type": 0},
                       {"value": str(max_delay), "type": 1}]
        }
        response = self.server.request(params=params)
        return response["result"]

    def set_mouse_movement_delay(self, min_delay, max_delay):
        """ 设置鼠标每两次移动之间的间隔时间;
        用于MoveMouseTo和SetMousePosition接口，
        该功能无记忆，软件每次运行都要重新设置，否则将使用默认值
        :param min_delay:最小延时时间，单位毫秒，默认30
        :param max_delay:最大延时时间，单位毫秒，默认100
        :return: 1:成功 0:失败
        """
        params = {
            "function": "SetMouseMovementDelay",
            "params": [{"value": str(min_delay), "type": 0},
                       {"value": str(max_delay), "type": 1}]
        }
        response = self.server.request(params=params)
        return response["result"]

    def set_mouse_movement_speed(self, speed_value):
        """ 设置鼠标移动速度;
        移动速度分为10个等级,等级越高移动速度越快，
        该功能无记忆,软件每次运行都要重新设置,否则将使用默认值
        :param speed_value:移动速度，取值范围1-10，其他值无效，默认7
        :return: 1:成功 0:失败
        """
        params = self._request_params("SetMouseMovementSpeed", str(speed_value), 0)
        response = self.server.request(params=params)
        return response["result"]
