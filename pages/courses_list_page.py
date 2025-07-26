from playwright.sync_api import Page,expect
from pages.base_page import BasePage
from dataclasses import dataclass

@dataclass
class CheckVisibleCourseCardParams:
    index: int
    title: str
    max_score: str
    min_score: str
    estimated_time: str
class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Заголовок и кнопка создания курса
        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

        # Карточка курса
        self.course_title = page.get_by_test_id('course-widget-title-text')
        self.course_image = page.get_by_test_id('course-preview-image')
        self.course_max_text = page.get_by_test_id('course-max-score-info-row-view-text')
        self.course_min_text = page.get_by_test_id('course-min-score-info-row-view-text')
        self.course_estimated_time = page.get_by_test_id('course-estimated-time-info-row-view-text')

        # Меню курса
        self.course_menu_button = page.get_by_test_id('course-view-menu-button')
        self.course_edit_menu_button = page.get_by_test_id('course-view-edit-menu-item')
        self.course_delete_menu_button = page.get_by_test_id('course-view-delete-menu-item')

        # Пустой блок при отсутствии курсов
        self.empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        self.empty_view_tittle = page.get_by_test_id('courses-list-empty-view-title-text')
        self.empty_view_description = page.get_by_test_id('courses-list-empty-view-description-text')

    def check_visible_courses_title(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text('Courses')

    def check_visible_empty_view(self):
        expect(self.empty_view_icon).to_be_visible()
        expect(self.empty_view_tittle).to_be_visible()
        expect(self.empty_view_tittle).to_have_text('There is no results')
        expect(self.empty_view_description).to_be_visible()
        expect(self.empty_view_description).to_have_text('Results from the load test pipeline will be displayed here')

    def check_visible_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def check_click_create_course_button(self):
        self.create_course_button.click()

    def check_visible_menu_card(self, params: CheckVisibleCourseCardParams):
        expect(self.course_image.nth(params.index)).to_be_visible()

        expect(self.course_title.nth(params.index)).to_be_visible()
        expect(self.course_title.nth(params.index)).to_have_text(params.title)

        expect(self.course_max_text.nth(params.index)).to_be_visible()
        expect(self.course_max_text.nth(params.index)).to_have_text(f'Max score: {params.max_score}')

        expect(self.course_min_text.nth(params.index)).to_be_visible()
        expect(self.course_min_text.nth(params.index)).to_have_text(f'Min score: {params.min_score}')

        expect(self.course_estimated_time.nth(params.index)).to_be_visible()
        expect(self.course_estimated_time.nth(params.index)).to_have_text(f'Estimated time: {params.estimated_time}')

    def click_edit_course(self, index: int):
        self.course_menu_button.nth(index).click()

        expect(self.course_edit_menu_button.nth(index)).to_be_visible()
        self.course_edit_menu_button.nth(index).click()

    def click_delete_course(self, index: int):
        self.course_menu_button.nth(index).click()

        expect(self.course_delete_menu_button.nth(index)).to_be_visible()
        self.course_delete_menu_button.nth(index).click()












