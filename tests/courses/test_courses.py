import pytest

from fixtures.pages import courses_list_page_with_state
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_empty_courses_list(self, courses_list_page_with_state: CoursesListPage):
        courses_list_page_with_state.visit(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        courses_list_page_with_state.navbar.check_visible('username')
        courses_list_page_with_state.sidebar.check_visible()
        courses_list_page_with_state.toolbar.check_visible()
        courses_list_page_with_state.check_visible_empty_view()


    def test_create_course(self, courses_list_page_with_state: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.create_course_toolbar.check_visible()
        create_course_page.image_upload_widget.check_visible(is_image_upload=False)
        create_course_page.create_course.check_visible(
            title="", max_score="0", min_score="0", description="", estimated_time=""
    )

        create_course_page.create_course_toolbar.check_visible()
        create_course_page.check_visible_exercise_empty_view()

        create_course_page.image_upload_widget.upload_preview_image("./testdata/files/image.png")
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

    def test_edit_course(self, courses_list_page_with_state, create_course_page: CreateCoursePage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.image_upload_widget.upload_preview_image("./testdata/files/image.png")
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











