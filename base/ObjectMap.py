# -*- coding: utf-8 -*-
# @Author     : Bonnie
# @Time       : 2022/10/22 12:55
# @FileName   : ObjectMap.py
# @Description:
import time
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException

from common.yaml_config import GetConf


class ObjectMap:
    # 获取基础地址 http://www.tcpjwtester.top
    url = GetConf().get_url()

    def element_get(self, driver, locate_type, locator_expression, timeout=10, must_be_visible=False):
        """
        单个元素获取
        :param driver:浏览器驱动
        :param locate_type:定位方式类型
        :param locator_expression:定位表达式
        :param timeout:超时时间
        :param must_be_visible:元素是否可见，Ture是必须可见，False是默认值
        :return:返回的元素
        """
        # 开始时间
        start_ms = time.time()
        # 设置的结束时间
        stop_ms = start_ms + (timeout * 1000)
        print(start_ms)
        for x in range(int(timeout * 10)):
            # 查找元素
            try:
                element = driver.find.element(by=locate_type, value=locator_expression)
                # 如果元素不是必须是可见的，则需要先判断元素是否可见
                if not must_be_visible:
                    return element
                # 如果元素是必须可见的，则需要先判断元素是否可见
                else:
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()

            except Exception:
                now_ms = time.time() * 1000
                if now_ms >= stop_ms:
                    break
            time.sleep(0, 1)
        raise ElementNotVisibleException("元素定位失败，定位方式：" + locate_type + " 定位表达式：" + locator_expression)

    def wait_for_ready_state_complete(self, driver, timeout=30):
        """
        等待页面完全加载完成
        :param driver: 浏览器驱动
        :param timeout:超时时间
        :return:
        """
        # 开始时间
        start_ms = time.time() * 1000
        # 设置的结束时间
        stop_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):
            try:
                # 获取页面的状态
                ready_state = driver.execute_script("return document.readyState")
            except WebDriverException:
                # 如果有driver的错误，执行js会失败，就直接跳过
                time.sleep(0.03)
                return True
            # 如果页面元素全部加载完成，返回True
            if ready_state == "complete":
                time.sleep(0.01)
                return True
            else:
                now_ms = time.time() * 1000
                # 如果超时了就break
                if now_ms >= stop_ms:
                    break
                time.sleep(0.1)
        raise Exception("打开网页时，页面元素在%s秒后仍然没有完全加载完" % timeout)

    def element_disappear(self, driver, locate_type, locator_expression, timeout=30):
        """
        等待页面元素小时
        :param driver:浏览器驱动
        :param locate_type:定位方式类型
        :param locator_expression:定位表达式
        :param timeout:超时时间
        :return:
        """
        if locate_type:
            # 开始时间
            start_ms = time.time() * 1000
            # 设置的结束时间
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find.element(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        now_ms = time.time() * 1000
                        if now_ms >= stop_ms:
                            break
                        time.sleep(0.1)
                except Exception:
                    return True
            raise ElementNotVisibleException(
                "元素定位失败，定位方式：" + locate_type + " 定位表达式：" + locator_expression)
        else:
            pass

    def element_appear(self, driver, locate_type, locator_expression, timeout=30):
        """
        等到页面元素出现
        :param driver:
        :param locate_type:
        :param locator_expression:
        :param timeout:
        :return:
        """
        if locate_type:
            # 开始时间
            start_ms = time.time() * 1000
            # 设置结束时间
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()

                except Exception:
                    now_ms = time.time() * 1000
                    if now_ms >= stop_ms:
                        break
                    time.sleep(0.1)
                    pass
            raise ElementNotVisibleException(
                "元素没有出现，定位方式：" + locate_type + " 定位表达式:" + locator_expression)

        def element_to_url(
                self,
                driver,
                url,
                locate_type_disappear=None,
                locator_expression_disappear=None,
                locate_type_appear=None,
                locator_expression_appear=None
        ):
            """
            跳转地址
            :param driver: 浏览器驱动
            :param url: 跳转的地址
            :param locate_type_disappear: 等待页面元素消失的定位方式
            :param locator_expression_disappear: 等待页面元素消失的定位表达式
            :param locate_type_appear: 等待页面元素出现的定位方式
            :param locator_expression_appear: 等待页面元素出现的定位表达式
            :return:
            """
            try:
                driver.get(self.url + url)
                # 等待页面元素都加载完成
                self.wait_for_ready_state_complete(driver)
                # 跳转地址后等待元素消失
                self.element_disappear(
                    driver,
                    locate_type_disappear,
                    locator_expression_disappear
                )
                # 跳转地址后等待元素出现
                self.element_appear(
                    driver,
                    locate_type_appear,
                    locator_expression_appear
                )
            except Exception as e:
                print("跳转地址出现异常，异常原因:%s" % e)
                return False
            return True


if __name__ == '__main__':
    ObjectMap().element_get()
