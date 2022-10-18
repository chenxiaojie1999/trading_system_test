# -*- coding: utf-8 -*-
# @Author     : Bonnie
# @Time       : 2022/10/14 22:27
# @FileName   : LoginBase.py
# @Description:

class LoginBase:
    def login_input(self, input_placeholder):
        """
        登录用户名、密码输入框
        :param input_placeholder:
        :return:
        """
        return "//input[@placeholder='" + input_placeholder + "']"

    def login_button(self, button_name):
        """
        登录按钮
        :param button_name:
        :return:
        """
        return "//span[text()='" + button_name + "']/parent::button"


if __name__ == '__main__':
    # print(LoginBase().login_input("用户名"))
    print(LoginBase().login_button("登录"))
