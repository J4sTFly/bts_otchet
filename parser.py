from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.options import Options


class Parser(webdriver.Chrome):
    stack = []
    server = None
    xpaths = []

    def __init__(self, config=None):
        self.config = config

        options = Options()
        #options.add_argument('-headless')
        options.add_argument('--start-maximized')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-default-apps')
        options.add_argument('--disable-dev-shm-usage')
        options.add_experimental_option('excludeSwitches', ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        super().__init__(options=options)

        self.set_page_load_timeout(10)
        self.implicitly_wait(10)

    def process(self):
        servers = config.servers

        for server in servers:
            self.log_in()

    def log_in(self):
        self.get(self.server['url'])


if __name__ == "__main__":
    parser = Parser()
