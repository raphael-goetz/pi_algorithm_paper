"""
In dieser Datei befindet sich nur die Implementation des Algorythmus!
"""

def calculate_sequence(k):
    """
    Berechnet die Leibnitz Reihe für PI

    param:
        k - Anzahl der Glieder

    returns:
        Approximiertes pi/4 (Summe der Reihe)
    """
    sum = 0
    for index in range(k):
        sum += ((-1)**index)/(2*index + 1)

    # Wird hier mit 4 mulitipliziert da die Summe PI/4 ergibt und wir nur PI benötigen
    return sum * 4
