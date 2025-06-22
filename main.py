import time
from datetime import datetime
from parser import parse_backup_table, format_markdown_table
import config as cfg
import Browser
import page


def display_employee_list():
    """Display the list of available employees."""
    print("\nСписок сотрудников:")
    for num, name in cfg.employees.items():
        print(f"{num}: {name}")


def get_user_input():
    """Get employee number and RR number from user input."""
    employee_num = input("\nВведите номер сотрудника, выполняющего РР РК: ")
    if employee_num not in cfg.employees:
        raise ValueError(f"Неверный номер сотрудника: {employee_num}")

    zni = input("\nВведите номер РР в СМКСС: ")
    return employee_num, zni


def process_backup_report(browser, employee_num, zni):
    """Process the backup report and create markdown file."""
    try:
        allure_table = parse_backup_table(browser, page.mail_backup_table)
        filename = f'Отчет {datetime.now().strftime("%d.%m.%Y")} Контроль создания резервных копий.md'

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(format_markdown_table(allure_table, cfg.employees[employee_num], zni))
        print(f"\n✅ Отчет успешно создан: {filename}")

    except AssertionError as e:
        print(f"\n❌ Ошибка: {e}")
        print("Файл отчета не создан из-за ошибок в бэкапах")
        raise


def main():
    """Main function to handle the backup report generation process."""
    start_time = time.time()
    browser = None

    try:
        # Display employee list and get user input
        display_employee_list()
        employee_num, zni = get_user_input()

        # Initialize browser and process report
        browser = Browser.Browser()
        browser.open_link(cfg.urls['mail'])
        browser.login_mail(cfg.mlogin, cfg.mpassword)
        time.sleep(2)

        browser.action_click(page.mail_backup_folder)
        time.sleep(5)
        browser.action_click(page.letter)
        time.sleep(5)

        process_backup_report(browser, employee_num, zni)

    except ValueError as e:
        print(f"\n❌ Ошибка ввода: {e}")
    except Exception as e:
        print(f"\n❌ Неожиданная ошибка: {e}")
    finally:
        if browser:
            try:
                browser.logout_mail()
            finally:
                browser.close_browser()

    duration = time.time() - start_time
    print(f"\n⏱️ Время выполнения: {duration:.2f} секунд")


if __name__ == "__main__":
    main()
