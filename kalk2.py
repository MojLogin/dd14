import sys

# print(sys.argv)
def divide(a, b):
    return a / b


def main():
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    wynik = divide(a, b)
    print(wynik)

if __name__ == '__main__':
    main()