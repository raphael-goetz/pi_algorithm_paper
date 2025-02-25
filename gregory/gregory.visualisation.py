import math
import matplotlib.pyplot as plt

import gregory

pi_outers = []
pi_inners = []
means = []
vertices = []

for iteration in range(10):
    pi_inner, pi_outer, mean, current_vertices = gregory.gregory_pi_approximation(iteration)
    pi_outers.append(pi_outer)
    pi_inners.append(pi_inner)
    means.append(mean)
    vertices.append(current_vertices)

plt.figure(figsize=(10, 6))
plt.title("Konvergenzverhalten des Umfangs eines n-Ecks")

plt.plot(pi_inners, label="Umfang des inneren Vielecks")
plt.plot(pi_outers, label="Umfang des äußeren Vielecks")
plt.plot(means, linestyle='--', label="Mittelwert")
plt.axhline(y=math.pi, color='red', linestyle='--', label='π (Referenzwert)')

plt.xlabel('Anzahl der Ecken (n)')
plt.ylabel('Annäherung an π')
plt.xticks(range(10), labels=vertices)
plt.legend()
plt.show()
