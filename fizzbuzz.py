import sys


class Pair:
    def __init__(self, number: int, word: str):
        self.number = number
        self.word = word


def fizzbuzz(numbers: list, words: list, n: int) -> list:
    if n < 1:
        raise ValueError("Invalid number: n must be bigger or equal to 1")
    bigger_size = 0
    words_size = len(words)
    numbers_size = len(numbers)
    if not all(isinstance(e, int) for e in numbers):
        raise TypeError("numbers list must only contain int")
    if not all(isinstance(e, str) for e in words):
        raise TypeError("words list must only contain str")

    if len(numbers) > len(words):
        bigger_size = numbers_size
        words = fill_words(words, bigger_size) 
    elif len(numbers) < len(words):
        bigger_size = words_size 
        words = fill_words(words, bigger_size) 

    l = []
    pairs = [Pair(pair[0], pair[1]) for pair in zip(numbers, words)]
    for i in range(n):
        output = ""
        for pair in pairs:
            if i % pair.number == 0:
                output += pair.word + " "
        if output: l.append(output.rstrip())
        else: l.append(str(i))

    return l


def fill_words(words: list, total: int) -> list:
    if not all(isinstance(e, str) for e in words):
        raise TypeError("words list must only contain str")
    return words


def fill_numbers(numbers: list, total: int) -> list:
    if not all(isinstance(e, int) for e in numbers):
        raise TypeError("numbers list must only contain int")
    return numbers


def infinifizzbuzz():
    i = 1
    while True:
        output = ""
        if i % 3 == 0: output += "Fizz"
        if i % 5 == 0: output += "Buzz"
        if not output: output = str(i)
        print(output)
        i += 1


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(*fizzbuzz([3, 5], ["Fizz", "Buzz"], 100), sep = '\n')
        sys.exit()
    elif (sys.argv[1:]) == "PRESS THE RED BUTTON":
        infinifizzbuzz()
        sys.exit()
    try:
        n = int(sys.argv[1])
        print(*fizzbuzz([3, 5], ["Fizz", "Buzz"], n), sep = '\n')
    except ValueError:
        print("Argument must be a positive integer.")
        sys.exit(1)
