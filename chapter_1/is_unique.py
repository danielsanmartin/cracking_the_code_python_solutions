# Is Unique: Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?


def test_func(func):
    assert func('daniele') == False
    assert func('daniel') == True
    assert func('aa') == False


# solution 1: using array. 
def is_unique_chars_with_array(word) -> bool:

    if len(word) > 128:
        return False
    
    char_set = [False for i in range(0, 128)]

    for i in range(0, len(word)):
        val = ord(word[i])
        if char_set[val]:
            return False
        else:
            char_set[val] = True

    return True


# solution 2: without using additional data structures.
def is_unique_chars(word) -> bool:

    if len(word) > 128:
        return False
    
    checker = 0
    a_val = ord('a')
    for i in range(0, len(word)):
        val = ord(word[i].lower()) - a_val
        if (checker & (1 << val)) > 0:
            return False
        
        checker |= (1 << val)

    return True


test_func(is_unique_chars_with_array)
test_func(is_unique_chars)
