import sys
from .fizzbuzz import fizzbuzz
from .fizzbuzz import infinifizzbuzz
from .fizzbuzz import Pair

if __name__ == '__main__':
    pairs = [Pair(3, "Fizz"), Pair(5, "Buzz")]
    if len(sys.argv) == 1:
        print(*fizzbuzz(pairs), sep='\n')
    elif (sys.argv[1:]) == "PRESS THE RED BUTTON":
        infinifizzbuzz()
    else:
        try:
            n = int(sys.argv[1])
            print(*fizzbuzz(pairs, n), sep='\n')
        except ValueError:
            print("Argument must be a positive integer.")
