from selenium.webdriver.common.by import By
from tests.Locators.BaseLocator import BaseLocator


class NewBlogPageLocators(BaseLocator):
    """A class for main page locators. All main page locators should come here"""

    # By.CLASS_NAME behave wierdly

    PAGE_TITLE = (By.CSS_SELECTOR, "h2[class='page-title']")

    PROFILE_LINK = (By.LINK_TEXT, "Profile")

    BLOG_MANAGEMENT_LINK = (By.LINK_TEXT, "Blog Management")

    # fetch status
    FETCH_STATUS_TITLE = (By.CSS_SELECTOR, "h3[class='fetch-status-title']")
