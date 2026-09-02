from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class CoursesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)


        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_courses_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

        self.empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        self.empty_view_title_text = page.get_by_test_id('courses-list-empty-view-title-text')
        self.empty_view_description_text = page.get_by_test_id('courses-list-empty-view-description-text')

        self.courses_title = page.get_by_test_id('course-widget-title-text')
        self.courses_image = page.get_by_test_id('course-preview-image')
        self.courses_max_text = page.get_by_test_id('course-max-score-info-row-view-text')
        self.courses_min_text = page.get_by_test_id('course-min-score-info-row-view-text')
        self.courses_estimated_text = page.get_by_test_id('course-estimated-time-info-row-view-text')

        self.courses_menu_button = page.get_by_test_id('course-view-menu-button')
        self.courses_edit_menu_button = page.get_by_test_id('course-view-edit-menu-item')
        self.courses_delete_menu_button = page.get_by_test_id('course-view-delete-menu-item')



    def check_visible_courses_title(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text('Courses')

    def check_visible_empty_view(self):
        expect(self.empty_view_icon).to_be_visible()

        expect(self.empty_view_title_text).to_be_visible()
        expect(self.empty_view_title_text).to_have_text('There is no results')

        expect(self.empty_view_description_text).to_be_visible()
        expect(self.empty_view_description_text).to_have_text('Results from the load test pipeline will be displayed here')

    def check_visible_create_course_button(self):
        expect(self.create_courses_button).to_be_visible()

    def check_visible_courses_card(
            self,
            index: int,
            title: str,
            max_score: str,
            min_score: str,
            estimated_time: str
    ):
        expect(self.courses_image.nth(index)).to_be_visible()

        expect(self.courses_title.nth(index)).to_be_visible()
        expect(self.courses_title.nth(index)).to_have_text(title)

        expect(self.courses_max_text.nth(index)).to_be_visible()
        expect(self.courses_max_text.nth(index)).to_have_text(f'Max score: {max_score}')

        expect(self.courses_min_text.nth(index)).to_be_visible()
        expect(self.courses_min_text.nth(index)).to_have_text(f'Min score: {min_score}')

        expect(self.courses_estimated_text.nth(index)).to_be_visible()
        expect(self.courses_estimated_text.nth(index)).to_have_text(f'Estimated time: {estimated_time}')

    def click_edit_course(self, index: int):
        self.courses_menu_button.nth(index).click()

        expect(self.courses_edit_menu_button.nth(index)).to_be_visible()
        self.courses_edit_menu_button.nth(index).click()

        expect(self.courses_delete_menu_button.nth(index)).to_be_visible()
        self.courses_delete_menu_button.nth(index).click()

    def click_delete_course(self, index: int):
        ...

