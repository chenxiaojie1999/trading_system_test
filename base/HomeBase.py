# -*- coding: utf-8 -*-
# @Author     : Bonnie
# @Time       : 2022/10/19 16:39
# @FileName   : HomeBase.py
# @Description:

class HomeBase:
    def wallet_switch(self):
        """
        首页的钱包开关
        :return:
        """
        return "//span[contains(@class,'switch')]"

    def logo(self):
        """
        进入系统后，首页右上角的logo
        :return:
        """
        return "//div[contains(text(),'二手')]"

    def welcome(self):
        """
        首页，欢迎您回来
        :return:
        """
        return "//span[starts-with(text(),'欢迎您回家’)]"

    def show_date(self):
        """
        首页显示日期
        :return:
        """
        return "//div[text()='我的日历‘]/following-sibling::div"

