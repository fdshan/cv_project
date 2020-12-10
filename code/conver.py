import os

files = os.listdir()

counter = 0

for file in files:
    if file[-4:] == '.ply':
        number = 200 + counter
        os.rename(file, "car_" + str(number) + "_mesh.ply")
        counter += 1
