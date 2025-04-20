import time
from datetime import date
import config as cfg, Browser, page


# zni = input("""
# 1. Сотрудник1
# 2. Сотрудник2
# 3. Сотрудник3
# Введите номер сотрудника, выполняиющего РР РК
# """)


#обьект браузера
browser = Browser.Browser()

try:
    browser.open_link(cfg.urls['mail'])
    # browser.login_in_owa(cfg.login_label,
    #                      cfg.login,
    #                      cfg.password_label,
    #                      cfg.password,
    #                      cfg.enter_button)

    browser.login_in_mail(cfg.mail_login,
                          cfg.mail_password,
                          page.mail_enter,
                          page.mail_login_input,
                          page.mail_enter_button,
                          page.skip_button,
                          page.mail_password_input,
                          page.mail_login_frame)

    browser.action_click(page.mail_folder)

    #доделать и отослалть еще письма
    # browser.action_click(cfg.mail_first_letter)

    browser.logout_from_mail(page.mail_profile_button, page.mail_exit_button)
finally:
    browser.close_browser()


#debug loop

# while True:
#     pass
