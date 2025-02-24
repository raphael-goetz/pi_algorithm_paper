import math
import leibnitz
k = 0
digit = 1
ks = []

def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

while digit < 5:
    k += 1
    current_truncate = digit*2
    sum = leibnitz.calculate_sequence(k)

    diff = abs(sum - math.pi)
    truncated_difference = truncate(diff, current_truncate)
    print(f'Diff of {k}: {diff}')
    if truncated_difference == 0:
        digit += 1
        ks.append(k)

    if digit == 4:
        break

print(ks)