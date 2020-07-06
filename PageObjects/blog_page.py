from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage

class Blogpage(BasePage):
    _blog = {"by": By.XPATH, "value": '//ul/li[7]/div[3]/ul/li[2]'}
    _logo = {"by": By.XPATH, "value": '//div/div[2]/div[1]/div[1]/a/img'}

    def click_on_blog(self):
        self._click(self._blog)

    def page_title(self):
        return self.get_page_title()

    def wait_logo_displayed(self):
        return self._is_element_displayed(self._logo, timeout=3)


