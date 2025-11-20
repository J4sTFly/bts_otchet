import re
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Parser(webdriver.Chrome):
    stack = []

    def __init__(self, config, start_date, end_date):
        self.config = config
        self.start_date = start_date
        self.end_date = end_date

        options = Options()
        # options.add_argument('-headless')
        options.add_argument("--start-maximized")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-default-apps")
        options.add_argument("--disable-dev-shm-usage")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        super().__init__(options=options)

        self.set_page_load_timeout(10)
        self.implicitly_wait(10)

    def process(self):
        servers = config.servers

        for server in servers:
            xpaths = server["xpaths"]
            self.log_in(server, xpaths)
            self._wait_for_page_loading()

            self.find_element(By.XPATH, xpaths["archives_section_btn"]).click()
            self._wait_for_page_loading()
            for obj_id in server["objectIds"]:
                obj_data = self._retrieve_obj_data(obj_id, server, xpaths)
                self.stack.append(obj_data)
        return self.stack

    def log_in(self, server, xpaths):
        self.get(server["url"])

        username = self.find_element(By.XPATH, xpaths["username_input"])
        username.send_keys(server["credentials"][0])
        self.find_element(By.XPATH, xpaths["password_input"]).send_keys(
            server["credentials"][1]
        )

        self.find_element(By.XPATH, xpaths["login_btn"]).click()

    def populate_objects(self, server, xpaths):
        self.execute_script(
            "Array.from(document.querySelectorAll('.glyphicon-chevron-right')).forEach((el) => {el.click()})"
        )

    def _wait_for_page_loading(self):
        WebDriverWait(self, 10).until(
            lambda driver: self.execute_script("return document.readyState")
            == "complete"
        )

    def _retrieve_obj_data(self, obj_id, server, xpaths):
        self.execute_script(
            f'$.cookie("RepIndexText", "{server["report_cookie_name"]}")'
        )
        request = (
            self.config.ajax_request_format.replace("$serverHost", server["url"])
            .replace("$reportIndex", self.config.report_index)
            .replace("$startDate", self.start_date)
            .replace("$endDate", self.end_date)
            .replace("$objectId", str(obj_id))
        )

        response = self.execute_async_script(request, 30)
        return self._parse_html_table(obj_id, response['data'])

    def _parse_html_table(self, obj_id, html):
        data = {}
        table_re = re.compile('<table.*?</table>', re.DOTALL)
        table = table_re.group() if (table_re := table_re.search(html)) else None

        if table:
            head_cols_re = re.compile('<th.*?>(.*?)</th>', re.DOTALL)
            head_cols = head_cols_re.findall(table)

            body_cols_re = re.compile('<th.*?>(.*?)></td>', re.DOTALL)
            body_cols = body_cols_re.findall(table)

            data = dict(zip(head_cols, body_cols))
        data['id'] = obj_id
        return data

if __name__ == "__main__":
    from config import Config

    config = Config()
    parser = Parser(config, "2025-10-01T21:00:00.000Z", "2025-11-04T21:00:00.000Z")
    parser.process()
    # parser.get("https://google.com")
