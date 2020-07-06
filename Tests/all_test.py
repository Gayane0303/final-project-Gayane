from PageObjects.blog_page import Blogpage
from PageObjects.home_page import Home
import time

from PageObjects.nested_iframes_review_us_page import ReviewUs
from PageObjects.search_result_page import SearchResultsPage
from PageObjects.switch_to_tab_twitter_page import TwitterPage
from PageObjects.youtube_page import YouTubePage


class TestHomePage():


    # Searching for a text and checking the found results' count, getting all the results links and checks if they all contain the searched item
    def test_search(self, browser):
        search_ = Home(browser)
        search_result_page_ = SearchResultsPage(browser)

        assert search_.page_title() == "Google Sites & G Suite Experts"
        search_.click_on_search_icon()
        search_.click_on_search_input()
        search_.search_text_("google")
        assert search_.get_filled_text() == "google"
        search_.search_item()
        time.sleep(3)
        assert search_.get_current_url() == "https://www.steegle.com/_/search?query=google&scope=site&showTabs=false"
        assert search_result_page_.check_found_results_count() == 10
        for i in search_result_page_.get_found_items_links():
            assert i.lower().find("google") != -1


    # Scroll into the footer, switches to the 4 nested items and get the text inside them
    def test_nested_irames_review_us(self, browser):
        review_us = ReviewUs(browser)

        review_us.scroll_into_footer()
        review_us.switch_to_iframes()
        review_us.wait_review_us_displayed()
        review_us.get_review_us_element_text()
        assert review_us.get_review_us_element_text() == 'Review us on'
        time.sleep(2)


    # 1. Scroll into the footer
    # 2. Wait twitter to be visible and click on Twitter
    # 3. Switch into the twitter new opened tab, check the link
    # 4. Switch into the first tab and click on Youtube
    # 5. Switch into the Youtube opened in a new tab and check the link
    def test_switch_to_tab_twitter_youtube(self, browser):
        review_us = ReviewUs(browser)
        twitter = TwitterPage(browser)
        youtube = YouTubePage(browser)
        home = Home(browser)

        review_us.scroll_into_footer()
        home.wait_twitter_displayed()
        home.click_on_twitter_icon()
        twitter.switch_to_opened_tab()
        time.sleep(3)
        assert twitter.get_current_url() == "https://twitter.com/DrSteegle"
        home.switch_to_tab_0()
        home.click_on_youtube_icon()
        youtube.switch_to_opened_tab2()
        assert youtube.get_current_url() == "https://www.youtube.com/Steegle"

    # Hover on About and click on item, check the link, the tile and logo displayed
    def test_blog(self, browser):
        about = Home(browser)
        blog = Blogpage(browser)

        about.hover_on_about()
        blog.click_on_blog()
        assert blog.get_page_title() == "Blog"
        assert blog.get_current_url() == "https://www.steegle.com/news"
        blog.wait_logo_displayed()


