import pytest

import pandas.util.testing as tm


@pytest.fixture(name="datetime_series")
def datetime_series_fixture():
    return datetime_series()


def datetime_series():
    """
    Fixture for Series of floats with DatetimeIndex
    """
    s = tm.makeTimeSeries()
    s.name = "ts"
    return s


@pytest.fixture(name="string_series")
def string_series_fixture():
    return string_series()


def string_series():
    """
    Fixture for Series of floats with Index of unique strings
    """
    s = tm.makeStringSeries()
    s.name = "series"
    return s


@pytest.fixture(name="object_series")
def object_series_fixture():
    return object_series()


def object_series():
    """
    Fixture for Series of dtype datetime64[ns] with Index of unique strings
    """
    s = tm.makeObjectSeries()
    s.name = "objects"
    return s
