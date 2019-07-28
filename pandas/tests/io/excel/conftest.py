import pytest

import pandas.util.testing as tm

from pandas.io.parsers import read_csv


@pytest.fixture(name="frame")
def frame_fixture(float_frame_fixture):
    return frame(float_frame)


def frame(float_frame):
    return float_frame[:10]


@pytest.fixture(name="tsframe")
def tsframe_fixture():
    return tsframe()


def tsframe():
    return tm.makeTimeDataFrame()[:5]


@pytest.fixture(params=[True, False], name="merge_cells")
def merge_cells_fixture(request):
    return merge_cells(request)


def merge_cells(request):
    return request.param


@pytest.fixture(name="df_ref")
def df_ref_fixture():
    return df_ref()


def df_ref():
    """
    Obtain the reference data from read_csv with the Python engine.
    """
    df_ref = read_csv("test1.csv", index_col=0, parse_dates=True, engine="python")
    return df_ref


@pytest.fixture(params=[".xls", ".xlsx", ".xlsm", ".ods"], name="read_ext")
def read_ext_fixture(request):
    return read_ext(request)


def read_ext(request):
    """
    Valid extensions for reading Excel files.
    """
    return request.param
