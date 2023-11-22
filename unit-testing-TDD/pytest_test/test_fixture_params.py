import pytest


@pytest.fixture(params=[1, 2, 3])
def setup(request):
    ret_val = request.param
    print(f"\nSetup! ret_val= {ret_val}")
    return ret_val


def test1(setup):
    print("\nSetup = {}".format(setup))
    assert True
