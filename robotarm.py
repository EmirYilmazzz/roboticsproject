from vpython import *

scene = canvas(title='Robot Arm', width=800, height=600)

base = cylinder(pos=vector(0, 0, 0), axis=vector(0, 1, 0), radius=0.3, color=color.red)

joint1 = cylinder(pos=vector(0, 2, -0.5), axis=vector(0, 0, 1), radius=0.3, color=color.blue)

joint2 = cylinder(pos=vector(3, 2, -0.5), axis=vector(0, 0, 1), radius=0.3, color=color.green)

# Connecting base and joint1 with a line
base_to_j1 = curve(pos=[vector(0, 0, 0), vector(0, 2, 0)], color=color.white)

#j1_hand_1 = curve(pos=[vector(0, 2, -0.5), vector(2, 2, -0.5)], color=color.white)
j1_hand_1 = curve(pos=[vector(joint1.pos.x, joint1.pos.y, joint1.pos.z), vector(joint2.pos.x-1, joint2.pos.y, joint2.pos.z)], color=color.white)

j1_hand_2 = curve(pos=[vector(joint1.pos.x, joint1.pos.y, joint1.pos.z+1), vector(joint2.pos.x-1, joint2.pos.y, joint2.pos.z+1)], color=color.white)

j1_hand_3 = curve(pos=[vector(2, 2, -0.5), vector(2, 2, 0.5)], color=color.white)

j1_hand_4 = curve(pos=[vector(2, 2, 0), vector(3, 2, 0)], color=color.white)

j2_to_end = curve(pos=[vector(3, 2, 0), vector(4, 2, 0)], color=color.white)


end = arrow(pos=vector(4, 2, 0), axis=vector(1, 0, 0), radius=0.3, color=color.orange)


def rotate_joint1(event):
    global joint1
    if event.key == 'a':  # Rotate joint1 counterclockwise
        joint1.rotate(angle=radians(5), axis=vector(0, 1, 0))
    elif event.key == 'd':  # Rotate joint1 clockwise
        joint1.rotate(angle=-radians(5), axis=vector(0, 1, 0))

def rotate_arm(event):
    global joint1, joint2, j1_hand_1, j1_hand_2, j1_hand_3, j1_hand_4, j2_to_end
    if event.key == 'b':  # Rotate arm counterclockwise
        joint1.rotate(angle=radians(5), axis=vector(0, 1, 0))
        joint2.rotate(angle=radians(5), axis=vector(0, 1, 0))
        j1_hand_1.modify(0, pos=[vector(joint1.pos.x, joint1.pos.y, joint1.pos.z), vector(joint2.pos.x-1, joint2.pos.y, joint2.pos.z)])
        j1_hand_2.modify(0, pos=[vector(joint1.pos.x, joint1.pos.y, joint1.pos.z+1), vector(joint2.pos.x-1, joint2.pos.y, joint2.pos.z+1)])
    elif event.key == 'c':  # Rotate arm clockwise
        joint1.rotate(angle=-radians(5), axis=vector(0, 1, 0))
        joint2.rotate(angle=-radians(5), axis=vector(0, 1, 0))
        j1_hand_1.modify(0, pos=[vector(joint1.pos.x, joint1.pos.y, joint1.pos.z), vector(joint2.pos.x-1, joint2.pos.y, joint2.pos.z)])
        j1_hand_2.modify(0, pos=[vector(joint1.pos.x, joint1.pos.y, joint1.pos.z+1), vector(joint2.pos.x-1, joint2.pos.y, joint2.pos.z+1)])


while True:
    try:
        scene.bind('keydown',rotate_arm) 
    except Exception as e:
         print(f"Failed to process line with error: {e}")
    rate(10)  # Run the loop at 50Hz or adjust according to your requirements
