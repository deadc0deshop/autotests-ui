from components.base_component import BaseComponent

from playwright.sync_api import Page
from elements.button import Button

class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = Button(page, 'course-view-menu-button', 'Menu button')
        self.edit_menu_button = Button(page, 'course-view-edit-menu-item', 'Edit menu button')
        self.delete_menu_button = Button(page, 'course-view-delete-menu-item', 'Delete menu button')

    def click_edit(self, index:int):
        self.menu_button.click(nth=index)

        self.edit_menu_button.check_visible(nth=index)
        self.edit_menu_button.click(nth=index)

    def click_delete(self, index:int):
        self.menu_button.click(nth=index)

        self.delete_menu_button.check_visible(nth=index)
        self.delete_menu_button.click(nth=index)
