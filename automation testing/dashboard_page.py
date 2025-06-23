# pages/dashboard_page.py

from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.time_at_work_widget = (By.XPATH, "//h6[text()='Time at Work']")
        self.quick_launch_widget = (By.XPATH, "//h6[text()='Quick Launch']")
        self.my_actions_widget = (By.XPATH, "//h6[text()='My Actions']")

    def is_time_at_work_displayed(self):
        return self.driver.find_element(*self.time_at_work_widget).is_displayed()

    def is_quick_launch_displayed(self):
        return self.driver.find_element(*self.quick_launch_widget).is_displayed()

    def is_my_actions_displayed(self):
        return self.driver.find_element(*self.my_actions_widget).is_displayed()
