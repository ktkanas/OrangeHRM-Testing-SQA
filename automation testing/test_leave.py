# tests/test_leave.py

import time
import unittest
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.leave_page import LeavePage

class TestLeave(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.login_page = LoginPage(self.driver)
        self.leave_page = LeavePage(self.driver)
        self.login_page.login("Admin", "admin123")
        time.sleep(2)

    def test_apply_leave(self):
        self.leave_page.navigate_to_apply_leave()
        self.leave_page.apply_leave("2024-11-25", "2024-11-25", "Test automation leave request")
        time.sleep(2)  # Simulate wait for confirmation or reload
        # Simple check - current URL should not be login or error page
        self.assertNotIn("auth/login", self.driver.current_url, "Apply Leave might have failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
