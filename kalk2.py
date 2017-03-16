import sys

# wypisuje argumenty - indeks 0 to zawsze nazwa pliku .py
# zakladam ze moj program bede uruchamiac z dwoma opcjami:
# python kalk2.py liczbaA liczbaB
print(sys.argv)


def divide(a, b):
    return a / b

def main():
    # przypisuje podane argumenty jako int
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    # uzywam mojej funkcji
    wynik = divide(a, b)
    print(wynik)

if __name__ == '__main__':
    main()
