
from appium import webdriver
from test_project.service.feature.appium_po.base_page import BasePage
from test_project.service.feature.appium_po.main_page import MainPage


class App(BasePage):

    def start(self, caps):

        if self.driver is None:
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver.launch_app()
        # 在 10 内，每 0.5 s 查找一次元素
        self.driver.implicitly_wait(120)

    def quit(self):
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)
