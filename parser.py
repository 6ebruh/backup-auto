from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from config import template


def parse_backup_table(browser, table_xpath):

    table = browser.wait_visible(table_xpath)
    rows = table.find_elements(By.TAG_NAME, "tr")
    backup_data = []

    for row in rows[1:]:
        cells = row.find_elements(By.TAG_NAME, "td")
        server = cells[1].text.strip()
        status = cells[9].text.strip()
        if status != "Completed":
            raise AssertionError(f"⚠️ VM {server} backup status: {status}")

        backup_entry = {
            'Server': server,
            'Start Time': cells[5].text.strip(),
            'End Time': cells[6].text.strip(),
            'Duration (mins)': cells[7].text.strip(),
            'Job Status': status
        }
        backup_data.append(backup_entry)

    return backup_data


def format_table(headers, data):
    column_widths = {header: len(header) for header in headers}
    for entry in data:
        for header in headers:
            if header in entry:
                column_widths[header] = max(column_widths[header], len(str(entry[header])))

    markdown = "\n"
    markdown += "| " + " | ".join(header.ljust(column_widths[header]) for header in headers) + " |\n"
    markdown += "| " + " | ".join("-" * width for width in column_widths.values()) + " |\n"

    for entry in data:
        row = "| " + " | ".join(
            str(entry.get(header, '')).ljust(column_widths[header])
            for header in headers
        ) + " |\n"
        markdown += row

    return markdown


def format_regulatory_table(employee, rr_number):

    current_time = datetime.now().strftime("%d.%m.%Y %H:%M")

    headers = ['Параметр', 'Значение']
    data = [
        {'Параметр': 'Наименование регламентной работы:', 'Значение': '«Контроль создания резервной копии»'},
        {'Параметр': 'Номер РР в СМКСС:', 'Значение': rr_number},
        {'Параметр': 'Сотрудник, выполнивший РР:', 'Значение': employee},
        {'Параметр': 'Дата и время проведения РР:', 'Значение': current_time}
    ]

    return format_table(headers, data)


def format_markdown_table(data, employee, rr_number):
    if not data:
        return ""

    regulatory_table = format_regulatory_table(employee, rr_number)
    backup_table = format_table(
        ['Server', 'Start Time', 'End Time', 'Duration (mins)', 'Job Status'],
        data
    )

    current_year = datetime.now().year
    markdown = template.format(
        year=current_year,
        regulatory_table=regulatory_table,
        backup_table=backup_table
    )

    return markdown
