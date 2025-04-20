import time
from datetime import date
import config as cfg, Browser


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
                          cfg.mail_enter,
                          cfg.mail_login_input,
                          cfg.mail_enter_button,
                          cfg.skip_button,
                          cfg.mail_password_input,
                          cfg.mail_login_frame)

    browser.action_click(cfg.mail_folder)

    #доделать и отослалть еще письма
    # browser.action_click(cfg.mail_first_letter)

    browser.logout_from_mail(cfg.mail_profile_button, cfg.mail_exit_button)
finally:
    browser.close_browser()


#debug loop

# while True:
#     pass
