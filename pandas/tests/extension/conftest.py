import operator

import pytest

from pandas import Series


@pytest.fixture(name=dtype)
def dtype_fixture():
    return dtype()


def dtype():
    """A fixture providing the ExtensionDtype to validate."""
    raise NotImplementedError


@pytest.fixture(name=data)
def data_fixture():
    return data()


def data():
    """Length-100 array for this type.

    * data[0] and data[1] should both be non missing
    * data[0] and data[1] should not be equal
    """
    raise NotImplementedError


@pytest.fixture(name=data_for_twos)
def data_for_twos_fixture():
    return data_for_twos()


def data_for_twos():
    """Length-100 array in which all the elements are two."""
    raise NotImplementedError


@pytest.fixture(name=data_missing)
def data_missing_fixture():
    return data_missing()


def data_missing():
    """Length-2 array with [NA, Valid]"""
    raise NotImplementedError


@pytest.fixture(params=["data", "data_missing"], name=all_data)
def all_data_fixture(request, data, data_missing):
    return all_data(request, data, data_missing)


def all_data(request, data, data_missing):
    """Parametrized fixture giving 'data' and 'data_missing'"""
    if request.param == "data":
        return data
    elif request.param == "data_missing":
        return data_missing


@pytest.fixture(name=data_repeated)
def data_repeated_fixture(data):
    return data_repeated(data)


def data_repeated(data):
    """
    Generate many datasets.

    Parameters
    ----------
    data : fixture implementing `data`

    Returns
    -------
    Callable[[int], Generator]:
        A callable that takes a `count` argument and
        returns a generator yielding `count` datasets.
    """

    def gen(count):
        for _ in range(count):
            yield data

    return gen


@pytest.fixture(name=data_for_sorting)
def data_for_sorting_fixture():
    return data_for_sorting()


def data_for_sorting():
    """Length-3 array with a known sort order.

    This should be three items [B, C, A] with
    A < B < C
    """
    raise NotImplementedError


@pytest.fixture(name=data_missing_for_sorting)
def data_missing_for_sorting_fixture():
    return data_missing_for_sorting()


def data_missing_for_sorting():
    """Length-3 array with a known sort order.

    This should be three items [B, NA, A] with
    A < B and NA missing.
    """
    raise NotImplementedError


@pytest.fixture(name=na_cmp)
def na_cmp_fixture():
    return na_cmp()


def na_cmp():
    """Binary operator for comparing NA values.

    Should return a function of two arguments that returns
    True if both arguments are (scalar) NA for your type.

    By default, uses ``operator.is_``
    """
    return operator.is_


@pytest.fixture(name=na_value)
def na_value_fixture():
    return na_value()


def na_value():
    """The scalar missing value for this type. Default 'None'"""
    return None


@pytest.fixture(name=data_for_grouping)
def data_for_grouping_fixture():
    return data_for_grouping()


def data_for_grouping():
    """Data for factorization, grouping, and unique tests.

    Expected to be like [B, B, NA, NA, A, A, B, C]

    Where A < B < C and NA is missing
    """
    raise NotImplementedError


@pytest.fixture(params=[True, False], name=box_in_series)
def box_in_series_fixture(request):
    return box_in_series(request)


def box_in_series(request):
    """Whether to box the data in a Series"""
    return request.param


@pytest.fixture(
    params=[
        lambda x: 1,
        lambda x: [1] * len(x),
        lambda x: Series([1] * len(x)),
        lambda x: x,
    ],
    ids=["scalar", "list", "series", "object"],
)
def groupby_apply_op(request):
    """
    Functions to test groupby.apply().
    """
    return request.param


@pytest.fixture(params=[True, False], name=as_frame)
def as_frame_fixture(request):
    return as_frame(request)


def as_frame(request):
    """
    Boolean fixture to support Series and Series.to_frame() comparison testing.
    """
    return request.param


@pytest.fixture(params=[True, False], name=as_series)
def as_series_fixture(request):
    return as_series(request)


def as_series(request):
    """
    Boolean fixture to support arr and Series(arr) comparison testing.
    """
    return request.param


@pytest.fixture(params=[True, False], name=use_numpy)
def use_numpy_fixture(request):
    return use_numpy(request)


def use_numpy(request):
    """
    Boolean fixture to support comparison testing of ExtensionDtype array
    and numpy array.
    """
    return request.param


@pytest.fixture(params=["ffill", "bfill"], name=fillna_method)
def fillna_method_fixture(request):
    return fillna_method(request)


def fillna_method(request):
    """
    Parametrized fixture giving method parameters 'ffill' and 'bfill' for
    Series.fillna(method=<method>) testing.
    """
    return request.param


@pytest.fixture(params=[True, False], name=as_array)
def as_array_fixture(request):
    return as_array(request)


def as_array(request):
    """
    Boolean fixture to support ExtensionDtype _from_sequence method testing.
    """
    return request.param
