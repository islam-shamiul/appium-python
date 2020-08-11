import pytest


@pytest.yield_fixture(scope='module')
def before_class():
    print("runs before class")
    yield
    print("runs after class")


@pytest.yield_fixture()
def before_method():
    print("before every method")
    yield
    print("after every method")


def test_methodA(before_class, before_method):
    print("This is method A")


def test_methodB(before_class, before_method):
    print("This is method B")
