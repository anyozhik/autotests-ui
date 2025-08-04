import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] Send data to the analytics.")


@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Initialize test settings.")


@pytest.fixture(scope="class")
def user():
    print("[CLASS] Create a user data once per a test class.")

@pytest.fixture(scope="function")
def browser():
    print("[FUNCTION] Open a browser for every autotest.")


class TestUserFlow:

    def test_user_can_login(self, settings, user, browser):
        pass


    def test_user_can_create_course(self, settings, user, browser):
        pass


class TestAccountFlow:

    def test_user_account(self, settings, user, browser):
        pass


