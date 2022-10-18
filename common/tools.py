# -*- coding: utf-8 -*-
# @Author     : Bonnie
# @Time       : 2022/10/9 0:29
# @FileName   : tools.py
# @Description:

import datetime
import os


def get_now_time():
    return datetime.datetime.now()


def get_project_path():
    """
    获取项目的绝对路径
    :return:
    """
    project_name = "trading_system_test"
    file_path = os.path.dirname(__file__)
    # print(file_path[:file_path.find(project_name)+len(project_name)])
    return file_path[:file_path.find(project_name) + len(project_name)]


def sep(path, add_sep_before=False, add_sep_after=False):
    """

    :param path: 路径列表，类型为数组
    :param add_sep_before: 是否需要在拼接的路径前加一个分隔符
    :param add_sep_after: 是否需要在拼接的路径后加一个分隔符
    :return:
    """
    all_path = os.sep.join(path)
    if add_sep_before:
        all_path = os.sep + all_path
    if add_sep_after:
        all_path = all_path + os.sep
    # print(all_path)
    return all_path


if __name__ == '__main__':
    print(get_now_time())
    get_project_path()
    sep(["config", "environment.yaml"], add_sep_before=True)
