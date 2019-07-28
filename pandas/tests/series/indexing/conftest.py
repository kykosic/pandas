import pytest

from pandas.tests.series.common import TestData


@pytest.fixture(scope="module", name="test_data")
def test_data_fixture():
    return test_data()


def test_data():
    return TestData()
