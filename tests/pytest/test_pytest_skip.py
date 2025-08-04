import pytest

@pytest.mark.skip(reason="Feature is in progress")
def test_feature_in_development():
    pass

@pytest.mark.skip(reason="Feature is in progress")
class TestSuiteSkip:
    def test_feature_in_development_1(self):
        pass

    def test_feature_in_development_2(self):
        pass