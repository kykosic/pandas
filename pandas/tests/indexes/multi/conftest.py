import numpy as np
import pytest

import pandas as pd
from pandas import Index, MultiIndex


@pytest.fixture(name="idx")
def idx_fixture():
    return idx()


def idx():
    # a MultiIndex used to test the general functionality of the
    # general functionality of this object
    major_axis = Index(["foo", "bar", "baz", "qux"])
    minor_axis = Index(["one", "two"])

    major_codes = np.array([0, 0, 1, 2, 3, 3])
    minor_codes = np.array([0, 1, 0, 1, 0, 1])
    index_names = ["first", "second"]
    mi = MultiIndex(
        levels=[major_axis, minor_axis],
        codes=[major_codes, minor_codes],
        names=index_names,
        verify_integrity=False,
    )
    return mi


@pytest.fixture(name="idx_dup")
def idx_dup_fixture():
    return idx_dup()


def idx_dup():
    # compare tests/indexes/multi/conftest.py
    major_axis = Index(["foo", "bar", "baz", "qux"])
    minor_axis = Index(["one", "two"])

    major_codes = np.array([0, 0, 1, 0, 1, 1])
    minor_codes = np.array([0, 1, 0, 1, 0, 1])
    index_names = ["first", "second"]
    mi = MultiIndex(
        levels=[major_axis, minor_axis],
        codes=[major_codes, minor_codes],
        names=index_names,
        verify_integrity=False,
    )
    return mi


@pytest.fixture(name="index_names")
def index_names_fixture():
    return index_names()


def index_names():
    # names that match those in the idx fixture for testing equality of
    # names assigned to the idx
    return ["first", "second"]


@pytest.fixture(name="holder")
def holder_fixture():
    return holder()


def holder():
    # the MultiIndex constructor used to base compatibility with pickle
    return MultiIndex


@pytest.fixture(name="compat_props")
def compat_props_fixture():
    return compat_props()


def compat_props():
    # a MultiIndex must have these properties associated with it
    return ["shape", "ndim", "size"]


@pytest.fixture(name="narrow_multi_index")
def narrow_multi_index_fixture():
    return narrow_multi_index()


def narrow_multi_index():
    """
    Return a MultiIndex that is narrower than the display (<80 characters).
    """
    n = 1000
    ci = pd.CategoricalIndex(list("a" * n) + (["abc"] * n))
    dti = pd.date_range("2000-01-01", freq="s", periods=n * 2)
    return pd.MultiIndex.from_arrays([ci, ci.codes + 9, dti], names=["a", "b", "dti"])


@pytest.fixture(name="wide_multi_index")
def wide_multi_index_fixture():
    return wide_multi_index()


def wide_multi_index():
    """
    Return a MultiIndex that is wider than the display (>80 characters).
    """
    n = 1000
    ci = pd.CategoricalIndex(list("a" * n) + (["abc"] * n))
    dti = pd.date_range("2000-01-01", freq="s", periods=n * 2)
    levels = [ci, ci.codes + 9, dti, dti, dti]
    names = ["a", "b", "dti_1", "dti_2", "dti_3"]
    return pd.MultiIndex.from_arrays(levels, names=names)
