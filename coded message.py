def solution(x):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    revAlphabet = alphabet[::-1]
    output = ""
    for char in x:
        if (char.islower()):
            index = alphabet.index(char)
            output = output + revAlphabet[index]
        else:
            output = output + char
    return output

if __name__ == '__main__':
    print(solution("Hzev blf hvvm gsv ozgvhg vkrhlwv?"))