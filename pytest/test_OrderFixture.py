import pytest


@pytest.mark.run(order=4)
def test_methodA():
    print("this is test A")


@pytest.mark.run(order=3)
def test_methodB():
    print("this is test B")


@pytest.mark.run(order=2)
def test_methodC():
    print("this is test C")


@pytest.mark.run(order=1)
def test_methodD():
    print("this is test D")
