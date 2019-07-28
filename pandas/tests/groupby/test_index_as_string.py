import numpy as np
import pytest

import pandas as pd
from pandas.util.testing import assert_frame_equal, assert_series_equal


@pytest.fixture(params=[["inner"], ["inner", "outer"]], name="frame")
def frame_fixture(request):
    return frame(request)


def frame(request):
    levels = request.param
    df = pd.DataFrame(
        {
            "outer": ["a", "a", "a", "b", "b", "b"],
            "inner": [1, 2, 3, 1, 2, 3],
            "A": np.arange(6),
            "B": ["one", "one", "two", "two", "one", "one"],
        }
    )
    if levels:
        df = df.set_index(levels)

    return df


@pytest.fixture(name="series")
def series_fixture():
    return series()


def series():
    df = pd.DataFrame(
        {
            "outer": ["a", "a", "a", "b", "b", "b"],
            "inner": [1, 2, 3, 1, 2, 3],
            "A": np.arange(6),
            "B": ["one", "one", "two", "two", "one", "one"],
        }
    )
    s = df.set_index(["outer", "inner", "B"])["A"]

    return s


@pytest.mark.parametrize(
    "key_strs,groupers",
    [
        ("inner", pd.Grouper(level="inner")),  # Index name
        (["inner"], [pd.Grouper(level="inner")]),  # List of index name
        (["B", "inner"], ["B", pd.Grouper(level="inner")]),  # Column and index
        (["inner", "B"], [pd.Grouper(level="inner"), "B"]),  # Index and column
    ],
)
def test_grouper_index_level_as_string(frame, key_strs, groupers):
    result = frame.groupby(key_strs).mean()
    expected = frame.groupby(groupers).mean()
    assert_frame_equal(result, expected)


@pytest.mark.parametrize(
    "levels",
    [
        "inner",
        "outer",
        "B",
        ["inner"],
        ["outer"],
        ["B"],
        ["inner", "outer"],
        ["outer", "inner"],
        ["inner", "outer", "B"],
        ["B", "outer", "inner"],
    ],
)
def test_grouper_index_level_as_string_series(series, levels):

    # Compute expected result
    if isinstance(levels, list):
        groupers = [pd.Grouper(level=lv) for lv in levels]
    else:
        groupers = pd.Grouper(level=levels)

    expected = series.groupby(groupers).mean()

    # Compute and check result
    result = series.groupby(levels).mean()
    assert_series_equal(result, expected)
