import math

import digits.digits

"""
Anzahl der Glieder in der Reihe verantwortlich für die Genauigkeit der Nachkommastelle

10. Nachkommastelle nicht erreichbar (zu groß)
"""

sum = 0
index = 0
k = 0
digit = 1
ks = []

while digit < 5:

    sum += ((-1) ** index) / (2 * index + 1)
    index += 1

    # Wird hier mit 4 mulitipliziert da die Summe PI/4 ergibt und wir nur PI benötigen

    k += 1
    current_truncate = digit * 2

    diff = abs((sum * 4) - math.pi)
    truncated_difference = digits.digits.truncate(diff, current_truncate)
    if truncated_difference == 0:
        digit += 1
        ks.append((k, current_truncate))

    if digit == 4:
        break

print(ks)
