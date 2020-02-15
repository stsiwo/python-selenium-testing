from tests.Pages.BasePage import BasePage
from tests.Locators.EditBlogComponentLocators import EditBlogComponentLocators


class EditBlogComponent(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    element_locators = {
            'main_image_input': EditBlogComponentLocators.MAIN_IMAGE_INPUT,
            'image_delete_icon': EditBlogComponentLocators.IMAGE_DELETE_ICON,
            'blog_title_input': EditBlogComponentLocators.BLOG_TITLE_INPUT,
            'blog_subtitle_input': EditBlogComponentLocators.BLOG_SUBTITLE_INPUT,
            'blog_tag_input': EditBlogComponentLocators.BLOG_TAG_INPUT,
            'blog_tag_delete_icon': EditBlogComponentLocators.BLOG_TAG_DELETE_ICON,
            'blog_content_input': EditBlogComponentLocators.BLOG_CONTENT_INPUT,
            'image_toolbar_icon': EditBlogComponentLocators.IMAGE_TOOLBAR_ICON,
            'embeds_toolbar_icon': EditBlogComponentLocators.EMBEDS_TOOLBAR_ICON,
            'publish_button': EditBlogComponentLocators.PUBLISH_BUTTON,
            }

    def __init__(self, driver):
        super().__init__(driver)
