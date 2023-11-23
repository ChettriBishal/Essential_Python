from unittest import mock

from ..my_app.sample import guess_number
import pytest


@pytest.mark.parametrize("_input, expected", [(3, "you won!"), (4, "you lost!")])
@mock.patch("mock_yt.my_app.sample.roll_dice")
def test_guess_number(mock_roll_dice, _input, expected):
    mock_roll_dice.return_value = 3
    assert guess_number(_input) == expected
    mock_roll_dice.assert_called_once()
