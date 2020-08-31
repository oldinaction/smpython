import time
import unittest

from appium import webdriver  # Appium-Python-Client==1.0.2


class MyTests(unittest.TestCase):
    # 测试开始前执行的方法。每次测试都感觉像第一次进入APP(会出现引导页)
    def setUp(self):
        desired_caps = {'platformName': 'Android',  # 平台名称
                        'platformVersion': '5.1.1',  # 系统版本号
                        'deviceName': '127.0.0.1:62001',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        'appPackage': 'com.youdao.calculator',  # apk的包名
                        'appActivity': 'com.youdao.calculator.activities.MainActivity'  # activity 名称
                        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
        self.driver.implicitly_wait(8)

    def test_calculator(self, t=500, n=4):
        """计算器测试"""
        time.sleep(3)

        # 执行引导
        window = self.driver.get_window_size()
        x0 = window['width'] * 0.8  # 起始x坐标
        x1 = window['width'] * 0.2  # 终止x坐标
        y = window['height'] * 0.5  # y坐标
        for i in range(n):
            self.driver.swipe(x0, y, x1, y, t)
            time.sleep(1)
        self.driver.find_element_by_id('com.youdao.calculator:id/guide_button').click()
        for i in range(6):
            self.driver.find_element_by_id('com.youdao.calculator:id/frag_calculator').click()
            time.sleep(1)

        btn_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.view.View/android.widget.GridView/android.widget.FrameLayout[{0}]/android.widget.FrameLayout'
        self.driver.find_element_by_xpath(btn_xpath.format(7)).click()
        self.driver.find_element_by_xpath(btn_xpath.format(10)).click()
        self.driver.find_element_by_xpath(btn_xpath.format(8)).click()
        time.sleep(1)

        # 获取结果（先根据id定位到父元素，再根据xpath定位很容易失败）
        # resultValue = self.driver.find_element_by_id('com.youdao.calculator:id/ll_top_area').find_elements_by_xpath(".//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]")[0].get_attribute("text")
        resultValue = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]").get_attribute('text')
        # self.assertEqual(resultValue.replace('\u200b', ''), "=55")  # 会生成失败的测试报告
        self.assertEqual(resultValue.replace('\u200b', ''), "=56")

    # 测试结束后执行的方法
    def tearDown(self):
        self.driver.quit()
