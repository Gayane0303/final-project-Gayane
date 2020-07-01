from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__ (self, driver):
        self.driver = driver

    def _visit(self, url):
        self.driver.get(url)

    def _find_element(self, locator):
        return self.driver.find_element(locator['by'], locator['value'])

    def _find_elements(self, locator):
        return self.driver.find_elements(locator['by'], locator['value'])

    def _click(self, locator):
        self._find_element(locator).click()

    def _type_text(self, locator, input_test):
        self._find_element(locator).send_keys(input_test)

    def _get_text(self, locator):
        return self._find_element(locator).get_attribute("value")

    def send_enter_key(self, locator):
        self._find_element(locator).send_keys(Keys.ENTER)

    def _is_displayed(self, locator):
        self._find_element(locator).is_displayed()

    def _is_checked(self, locator):
        self._find_element(locator).is_selected()

    def _is_checkbox_checked(self, locator):
        return self._find_element(locator).get_attribute("checked")

    def _is_checkbox_selected(self, locator):
        return self._find_element(locator).is_selected()

    def get_current_url(self):
        return (self.driver.current_url)

    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self._find_element(locator))

    def get_page_title(self):
        return self.driver.title

    def _is_element_displayed(self, locator, timeout=0):
        if timeout > 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(expected_conditions.visibility_of_element_located((
                        locator["by"], locator["value"])))
            except TimeoutException:
                return False
            return True
        else:
            try:
                return self._find_element(locator).is_displayed()
            except NoSuchElementException:
                return False























