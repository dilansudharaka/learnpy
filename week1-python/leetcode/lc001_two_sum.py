def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        remain = target - num
        if remain in seen:
            return [seen[remain], i]

        if num not in seen:
            seen[num] = i
    return [-1, -1]


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
