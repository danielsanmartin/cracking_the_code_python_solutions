# The algorithm assumes the char is encoded in ASCII

def check(a, b):

    if len(a) != len(b): return False

    letters = [0] * 128

    for c in a:
        letters[ord(c)] += 1

    for c in b:
        letters[ord(c)] -= 1
        if letters[ord(c)] < 0:
            return False

    return True


assert check('aabb', 'abab') == True
assert check('acbb', 'abab') == False
assert check('aabt', 'abab') == False
assert check('aabbf', 'ababf') == True






