# -*- coding: utf-8 -*-
# @Author     : Bonnie
# @Time       : 2022/10/30 18:29
# @FileName   : AccountBase.py
# @Description:
class AccountBase:
    def basic_info_avatar_input(self):
        """
        基本资料-个人头像
        :return:
        """
        return "//input[@type='file']"

    def basic_info_save_button(self):
        """
        基本资料-保存按钮
        :return:
        """
        return "//span[text()='保存']/parent::button"
