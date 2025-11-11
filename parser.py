from time import sleep
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Parser(webdriver.Chrome):
    stack = []
    server = None
    xpaths = []

    def __init__(self, config, start_date, end_date):
        self.config = config

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
            self.wait_for_page_loading()

            self.find_element(By.XPATH, xpaths["archives_section"]).click()
            self.wait_for_page_loading()
            
            for obj_id in server['objectIds']:
                self.retrieve_obj_data(self, obj_id, server, xpaths)
            # self.populate_objects()

    def log_in(self, server, xpaths):
        self.get(server["url"])

        self.find_element(By.XPATH, xpaths["username_input"]).send_keys(
            server["credentials"]
        )[0]
        self.find_element(By.XPATH, xpaths["password_input"]).send_keys(
            server["credentials"]
        )[1]

        self.find_element(By.XPATH, xpaths["login_btn"]).click()

    def populate_objects(self, server, xpaths):
        self.execute_script(
            "Array.from(document.querySelectorAll('.glyphicon-chevron-right')).forEach((el) => {el.click()})"
        )

    def _wait_for_page_loading(self):
        WebdriverWait(self, 10).until(
            self.execute_script("return document.readyState") == "complete"
        )

    def retrieve_obj_data(self, obj_id, server, xpaths):
        self.execute_script(f'$.cookie("RepIndexText", "{server["report_cookie_name"]}")')
        
        self.execute_script(server['ajax_request_format'].replace('$dateFrom', self.start_date) \                             
                            .replace('$dateTo', self.end_date) \
                            .replace('$objectId', obj_id)
        
    def _wait_until_jquery_finished(self):
        WebDriverWait(self, 25).until(
            self.execute_script('return $.active === 0')
        }



if __name__ == "__main__":
    parser = Parser(None, None, None)
    parser.get("https://goolge.com")
