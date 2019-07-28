import pytest


@pytest.fixture(params=[True, False], name="raw")
def raw_fixture(request):
    return raw(request)


def raw(request):
    return request.param


@pytest.fixture(
    params=[
        "triang",
        "blackman",
        "hamming",
        "bartlett",
        "bohman",
        "blackmanharris",
        "nuttall",
        "barthann",
    ]
)
def win_types(request):
    return request.param


@pytest.fixture(params=["kaiser", "gaussian", "general_gaussian", "exponential"], name="win_types_special")
def win_types_special_fixture(request):
    return win_types_special(request)


def win_types_special(request):
    return request.param


@pytest.fixture(
    params=["sum", "mean", "median", "max", "min", "var", "std", "kurt", "skew"]
)
def arithmetic_win_operators(request):
    return request.param


@pytest.fixture(params=["right", "left", "both", "neither"], name="closed")
def closed_fixture(request):
    return closed(request)


def closed(request):
    return request.param


@pytest.fixture(params=[True, False], name="center")
def center_fixture(request):
    return center(request)


def center(request):
    return request.param


@pytest.fixture(params=[None, 1], name="min_periods")
def min_periods_fixture(request):
    return min_periods(request)


def min_periods(request):
    return request.param
