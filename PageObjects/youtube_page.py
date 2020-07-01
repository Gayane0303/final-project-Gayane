from PageObjects.BasePage import BasePage
import time

class YouTubePage(BasePage):
    def switch_to_opened_tab2(self):
        self.driver.switch_to.window(self.driver.window_handles[2])
        time.sleep(2)

    def page_title(self):
        return self.get_page_title()