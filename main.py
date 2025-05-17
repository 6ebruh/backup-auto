import time
from datetime import datetime
from parser import parse_backup_table, format_markdown_table
import config as cfg, Browser, page


print("\nСписок сотрудников:")
for num, name in cfg.employees.items():
    print(f"{num}: {name}")

employee_num = input("\nВведите номер сотрудника, выполняющего РР РК: ")

zni = input("\nВведите номер РР в СМКСС: ")

browser = Browser.Browser()

try:
    browser.open_link(cfg.urls['mail'])
    browser.login_mail(cfg.mlogin, cfg.mpassword)
    time.sleep(2)
    browser.action_click(page.mail_backup_folder)
    time.sleep(5)
    browser.action_click(page.first_mail)
    time.sleep(5)

    try:
        allure_table = parse_backup_table(browser, page.mail_backup_table)
        with open(f'Отчет {datetime.now().strftime("%d.%m.%Y")} Контроль создания резервных копий.md', 'w', encoding='utf-8') as f:
            f.write(format_markdown_table(allure_table, cfg.employees[employee_num], zni))
    except AssertionError as e:
        print(f"\nОшибка: {e}")
        print("Файл отчета не создан из-за ошибок в бэкапах")

    browser.logout_mail()

finally:
    browser.close_browser()
