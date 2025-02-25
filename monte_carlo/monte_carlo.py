import random

coordinates = []
coordinates_inside = []


def monte_carlo_pi(n):
    numbers = 0
    numbers_k = 0

    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        pair = (x, y)

        if (x**2 + y**2) <= 1:
            coordinates_inside.append(pair)
            numbers_k += 1

        coordinates.append(pair)
        numbers += 1

    return 4 * numbers_k / numbers