from tests.Pages.BlogPage import BlogPage
from tests.Pages.HomePage import HomePage
import pytest
import marks
pytestmark = [marks.blog_page, pytest.mark.blog]


# BLOGLISTPAGE
@marks.all_ssize
def test_blog_page_should_display_blog_at_blog_page(responsive_target):

    home_page = HomePage(responsive_target['driver'])

    home_page.wait_for_element('blog_item')
    target_blog_item = home_page.get_one_of_blog_items(0)

    target_blog_title = target_blog_item.text

    # home_page.wait_for_element_to_be_visible(element=target_blog_item)
    target_blog_item.click()
    # home_page.click_element('blog_item')

    home_page.wait_for_animation_finish()
    blog_page = BlogPage(responsive_target['driver'], independent=False)

    blog_page.wait_for_element('blog_page_title')

    target_blog_page_title = blog_page.get_text_of_element('blog_page_title')

    assert target_blog_page_title in target_blog_title
