# -*- coding: utf-8 -*-
# @Author     : Bonnie
# @Time       : 2022/10/10 22:45
# @FileName   : yaml_config.py
# @Description:

import yaml
from common.tools import get_project_path, sep


class GetConf:
    def __init__(self):
        # C:\Users\bonnie\PycharmProjects\trading_system_test\config\environment.yaml
        # get_project_path() + sep(["config", "environment.yaml"], add_sep_before=True)
        with open(get_project_path() + sep(["config", "environment.yaml"], add_sep_before=True), "r",
                  encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, yaml.FullLoader)
            print(self.env)

    def get_username_password(self):
        return self.env["username"], self.env["password"]


if __name__ == '__main__':
    print(GetConf().get_username_password())
