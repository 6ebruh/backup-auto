from selenium import webdriver
import time
import page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Browser():

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--disable-blink-features=AutomationControlled")
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

    def switch_to_default(self):
        return self.driver.switch_to.default_content()

    def login_mail(self, mail_login, mail_password):
        self.action_click(page.mail_enter_button)
        time.sleep(2)
        self.switch_to_frame(page.mail_enter_frame)
        time.sleep(2)
        self.action_send_keys(page.mail_login_input, mail_login)
        time.sleep(2)
        self.action_click(page.mail_logpass_button)
        time.sleep(2)
        self.action_send_keys(page.mail_password_input, mail_password)
        self.action_click(page.mail_logpass_button)
        time.sleep(2)
        self.switch_to_default()

    def logout_mail(self):
        self.action_click(page.profile_icon)
        self.action_click(page.mexit_button)


    def login_gmail(self, login, password):
        self.action_send_keys(page.gmail_login_input, login)
        self.action_click(page.gmail_next_login_button)
        self.action_send_keys(page.gmail_password_input, password)
        self.action_click(page.gmail_next_password_button)

    def logout_gmail(self):
        self.action_click(page.gmail_profile_logo)
        self.switch_to_frame(page.gmail_logout_frame)
        self.action_click(page.gmail_logout_button)
