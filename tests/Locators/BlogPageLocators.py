from selenium.webdriver.common.by import By
from tests.Locators.BaseLocator import BaseLocator


class BlogPageLocators(BaseLocator):
    """A class for main page locators. All main page locators should come here"""
    BLOG_PAGE_TITLE = (By.CSS_SELECTOR, "h1[role='blog-title']")
