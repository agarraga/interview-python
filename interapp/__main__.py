import sys
from .fizzbuzz import fizzbuzz
from .fizzbuzz import infinifizzbuzz

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(*fizzbuzz([3, 5], ["Fizz", "Buzz"], 100), sep='\n')
        sys.exit()
    elif (sys.argv[1:]) == "PRESS THE RED BUTTON":
        infinifizzbuzz()
        sys.exit()
    try:
        n = int(sys.argv[1])
        print(*fizzbuzz([3, 5], ["Fizz", "Buzz"], n), sep='\n')
    except ValueError:
        print("Argument must be a positive integer.")
        sys.exit(1)
