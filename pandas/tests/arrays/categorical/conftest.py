import pytest


@pytest.fixture(params=[True, False], name="allow_fill")
def allow_fill_fixture(request):
    return allow_fill(request)


def allow_fill(request):
    """Boolean 'allow_fill' parameter for Categorical.take"""
    return request.param
