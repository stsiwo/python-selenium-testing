import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from tests.Pages.HomePage import HomePage
from tests.Pages.SignupPage import SignupPage
from tests.Pages.LoginPage import LoginPage
from tests.Pages.BlogListPage import BlogListPage
from tests.Pages.ProfilePage import ProfilePage
from tests.Pages.BlogManagementPage import BlogManagementPage
from tests.Pages.NewBlogPage import NewBlogPage
from tests.Pages.UpdateBlogPage import UpdateBlogPage
from tests.Pages.BlogPage import BlogPage
import tests.config as cfg


def pytest_addoption(parser):
    parser.addoption(
        "--driver", action="store", default="all", help="type of driver you want to use with test. available options: {}".format(cfg.available_driver_options)
    )
    parser.addoption(
        "--ssize", action="store", default="all", help="type of screen size you want to use with test. available options: {}".format(cfg.available_ssize_options)
    )
    parser.addoption(
        "--page", action="store", default="all", help="type of page you want to use with test. available options: {}".format(cfg.available_page_options)
    )


@pytest.fixture(params=cfg.available_driver_options, scope='session')
def target_driver(request):
    print("*** target_driver setup ***")
    driver_option = request.config.getoption('--driver')
    print(driver_option)

    # skip not selected driver by command line option
    if driver_option != 'all' and driver_option != request.param:
        pytest.skip('skipped on this size because of command line option: {}'.format(driver_option))

    if 'chrome' == request.param:
        print('target driver is chrome')
        target_driver = webdriver.Remote(
                 command_executor=cfg.seleniumServerUrl,
                 desired_capabilities=DesiredCapabilities.CHROME
             )
    if 'firefox' == request.param:
        print('target driver is firefox')
        target_driver = webdriver.Remote(
                 command_executor=cfg.seleniumServerUrl,
                 desired_capabilities=DesiredCapabilities.FIREFOX
             )

    def fin():
        print('start teardown target_driver')
        target_driver.close()

    request.addfinalizer(fin)
    return target_driver


@pytest.fixture(params=cfg.available_ssize_options)
def responsive_target(target_driver, request):
    print("*** responsive_target setup ***")
    target_driver.set_window_position(0, 0)
    if 'mobile' == request.param:
        model_size = {'width': cfg.ssize_width_mobile, 'height': cfg.ssize_height}
        target_driver.set_window_size(model_size['width'], model_size['height'])
    if 'tablet' == request.param:
        model_size = {'width': cfg.ssize_width_tablet, 'height': cfg.ssize_height}
        target_driver.set_window_size(model_size['width'], model_size['height'])
    if 'laptop' == request.param:
        model_size = {'width': cfg.ssize_width_laptop, 'height': cfg.ssize_height}
        target_driver.set_window_size(model_size['width'], model_size['height'])
    if 'desktop' == request.param:
        model_size = {'width': cfg.ssize_width_desktop, 'height': cfg.ssize_height}
        target_driver.set_window_size(model_size['width'], model_size['height'])
    return {
            'driver': target_driver,
            'size_type': request.param,
            'model_size': model_size
            }


# params cause to run multiple times as the same number of its value (usually array)
# add when new page added
@pytest.fixture(params=cfg.available_page_options)
def TargetPage(request):
    print("*** TargetPage setup ***")
    print(request.param)
    if 'home' == request.param:
        return HomePage
    if 'signup' == request.param:
        return SignupPage
    if 'login' == request.param:
        return LoginPage
    if 'blog_list' == request.param:
        return BlogListPage
    if 'profile' == request.param:
        return ProfilePage
    if 'blog_management' == request.param:
        return BlogManagementPage
    if 'new_blog' == request.param:
        return NewBlogPage
    if 'update_blog' == request.param:
        return UpdateBlogPage
    if 'blog' == request.param:
        return BlogPage


@pytest.fixture()
def login_if_necessary_for_component(TargetPage, responsive_target):
    print("*** login_if_necessary_for_component setup ***")
    print("target page: {0} and target ssize: {1} and".format(TargetPage.name, responsive_target['size_type']))

    if TargetPage.name in cfg.member_only_pages:
        print("*** login required at {}".format(TargetPage.name))
        login_page = LoginPage(responsive_target['driver'])

        login_page.type_text_in_input(locator='email_input', text=cfg.test_user_email_for_profile)
        login_page.type_text_in_input(locator='password_input', text=cfg.test_user_password_for_profile)
        login_page.type_text_in_input(locator='confirm_input', text=cfg.test_user_password_for_profile)
        login_page.click_element('submit_btn')

        home_page = HomePage(responsive_target['driver'], independent=False)

        home_page.wait_for_element('slogan')

    yield None

    if TargetPage.name in cfg.member_only_pages:
        print("*** logout required at {}".format(TargetPage.name))
        home_page = HomePage(responsive_target['driver'], independent=False)
        # home_page.wait_for_element('slogan')

        if responsive_target['size_type'] != 'desktop':
            print("*** desktop size requires open nav menu***")
            home_page.click_element_in_header('menu_toggle_icon', waiting_element_locator=None, animation_duration_sc=cfg.animation_duration_sc)
        home_page.click_element_in_header('logout_menu_link')


@pytest.fixture(autouse=True)
def selective_marks(request, responsive_target, TargetPage):
    print("*** selective_marks setup ***")
    ssize_option = request.config.getoption('--ssize')
    available_ssize_command_options = [*cfg.available_ssize_options, 'all']

    print("*** debugging ***")
    print("command line options: ssize: {0}, page: {1}, driver: {2} ".format(request.config.getoption('--ssize'), request.config.getoption('--page'), request.config.getoption('--driver')))

    if ssize_option not in available_ssize_command_options:
        raise Exception('provided ssize option ({}) is not supoorted. available options are {}'.format(ssize_option, available_ssize_command_options))

    # skip test if ssize does not match with target test's mark or does not spcecify with command line option
    if request.node.get_closest_marker('responsive'):
        # if test function does hot have responsive mark with its ssize, skip
        if responsive_target.get('size_type') not in request.node.get_closest_marker('responsive').kwargs['size']:
            pytest.skip('skipped on this size because of marks: {}'.format(responsive_target.get('size_type')))

        # also, if command line option is specified about ssize and current fixture parameter is not match, skip because it is not specified ssize by user
        if ssize_option != 'all' and ssize_option not in responsive_target['size_type']:
            pytest.skip('skipped on this size because of command line option: {} is not {}'.format(ssize_option, responsive_target['size_type']))

    page_option = request.config.getoption('--page')
    available_page_command_options = [*cfg.available_page_options, 'all']

    if page_option not in available_page_command_options:
        raise Exception('provided page option ({}) is not supoorted. available options are {}'.format(page_option, available_page_command_options))

    # skip test if size does not match with target test's mark or does not spcecify with command line option
    if request.node.get_closest_marker('page'):
        print(TargetPage.name)
        print(request.node.get_closest_marker('page').kwargs['page'])
        if TargetPage.name not in request.node.get_closest_marker('page').kwargs['page']:
            print(TargetPage.name)
            print(request.node.get_closest_marker('page').kwargs['page'])
            pytest.skip('skipped on this size because of not selected marks: {}'.format(TargetPage.name))

        if page_option != 'all' and page_option != TargetPage.name:
            print(page_option)
            print(TargetPage.name)
            pytest.skip('skipped on this page because of command line option: {} is not {}'.format(page_option, TargetPage.name))
