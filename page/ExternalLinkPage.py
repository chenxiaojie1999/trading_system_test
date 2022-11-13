# -*- coding: utf-8 -*-
# @Author     : Bonnie
# @Time       : 2022/10/30 17:53
# @FileName   : ExternalLinkPage.py
# @Description:

from base.ObjectMap import ObjectMap


class ExternalLinkPage(ObjectMap):
    def goto_imooc(self, driver):
        """
        切换窗口为慕课网
        :param driver:
        :return:
        """
        self.switch_window_2_latest_handle(driver)
        return driver.title
