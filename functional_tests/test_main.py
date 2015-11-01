from .base import FunctionalTest
from selenium import webdriver

class MainTest(FunctionalTest):

    def test_sees_a_list_of_links_and_can_click_them(self):
        # Person visits the site
        self.browser.get(self.server_url)

        # Sees several links
        posts = self.browser.find_elements_by_class_name('link')
        self.assertGreater(len(posts),0)

        # Can click them to visit the url and a new page/tab actually opens
        firstpost = posts[0]
        firstlink = firstpost.find_element_by_tag_name('a').click()
        self.assertGreater(len(self.browser.window_handles), 0)
