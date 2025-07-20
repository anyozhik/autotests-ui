from playwright.sync_api import expect
import pytest

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    title_header = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(title_header).to_be_visible()
    expect(title_header).to_have_text('Courses')

    courses_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_icon).to_be_visible()

    block_header = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(block_header).to_be_visible()
    expect(block_header).to_have_text('There is no results')

    block_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(block_text).to_be_visible()
    expect(block_text).to_have_text('Results from the load test pipeline will be displayed here')