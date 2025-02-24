from math import sqrt

def calculate_boundaries(n):
    # Initial values for a square (4 sides)
    v_inner = 4 * sqrt(2)  # Perimeter of the inscribed square
    v_outer = 8            # Perimeter of the circumscribed square
    vertices = 4           # Number of vertices (starting with a square)
    radius = 1

    for iteration in range(n):
        # Double the number of vertices
        vertices *= 2

        # Update the inner and outer boundaries
        v_inner = (2 * v_inner * v_outer) / (v_inner + v_outer)  # Harmonic mean
        v_outer = sqrt(v_inner * v_outer)                        # Geometric mean

    # Calculate the approximations for π
    pi_inner = v_inner / 2 / radius # Half the perimeter of the inscribed polygon
    pi_outer = v_outer / 2 / radius # Half the perimeter of the circumscribed polygon

    # Print the results
    print(f'Inner bound: {pi_inner}')
    print(f'Outer bound: {pi_outer}')

    # Calculate the middle value
    middle = (pi_inner + pi_outer) / 2
    print(f'Middle: {middle}')
    print(f'Number of vertices: {vertices}')

# Example usage
calculate_boundaries(200)
