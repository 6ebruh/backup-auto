from selenium import webdriver
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

    def login_in_owa(self, login_label, login, password_label, password):
        self.get_element(login_label).send_keys(login)
        self.get_element(password_label).send_keys(password)

    def logout_from_owa():
        pass
