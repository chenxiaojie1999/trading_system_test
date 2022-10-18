# -*- coding: utf-8 -*-
# @Author     : Bonnie
# @Time       : 2022/10/14 22:19
# @FileName   : LoginPage.py
# @Description:
from base.LoginBase import LoginBase


class LoginPage(LoginBase):
    def login_input_value(self, driver, input_placehoder, input_value):
        """
        登录页输入值
        :param driver:
        :param input_placehoder:
        :param input_value:
        :return:
        """
        input_xpath = self.login_input(input_placehoder)
        return driver.find_element_by_xpath(input_xpath).send_keys(input_value)

    def click_login(self, driver, button_name):
        """
        点击登录
        :param driver:
        :param button_name:
        :return:
        """
        button_xpath = self.login_button(button_name)
        return driver.find_element_by_xpath(button_xpath).click()
