import allure

@allure.step('Opening browser')
def open_browser():
    pass

@allure.step('Creating course with title "{title}"')
def create_course(title: str):
    pass

@allure.step('Closing browser')
def close_browser():
    pass



def test_feature():
    open_browser()
    create_course(title="Locust")
    create_course(title="Python")
    create_course(title="Pytest")
    close_browser()

