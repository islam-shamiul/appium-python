import pytest


@pytest.yield_fixture(scope='module')
def beforeClass():
    print('Before Class')
    yield
    print('After Class')


@pytest.yield_fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')
