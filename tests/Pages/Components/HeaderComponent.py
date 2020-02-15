from selenium.webdriver.support.ui import WebDriverWait
from tests.Pages.BasePage import BasePage
from tests.Locators.HeaderComponentLocators import HeaderComponentLocators
import time


class HeaderComponent(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    element_locators = {
            'logo_title': HeaderComponentLocators.LOGO_TITLE,
            'menu': HeaderComponentLocators.MENU,
            'menu_toggle_icon': HeaderComponentLocators.MENU_TOGGLE_ICON,
            'menu_close_icon': HeaderComponentLocators.MENU_CLOSE_ICON,
            'blogs_menu_link': HeaderComponentLocators.BLOGS_NAV_ITEM,
            'signup_menu_link': HeaderComponentLocators.SIGNUP_NAV_ITEM,
            'login_menu_link': HeaderComponentLocators.LOGIN_NAV_ITEM,
            'account_menu_link': HeaderComponentLocators.ACCOUNT_NAV_ITEM,
            'logout_menu_link': HeaderComponentLocators.LOGOUT_NAV_ITEM,
            }

    def __init__(self, driver):
        super().__init__(driver)

    def get_text_of_element_in_header(self, locator: str):
        if locator not in self.element_locators:
            raise Exception('locator you provide is not available. available locators: %s' % self.element_locators)

        target_element = self.driver.find_element(*self.element_locators[locator])
        return target_element.text

    def click_element_in_header(self, locator: str, waiting_element_locator: str = None, animation_duration_sc: int = None):
        if locator not in self.element_locators:
            raise Exception('locator you provide is not available. available locators: %s' % self.element_locators)

        target_element = self.driver.find_element(*self.element_locators[locator])
        target_element.click()
        if animation_duration_sc is not None:
            time.sleep(animation_duration_sc)  # works!! use this for wait animation done
        if waiting_element_locator is not None:
            WebDriverWait(self.driver, 500).until(
                    lambda driver: driver.find_elements(*self.element_locators[waiting_element_locator])
                    )

    def get_size_of_element_in_header(self, locator: str):
        """ use when want to check an element is on the document but hidden because of its size is 0 """
        if locator not in self.element_locators:
            raise Exception('locator you provide is not available. available locators: %s' % self.element_locators)

        target_element = self.driver.find_element(*self.element_locators[locator])
        return target_element.size

    def check_visibility_of_element_in_header(self, locator: str):
        if locator not in self.element_locators:
            raise Exception('locator you provide is not available. available locators: %s' % self.element_locators)
        target_element = self.driver.find_element(*self.element_locators[locator])
        return target_element.is_displayed()
