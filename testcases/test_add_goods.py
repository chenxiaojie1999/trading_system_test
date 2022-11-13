# -*- coding: utf-8 -*-
# @Author     : Bonnie
# @Time       : 2022/10/29 17:08
# @FileName   : test_add_goods.py
# @Description:
from time import sleep

import pytest

from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.GoodsPage import GoodsPage


class TestAddGoods:
    def test_add_goods_001(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "产品")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "新增二手商品")
        sleep(2)
        print(driver.page_source.encode('utf-8'))
        # GoodsPage().add_new_goods(
        #     driver,
        #     goods_title="新增商品测试wiiliam",
        #     goods_details="新增商品测试详情william",
        #     goods_num=1,
        #     goods_pic_list=["商品图片一.jpg"],
        #     goods_price=123,
        #     goods_status="上架",
        #     bottom_button_name="提交"
        # )
        sleep(3)
        driver.quit()
