from machine import Pin, I2C
import ht16k33_matrix
import time

i2c = I2C(0)                                            # Init I2C using I2C0 defaults, SCL=Pin(GP9), SDA=Pin(GP8), freq=400000
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config

matrix1 = ht16k33_matrix.MatrixBackpack16x8(i2c, 0x70)
matrix2 = ht16k33_matrix.MatrixBackpack16x8(i2c, 0x71)

# Clear the matrix.
matrix1.fill(0)
matrix2.fill(0)

# Setting the Brightness
matrix1.brightness(1)
matrix2.brightness(1)

# Set a pixel in the origin 0, 0 position.
matrix1[0, 0] = 1
matrix2[0, 0] = 1
# Set a pixel in the middle 8, 4 position.
matrix1[8, 4] = 1
matrix2[8, 4] = 1
# Set a pixel in the opposite 15, 7 position.
matrix1[15, 7] = 1
matrix2[15, 7] = 1

time.sleep(2)

# Draw a Smiley Face
matrix1.fill(0)
matrix2.fill(0)

for row in range(2, 6):
    matrix1[row, 0] = 1
    matrix2[row, 0] = 1
    matrix1[row, 7] = 1
    matrix2[row, 7] = 1

for column in range(2, 6):
    matrix1[0, column] = 1
    matrix2[0, column] = 1
    matrix1[7, column] = 1
    matrix2[7, column] = 1

matrix1[1, 1] = 1
matrix2[1, 1] = 1
matrix1[1, 6] = 1
matrix2[1, 6] = 1
matrix1[6, 1] = 1
matrix2[6, 1] = 1
matrix1[6, 6] = 1
matrix2[6, 6] = 1
matrix1[2, 5] = 1
matrix2[2, 5] = 1
matrix1[5, 5] = 1
matrix2[5, 5] = 1
matrix1[2, 3] = 1
matrix2[2, 3] = 1
matrix1[5, 3] = 1
matrix2[5, 3] = 1
matrix1[3, 2] = 1
matrix2[3, 2] = 1
matrix1[4, 2] = 1
matrix2[4, 2] = 1

# Move the Smiley Face Around
while True:
    for frame in range(0, 8):
        matrix1.shift_right(True)
        matrix2.shift_right(True)
        time.sleep(0.05)
    for frame in range(0, 8):
        matrix1.shift_down(True)
        matrix2.shift_down(True)
        time.sleep(0.05)
    for frame in range(0, 8):
        matrix1.shift_left(True)
        matrix2.shift_left(True)
        time.sleep(0.05)
    for frame in range(0, 8):
        matrix1.shift_up(True)
        matrix2.shift_up(True)
        time.sleep(0.05)
        