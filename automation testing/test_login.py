# tests/test_login.py

import time
import unittest
from utils.driver_setup import get_driver
from pages.login_page import LoginPage

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.login_page = LoginPage(self.driver)

    def test_valid_login(self):
        self.login_page.login("Admin", "admin123")
        time.sleep(2)  # wait for dashboard to load
        self.assertIn("dashboard", self.driver.current_url.lower(), "Login failed or dashboard not reached")

    def test_invalid_login(self):
        self.login_page.login("Admin", "wrongpassword")
        time.sleep(2)  # wait for error message to appear
        error_message = self.driver.find_element("xpath", "//p[contains(text(),'Invalid credentials')]").text
        self.assertEqual(error_message, "Invalid credentials", "Error message not displayed or incorrect")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
