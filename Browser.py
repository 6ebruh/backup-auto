from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def wait_visible(self, element, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, element))
            )
        except Exception as e:
            raise TimeoutError(f"Элемент {element} не появился на странице в течение {timeout} секунд")

    def action_click(self, element):
        self.wait_visible(element).click()

    def action_send_keys(self, element, key):
        self.wait_visible(element).send_keys(key)

    def login_in_owa(self, login_label, login, password_label, password, enter_button):
        self.action_send_keys(login_label, login)
        self.action_send_keys(password_label, password)
        self.action_click(enter_button)

    def logout_from_mail(self, profile_button, exit_button):
        self.action_click(profile_button)
        self.action_click(exit_button)

    def take_screenshot(self, filename):
        screenshot_path = filename
        self.driver.save_screenshot(screenshot_path)

    def switch_to_frame(self, frame_xpath):
        return self.driver.switch_to.frame(self.wait_visible(frame_xpath))

    def login_in_mail(self, mail_login, mail_password, mail_enter, mail_login_input, mail_enter_button, skip_button, mail_password_input, mail_login_frame):
        self.action_click(mail_enter)
        self.switch_to_frame(mail_login_frame)
        self.action_send_keys(mail_login_input, mail_login)
        self.action_click(mail_enter_button)
        self.action_click(skip_button)
        self.action_send_keys(mail_password_input, mail_password)
        self.action_click(mail_enter_button)
