"""
FORMAT represents the format used by linux kernel input event struct
See https://github.com/torvalds/linux/blob/master/include/uapi/linux/input.h#L28
Stands for: long int, long int, unsigned short, unsigned short, unsigned int

https://github.com/torvalds/linux/blob/master/include/uapi/linux/input-event-codes.h#L38
EV_SYN 同步事件
EV_KEY 键盘事件
EV_REL 相对坐标事件，用于鼠标
EV_ABS 绝对坐标事件，用于摇杆
EV_MSC 其他事件
EV_LED LED灯事件
EV_SND 声音事件
EV_REP 重复按键事件
EV_FF 受力事件
EV_PWR 电源事件
EV_FF_STATUS 受力状态事件
"""
FORMAT = 'llHHI'

EV_SYN = 0x00
EV_KEY = 0x01
EV_REL = 0x02
EV_ABS = 0x03
EV_MSC = 0x04
EV_SW = 0x05
EV_LED = 0x11
EV_SND = 0x12
EV_REP = 0x14
EV_FF = 0x15
EV_PWR = 0x16
EV_FF_STATUS = 0x17
EV_MAX = 0x1f

# https://github.com/torvalds/linux/blob/master/include/uapi/linux/input-event-codes.h#L75
KEY_ENTER = 28
KEY_UP = 103
KEY_LEFT = 105
KEY_RIGHT = 106
KEY_DOWN = 108
KEY_BACKSPACE = 14