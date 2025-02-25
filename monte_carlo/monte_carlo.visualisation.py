from matplotlib import pyplot as plt
import monte_carlo
import math

k = 100000
sums = []
for amount in range(100, k, 100):
    carlo = monte_carlo.monte_carlo_pi(amount)
    sums.append(carlo)

plt.plot(sums)
plt.title("Konvergenzverhalten der Monte Carlo-Methode zur π-Annäherung")
plt.axhline(y=3.1416, color='red', linestyle='--', label='π (Referenzwert)')
plt.ylabel("Näherungswert von π")
plt.xlabel("Anzahl der Zufallspunkte (K)")
plt.ylim(3.20, 3.05)
plt.legend()

plt.show()

pi_sum = 0
for current_sum in sums:
    pi_sum += current_sum

mean = pi_sum / len(sums)

pi_distance_sum = 0
for curr in sums:
    pi_distance_sum += (curr - mean)**2

sigma = math.sqrt(pi_distance_sum / len(sums))

plt.axvline(x=mean, color='blue', linestyle='--', label="Mittelwert")
plt.axvline(x=mean+sigma, color='red', linestyle='--')
plt.axvline(x=mean-sigma, color='red', linestyle='--', label="Standardabweichung")
plt.hist(sums, bins=1000, facecolor='g')
plt.title("Verteilung der Näherungswerte von π")
plt.xlabel("Näherungswert von π")
plt.ylabel("Häufigkeit")
plt.axis((3.18, 3.1, 0, 25))
plt.legend()

plt.show()


