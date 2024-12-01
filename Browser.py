from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Browser():

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(self.chrome_options)
        self.driver.maximize_window()

    def open_link(self, link):
        self.driver.get(link)

    def close_browser(self):
        self.driver.quit()

    def get_element(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    def action_click(self, element):
        self.get_element(element).click()

    def action_send_keys(self, element, key):
        self.get_element(element).send_keys(key)

    def login_in_owa(self, login_label, login, password_label, password, enter_button):
        self.action_send_keys(login_label, login)
        self.action_send_keys(password_label, password)
        self.action_click(enter_button)

    def logout_from_owa(self, profile_button, exit_button):
        self.action_click(profile_button)
        self.action_click(exit_button)

    def take_screenshot(self, filename):
        screenshot_path = filename
        self.driver.save_screenshot(screenshot_path)
