import pytest


@pytest.fixture()
def setup():
    print("runs before every method")


def test_methodA(setup):
    print("This is method A")


def test_methodB(setup):
    print("This is method B")
