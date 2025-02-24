"""
In diesem File befindet sich nur die visualisierung des leibnitz alogrythmus
"""

from matplotlib import pyplot as plt
import leibnitz

k = 5000
sums = []
for amount in range(k):
    current_sum = leibnitz.calculate_sequence(amount)
    sums.append(current_sum)

print(sums)

plt.plot(sums)
plt.title("Konvergenzverhalten der Leibnitzreihe")
plt.axhline(y=3.1416, color='red', linestyle='--', label='Realwert für π')
plt.ylabel("Größe der Summe (Näherungswert an π)")
plt.xlabel("K - Anzahl der Summenglieder")
plt.ylim(3.1316, 3.1516)
plt.legend()

plt.show()