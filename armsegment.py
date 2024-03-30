from vpython import *

scene = canvas(title='Robot Arm', width=800, height=600)

base = cylinder(pos=vector(0, 0, 0), axis=vector(0, 1, 0), radius=0.3, color=color.red)

joint1 = cylinder(pos=vector(0, 2, -0.5), axis=vector(0, 0, 1), radius=0.3, color=color.blue)

joint2 = cylinder(pos=vector(3, 2, -0.5), axis=vector(0, 0, 1), radius=0.3, color=color.green)

# Connecting base and joint1 with a line
base_to_j1 = curve(pos=[vector(0, 0, 0), vector(0, 2, 0)], color=color.white)

# Draw lines representing arm segments (optional)
arm_segment1 = curve(pos=[vector(0, 2, -0.5), vector(3, 2, -0.5)], color=color.white)
arm_segment2 = curve(pos=[vector(3, 2, -0.5), vector(4, 2, 0)], color=color.white)

end = arrow(pos=vector(4, 2, 0), axis=vector(1, 0, 0), radius=0.3, color=color.orange)

def rotate_arm(event):
    global joint2, arm_segment2
    if event.key == 'a':  # Rotate arm counterclockwise
        joint2.rotate(angle=radians(5), axis=vector(0, 1, 0))
        arm_segment2.modify(0, pos=[vector(3, 2, -0.5), vector(4, 2, 0)])
    elif event.key == 'd':  # Rotate arm clockwise
        joint2.rotate(angle=-radians(5), axis=vector(0, 1, 0))
        arm_segment2.modify(0, pos=[vector(3, 2, -0.5), vector(4, 2, 0)])

while True:
    try:
        scene.bind('keydown',rotate_arm) 
    except Exception as e:
         print(f"Failed to process line with error: {e}")
    rate(10)  # Run the loop at 50Hz or adjust according to your requirements
