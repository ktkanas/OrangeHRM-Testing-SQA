# pages/leave_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LeavePage:
    def __init__(self, driver):
        self.driver = driver
        self.apply_tab = (By.XPATH, "//a[contains(@href,'applyLeave')]")
        self.leave_type_dropdown = (By.XPATH, "//label[text()='Leave Type']/following::div[1]")
        self.leave_type_option = (By.XPATH, "//span[text()='CAN - Vacation']")
        self.from_date_input = (By.XPATH, "//label[text()='From Date']/following::input[1]")
        self.to_date_input = (By.XPATH, "//label[text()='To Date']/following::input[1]")
        self.comment_input = (By.XPATH, "//label[text()='Comment']/following::textarea")
        self.apply_button = (By.XPATH, "//button[@type='submit']")

    def navigate_to_apply_leave(self):
        self.driver.find_element(*self.apply_tab).click()

    def apply_leave(self, from_date, to_date, comment):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.leave_type_dropdown)).click()
        self.driver.find_element(*self.leave_type_option).click()
        self.driver.find_element(*self.from_date_input).clear()
        self.driver.find_element(*self.from_date_input).send_keys(from_date)
        self.driver.find_element(*self.to_date_input).clear()
        self.driver.find_element(*self.to_date_input).send_keys(to_date)
        self.driver.find_element(*self.comment_input).send_keys(comment)
        self.driver.find_element(*self.apply_button).click()
