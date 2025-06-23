# tests/test_dashboard.py

import time
import unittest
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

class TestDashboard(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
        self.login_page.login("Admin", "admin123")
        time.sleep(2)

    def test_dashboard_widgets(self):
        self.assertTrue(self.dashboard_page.is_time_at_work_displayed(), "Time at Work widget not visible")
        self.assertTrue(self.dashboard_page.is_quick_launch_displayed(), "Quick Launch widget not visible")
        self.assertTrue(self.dashboard_page.is_my_actions_displayed(), "My Actions widget not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
