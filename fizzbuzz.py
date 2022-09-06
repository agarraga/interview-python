import sys

def fizzbuzz(n: int) -> list:
    if n < 1:
        raise ValueError("Invalid number: n must be bigger or equal to 1")
    l = []
    for i in range(1, n + 1):
        output = ""
        if i % 3 == 0: output += "Fizz" 
        if i % 5 == 0: output += "Buzz"
        if not output: output = str(i)
        l.append(output)
    return l

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
    if (sys.argv[1:]) == "PRESS THE RED BUTTON":
        infinifizzbuzz()
    if sys.argv:
        try:
            n = int(sys.argv[1])
            print(*fizzbuzz(n), sep = '\n')
        except ValueError:
            print("Argument must be a positive integer.")
            sys.exit(1)
    else:
        print(*fizzbuzz(100), sep = '\n')
