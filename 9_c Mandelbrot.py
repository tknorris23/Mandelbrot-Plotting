"""
Mandelbrot Set Plotting
Kelly Norris - 3/13/2024

From "Draw the Mandelbrot Set in Python"
By Bartosz Zaczyński
https://realpython.com/mandelbrot-set-python/#understanding-the-mandelbrot-set
"""

import matplotlib.pyplot as plt
import numpy as np


def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    """
    Form a matrix of complex numbers.

    Generates a 2d array of equidistant complex numbers within the
        specified ranges on the complex plane.
    X axis is the real axis, Y axis is the imaginary axis.
    Note that in Python, sqrt(-1) is defined as 'j' instead of 'i'.

    Arguments:
    xmin -- minimum x coordinate
    xmax -- maximum x coordinate
    ymin -- minimum y coordinate
    ymax -- maximum y coordinate
    pixel_density -- number of points to be generated between min and max
    """
    re = np.linspace(xmin, xmax, pixel_density)
    im = np.linspace(ymin, ymax, pixel_density)
    # Creates a 2d array with real numbers as columns
    #   and imaginary as rows.
    # An addition operation is broadcast along the axes
    #   creating our "grid" of complex points.
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

def is_stable(c, num_iterations):
    """
    Roughly determines if numbers in a complex matrix are stable.

    Takes each element of a complex array c and submits it to the
        Mandelbrot recursive formula.
    Iterates num_iterations number of times, and then checks if the
        result is less than or equal to 2.
    If the result is less than or equal to 2, it is likely stable,
        and therefore within the Mandelbrot set.
    
    Returns a boolean 2d array in the shape of c.

    Arguments:
    c -- a 2d matrix of complex numbers
    num_iterations -- the amount of times an element is submitted to
                        recursion
    """
    z = 0
    for _ in range(num_iterations):
        z = z ** 2 + c
    return abs(z) <= 2

def get_mandelbrot_members(c, num_iterations):
    """
    Returns elements of c that are within the mandelbrot set.
    """
    mask = is_stable(c, num_iterations)
    return c[mask]

fig, axes = plt.subplots(1, 2)

### Big Mandelbrot
# Generate a set of complex numbers
c = complex_matrix(-2, 0.5, -1.5, 1.5, 6000)
# Get the set of complex numbers that belong to the Mandelbrot set
members = get_mandelbrot_members(c, 75)

# Create a scatter plot of members
axes[0].scatter(members.real, members.imag, color="black", marker=',', s=1)
## Tune subplot
# Set subplot's aspect ratio to equal
axes[0].set_aspect("equal")

# Set yticks for labels
axes[0].set_yticks([-1, -0.5, 0, 0.5, 1])
# Set ytick labels
axes[0].set_yticklabels(["-1j", "-0.5j", "0j", "0.5j", "1j"])

# Set background color
axes[0].set_facecolor("#EAEAF2")
# Add white grid lines
axes[0].grid(visible=True, color="white")
# Send grid to background
axes[0].set_axisbelow(True)

# Add circle highlighting recursion area
highlight = plt.Circle((-1.76, 0), 0.1, color="red", fill=False)
axes[0].add_patch(highlight)

# Get rid of black figure borders
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)
axes[0].spines['bottom'].set_visible(False)
axes[0].spines['left'].set_visible(False)

axes[0].title.set_text("The Mandelbrot Set")


### Small Recursion
c = complex_matrix(-1.8, -1.74, -0.025, 0.025, 2048)
members = get_mandelbrot_members(c, 100)

axes[1].scatter(members.real, members.imag, color="black", marker=",", s=1)
axes[1].set_aspect("equal")

axes[1].set_yticks([-0.02, -0.01, 0, 0.01, 0.02])
axes[1].set_yticklabels(["-0.02j", "-0.01j", "0j", "0.01j", "0.02j"])
axes[1].set_facecolor('#EAEAF2')

axes[1].grid(visible=True, color="white")
axes[1].set_axisbelow(True)

axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)
axes[1].spines['bottom'].set_visible(False)
axes[1].spines['left'].set_visible(False)

axes[1].title.set_text("Highlighted Fractal Recursion")

fig.tight_layout()
fig.savefig("mandelbrot.png", dpi=400)