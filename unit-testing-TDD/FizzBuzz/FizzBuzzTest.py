import pytest


def is_multiple(value, mod):
    return value % mod == 0


def fizzbuzz(value):
    if is_multiple(value, 3) and is_multiple(value, 5):
        return "FizzBuzz"
    if is_multiple(value, 3):
        return "Fizz"
    if is_multiple(value, 5):
        return "Buzz"

    return str(value)


def check_fizz_buzz(value, expected_val):
    ret_val = fizzbuzz(value)
    assert ret_val == expected_val


def test_can_call_fizz_buzz():
    fizzbuzz(1)


def test_returns_with_1_passed():
    check_fizz_buzz(1, '1')


def test_returns_with_2_passed():
    check_fizz_buzz(2, '2')


def test_returns_with_3_passed():
    check_fizz_buzz(3, 'Fizz')


def test_returns_with_4_passed():
    check_fizz_buzz(4, '4')


def test_returns_with_5_passed():
    check_fizz_buzz(5, 'Buzz')


def test_returns_with_15_passed():
    check_fizz_buzz(15, 'FizzBuzz')


def test_returns_with_6_passed():
    check_fizz_buzz(5, 'Buzz')
