from collections import Counter


def is_anagram1(s:str, t:str) -> bool:
    return Counter(s) == Counter(t)

def is_anagram(s:str, t:str) -> bool:
    if len(s) != len(t):
        return False
    
    s_dict: dict[str, int] = {}
    t_dict: dict[str, int] = {}

    for c1 in s:
        s_dict[c1] = s_dict.get(c1, 0) + 1

    for t1 in t:
        if t1 not in s_dict:
            return False

        t_dict[t1] = t_dict.get(t1, 0) + 1

    if len(s_dict) != len(t_dict):
        return False

    for key, val in s_dict.items():
        if key not in t_dict or t_dict.get(key) != val:
            return False
        
    return True