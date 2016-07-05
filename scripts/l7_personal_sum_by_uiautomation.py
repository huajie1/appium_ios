# -*- coding:utf-8 -*-
import os
import unittest
import sys
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


# 使用find_element_by_ios_uiautomation改写求和测试用例
class ByUiautomation(unittest.TestCase):

	method_name = None
	first_value = 10
	second_value = 5

	def setUp(self):
		print "Start setUp"
		app = 'com.huajie.appiumdemo'
		desired_caps = {}
		desired_caps['platformName'] = 'iOS'
		desired_caps['platformVersion'] = '9.3'
		desired_caps['udid'] = '6abbdd3af4fe3eb2b269bebd496081cf2fefd516'
		# real device
		desired_caps['deviceName'] = 'iPhone 6'
		desired_caps['app'] = app
		# desired_caps['app'] = PATH('../app/TestApp/build/Debug-iphoneos/TestApp.app')
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

	def tearDown(self):
		print "Finished"
		picture_name = str(self.method_name)+".png"
		# 若执行失败则截图保存
		if sys.exc_info()[0]:
			self.driver.save_screenshot(picture_name)
		self.driver.quit()

	def test_by_uiautomation(self):
		# 获取方法名
		self.method_name = sys._getframe().f_code.co_name
		# 定位两个输入框
		first_arg = self.driver.find_element_by_ios_uiautomation("target.frontMostApp().mainWindow().elements()['IntegerA']")
		second_arg = self.driver.find_element_by_ios_uiautomation("target.frontMostApp().mainWindow().elements()['TextField2']")
		first_arg.send_keys(self.first_value)
		second_arg.send_keys(self.second_value)
		sum_button = self.driver.find_element_by_ios_uiautomation("target.frontMostApp().mainWindow().elements()['ComputeSumButton']")
		sum_button.click()
		# 判断求和值
		answer_value = self.driver.find_element_by_ios_uiautomation("target.frontMostApp().mainWindow().elements()['Answer']").text
		self.assertEqual(answer_value, str(self.first_value + self.second_value))

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase('ByUiautomation')
	unittest.TextTestRunner(verbosity=2).run(suite)
