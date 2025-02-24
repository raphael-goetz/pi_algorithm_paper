def calculate_sequence(k):
    """
    Berechnet die Leibnitz Reihe für PI

    param:
        k - Anzahl der Glieder

    returns:
        Approximiertes pi/4 (Summe der Reihe)
    """
    sum = 0
    for index in range(0, k):
        sum += ((-1)**index)/(2*index + 1)

    return sum

sum = calculate_sequence(2000000)
# Hier multipilitert mit 4 --> ergibt pi
print(sum * 4)
