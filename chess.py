from collections import defaultdict
from collections import deque

BOARD = [
[ 0, 1, 2, 3, 4, 5, 6, 7],
[ 8, 9,10,11,12,13,14,15],
[16,17,18,19,20,21,22,23],
[24,25,26,27,28,29,30,31],
[32,33,34,35,36,37,38,39],
[40,41,42,43,44,45,46,47],
[48,49,50,51,52,53,54,55],
[56,57,58,59,60,61,62,63]
]
MOVE_OFFSETS = ((-1, -2), ( 1, -2), (-2, -1), ( 2, -1), (-2,  1), ( 2,  1), (-1,  2), ( 1,  2),)

def traverse(graph, starting_vertex):
    visited = set()
    queue = deque([[starting_vertex]])
    while queue:
        path = queue.popleft()
        vertex = path[-1]
        yield vertex, path
        for neighbor in graph[vertex] - visited:
            visited.add(neighbor)
            queue.append(path + [neighbor])

def add_edge(graph, vertex_a, vertex_b):
    graph[vertex_a].add(vertex_b)
    graph[vertex_b].add(vertex_a)

def legal_moves_from(row, col):
    for row_offset, col_offset in MOVE_OFFSETS:
        move_row, move_col = row + row_offset, col + col_offset
        if 0 <= move_row < 8 and 0 <= move_col < 8:
            yield move_row, move_col

def build_graph():
    graph = defaultdict(set)
    for row in range(8):
        for col in range(8):
            for to_row, to_col in legal_moves_from(row, col):
                add_edge(graph, (row, col), (to_row, to_col))
    return graph

def index_2d(twoDlist, elem):
    for row, col in enumerate(twoDlist):
        if elem in col:
            return (row, col.index(elem))

def solution(src, dest):
    start = index_2d(BOARD, src)
    end = index_2d(BOARD, dest)
    graph = build_graph()
    for vertex, path in traverse(graph, start):
        if vertex == end:
            return len(path)-1
    
if __name__ == '__main__':
    print(solution(0,1))
    print(solution(19,36))