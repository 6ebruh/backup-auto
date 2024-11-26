import time
import config as cfg, Browser
from selenium.webdriver.common.by import By

#обьект браузера
browser = Browser.Browser()

try:
    browser.open_link(cfg.urls['mail'])
    time.sleep(3)
    browser.login_in_owa(cfg.login_label,
                         cfg.login,
                         cfg.password_label,
                         cfg.password,
                         cfg.enter_button)
    time.sleep(3)
    browser.logout_from_owa(cfg.profile_button, cfg.exit_button)
    time.sleep(3)
    browser.open_link(cfg.urls['backup'])
    time.sleep(2)
finally:
    browser.close_browser()


#debug loop

# while True:
#     pass
