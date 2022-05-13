def solution(l):
    length = len(l)
    if length < 3 or length > 2000: return 0
    result = 0
    for second in range(1, len(l) - 1):
        count_first = len([first for first in l[:second] if l[second] % first == 0])
        count_third = len([third for third in l[second + 1:] if third % l[second] == 0])

        result += count_first * count_third
    return result

if __name__ == '__main__':
    print(solution([1,1]))
    print(solution([1,2,3]))
    print(solution([0,1,2]))
    print(solution([1, 1, 1]))
    print(solution([1, 2, 3, 4, 5, 6]))