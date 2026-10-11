def contains_duplicate(nums:list[int]) -> bool:
    seen: set[int] = set()
    for n in nums:
        if n in seen:
            return True
        else:
            seen.add(n)

    return False

assert contains_duplicate([1,2,1]) is True