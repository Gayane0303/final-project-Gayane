from selenium.webdriver.common.by import By
import time

from PageObjects.BasePage import BasePage


class ReviewUs(BasePage):

    _review_us = {"by": By.ID, "value": 'evaluateUrl'}
    _footer = {"by": By.XPATH, "value": '//*[@id="yDmH0d"]/div[1]/div/div[2]/div[2]/footer'}

    #_iframe_1 = {"by": By.CSS_SELECTOR, "value": '#s_LtRsq2t9i4Rl'}
    _iframe_1 = {"by": By.NAME, "value": '627c852b818b603a_6'}
    _iframe_2 = {"by": By.CSS_SELECTOR, "value": '#innerFrame'}
    _iframe_3 = {"by": By.CSS_SELECTOR, "value": '#userHtmlFrame'}
    _iframe_4 = {"by": By.CSS_SELECTOR, "value": 'body > div > iframe'}

    def scroll_into_footer(self):
        self.scroll_to_element(self._footer)
        time.sleep(3)

    def get_review_us_element_text(self):
        return self._find_element(self._review_us).text

    def switch_to_iframes(self):
        self.driver.switch_to.frame(self._find_element(self._iframe_1))
        self.driver.switch_to.frame(self._find_element(self._iframe_2))
        self.driver.switch_to.frame(self._find_element(self._iframe_3))
        self.driver.switch_to.frame(self._find_element(self._iframe_4))

    def wait_review_us_displayed(self):
        return self._is_element_displayed(self._review_us, timeout=3)



