from selenium.webdriver.support.ui import WebDriverWait
from tests.Pages.Components.HeaderComponent import HeaderComponent
from tests.Pages.Components.FooterComponent import FooterComponent
from tests.Locators.BlogPageLocators import BlogPageLocators
from selenium.webdriver.common.keys import Keys
from tests.config import base_url
from selenium.webdriver.common.by import By
from utils import wait_for_element


class BlogPage(HeaderComponent, FooterComponent):
    """Blog page action methods come here. I.e. Python.org"""

    name = 'blog'

    element_locators = {
            'blog_page_title': BlogPageLocators.BLOG_PAGE_TITLE
            }

    def __init__(self, driver, independent: bool = True):
        super().__init__(driver)
        # merge all parent element locators with this element locators
        # ends up self.element_locators include all parent element locators
        self.element_locators = {
                **self.element_locators,
                **HeaderComponent.element_locators,
                **FooterComponent.element_locators,
                }

        if independent:
            self.driver.get(base_url)
            # need this one to avoid 'NosuchElementException'
            # - esp for when find element by link test
            # reference: https://stackoverflow.com/questions/6936149/how-to-use-find-element-by-link-text-properly-to-not-raise-nosuchelementexcept
            wait_for_element(self.driver, By.ID, 'root')
