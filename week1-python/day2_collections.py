##
# Part A: dict (your missing section 3)
#
# Start with stock = {"apple": 3, "pear": 0, "kiwi": 12}.
#
# Add "plum": 5 and change apple to 4.
# Print the count for "mango" with a default of 0, without raising KeyError.
# Loop over the dict and print each entry as apple: 4.
# Remove pear, then print whether "pear" is still a key. Expected: False.
# Count the words in "the cat and the hat and the bat", first with a plain dict, then with collections.Counter. Expected: {'the': 3, 'cat': 1, 'and': 2, 'hat': 1, 'bat': 1}.
# Part B: set
#
# Start with a = {1, 2, 3, 4} and b = {3, 4, 5}.
#
# Print the union, intersection, difference (a - b) and symmetric difference. Expected: {1, 2, 3, 4, 5}, {3, 4}, {1, 2}, {1, 2, 5}.
# De-duplicate [3, 1, 3, 2, 1] into a sorted list. Expected: [1, 2, 3].
# Stretch: de-duplicate the same list while keeping first-seen order. Expected: [3, 1, 2].
# Create an empty set and print its type. Note in a comment what {} gives you instead.
# Part C: comprehensions
# Squares of the even numbers from 1 to 10. Expected: [4, 16, 36, 64, 100].
# A dict of number to cube for 1 to 5. Expected: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}.
# The set of word lengths in ["go", "java", "rust", "c", "python"]. Expected: {1, 2, 4, 6}.
# Flatten [[1, 2], [3, 4], [5]]. Expected: [1, 2, 3, 4, 5].
# Label 1 to 4 as odd or even in one comprehension. Expected: ['odd', 'even', 'odd', 'even'].
# Part D: LINQ rewrites
# python
# people = [
#     {"name": "Ana", "age": 31, "city": "Seattle"},
#     {"name": "Bo",  "age": 17, "city": "Tacoma"},
#     {"name": "Cy",  "age": 45, "city": "Seattle"},
#     {"name": "Di",  "age": 22, "city": "Everett"},
# ]
#
# Rewrite each query, with the C# version as a comment above it.
#
# people.Where(p => p.Age >= 18).Select(p => p.Name).ToList(). Expected: ['Ana', 'Cy', 'Di'].
# people.ToDictionary(p => p.Name, p => p.Age). Expected: {'Ana': 31, 'Bo': 17, 'Cy': 45, 'Di': 22}.
# people.Select(p => p.City).Distinct(). Expected: the three cities, in any order.
# Bonus: Any(p => p.Age < 18), All(p => p.Age >= 18), and OrderByDescending(p => p.Age).First().Name. Expected: True, False, 'Cy'.
# Part E: LeetCode
#
# One file each in week1-python/leetcode/, aiming for O(n) time.
#
# Problem	File	Day 2 tool to reach for
# 217 Contains Duplicate	lc0217_contains_duplicate.py	set
# 242 Valid Anagram	lc0242_valid_anagram.py	dict or Counter
# 121 Best Time to Buy and Sell Stock	lc0121_best_time_to_buy_and_sell_stock.py	single pass, tracking the minimum so far
# Done when
# The file runs with no errors and every printed result matches the expected output.
# The four small fixes from my last message are applied.
# uv run ruff check . passes.
# Everything is committed as “Day 2” and there is a Day 2 entry in your progress log.
#
# When you’ve finished, tell me and I’ll review it the way Day 1 was reviewed.
##

from collections import Counter

nums = [5, 2, 9]  ## define a collection
nums.append(7)  ## Add to the end.
nums.insert(0, 1)  ## Insert 1 to the 0th location.
print(nums)  ## print the collection.
x: int = nums.pop()  ## remove the last element
print(str(x))
nums.remove(2)  ## remove the first occurance of 2
print(nums)
print(str(len(nums)))  ## print the length of the array.
print(9 in nums)  ## checks whether a given value is in the list.
nums.sort()  # sort the values in order
sorted(nums, reverse=True)  # create a new list in reverse order
print(f"Sum = {sum(nums)}, Min= {min(nums)}, Max ={max(nums)}")

