# -*- coding: utf-8 -*-
# @Author     : Bonnie
# @Time       : 2022/10/9 0:29
# @FileName   : tools.py
# @Description:

import datetime


def get_now_time():
    return datetime.datetime.now()


if __name__ == '__main__':
    print(get_now_time())
