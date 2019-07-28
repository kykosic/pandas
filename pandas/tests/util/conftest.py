import pytest


@pytest.fixture(params=[True, False], name=check_dtype)
def check_dtype_fixture(request):
    return check_dtype(request)


def check_dtype(request):
    return request.param


@pytest.fixture(params=[True, False], name=check_exact)
def check_exact_fixture(request):
    return check_exact(request)


def check_exact(request):
    return request.param


@pytest.fixture(params=[True, False], name=check_index_type)
def check_index_type_fixture(request):
    return check_index_type(request)


def check_index_type(request):
    return request.param


@pytest.fixture(params=[True, False], name=check_less_precise)
def check_less_precise_fixture(request):
    return check_less_precise(request)


def check_less_precise(request):
    return request.param


@pytest.fixture(params=[True, False], name=check_categorical)
def check_categorical_fixture(request):
    return check_categorical(request)


def check_categorical(request):
    return request.param
