def check_edit(a, b) -> bool:

    if abs(len(a) - len(b)) > 1:
        return False

    longer = a if len(a) > len(b) else b
    shorter = a if len(a) < len(b) else b

    print('Words: {} (longer) and {} (shorter)'.format(longer, shorter))

    i_longer = i_shorter = 0
    diff = False

    while i_longer < len(longer) and i_shorter < len(shorter):
        print('comparing {} and {}'.format(longer[i_longer], shorter[i_shorter]))

        if longer[i_longer] != shorter[i_shorter]:
            if diff is True:
                return False
            else: 
                diff = True
                print('differents')
                i_longer += 1
        else:         
            i_longer += 1
            i_shorter += 1
      
    return True


assert check_edit('pascal', 'ascal') is True
assert check_edit('pascal', 'pasca') is True
assert check_edit('pascal', 'pascau') is True
assert check_edit('pascal', 'pascali') is True

assert check_edit('ascal', 'pascal') is True
assert check_edit('pasca', 'pascal') is True
assert check_edit('pascau', 'pascal') is True
assert check_edit('pascali', 'pascal') is True

assert check_edit('pascal', 'pascalin') is False
assert check_edit('pascal', 'asca') is False

assert check_edit('b', 'a') is True
assert check_edit('b', '') is True
assert check_edit('b', 'aa') is False