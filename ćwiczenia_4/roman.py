import sys

roman_numbers = [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1)
    ]

if sys.argv[1] == 'r':

    x = int(sys.argv[2])
    result = []
    for (roman, val) in roman_numbers:
        num = x // val  # ile razy val mieści się w x
        result.append(roman * num) # dodajemy str roman powtórzoną num razy
        x = x % val  # reszta z dzielenia x przez val

    print(''.join(result))

if sys.argv[1] == 'a':

    x = sys.argv[2]
    i = 0 # indeksy kolejnych znaków w x
    result = 0

    for (roman, val) in roman_numbers:

        while x[i : i+len(roman)] == roman:
            result += val
            i += len(roman)
    
    print(result)