from playwright.sync_api import Page, expect

from components.courses.course_view_component import CourseViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SideBarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.courses.courses_list_toolbaar_view_component import CoursesListToolbarViewComponent
from pages.base_page import BasePage


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SideBarComponent(page)
        self.toolbar = CoursesListToolbarViewComponent(page)
        self.course_view = CourseViewComponent(page)
        self.empty_view = EmptyViewComponent(page, identifier='courses-list')




    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )





