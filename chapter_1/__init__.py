


n = [5,6,5,6,9,7,7]

def solve(n):
    tmp = []
    for i in range(0, len(n)-1):
        if n[i] not in tmp:
            tmp.append(n[i])
        else:
            tmp.remove(n[i])

    return tmp[0]

print(solve(n))



