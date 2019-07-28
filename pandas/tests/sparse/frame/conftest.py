import numpy as np
import pytest

from pandas import DataFrame, SparseArray, SparseDataFrame, bdate_range

data = {
    "A": [np.nan, np.nan, np.nan, 0, 1, 2, 3, 4, 5, 6],
    "B": [0, 1, 2, np.nan, np.nan, np.nan, 3, 4, 5, 6],
    "C": np.arange(10, dtype=np.float64),
    "D": [0, 1, 2, 3, 4, 5, np.nan, np.nan, np.nan, np.nan],
}
dates = bdate_range("1/1/2011", periods=10)


# fixture names must be compatible with the tests in
# tests/frame/test_api.SharedWithSparse


@pytest.fixture(name="float_frame_dense")
def float_frame_dense_fixture():
    return float_frame_dense()


def float_frame_dense():
    """
    Fixture for dense DataFrame of floats with DatetimeIndex

    Columns are ['A', 'B', 'C', 'D']; some entries are missing
    """
    return DataFrame(data, index=dates)


@pytest.fixture(name="float_frame")
def float_frame_fixture():
    return float_frame()


def float_frame():
    """
    Fixture for sparse DataFrame of floats with DatetimeIndex

    Columns are ['A', 'B', 'C', 'D']; some entries are missing
    """
    # default_kind='block' is the default
    return SparseDataFrame(data, index=dates, default_kind="block")


@pytest.fixture(name="float_frame_int_kind")
def float_frame_int_kind_fixture():
    return float_frame_int_kind()


def float_frame_int_kind():
    """
    Fixture for sparse DataFrame of floats with DatetimeIndex

    Columns are ['A', 'B', 'C', 'D'] and default_kind='integer'.
    Some entries are missing.
    """
    return SparseDataFrame(data, index=dates, default_kind="integer")


@pytest.fixture(name="float_string_frame")
def float_string_frame_fixture():
    return float_string_frame()


def float_string_frame():
    """
    Fixture for sparse DataFrame of floats and strings with DatetimeIndex

    Columns are ['A', 'B', 'C', 'D', 'foo']; some entries are missing
    """
    sdf = SparseDataFrame(data, index=dates)
    sdf["foo"] = SparseArray(["bar"] * len(dates))
    return sdf


@pytest.fixture(name="float_frame_fill0_dense")
def float_frame_fill0_dense_fixture():
    return float_frame_fill0_dense()


def float_frame_fill0_dense():
    """
    Fixture for dense DataFrame of floats with DatetimeIndex

    Columns are ['A', 'B', 'C', 'D']; missing entries have been filled with 0
    """
    values = SparseDataFrame(data).values
    values[np.isnan(values)] = 0
    return DataFrame(values, columns=["A", "B", "C", "D"], index=dates)


@pytest.fixture(name="float_frame_fill0")
def float_frame_fill0_fixture():
    return float_frame_fill0()


def float_frame_fill0():
    """
    Fixture for sparse DataFrame of floats with DatetimeIndex

    Columns are ['A', 'B', 'C', 'D']; missing entries have been filled with 0
    """
    values = SparseDataFrame(data).values
    values[np.isnan(values)] = 0
    return SparseDataFrame(
        values, columns=["A", "B", "C", "D"], default_fill_value=0, index=dates
    )


@pytest.fixture(name="float_frame_fill2_dense")
def float_frame_fill2_dense_fixture():
    return float_frame_fill2_dense()


def float_frame_fill2_dense():
    """
    Fixture for dense DataFrame of floats with DatetimeIndex

    Columns are ['A', 'B', 'C', 'D']; missing entries have been filled with 2
    """
    values = SparseDataFrame(data).values
    values[np.isnan(values)] = 2
    return DataFrame(values, columns=["A", "B", "C", "D"], index=dates)


@pytest.fixture(name="float_frame_fill2")
def float_frame_fill2_fixture():
    return float_frame_fill2()


def float_frame_fill2():
    """
    Fixture for sparse DataFrame of floats with DatetimeIndex

    Columns are ['A', 'B', 'C', 'D']; missing entries have been filled with 2
    """
    values = SparseDataFrame(data).values
    values[np.isnan(values)] = 2
    return SparseDataFrame(
        values, columns=["A", "B", "C", "D"], default_fill_value=2, index=dates
    )


@pytest.fixture(name="empty_frame")
def empty_frame_fixture():
    return empty_frame()


def empty_frame():
    """
    Fixture for empty SparseDataFrame
    """
    return SparseDataFrame()
