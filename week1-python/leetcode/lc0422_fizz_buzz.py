def fizz_buzz(n) -> list[str]:
    items: list[str] = []
    for s in range(1, n + 1):
        if s % 3 == 0 and s % 5 == 0:
            items.append("FizzBuzz")
        elif s % 3 == 0:
            items.append("Fizz")
        elif s % 5 == 0:
            items.append("Buzz")
        else:
            items.append(str(s))
    return items


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
