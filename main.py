def divide(a: str, b: str) -> (int, int):
    a, b = a.lstrip("0"), b.lstrip("0")
    if b == '':
        raise ZeroDivisionError
    n, m = len(a), len(b)
    r = 0
    s = []
    b = int(b)
    for i in range(n):
        r = r * 10 + int(a[i])
        q = 0
        while q < 10 and q * b <= r:
            q += 1
        q -= 1
        s.append(str(q))
        r -= q * b
    if not s:
        s = 0
    else:
        s = int(''.join(s))
    return s, r


def test_divide():
    assert divide("12345", "12") == (1028, 9)

    assert divide("987654321", "1") == (987654321, 0)

    assert divide("123456789101112131415161718192021222324252627282930", "31323334353637383940") == divmod(123456789101112131415161718192021222324252627282930, 31323334353637383940)

    assert divide("12345", "12345") == (1, 0)

    assert divide("100", "10") == (10, 0)

    assert divide("123", "12") == (10, 3)

    assert divide("123", "1000") == (0, 123)

    assert divide("0", "123") == (0, 0)

    try:
        divide("123", "0")
    except ZeroDivisionError:
        print("ZeroDivisionError caught")

    assert divide("00123", "012") == (10, 3)


test_divide()

