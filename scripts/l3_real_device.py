# -*- coding:utf-8 -*-
import os
import unittest

from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestiOSEnvironment(unittest.TestCase):
    def setUp(self):
        # open helloworld.app on simulator iPhone 4s (9.2)
        desired_caps = {}
        app = "com.huajie.appiumdemo"
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.3'
        desired_caps['deviceName'] = 'iPhone 6'
        desired_caps['udid'] = '6abbdd3af4fe3eb2b269bebd496081cf2fefd516'
        # desired_caps['app'] = app
        desired_caps['app'] = PATH('../app/TestApp/build/Debug-iphoneos/TestApp.ipa')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_screenshot(self):
        # wait for 5 seconds
        sleep(5)
        # take screenshot
        self.driver.save_screenshot("helloworld_screenshot.png")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestiOSEnvironment)
    unittest.TextTestRunner(verbosity=2).run(suite)
