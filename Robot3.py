from vpython import *
import numpy as np

# Initialize the VPython scene
scene = canvas()

def rotate_matrix(t):
    # Ensure t is in radians; t is assumed to be in radians as input
    rotation_matrix = np.array([[np.cos(t), -np.sin(t), 0],
                                [np.sin(t), np.cos(t), 0],
                                [0, 0, 1]])
    return rotation_matrix

def translation_matrix(x, y, z):
    # This function should return a 4x1 translation vector for homogeneous transformation
    translation_matrix = np.array([x, y, z])  # Make it 4x1 for homogeneous coordinates
    return translation_matrix

def homogeneous_matrix(rotation_matrix, translation_vector):
    # Create a 4x4 identity matrix and populate it with rotation and translation components
    T = np.eye(4)  # start with an identity matrix
    T[0:3, 0:3] = rotation_matrix  # replace the top-left 3x3 block with the rotation matrix
    T[0:3, 3] = translation_vector[0:3]  # replace the last column of the first three rows
    return T

def forward(matrix1, matrix2):
    # Perform matrix multiplication using np.dot
    result = np.dot(matrix1, matrix2)
    return result

identity_matrix = np.eye(3)
theta1=0
theta2=0
theta3=0
d1=1
d2=1
d3=1
# Usage example
rotate_matrixBase = rotate_matrix(0)
translation_matrixBase = translation_matrix(0, 0, 0)
homogeneous_matrixBase = homogeneous_matrix(rotate_matrixBase, translation_matrixBase)
rotate_matrix1 = rotate_matrix(theta1)
translation_matrix1 = translation_matrix(0, 0, d1)# Now it will print the actual matrix, not the function
rotate_matrix2 = rotate_matrix(theta2)
translation_matrix2 = translation_matrix(d2 ,0, 0)# Now it will print the actual matrix, not the function
rotate_matrixendeffector = rotate_matrix(theta3)
translation_matrixendeffector = translation_matrix(d3, 0, 0)# Now it will print the actual matrix, not the function

def RotateBase(theta1):
    rotate_matrixBase = rotate_matrix(theta1)
    translation_matrixBase = translation_matrix(0, 0, 0)
    homogeneous_matrixBase = homogeneous_matrix(rotate_matrixBase, translation_matrixBase)
    return homogeneous_matrixBase

def RotateMotor1(theta1,d1):
    rotate_matrix1Raw = rotate_matrix(theta1)
    matrixMap=([0, 0, 1],
              [1, 0, 0],
              [0, 1, 0])
    rotate_matrix1 = forward(rotate_matrix1Raw,matrixMap)
    translation_matrix1 = translation_matrix(0, 0, d1)# Now it will print the actual matrix, not the function
    homogeneous_matrix1 = homogeneous_matrix(rotate_matrix1, translation_matrix1)
    return homogeneous_matrix1

def RotateMotor2(theta1):
    rotate_matrix2Raw = rotate_matrix(theta2)
    rotate_matrix2=forward(rotate_matrix2Raw,identity_matrix)
    translation_matrix2 = translation_matrix(d2*cos(theta2) ,d2*sin(theta2), 0)# Now it will print the actual matrix, not the function
    homogeneous_matrix2 = homogeneous_matrix(rotate_matrix2, translation_matrix2)
    return homogeneous_matrix2

def RotateMotor3():
    rotate_matrix3Raw = rotate_matrix(theta3)
    rotate_matrix3=forward(rotate_matrix3Raw,identity_matrix)
    translation_matrix3 = translation_matrix(d3*cos(theta3),d3*sin(theta2), 0)# Now it will print the actual matrix, not the function
    homogeneous_matrixendeffector = homogeneous_matrix(rotate_matrix3, translation_matrix3)
    return homogeneous_matrixendeffector



def endeffector(theta1,theta2,theta3,d1,d2,d3):
    rotate_matrix1Raw = rotate_matrix(theta1)
    matrixMap=([0, 0, 1],
              [1, 0, 0],
              [0, 1, 0])
    rotate_1 = forward(rotate_matrix1Raw,matrixMap)
    rotate_matrix2Raw = rotate_matrix(theta2)
    rotate_2=forward(rotate_matrix2Raw,identity_matrix)
    rotate_matrix3Raw = rotate_matrix(theta3)
    rotate_3=forward(rotate_matrix3Raw,identity_matrix)
    RotateEnd=forward(rotate_3,forward(rotate_2,rotate_1))
    translation_matrix1 = translation_matrix(0, 0, d1)
    translation_matrix2 = translation_matrix(d2*cos(theta2) ,d2*sin(theta2), 0)
    translation_matrix3 = translation_matrix(d3*cos(theta3),d3*sin(theta3), 0)
    PosStep1=translation_matrix1+forward(rotate_1,(translation_matrix2+(forward(rotate_2,translation_matrix3))))
    RotateFinal=homogeneous_matrix(RotateEnd,PosStep1)
    return RotateFinal 


