from pytest import raises


def raisesValueException():
    raise ValueError


def test_exception_():
    with raises(ValueError):
        raisesValueException()
