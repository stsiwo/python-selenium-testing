from selenium.webdriver.common.by import By


class EditBlogComponentLocators(object):
    """A class for main page locators. All main page locators should come here"""

    # blog info
    MAIN_IMAGE_INPUT = (By.CSS_SELECTOR, "input[id='update-blog-picture-input']")

    IMAGE_DELETE_ICON = (By.CSS_SELECTOR, "div[role='avatar-delete-icon']")

    BLOG_TITLE_INPUT = (By.CSS_SELECTOR, "input[id='title']")

    BLOG_SUBTITLE_INPUT = (By.CSS_SELECTOR, "input[id='subtitle']")

    BLOG_TAG_INPUT = (By.CSS_SELECTOR, "input[id='tag']")

    BLOG_TAG_DELETE_ICON = (By.CSS_SELECTOR, "div[class='small-icon-wrapper tags-item-close-icon-wrapper']")

    BLOG_CONTENT_INPUT = (By.CSS_SELECTOR, "div[role='blog-content-editable']")

    # toolbar
    IMAGE_TOOLBAR_ICON = (By.CSS_SELECTOR, "span[role='image-toolbar-icon']")

    EMBEDS_TOOLBAR_ICON = (By.CSS_SELECTOR, "span[role='embeds-toolbar-icon']")

    # publish
    PUBLISH_BUTTON = (By.CSS_SELECTOR, "input[role='publish-btn']")