def motor2(theta1,theta2,d1,d2):
    rotate_matrix1Raw = rotate_matrix(theta1)
    matrixMap=([0, 0, 1],
              [1, 0, 0],
              [0, 1, 0])
    rotate_1= forward(rotate_matrix1Raw,matrixMap)
    rotate_matrix2Raw = rotate_matrix(theta2)
    rotate_2=forward(rotate_matrix2Raw,identity_matrix)
    RotateEnd=forward(rotate_2,rotate_1)
    translation_matrix1 = translation_matrix(0, 0, d1)
    translation_matrix2 = translation_matrix(d2*cos(theta2) ,d2*sin(theta2), 0)
    PosStep1M2=translation_matrix1+forward(rotate_1,(translation_matrix2))
    RotateM2Final=homogeneous_matrix(RotateEnd,PosStep1M2)
    return RotateM2Final 

def motor1(theta1,d1):
    rotate_matrix1Raw = rotate_matrix(theta1)
    matrixMap=([0, 0, 1],
              [1, 0, 0],
              [0, 1, 0])
    rotate_1= forward(rotate_matrix1Raw,matrixMap)
    RotateEnd=rotate_1
    translation_matrix1 = translation_matrix(0, 0, d1)
    PosStep1M2=translation_matrix1
    RotateM2Final=homogeneous_matrix(RotateEnd,PosStep1M2)
    return RotateM2Final 
theta1=(pi/180)*0
theta2=(pi/180)*0
theta3=(pi/180)*0
d1=2
d2=2
d3=2
motor1Val= motor1(theta1,d1)
motor2Val= motor2(theta1,theta2,d1,d2)

endeffectorVal= endeffector(theta1,theta2,theta3,d1,d2,d3)





bluepos=vector(motor1Val[0][3],motor1Val[1][3],motor1Val[2][3])
redpos=vector(motor2Val[0][3],motor2Val[1][3],motor2Val[2][3])
Endpos=vector(endeffectorVal[0][3],endeffectorVal[1][3],endeffectorVal[2][3])

main_cylinder = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, d1/2), radius=0.5, color=color.green)
grayofgreen= cylinder(pos=(bluepos+main_cylinder.pos)/2,axis=vector(bluepos-((bluepos+main_cylinder.pos)/2)),radius=0.25,color=color.gray(0.5))

blue_cylinder = cylinder(pos=bluepos,axis=vector((redpos-bluepos)/2), radius=0.5, color=color.blue)
grayofblue= cylinder(pos=(redpos+bluepos)/2,axis=vector(redpos-((redpos+bluepos)/2)),radius=0.25,color=color.gray(0.5))

red_cylinder = cylinder(pos=redpos,axis=vector((Endpos-redpos)/2),radius=0.5,color=color.red)
grayofred= cylinder(pos=(Endpos+redpos)/2,axis=vector(Endpos-((Endpos+redpos)/2)),radius=0.25,color=color.gray(0.5))

def handle_keydown(evt):
    global theta1, theta2, theta3
    step = (pi/360) * 0.01  # Angle change step size in degrees
    if evt.key == 'a':
        theta1 += step
    elif evt.key == 'b':
        theta1 -= step
    elif evt.key == 'c':
        theta2 += step
    elif evt.key == 'd':
        theta2 -= step
    elif evt.key == 'e':
        theta3 += step
    elif evt.key == 'f':
        theta3 -= step
            
def update_visual():
    global main_cylinder, blue_cylinder, red_cylinder
    motor1Val= motor1(theta1,d1)
    motor2Val= motor2(theta1,theta2,d1,d2)
    endeffectorVal= endeffector(theta1,theta2,theta3,d1,d2,d3)
    bluepos=vector(motor1Val[0][3],motor1Val[1][3],motor1Val[2][3])
    redpos=vector(motor2Val[0][3],motor2Val[1][3],motor2Val[2][3])
    Endpos=vector(endeffectorVal[0][3],endeffectorVal[1][3],endeffectorVal[2][3])
    # Calculate new positions and axes based on current angles
    blue_cylinder.pos =bluepos  # Example position update
    blue_cylinder.axis = vector((redpos-bluepos)/2) # Example axis update
    grayofblue.pos=(redpos+bluepos)/2
    grayofblue.axis=vector(redpos-((redpos+bluepos)/2))
    
    red_cylinder.pos = redpos
    red_cylinder.axis = vector((Endpos-redpos)/2)
    grayofred.pos=(Endpos+redpos)/2
    grayofred.axis=(Endpos-((Endpos+redpos)/2))
            
i=0
while True:
    rate(10)
    if(theta1>2*pi):
        theta1=theta1-2*pi
    if(theta1<-2*pi):
        theta1=theta1+2*pi
    if(theta2>2*pi):
        theta2=theta2-2*pi
    if(theta2<-2*pi):
        theta2=theta2+2*pi
    if(theta3>2*pi):
        theta3=theta3-2*pi
    if(theta3<-2*pi):
        theta3=theta3+2*pi
    i += 1
    if i % 10 == 0:
      
        print("theta1: ", theta1)
        print("theta2: ", theta2)
        print("theta3: ", theta3)
        print("-------------------------")
     # Update visuals after changing angles

    # Bind the keydown event to the handler
    scene.bind('keydown', handle_keydown)
    update_visual()
    

   

   