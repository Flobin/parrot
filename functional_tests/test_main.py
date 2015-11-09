from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MainTest(FunctionalTest):

    def test_sees_a_list_of_links_and_can_click_them(self):
        # Person visits the site
        self.browser.get(self.server_url)

        # Goes to submit a new link
        self.browser.find_element_by_class_name('submit-link').click()

        # Has to sign in. For now I don't know how to properly test it...
        # so this will have to do
        self.browser.find_element_by_id('id_login').send_keys('fcbf6e02@opayq.com')
        self.browser.find_element_by_id('id_password').send_keys('3Z#CqGRdG$GXQ3Dv')
        self.browser.find_element_by_id('id_remember').click()
        self.browser.find_element_by_class_name('primaryAction').click()

        # Goes to the main page and has to click the submit link again
        # Should fix this, too
        auth_div = self.browser.find_element_by_id('auth')
        self.assertIn("You are signed in", auth_div)
        self.browser.find_element_by_class_name('submit-link').click()

        # Sees the submit page
        self.assertIn("Submit a Link", self.browser.title)

        # Submits a link
        self.browser.find_element_by_id("title").send_keys('Poop')
        self.browser.find_element_by_id("url").send_keys('http://poop.bike')
        self.browser.find_element_by_id("url").send_keys(Keys.ENTER)

        # Is redirected and sees her link
        posts = self.browser.find_elements_by_class_name('link')
        self.assertGreater(len(posts),0)

        # Can click them to visit the url and a new page/tab actually opens
        firstpost = posts[0]
        firstlink = firstpost.find_element_by_tag_name('a').click()
        self.assertGreater(len(self.browser.window_handles), 0)

        # Posts have scores
        score = firstpost.find_elements_by_class_name('link-score')
        self.assertIsNotNone(score)
