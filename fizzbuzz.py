def fizzbuzz(n: int):
    for i in range(n):
        output: str = ""
        if i % 3 == 0: output += "Fizz"
        if i % 5 == 0: output += "Buzz"
        if not output: output = str(i)
        print(output)

def main():
    fizzbuzz(100)

if __name__ == '__main__':
    main()
