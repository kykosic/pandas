from datetime import datetime

import numpy as np
import pytest

from pandas import DataFrame, Series
from pandas.core.indexes.datetimes import date_range
from pandas.core.indexes.period import period_range

# The various methods we support
downsample_methods = [
    "min",
    "max",
    "first",
    "last",
    "sum",
    "mean",
    "sem",
    "median",
    "prod",
    "var",
    "std",
    "ohlc",
    "quantile",
]
upsample_methods = ["count", "size"]
series_methods = ["nunique"]
resample_methods = downsample_methods + upsample_methods + series_methods


@pytest.fixture(params=downsample_methods, name=downsample_method)
def downsample_method_fixture(request):
    return downsample_method(request)


def downsample_method(request):
    """Fixture for parametrization of Grouper downsample methods."""
    return request.param


@pytest.fixture(params=upsample_methods, name=upsample_method)
def upsample_method_fixture(request):
    return upsample_method(request)


def upsample_method(request):
    """Fixture for parametrization of Grouper upsample methods."""
    return request.param


@pytest.fixture(params=resample_methods, name=resample_method)
def resample_method_fixture(request):
    return resample_method(request)


def resample_method(request):
    """Fixture for parametrization of Grouper resample methods."""
    return request.param


@pytest.fixture(name=simple_date_range_series)
def simple_date_range_series_fixture():
    return simple_date_range_series()


def simple_date_range_series():
    """
    Series with date range index and random data for test purposes.
    """

    def _simple_date_range_series(start, end, freq="D"):
        rng = date_range(start, end, freq=freq)
        return Series(np.random.randn(len(rng)), index=rng)

    return _simple_date_range_series


@pytest.fixture(name=simple_period_range_series)
def simple_period_range_series_fixture():
    return simple_period_range_series()


def simple_period_range_series():
    """
    Series with period range index and random data for test purposes.
    """

    def _simple_period_range_series(start, end, freq="D"):
        rng = period_range(start, end, freq=freq)
        return Series(np.random.randn(len(rng)), index=rng)

    return _simple_period_range_series


@pytest.fixture(name=_index_start)
def _index_start_fixture():
    return _index_start()


def _index_start():
    """Fixture for parametrization of index, series and frame."""
    return datetime(2005, 1, 1)


@pytest.fixture(name=_index_end)
def _index_end_fixture():
    return _index_end()


def _index_end():
    """Fixture for parametrization of index, series and frame."""
    return datetime(2005, 1, 10)


@pytest.fixture(name=_index_freq)
def _index_freq_fixture():
    return _index_freq()


def _index_freq():
    """Fixture for parametrization of index, series and frame."""
    return "D"


@pytest.fixture(name=_index_name)
def _index_name_fixture():
    return _index_name()


def _index_name():
    """Fixture for parametrization of index, series and frame."""
    return None


@pytest.fixture(name=index)
def index_fixture(_index_fixture_factory, _index_fixture_start, _index_fixture_end, _index_fixture_freq, _index_fixture_name):
    return index(_index_factory, _index_start, _index_end, _index_freq, _index_name)


def index(_index_factory, _index_start, _index_end, _index_freq, _index_name):
    """Fixture for parametrization of date_range, period_range and
    timedelta_range indexes"""
    return _index_factory(_index_start, _index_end, freq=_index_freq, name=_index_name)


@pytest.fixture(name=_static_values)
def _static_values_fixture(index):
    return _static_values(index)


def _static_values(index):
    """Fixture for parametrization of values used in parametrization of
    Series and DataFrames with date_range, period_range and
    timedelta_range indexes"""
    return np.arange(len(index))


@pytest.fixture(name=_series_name)
def _series_name_fixture():
    return _series_name()


def _series_name():
    """Fixture for parametrization of Series name for Series used with
    date_range, period_range and timedelta_range indexes"""
    return None


@pytest.fixture(name=series)
def series_fixture(index, _series_fixture_name, _static_values):
    return series(index, _series_name, _static_values)


def series(index, _series_name, _static_values):
    """Fixture for parametrization of Series with date_range, period_range and
    timedelta_range indexes"""
    return Series(_static_values, index=index, name=_series_name)


@pytest.fixture(name=empty_series)
def empty_series_fixture(series):
    return empty_series(series)


def empty_series(series):
    """Fixture for parametrization of empty Series with date_range,
    period_range and timedelta_range indexes"""
    return series[:0]


@pytest.fixture(name=frame)
def frame_fixture(index, _series_name, _static_values):
    return frame(index, _series_name, _static_values)


def frame(index, _series_name, _static_values):
    """Fixture for parametrization of DataFrame with date_range, period_range
    and timedelta_range indexes"""
    # _series_name is intentionally unused
    return DataFrame({"value": _static_values}, index=index)


@pytest.fixture(name=empty_frame)
def empty_frame_fixture(series):
    return empty_frame(series)


def empty_frame(series):
    """Fixture for parametrization of empty DataFrame with date_range,
    period_range and timedelta_range indexes"""
    index = series.index[:0]
    return DataFrame(index=index)


@pytest.fixture(params=[Series, DataFrame], name=series_and_frame)
def series_and_frame_fixture(request, series, frame):
    return series_and_frame(request, series, frame)


def series_and_frame(request, series, frame):
    """Fixture for parametrization of Series and DataFrame with date_range,
    period_range and timedelta_range indexes"""
    if request.param == Series:
        return series
    if request.param == DataFrame:
        return frame
