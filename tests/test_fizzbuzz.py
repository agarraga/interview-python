import pytest
from interapp import fizzbuzz

def test_validate_numbers_good():
    output = fizzbuzz.validate_numbers([1, 3, 5])
    assert output == None

def test_validate_numbers_type_error():
    with pytest.raises(TypeError):
        fizzbuzz.validate_numbers([0, 1, "2"])

def test_validate_numbers_value_error():
    with pytest.raises(ValueError):
        fizzbuzz.validate_numbers([0, -1, 2])

def test_validate_words_good():
    output = fizzbuzz.validate_words(["Fizz", "Buzz", "Nozz"])
    assert output == None

def test_validate_words_value_error_0():
    with pytest.raises(ValueError):
        fizzbuzz.validate_words(["Fizz", "Buzz", "cuzz"])

def test_validate_words_value_error_1():
    with pytest.raises(ValueError):
        fizzbuzz.validate_words(["Fizz", "Buzz", "suzz "])

def test_validate_words_value_error_2():
    with pytest.raises(ValueError):
        fizzbuzz.validate_words(["Fizz", "Buzz", "Fizs"])

def test_validate_words_type_error():
    with pytest.raises(TypeError):
        fizzbuzz.validate_words(["Fizz", "Buzz", False])
