# -*- coding:utf-8 -*-
import os
import unittest
import sys
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class GestureUnlock(unittest.TestCase):

	method_name = None

	def setUp(self):
		print "Start setUp"
		app = 'com.appiumios.appForUITest1'
		desired_caps ={}
		desired_caps['deviceName'] = 'iPhone 6'
		desired_caps['platformName'] = 'iOS'
		desired_caps['platformVersion'] = '9.3'
		desired_caps['app'] = PATH('../app/AppForUITest/appForUITest/build/Debug-iphonesimulator/appForUITest.app')
		# desired_caps['app'] = app
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

	def tearDown(self):
		print "Finished"
		picture_name = str(self.method_name)+".png"
		# 若执行失败则截图保存
		if sys.exc_info()[0]:
			self.driver.save_screenshot(picture_name)
		self.driver.quit()

	def test_unlock(self):
		self.method_name = sys._getframe().f_code.co_name
		# 点击gesture Tab
		self.driver.find_element_by_accessibility_id("Gesture").click()
		# 进入九宫格界面
		self.driver.find_element_by_accessibility_id("Gesture Locker (TouchAction)").click()
		# 开始滑动
		btn1 = self.driver.find_element_by_accessibility_id("Button1")
		btn3 = self.driver.find_element_by_accessibility_id("Button3")
		btn5 = self.driver.find_element_by_accessibility_id("Button5")
		btn6 = self.driver.find_element_by_accessibility_id("Button6")
		btn7 = self.driver.find_element_by_accessibility_id("Button7")
		# 按照3-6-5-7-1的顺序设置密码
		action = TouchAction(self.driver)
		action.press(btn3).wait(200).press(btn6).wait(200).press(btn5).wait(200).press(btn7).wait(200).move_to(btn1).press().release().perform()
		sleep(2)
		action.press(btn3).wait(200).press(btn6).wait(200).press(btn5).wait(200).press(btn7).wait(200).move_to(btn1).press().release().perform()
		# 设置成功的提示校验
		success_notice = self.driver.find_element_by_class_name("UIAStaticText")
		success_text = "password has been setup!"
		self.assertEqual(success_notice.text, success_text)
		print success_notice.text
		# 登录校验
		action.press(btn3).wait(200).press(btn6).wait(200).press(btn5).wait(200).move_to(btn7).press().move_to(btn1).press().release().perform()
		self.assertEqual(success_notice.text, "login success!")
		print success_notice.text

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase('GestureUnlock')
	unittest.TextTestRunner(verbosity=2).run(suite)
