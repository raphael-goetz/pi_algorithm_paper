"""
In dieser Datei befindet sich nur die Implementierung des Gregory Verfahren!
"""
import math


def gregory_pi_approximation(iteration):
    """
    Approximiert π durch zwei anschmiegende Vielecke!

    Parameter:
        - iteration: Anzahl der Iterationen

    Rückgabewerte:
        - pi_inner: untere Näherung für π
        - pi_outer: obere Näherung für π
        - mean: Mittelwert zwischen der oberen und unteren Näherung
        - vertices: Anzahl der Ecken des Vielecks
        - difference: Abweichung zu π
    """
    # Defninition der Startwerte
    vertices = 4 # Anzahl der Ecken
    inner = 4 * math.sqrt(2)  # Umfang des einbeschriebenen Vierecks
    outer = 8  # Umfang des umbeschriebenen Vierecks

    for _ in range(iteration):
        outer = 2 * inner * outer / (inner + outer)  # Neuer Umfang des umbeschriebenen n-Ecks
        inner = math.sqrt(inner * outer)  # Neuer Umfang des einbeschriebenen n-Ecks
        vertices = 2 * vertices

    # Pi berechnen
    pi_inner = inner / 2  # untere Näherung für Pi
    pi_outer = outer / 2  # obere Näherung für Pi
    mean = (pi_inner + pi_outer) / 2  # Mittelwert der Näherung
    difference = abs(math.pi - mean)  # Abweichung vom Vergleichswert

    return pi_inner, pi_outer, mean, vertices, difference
