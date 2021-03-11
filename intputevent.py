#!/usr/bin/python
"""
https://www.kernel.org/doc/Documentation/input/input.txt
struct input_event {
    struct timeval time;
    unsigned short type;
    unsigned short code;
    unsigned int value;
};

event code:
https://www.kernel.org/doc/Documentation/input/event-codes.txt
https://github.com/torvalds/linux/blob/master/include/uapi/linux/input-event-codes.h#L75

"""
import struct
import sys
from typing import Union, BinaryIO

FORMAT = "llHHI"

# type
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
EV_MAX = 0x1F

# code
KEY_ENTER = 28
KEY_UP = 103
KEY_LEFT = 105
KEY_RIGHT = 106
KEY_DOWN = 108
KEY_BACKSPACE = 14

# value
KEY_RELEASE = 0
KEY_PRESS = 1
KEY_AUTOREPEAT = 2

EVENT_SIZE = struct.calcsize(FORMAT)


class Event:
    def __init__(self, tv_sec, tv_usec, type, code, value):
        self.tv_sec = tv_sec
        self.tv_usec = tv_usec
        self.type = type
        self.code = code
        self.value = value

    def __str__(self):
        return f"Event type {self.type}, code {self.code}, value {self.value} at {self.tv_sec}.{self.tv_usec}"

    __repr__ = __str__


def read_event(fp: BinaryIO) -> Union[Event, None]:
    """
    :param fp: /dev/input/eventX IO
    """
    event_bytes = fp.read(EVENT_SIZE)
    if not event_bytes:
        return
    return Event(*struct.unpack(FORMAT, event_bytes))


if __name__ == "__main__":
    event_path = "/dev/input/event" + (sys.argv[1] if len(sys.argv) > 1 else "0")

    event_fp = open(event_path, "rb")
    event = read_event(event_fp)
    while event:
        if event.type == EV_KEY:
            if event.value == KEY_RELEASE:
                action = "Release"
            elif event.value == KEY_PRESS:
                action = "Press"
            else:
                action = "AutoRepeat"
            print(f"Key: {event.code}, Action: {action}")
        event = read_event(event_fp)
    event_fp.close()
