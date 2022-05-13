def solution(x, y):
    mach = max(int(x), int(y))
    facula = min(int(x), int(y))
    result = 0
    while facula > 0:
        result += mach // facula
        temp_mach = facula
        facula = mach % facula
        mach = temp_mach
    if mach != 1:
        return 'impossible'
    return str(result - 1)

if __name__ == '__main__':
    print(solution('2', '1'))
    print(solution('4','7'))