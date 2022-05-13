MOVES = ((1,0),(-1,0),(0,-1),(0,1),)

def calc_path(start, map):
    width = len(map[0])
    height = len(map)
    path = [[None for x in range(width)] for y in range(height)]
    path[start[0]][start[1]] = 1
    curr_location = [start]
    while curr_location:
        curr_x, curr_y = curr_location.pop(0)
        for move in MOVES:
            new_x = curr_x + move[0]
            new_y = curr_y + move[1]
            if 0 <= new_x < height and 0 <= new_y < width:
                if path[new_x][new_y] is None:
                    path[new_x][new_y] = path[curr_x][curr_y] + 1
                    if map[new_x][new_y] == 1:
                        continue
                    curr_location.append((new_x, new_y))
    return path

def solution(map):
    width = len(map[0])
    height = len(map)
    path_forward = calc_path((0,0), map)
    path_backward = calc_path((height-1,width-1), map)

    result = 4294967295
    for i in range(height):
        for j in range(width):
            if path_forward[i][j] and path_backward[i][j]:
                result = min(path_forward[i][j] + path_backward[i][j] - 1, result)
    return result

if __name__ == '__main__':
    print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
    print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))