import pytest
from interapp import fizzbuzz

def test_default_fizzbuzz():
    with open("tests/default_output.txt", "r") as file:
        default = file.read()
    pairs = [fizzbuzz.Pair(3, "Fizz"), fizzbuzz.Pair(5, "Buzz")]
    output = '\n'.join(fizzbuzz.fizzbuzz(pairs)) + '\n'
    assert output == default


def test_validate_numbers_good():
    output = fizzbuzz.validate_number(1)
    assert output is None


def test_validate_numbers_value_error_0():
    with pytest.raises(ValueError):
        fizzbuzz.validate_number(-1)


def test_validate_numbers_value_error_1():
    with pytest.raises(ValueError):
        fizzbuzz.validate_number(0)


def test_validate_words_good():
    output = fizzbuzz.validate_word("Fizz")
    assert output is None


def test_validate_words_value_error_0():
    with pytest.raises(ValueError):
        fizzbuzz.validate_word("cuzz")


def test_validate_words_value_error_1():
    with pytest.raises(ValueError):
        fizzbuzz.validate_word("suzz ")


def test_validate_words_value_error_2():
    with pytest.raises(ValueError):
        fizzbuzz.validate_word("Fizs")
