import pytest
import allure

from config import settings
from allure_commons.types import Severity
from fixtures.pages import courses_list_page_with_state
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.routes import AppRoute


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.suite(AllureFeature.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page_with_state: CoursesListPage):
        courses_list_page_with_state.visit(AppRoute.COURSES)
        courses_list_page_with_state.navbar.check_visible(username=settings.test_user.username)
        courses_list_page_with_state.sidebar.check_visible()
        courses_list_page_with_state.toolbar.check_visible()
        courses_list_page_with_state.check_visible_empty_view()

    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page_with_state: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit(AppRoute.COURSES_CREATE)
        create_course_page.create_course_toolbar.check_visible()
        create_course_page.image_upload_widget.check_visible(is_image_upload=False)
        create_course_page.create_course.check_visible(
            title="", max_score="0", min_score="0", description="", estimated_time=""
    )

        create_course_page.create_course_toolbar.check_visible()
        create_course_page.check_visible_exercise_empty_view()

        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.image_upload_widget.check_visible(is_image_upload=True)
        create_course_page.create_course.fill(
            title="Playwright",
            max_score="100",
            min_score="10",
            description="Playwright",
             estimated_time="2 weeks"
    )

        create_course_page.create_course_toolbar.click_create_course_button()

        courses_list_page_with_state.toolbar.check_visible()
        courses_list_page_with_state.course_view.check_visible(
        index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
    )

    @allure.title("Edit course")
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, courses_list_page_with_state, create_course_page: CreateCoursePage):
        create_course_page.visit(AppRoute.COURSES_CREATE)
        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.create_course.fill(
            title="Playwright",
            max_score="100",
            min_score="10",
            description="Playwright",
            estimated_time="2 weeks"
        )
        create_course_page.create_course_toolbar.click_create_course_button()
        courses_list_page_with_state.course_view.check_visible(index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks")
        courses_list_page_with_state.course_view_menu.click_edit(index=0)
        create_course_page.create_course.fill(
            title="Playwright2",
            max_score="1000",
            min_score="100",
            description="Playwright2",
            estimated_time="3 weeks"
        )
        create_course_page.create_course_toolbar.click_create_course_button()
        courses_list_page_with_state.course_view.check_visible(index=0, title="Playwright2", max_score="1000", min_score="100", estimated_time="3 weeks")











