import random
import re

CONS = ['B', 'D', 'F', 'G', 'H', 'J', 'L', 'N', 'P', 'R', 'S', 'V', 'Y', 'W', 'Z'] # noqa
VOWL = ['a', 'e', 'i', 'o', 'u']


class Pair:
    def __init__(self, number: int, word: str):
        self.number = number
        self.word = word


def fizzbuzz(numbers: list, words: list, n: int) -> list:
    if n < 1:
        raise ValueError("Invalid number: n must be bigger or equal to 1")
    try:
        validate_words(words)
        validate_numbers(numbers)
    except TypeError or ValueError:
        raise
    else:
        bigger_size = 0
        words_size = len(words)
        numbers_size = len(numbers)

        if len(numbers) > len(words):
            bigger_size = numbers_size
            fill_words(words, bigger_size)
        elif len(numbers) < len(words):
            bigger_size = words_size
            fill_words(words, bigger_size)

        results = []
        pairs = [Pair(pair[0], pair[1]) for pair in zip(numbers, words)]
        for i in range(n):
            output = ""
            for pair in pairs:
                if i % pair.number == 0:
                    output += pair.word + " "
            if output:
                results.append(output.rstrip())
            else:
                results.append(str(i))

        return results


def fill_words(words: list, total: int):
    try:
        validate_words(words)
    except TypeError:
        raise
    else:
        while len(words) < total:
            candidate = random.choice(CONS) + random.choice(VOWL) + "zz"
            if candidate in words:
                continue
            words.append(candidate)


def fill_numbers(numbers: list, total: int):
    try:
        validate_numbers(numbers)
    except TypeError or ValueError:
        raise
    else:
        # Add contiguous primes from least after max(numbers)
        pass


def validate_words(words: list):
    if any(not isinstance(s, str) for s in words):
        raise TypeError("words list must only contain str")
    pattern = fr"^[{('').join(CONS)}][{('').join(VOWL)}]zz$"
    if any(not bool(re.search(pattern, s)) for s in words):
        raise ValueError("str in word list must be of format Fizz Buzz")


def validate_numbers(numbers: list):
    if any(not isinstance(n, int) for n in numbers):
        raise TypeError("numbers list must only contain int")
    if any(n < 1 for n in numbers):
        raise ValueError("numbers list must only contain n >= 1")


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
