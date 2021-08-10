paths = list()
distances = list()
matrix = [  [0, 4, 0, 0, 0, 0],
            [0, 0, 2, 2, 0, 0],
            [0, 2, 0, 0, 7, 0],
            [1, 2, 3, 0, 0, 0],
            [0, 0, 0, 0, 0, 2],
            [0, 0, 2, 0, 0, 0]  ]


def get_paths_between(departure, arrival, cities = list()):

    for city in range(len(matrix[departure])):

        distance = matrix[departure][city] # distance entre la ville <departure> et la prochaine ville <city>

        if city == arrival and distance != 0:
            return paths.append(cities + [departure, arrival])

        if distance != 0 and not city in cities:
            get_paths_between(city, arrival, cities + [departure])

def get_distance():

    for path in paths:

        total = 0

        for i in range(len(path) - 1):
            x = path[i + 1]
            y = path[i]
            total += matrix[y][x]

        distances.append(total)

def print_best_distance():

    maximum = 0

    for i in range(len(distances)):
        if distances[i] > maximum:
            maximum = distances[i]

    print("La plus courte distance est : ")
    print(paths[i])
    print(distances[i], "km")


get_paths_between(3, 5)
get_distance()
print_best_distance()