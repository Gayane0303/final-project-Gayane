import ec as ec
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.BasePage import BasePage


class Home(BasePage):
    _search_icon = {"by": By.XPATH, "value": '//*[@id="atIdViewHeader"]/div[2]/div[2]/div[1]/div[2]/div'}
    _search_input = {"by": By.CSS_SELECTOR, "value": 'div.aCsJod.oJeWuf > div > div.Xb9hP > input'}
    _start_searching = {"by": By.XPATH, "value": '//*/div/div[1]/div/span[1]/div[1]'}
    _twitter = {"by": By.LINK_TEXT, "value": 'Twitter'}
    _youtube = {"by": By.LINK_TEXT, "value": 'YouTube'}




    def __init__(self, driver):
        self.driver=driver

    def hover_on_about(self):
        action = ActionChains(self.driver)
        _about = self.driver.find_element_by_xpath('//*[@id="WDxLfe"]/ul/li[7]/div[1]')
        action.move_to_element(_about).perform()

    def wait_twitter_displayed(self):
        return self._is_element_displayed(self._twitter, timeout=3)

    def wait_youtube_displayed(self):
        return self._is_element_displayed(self._youtube, timeout=3)

    def click_on_twitter_icon(self):
        self._find_element(self._twitter).click()

    def click_on_youtube_icon(self):
        self._find_element(self._youtube).click()

    def click_on_search_icon(self):
        self._click(self._search_icon)
        time.sleep(2)

    def click_on_search_input(self):
        self._click(self._search_input)

    def search_text_(self, input_text):
        self._type_text(self._search_input, input_text)

    def get_filled_text(self):
        return self._get_text(self._search_input)

    def tap_enter_key(self):
        self.send_enter_key(self._start_searching)

    def search_item(self):
        self._click(self._start_searching)

    def page_title(self):
        return self.get_page_title()

    def switch_to_tab_0(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)

