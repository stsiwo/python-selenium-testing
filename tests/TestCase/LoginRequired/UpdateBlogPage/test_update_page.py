from tests.Pages.UpdateBlogPage import UpdateBlogPage
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import marks
import os
pytestmark = [marks.update_blog_page, pytest.mark.update_blog]

# caveats:
# - this test share the login state for this entire module, so each test function might affect each other.
#   so please keep the state original if you modify the state during a test function
# ex)
#   if you add avatar image during a test function, as cleanup, you should remove the avatar image after assertion


# BLOGLISTPAGE
@marks.all_ssize
def test_update_blog_page_should_display_update_blog_page_heading(responsive_target, login_for_update_blog):

    update_blog_page = UpdateBlogPage(responsive_target['driver'], independent=False)

    # check page title does exist
    assert update_blog_page.does_have_text_in_page('Update Blog')


@marks.all_ssize
def test_update_blog_page_should_save_update_blog(responsive_target, login_for_update_blog):

    update_blog_page = UpdateBlogPage(responsive_target['driver'], independent=False)

    update_blog_page.scroll_to_top()

    update_blog_page.enter_text_in_element(os.getcwd()+"/tests/data/test_image.jpg", 'main_image_input')
    update_blog_page.enter_text_in_element('selenium title', 'blog_title_input', clear=True)
    update_blog_page.enter_text_in_element('selenium subtitle', 'blog_subtitle_input', clear=True)
    update_blog_page.enter_text_in_element_and_click('new-tag', 'blog_tag_input')
    # update_blog_page.enter_text_in_element('selenium content', 'blog_content_input')

    # update_blog_page.wait_for_text('saving...')
    # update_blog_page.wait_for_text('ok')
    update_blog_page.wait_for_text('ok')

    # errors:
    # - sometimes, fetch result display 'timeout error'
    # - firefox does not allow to input text at div element
    # - steps such as wait for element issue

    # should re-implement this

    # check page title does exist
    assert update_blog_page.does_element_exist('fetch_status_title')

    # clean up
    update_blog_page.click_element('image_delete_icon')
    update_blog_page.click_element('blog_tag_delete_icon')


@marks.all_ssize
def test_update_blog_page_should_publish_update_blog(responsive_target, login_for_update_blog):

    update_blog_page = UpdateBlogPage(responsive_target['driver'], independent=False)

    update_blog_page.scroll_to_top()

    update_blog_page.enter_text_in_element('selenium title', 'blog_title_input', clear=True)
    update_blog_page.enter_text_in_element('selenium subtitle', 'blog_subtitle_input', clear=True)

    update_blog_page.scroll_to_bottom()
    update_blog_page.wait_for_animation_finish()

    update_blog_page.click_element("publish_button")
    update_blog_page.wait_for_text('ok')

    # errors:
    # - sometimes, fetch result display 'timeout error'
    # - firefox does not allow to input text at div element
    # - steps such as wait for element issue

    # should re-implement this

    # check page title does exist
    assert update_blog_page.does_element_exist('fetch_status_title')
