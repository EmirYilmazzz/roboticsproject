from vpython import *
import serial
import time

# Initialize the VPython scene
scene = canvas()

# Create cylinders for the axes
x_axis = cylinder(pos=vector(0, 0, 0), axis=vector(1, 0, 0), radius=0.05, color=color.red)
y_axis = cylinder(pos=vector(0, 0, 0), axis=vector(0, 1, 0), radius=0.05, color=color.green)
z_axis = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, 1), radius=0.05, color=color.blue)

# Establish a serial connection to the Arduino
arduino = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)  # Give the connection a second to settle

def parse_line(line):
    try:
        # Creating a dictionary from the formatted string
        parts = line.split('    ')
        data_dict = {part.split(': ')[0]: int(part.split(': ')[1]) for part in parts}
        return data_dict
    except Exception as e:
        print(f"Failed to parse line '{line}' with error: {e}")
        return None

# Orientation angles initialized to 0
orientation = {'x': 0, 'y': 0, 'z': 0}

def update_orientation(gx, gy, gz, dt):
    # Convert gyroscope data to angular displacements
    orientation['x'] += gx * dt
    orientation['y'] += gy * dt
    orientation['z'] += gz * dt

    # Apply the updated orientations to the 3D model
    # Note: This resets the orientation each time to prevent compound rotations
    x_axis.axis = vector(1, 0, 0).rotate(angle=radians(orientation['x']), axis=vector(1, 0, 0))
    x_axis.axis = x_axis.axis.rotate(angle=radians(orientation['y']), axis=vector(0, 1, 0))
    x_axis.axis = x_axis.axis.rotate(angle=radians(orientation['z']), axis=vector(0, 0, 1))
    
    y_axis.axis = vector(0, 1, 0).rotate(angle=radians(orientation['x']), axis=vector(1, 0, 0))
    y_axis.axis = y_axis.axis.rotate(angle=radians(orientation['y']), axis=vector(0, 1, 0))
    y_axis.axis = y_axis.axis.rotate(angle=radians(orientation['z']), axis=vector(0, 0, 1))
    
    z_axis.axis = vector(0, 0, 1).rotate(angle=radians(orientation['x']), axis=vector(1, 0, 0))
    z_axis.axis = z_axis.axis.rotate(angle=radians(orientation['y']), axis=vector(0, 1, 0))
    z_axis.axis = z_axis.axis.rotate(angle=radians(orientation['z']), axis=vector(0, 0, 1))

# Main loop
last_time = time.time()
while True:
    try:
        now = time.time()
        dt = now - last_time  # Time difference in seconds
        last_time = now

        # Read the next line from the Arduino
        line = arduino.readline().decode('utf-8').rstrip()
        if line:  # Check if the line is not empty
            data_dict = parse_line(line)
            if data_dict and all(k in data_dict for k in ['gX', 'gY', 'gZ']):  # Ensure all keys are present
                # Extract gyroscope values
                gx, gy, gz = data_dict['gX'], data_dict['gY'], data_dict['gZ']
                gz=gz+10
                gy=gy+200
                gx=780+gx
                if gx<100 and gx >-100:
                        gx=0
                if gy<100 and gy >-100:
                        gy=0
                if gz<100 and  gz>-100:
                        gz=0
                gx=gx/100
                gy=gy/100
                gz=gz/100 
                print(f"Gyroscope: ({gx}, {gy}, {gz})")
                
                update_orientation(gx, gy, gz, dt)
    except Exception as e:
         print(f"Failed to process line with error: {e}")
    rate(10)  # Run the loop at 50Hz or adjust according to your requirements
