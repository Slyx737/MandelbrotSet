# Mandelbrot Fractal Visualizer

Visualize the beauty and complexity of the Mandelbrot set with this Python script. The Mandelbrot set is a mathematical set of points in the complex plane that exhibits fractal properties. This script allows you to generate and display Mandelbrot fractals with customizable image size, bounds, and iteration count.

## Features

- Generate Mandelbrot fractals with a specified image size (width and height).
- Customize the bounds of the complex plane (x_min, x_max, y_min, y_max) to zoom in and explore different regions of the Mandelbrot set.
- Adjust the maximum number of iterations to control the level of detail in the fractal image.
- Display the generated Mandelbrot image with a color map of your choice.

## Usage

1. Set the desired image size, bounds, and maximum number of iterations in the script.
2. Run the script to generate and display the Mandelbrot fractal image.

```python
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

# Dependencies
NumPy
Matplotlib

# License
This project is open source and available under the MIT License.

# Contact
If you have any questions or suggestions, please feel free to reach out or open an issue on GitHub.