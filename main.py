import time
from datetime import date
import config as cfg, Browser

#обьект браузера
browser = Browser.Browser()

try:
    browser.open_link(cfg.urls['mail'])
    time.sleep(5)
    browser.login_in_owa(cfg.login_label,
                         cfg.login,
                         cfg.password_label,
                         cfg.password,
                         cfg.enter_button)
    time.sleep(10)

    browser.action_click(cfg.mail_folder)

    time.sleep(3)

    browser.take_screenshot(f'screenshots/screenshot_{date.today()}.png')

    time.sleep(3)

    browser.logout_from_owa(cfg.profile_button, cfg.exit_button)
    time.sleep(10)
    browser.open_link(cfg.urls['backup'])
    time.sleep(2)
finally:
    browser.close_browser()


#debug loop

# while True:
#     pass
