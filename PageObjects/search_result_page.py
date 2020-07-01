from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class SearchResultsPage(BasePage):
    _found_results = {"by": By.XPATH, "value": '//*[@class="gtazFe"]'}
    _found_links = {"by": By.CSS_SELECTOR, "value": 'div:nth-child(3) > div.i3uTwd > div > div.lZsZxe > div > div > a'}

    def check_found_results_count(self):
        return (len(self._find_elements(self._found_results)))

    def get_found_items_links(self):
        items = (self._find_elements(self._found_results))
        items_list = list()
        for i in items:
            items_list.append(i.text)
        return (items_list)






