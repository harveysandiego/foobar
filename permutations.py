from itertools import permutations

def getPermutations(series, length):
    return {"".join(p) for p in permutations(series, length)}

def solution(l):
    sorted_in = sorted(map(str, l))
    perms = []
    for i in range(1, len(sorted_in)+1):
        perms.extend(getPermutations(sorted_in, i))
    sorted_perms = sorted(map(int, perms), reverse=True)
    index = -1
    for perm in sorted_perms:
        if perm % 3 == 0 :
            index=sorted_perms.index(perm)
            break

    if index == -1:
        return 0
    else:
        return sorted_perms[index]

if __name__ == '__main__':
    print(solution([3, 1, 4, 1]))
    print(solution([3, 1, 4, 1, 5, 9]))