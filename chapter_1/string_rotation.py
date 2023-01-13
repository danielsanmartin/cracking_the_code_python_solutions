def string_rotation(s1, s2) -> str:
    if len(s1) != len(s2):
        return False   

    return s2 in (s1+s1)


print(string_rotation('waterbottle', 'erbottlewat'))

print(string_rotation('casaco', 'cocasa'))