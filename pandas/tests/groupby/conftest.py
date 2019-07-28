import numpy as np
import pytest

from pandas import DataFrame, MultiIndex
from pandas.core.groupby.base import reduction_kernels
from pandas.util import testing as tm


@pytest.fixture(name="mframe")
def mframe_fixture():
    return mframe()


def mframe():
    index = MultiIndex(
        levels=[["foo", "bar", "baz", "qux"], ["one", "two", "three"]],
        codes=[[0, 0, 0, 1, 1, 2, 2, 3, 3, 3], [0, 1, 2, 0, 1, 1, 2, 0, 1, 2]],
        names=["first", "second"],
    )
    return DataFrame(np.random.randn(10, 3), index=index, columns=["A", "B", "C"])


@pytest.fixture(name="df")
def df_fixture():
    return df()


def df():
    return DataFrame(
        {
            "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
            "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
            "C": np.random.randn(8),
            "D": np.random.randn(8),
        }
    )


@pytest.fixture(name="ts")
def ts_fixture():
    return ts()


def ts():
    return tm.makeTimeSeries()


@pytest.fixture(name="tsd")
def tsd_fixture():
    return tsd()


def tsd():
    return tm.getTimeSeriesData()


@pytest.fixture(name="tsframe")
def tsframe_fixture(tsd):
    return tsframe(tsd)


def tsframe(tsd):
    return DataFrame(tsd)


@pytest.fixture(name="df_mixed_floats")
def df_mixed_floats_fixture():
    return df_mixed_floats()


def df_mixed_floats():
    return DataFrame(
        {
            "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
            "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
            "C": np.random.randn(8),
            "D": np.array(np.random.randn(8), dtype="float32"),
        }
    )


@pytest.fixture(name="three_group")
def three_group_fixture():
    return three_group()


def three_group():
    return DataFrame(
        {
            "A": [
                "foo",
                "foo",
                "foo",
                "foo",
                "bar",
                "bar",
                "bar",
                "bar",
                "foo",
                "foo",
                "foo",
            ],
            "B": [
                "one",
                "one",
                "one",
                "two",
                "one",
                "one",
                "one",
                "two",
                "two",
                "two",
                "one",
            ],
            "C": [
                "dull",
                "dull",
                "shiny",
                "dull",
                "dull",
                "shiny",
                "shiny",
                "dull",
                "shiny",
                "shiny",
                "shiny",
            ],
            "D": np.random.randn(11),
            "E": np.random.randn(11),
            "F": np.random.randn(11),
        }
    )


@pytest.fixture(params=sorted(reduction_kernels), name="reduction_func")
def reduction_func_fixture(request):
    return reduction_func(request)


def reduction_func(request):
    """yields the string names of all groupby reduction functions, one at a time.
    """
    return request.param
