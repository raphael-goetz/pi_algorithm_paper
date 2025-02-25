import gregory
import digits.digits as digits

"""
Anzahl der Ecken ist verantwortlich für die Genauigkeit
"""

digit = 1
results = []

for index in range(100):
    _, _, _, vertices, difference = gregory.gregory_pi_approximation(index)
    current_truncate = digit * 2

    truncated_difference = digits.truncate(difference, current_truncate)
    if truncated_difference == 0:
        digit += 1
        if digit == 4:
            digit += 1

        results.append((vertices, current_truncate))

    if digit > 5:
        break

print(f"{'Anzahl der Ecken':<20} | {'Genauigkeit (zu π) auf Nachkommastellen':<10}")
print("-" * 60)

# Table rows
for vertices, current_truncate in results:
    print(f"{vertices:<20} | {current_truncate:<10}")
