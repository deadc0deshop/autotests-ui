from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self,page):
        super().__init__(page)

        # Область пустого Exercises
        self.title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.exercises_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

    def check_visible(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Exercises')
        expect(self.exercises_button).to_be_visible()

    def click_create_exercise_button(self):
        self.exercises_button.click()

