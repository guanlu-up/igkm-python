# igkm

这是键盘鼠标模拟输入工具，依赖igkm服务。可远程调本机或者其他机器的硬件输入

## 内容列表

- [依赖](#依赖)
- [快速开始](#快速开始)

## 依赖

- 幽灵键鼠
- igkm服务

## 快速开始

- 在要操作的电脑上插入幽灵键鼠
- 在要操作的电脑上启动igkm.exe（igkmlib32.dll和igkm.exe在同级目录）
- 安装依赖库,python调用

```shell
# 安装依赖
pip install -r requirements.txt
```

```python
if __name__ == '__main__':
    from rfc import RFC
    from mouse import Mouse
    from device import Device

    rfc = RFC("http://localhost:5000")
    code = Device(rfc).is_device_connected()
    print(f"code:{code}")
    code = Mouse(rfc).is_mouse_pressed(3)
    print(code)
```

```python
if __name__ == '__main__':
    from rfc import RFC
    from keyboard import KeyBoard

    rfc = RFC("http://localhost:5000")
    code = KeyBoard(rfc).input_string("123")
    print(code)
```

### 键盘参照

![mapper.png](mapper.png)
