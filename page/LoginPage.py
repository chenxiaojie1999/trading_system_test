# -*- coding: utf-8 -*-
# @Author     : Bonnie
# @Time       : 2022/10/14 22:19
# @FileName   : LoginPage.py
# @Description:
from selenium.webdriver.common.by import By
from base.LoginBase import LoginBase
from base.ObjectMap import ObjectMap
from common.yaml_config import GetConf


class LoginPage(LoginBase, ObjectMap):
    def login_input_value(self, driver, input_placehoder, input_value):
        """
        登录页输入值
        :param driver:
        :param input_placehoder:
        :param input_value:
        :return:
        """
        input_xpath = self.login_input(input_placehoder)
        # return driver.find_element_by_xpath(input_xpath).send_keys(input_value)
        return self.element_fill_value(driver, By.XPATH, input_xpath, input_value)

    def click_login(self, driver, button_name):
        """
        点击登录
        :param driver:
        :param button_name:
        :return:
        """
        button_xpath = self.login_button(button_name)
        # return driver.find_element_by_xpath(button_xpath).click()
        return self.element_click(driver, By.XPATH, button_xpath)

    def login(self, driver, user):
        """
        登录
        :param driver:
        :param user:
        :return:
        """
        self.element_to_url(driver, "/login")
        username, password = GetConf().get_username_password(user)
        self.login_input_value(driver, "用户名", username)
        self.login_input_value(driver, "密码", password)
        self.click_login(driver, "登录")

