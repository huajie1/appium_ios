# -*- coding:utf-8 -*-
import os
import unittest
import sys

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

SCREENSHOT_NAME = "check_sum_error.png"

class TestAppiumIosL4(unittest.TestCase):
    def setUp(self):
        # open TestApp.app on iPhone 6 (9.3)
        desired_caps = {}
        app = 'com.huajie.appiumdemo'
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.3'
        desired_caps['udid'] = '6abbdd3af4fe3eb2b269bebd496081cf2fefd516'
        # simulator
        desired_caps['deviceName'] = 'iPhone 6'
        desired_caps['app'] = app
        # desired_caps['app'] = PATH('../app/TestApp/build/Debug-iphoneos/TestApp.app')

        # real device
        # desired_caps['deviceName'] = "hengjie's iPhone"
        # desired_caps['udid'] = '0b2fbaaf7fa0e752ea908b3d1287be783bffdb57'
        # desired_caps['app'] = PATH(
        #     '../app/TestApp/build/Debug-iphoneos/TestApp.ipa'
        # )

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        # clear screenshot
        if os.path.exists(SCREENSHOT_NAME):
            os.remove(SCREENSHOT_NAME)

    def tearDown(self):

        # check if need to take screenshot
        if sys.exc_info()[0]:  # Returns the info of exception being handled
            # take screenshot
            self.driver.save_screenshot(SCREENSHOT_NAME)

        # end the session
        self.driver.quit()

    def test_check_minus_function(self):
        first_arg = 10
        second_arg = 5

        # find elements
        first_arg_textfield = self.driver.find_element_by_accessibility_id("IntegerA")
        second_arg_textfield = self.driver.find_element_by_accessibility_id("TextField2")
        minus_button = self.driver.find_element_by_accessibility_id("MinusButton")

        # compute sum
        first_arg_textfield.send_keys(str(first_arg))
        second_arg_textfield.send_keys(str(second_arg))
        minus_button.click()

        # check if sum correct
        minus_result_id = self.driver.find_element_by_accessibility_id("MinusAnswer")
        self.assertEqual(minus_result_id.text, str(first_arg - second_arg))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAppiumIosL4)
    unittest.TextTestRunner(verbosity=2).run(suite)