### Slicing
## seq[start: stop: step](excluded)
a = [10, 20, 30, 40, 50]
a[1:4]  # 20, 30, 40
a[:2]  # 10, 20 => First two
a[-2:]  # 40, 50 => last two elements
a[::2]  # 10, 30, 50 => Every second Item
a[::-1]  # reverse order => 50, 40, 30, 20, 10
"hello"[1:3]  ## el, starting at index1, stop at index 3(excluded)

## 4. Tuples & unpacking
point = (3, 4)
x, y = point
a, b = 5, 8
a, b = b, a  # swap without temp variable.
print(f"{a=}, {b=}")
first, *rest = [1, 2, 3, 4]
print(f"{first=}, {rest=}")

# Part A: dict
stock: dict[str, int] = {"apple": 3, "pear": 0, "kiwi": 12}
stock["plum"] = 5
stock["apple"] = 4
print(stock.get("mango", 0))
for key, value in stock.items():
    print(f"{key}:{value}")
del stock["pear"]
stock.pop("pear", None)
print("pear" in stock)

sentence: str = "the cat and the hat and the bat"
word_counts: dict[str, int] = {}

for w in sentence.split():
    word_counts[w] = word_counts.get(w, 0) + 1

# Print using dictionary.
for key, value in word_counts.items():
    print(f"{key}:{value}", end=" ")
print()

# print using collections
word_counter = Counter(sentence.split())
print(word_counter)


# Part B: set
set_a: set[int] = {1, 2, 3, 4}
set_b: set[int] = {3, 4, 5}

# Union
print("Union:", set_a | set_b)

# Intersection
print("Intersection: ", set_a & set_b)

# Difference( In A but not B)
print("Difference: ", set_a - set_b)

# Symmetric diff(Elements in either A or B, but not both)
print("Symmetric diff:", set_a ^ set_b)

list_x: list[int] = [3, 1, 3, 2, 1]
list_y = sorted(set(list_x))
print(list_y)

z = list(dict.fromkeys(list_x))
print(z)

# Empty set
emptyset = set()
print(type(emptyset))
## print <class 'set'>

empty_dict = {}
print(type(empty_dict))

########### PART C ###############
square_list = [n**2 for n in range(1, 11, 1) if n % 2 == 0]
print(square_list)

cubes = {n: n**3 for n in range(1, 6, 1)}
print(cubes)

words: list[str] = ["go", "java", "rust", "c", "python"]
word_lengths_c: set[int] = {len(w) for w in words}
print(word_lengths_c)

## Flatten [[1, 2], [3, 4], [5]]. Expected: [1, 2, 3, 4, 5].
nested_list = [[1, 2], [3, 4], [5]]

result = [n for inner in nested_list for n in inner]
print(result)

# Label 1 to 4 as odd or even in one comprehension. Expected: ['odd', 'even', 'odd', 'even'].
result1 = ["even" if x % 2 == 0 else "odd" for x in range(1, 5, 1)]
print(result1)

############# PART D #############################
people = [
    {"name": "Ana", "age": 31, "city": "Seattle"},
    {"name": "Bo",  "age": 17, "city": "Tacoma"},
    {"name": "Cy",  "age": 45, "city": "Seattle"},
    {"name": "Di",  "age": 22, "city": "Everett"},
]

#Rewrite each query, with the C# version as a comment above it.
# people.Where(p => p.Age >= 18).Select(p => p.Name).ToList(). Expected: ['Ana', 'Cy', 'Di'].

names: list[str] = [p["name"] for p in people if p["age"] >= 18]
print(names)

#people.ToDictionary(p => p.Name, p => p.Age). Expected: {'Ana': 31, 'Bo': 17, 'Cy': 45, 'Di': 22}.
p_1: dict[str, int] = {p["name"]: p["age"] for p in people}
print(p_1)

#people.Select(p => p.City).Distinct(). Expected: the three cities, in any order.
p_cities:set[str] = {p["city"] for p in people}
print(p_cities)

#Any(p => p.Age < 18)
p_under18 = any(p["age"]< 18 for p in people) 
print(p_under18)

#All(p => p.Age >= 18)
all_adults = all(p["age"] >= 18 for p in people)
print(all_adults)

#OrderByDescending(p => p.Age).First().Name
oldest = max(people, key=lambda p: p["age"])["name"]
print(oldest)
