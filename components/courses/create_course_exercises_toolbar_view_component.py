from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self,page):
        super().__init__(page)

        # Область пустого Exercises
        self.title = Text(page, 'create-course-exercises-box-toolbar-title-text', 'Title')
        self.exercises_button = Button(page, 'create-course-exercises-box-toolbar-create-exercise-button', 'Exercises button')

    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Exercises')
        self.exercises_button.check_visible()

    def click_create_exercise_button(self):
        self.exercises_button.click()

