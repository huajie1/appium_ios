# -*- coding:utf-8 -*-
import unittest
import sys
from appium import webdriver

first_arg = 10
second_arg = 5


# 如果执行失败截图保存并以方法名命名
class TestAppiumIosL5(unittest.TestCase):

    method_name = None
    @classmethod
    def setUpClass(cls):
        print "setUpClass"
        super(TestAppiumIosL5, cls).setUpClass()
        app = 'com.huajie.appiumdemo'
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.3'
        desired_caps['udid'] = '6abbdd3af4fe3eb2b269bebd496081cf2fefd516'
        # simulator
        desired_caps['deviceName'] = 'iPhone 6'
        desired_caps['app'] = app
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    def tearDownClass(cls):
        super(TestAppiumIosL5, cls).tearDownClass()
        print "tearDownClass"
        cls.driver.quit()

    def setUp(self):
        print "Set up"
        super(TestAppiumIosL5, self).setUp()

    def tearDown(self):
        print "tearDown"
        picture_name = str(self.method_name)+".png"
        super(TestAppiumIosL5, self).tearDown()
        if sys.exc_info()[0]:
           self.driver.save_screenshot(picture_name)
        print picture_name

    def test_calculate0(self):
        print "Start minusing"
        # 获取方法名并赋值/需要在方法下就执行,否则可能执行不到就取不到值了
        self.method_name = sys._getframe().f_code.co_name
        first_arg_textfield = self.driver.find_element_by_accessibility_id("IntegerA")
        second_arg_textfield = self.driver.find_element_by_accessibility_id("TextField2")
        minus_button = self.driver.find_element_by_accessibility_id("MinusButton")
        # compute minus
        first_arg_textfield.send_keys(str(first_arg))
        second_arg_textfield.send_keys(str(second_arg))
        minus_button.click()
        # check if minus correct
        minus_result_id = self.driver.find_element_by_accessibility_id("MinusAnswer")
        self.assertEqual(minus_result_id.text, str(first_arg - second_arg))
        # self.assertEqual(minus_result_id.text, str(first_arg - second_arg + 1))
        print "The minus result is "+minus_result_id.text

    def test_calculate1(self):
        print "Start addition"
        # 获取方法名并赋值
        self.method_name = sys._getframe().f_code.co_name
        sum_button = self.driver.find_element_by_accessibility_id("ComputeSumButton")
        sum_button.click()

        # check if sum correct
        sum_result_label = self.driver.find_element_by_accessibility_id("Answer")
        # self.assertEqual(sum_result_label.text, str(first_arg + second_arg - 1))
        self.assertEqual(sum_result_label.text, str(first_arg + second_arg))
        print "The sum is "+sum_result_label.text

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAppiumIosL5)
    unittest.TextTestRunner(verbosity=2).run(suite)
