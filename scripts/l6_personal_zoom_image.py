# -*- coding:utf-8 -*-
import os
import unittest
import sys
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class ZoomImage(unittest.TestCase):

	method_name = None

	def setUp(self):
		print "Start setUp"
		# app = 'com.appiumios.appForUITest1'
		desired_caps ={}
		desired_caps['deviceName'] = 'iPhone 6'
		desired_caps['platformName'] = 'iOS'
		desired_caps['platformVersion'] = '9.3'
		# real device TestApp
		app = 'com.huajie.appiumdemo'
		desired_caps['app'] = app
		desired_caps['udid'] = '6abbdd3af4fe3eb2b269bebd496081cf2fefd516'
		# desired_caps['app'] = PATH('../app/AppForUITest/appForUITest/build/Debug-iphonesimulator/appForUITest.app')
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		# self.driver.find_element_by_accessibility_id("Gesture").click()

	def tearDown(self):
		print "Finished"
		picture_name = str(self.method_name)+".png"
		# 若执行失败则截图保存
		if sys.exc_info()[0]:
			self.driver.save_screenshot(picture_name)
		self.driver.quit()

	# # 使用zoom和pinch实现缩放
	# def test_by_zoom_and_pinch(self):
	# 	self.method_name = sys._getframe().f_code.co_name
	# 	# 进入图片界面(appForUITest1)
	# 	# self.driver.find_element_by_accessibility_id("Image (Zoom and Pinch)").click()
	# 	# image = self.driver.find_element_by_accessibility_id("imageScrollView")
	#   # 进入gesture界面(TestApp)
	# 	self.driver.find_element_by_accessibility_id("Test Gesture").click()
	# 	image = self.driver.find_element_by_class_name("UIAMapView")
	# 	self.driver.zoom(element=image, percent=150, steps=10)
	# 	sleep(5)
	# 	self.driver.pinch(element=image, percent=50, steps=10)
	# 	sleep(10)

	# 使用multifuction来实现缩放
	def test_by_multiaction(self):
		print "By multiaction"
		self.method_name = sys._getframe().f_code.co_name
		# self.driver.find_element_by_accessibility_id("Image (Zoom and Pinch)").click()
		self.driver.find_element_by_accessibility_id("Test Gesture").click()
		# 选取两个点
		action1 = TouchAction(self.driver)
		action1.press(x=87, y=150).move_to(x=45, y=150).release()
		action2 = TouchAction(self.driver)
		action2.press(x=120, y=150).move_to(x=150, y=150).release()
		# action2.press(x=200, y=150).move_to(x=280, y=150).release() # 无法执行
		ma = MultiAction(self.driver)
		ma.add(action1, action2)
		ma.perform()
		sleep(5)


if __name__ == '__main__':
	# suite = unittest.TestLoader().loadTestsFromTestCase('ZoomImage')
	# unittest.TextTestRunner(verbosity=2).run(suite)
	suite = unittest.TestSuite()
	# 将方法依次加入以下执行序列使其顺序执行(仅限命令行执行时)
	# suite.addTest(ZoomImage("test_by_zoom_and_pinch"))
	suite.addTest(ZoomImage("test_by_multiaction"))
	unittest.TextTestRunner().run(suite)
