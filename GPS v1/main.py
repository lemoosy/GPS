paths = list()
distances = list()
matrix = [  [0, 4, 0, 0, 0, 0],
            [0, 0, 2, 2, 0, 0],
            [0, 2, 0, 0, 7, 0],
            [1, 2, 3, 0, 0, 0],
            [0, 0, 0, 0, 0, 2],
            [0, 0, 2, 0, 0, 0]  ]


def get_paths_between(start, end, path = list()):

    for x in range(len(matrix[start])):

        if x == start:
            continue

        if x == end and matrix[start][x] != 0:
            return paths.append(path + [start, end])

        if matrix[start][x] != 0:
            if not x in path:
                get_paths_between(x, end, path + [start])

def get_total_distance():

    for path in paths:

        total = 0

        for i in range(len(path) - 1):
            x = path[i + 1]
            y = path[i]
            total += matrix[y][x]

        distances.append(total)


get_paths_between(0, 5)
get_total_distance()


print(paths)
print(distances)