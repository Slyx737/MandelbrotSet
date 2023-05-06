import matplotlib.pyplot as plt
import numpy as np

def mandelbrot(c, max_iter):
    z = 0.0j
    for i in range(max_iter):
        z = z*z + c
        if abs(z) > 2.0:
            return i
    return max_iter

def create_mandelbrot_image(width, height, x_min, x_max, y_min, y_max, max_iter):
    r1 = np.linspace(x_min, x_max, width)
    r2 = np.linspace(y_min, y_max, height)
    return (r1, r2, np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2]))

# Image size and bounds
width, height = 800, 800
x_min, x_max = -2, 2
y_min, y_max = -2, 2
max_iter = 256

# Generate Mandelbrot image
x, y, mandelbrot_image = create_mandelbrot_image(width, height, x_min, x_max, y_min, y_max, max_iter)

# Display the image
plt.imshow(mandelbrot_image.T, extent=(x_min, x_max, y_min, y_max), cmap='hot')
plt.colorbar()
plt.show()
