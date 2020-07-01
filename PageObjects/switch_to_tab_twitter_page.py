import time

from PageObjects.BasePage import BasePage


class TwitterPage(BasePage):

    def switch_to_opened_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)

    def page_title(self):
        return self.get_page_title()