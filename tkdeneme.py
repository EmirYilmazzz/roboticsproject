from vpython import *

# Create cylinders for the axes
x_axis = cylinder(pos=vector(0, 0, 0), axis=vector(1, 0, 0), radius=0.05, color=color.red)
y_axis = cylinder(pos=vector(0, 0, 0), axis=vector(0, 1, 0), radius=0.05, color=color.green)
z_axis = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, 1), radius=0.05, color=color.blue)

# Create cones for the arrowheads
x_arrow = cone(pos=vector(1, 0, 0), axis=vector(0.3, 0, 0), radius=0.1, color=color.red)
y_arrow = cone(pos=vector(0, 1, 0), axis=vector(0, 0.3, 0), radius=0.1, color=color.green)
z_arrow = cone(pos=vector(0, 0, 1), axis=vector(0, 0, 0.3), radius=0.1, color=color.blue)

# Function to rotate y and z axes around x-axis by 5 degrees
def rotate_axes(event):
    if event.key == 'a':
        y_axis.rotate(angle=radians(5), axis=vector(1, 0, 0))
        z_axis.rotate(angle=radians(5), axis=vector(1, 0, 0))
        y_arrow.rotate(angle=radians(5), axis=vector(1, 0, 0))
        z_arrow.rotate(angle=radians(5), axis=vector(1, 0, 0))

# Bind keyboard event to rotate_axes function
scene.bind('keydown', rotate_axes)

# Run the scene
scene.waitfor('click')
    