# -*- coding: utf-8 -*-
# @Author     : Bonnie
# @Time       : 2022/11/5 18:11
# @FileName   : IframeBaiduMapBase.py
# @Description:
class IframeBaiduMapBase:
    def search_button(self):
        return "//button[@id='search-button']"

    def baidu_map_iframe(self):
        return "//iframe[@src='https://map.baidu.com/']"
