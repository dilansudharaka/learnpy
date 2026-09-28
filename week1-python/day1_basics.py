x = 10
if x > 5:
    print("big")
elif x == 5:
    print("five") # "else if is elif"
else:
    print("small")

name = "Dilan"
age = 40
price = 19.99
is_active = True
nothing = None

# && => and
# || => or
# ! => not
# 7/ 2 => 3.5 (division always returns a float)
# 7 //2 => 3 (floor division returns an integer)
# 2** 10 => Math.Pow(2, 10) in other languages, but in Python it is 2**10
# x++ => x += 1 (Python does not have the ++ operator)
# a == null => a is None (Python uses None instead of null)

print(f"Hi {name}, total {price: .2f}")
print(f"{age=}")

# Loops
for i in range(5):
    print(i)

for i in range(1, 10, 2):  # start, stop(exclusive), step
    print(i)    # prints 1, 3, 5, 7, 9

for ch in "hello":
    print(ch)

for i, ch in enumerate("hello"):
    print(i, ch)

n = 3
while n > 0:
    n -= 1
    print(n)

items =[]
if not items:
    print("empty")


print("Exercise 1: F -> C")
Cs = [0, 25, 37.5, 100]
for c in Cs:
    f = c * 9/5 + 32
    print(f"{c}C = {f}F")

def grage(score):
    if score >= 90 :
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

scores =[92, 45, 78, 67, 88]
for score in scores:
    print(f"{score=}, grade={grage(score)}")

start = 10
while start > 0:
    print(start)
    start -= 1
print("Leftoff")

def count_vowels(word):
    count = 0
    for ch in word:
        if ch.lower() in "aeiou":
            count += 1
    return count

print(f"Vowels in word 'Dilan is soo fucking ass hole' is {count_vowels('Dilan is soo fucking ass hole')}")

def print_table():
    for row in range(1, 10):
        for col in range(1, 10):
            print(f"{row*col: 3}", end="")
        print()

print_table()