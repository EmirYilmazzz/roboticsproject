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



print(joint1.pos.x,joint1.pos.y,joint1.pos.z)