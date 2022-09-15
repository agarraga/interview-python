import random
import re

CONS = ['B', 'D', 'F', 'G', 'H', 'J', 'L', 'N', 'P', 'R', 'S', 'V', 'Y', 'W', 'Z'] # noqa
VOWL = ['a', 'e', 'i', 'o', 'u']


class Pair:
    def __init__(self, number: int, word: str):
        try:
            validate_number(number)
            validate_word(word)
        except ValueError:
            raise
        else:
            self.number = number
            self.word = word


def fizzbuzz(pairs: list, n: int = 100) -> list:
    if n < 1:
        raise ValueError("Invalid number: n must be bigger or equal to 1")
    try:
        validate_pairs(pairs)
    except TypeError:
        raise
    else:
        results = []

        for i in range(1, n + 1):
            output = ""

            for pair in pairs:
                if i % pair.number == 0:
                    output += pair.word + " "
            if output:
                results.append(output.rstrip())
            else:
                results.append(str(i))

        return results


def make_pairs(numbers: list, words: list) -> list:
    try:
        bigger_size = 0
        words_size = len(words)
        numbers_size = len(numbers)

        if len(numbers) > len(words):
            bigger_size = numbers_size
            fill_words(words, bigger_size)
        elif len(numbers) < len(words):
            bigger_size = words_size
            fill_words(words, bigger_size)

        return [Pair(pair[0], pair[1]) for pair in zip(numbers, words)]
    except ValueError:
        raise


def fill_words(words: list, total: int):
    try:
        map(validate_word, words)
    except ValueError:
        raise
    else:
        while len(words) < total:
            candidate = random.choice(CONS) + random.choice(VOWL) + "zz"
            if candidate in words:
                continue
            words.append(candidate)


def fill_numbers(numbers: list, total: int):
    try:
        map(validate_number, numbers)
    except ValueError:
        raise
    else:
        # Add contiguous primes from least after max(numbers)
        pass


def validate_word(word: str):
    pattern = fr"^[{('').join(CONS)}][{('').join(VOWL)}]zz$"
    if not bool(re.search(pattern, word)):
        raise ValueError("str in word list must be of format Fizz Buzz")


def validate_number(number: int):
    if number < 1:
        raise ValueError("numbers list must only contain n >= 1")


def validate_pairs(pairs: list):
    if any(not isinstance(p, Pair) for p in pairs):
        raise TypeError("pairs list must only contain Pair")


def infinifizzbuzz():
    """
    Flame King: 'Evil, evil, evil, evil. Evil, evil, evil. Evil!'
    https://www.youtube.com/watch?v=N2S7iwEHOV4
    """
    i = 1
    while True:
        output = ""
        if i % 3 == 0: output += "Fizz"  # noqa
        if i % 5 == 0: output += "Buzz"  # noqa
        if not output: output = str(i)  # noqa
        print(output)
        i += 1
