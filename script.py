'''P3
4 3
255
255 0 0 255 0 0 255 0 0 255 0 0
0 255 0 0 255 0 0 255 0 0 255 0
0 0 255 0 0 255 0 0 255 0 0 255
'''

def triplets(width, height):
    string = "P3\n" + str(width) + " " + str(height) + "\n255\n"

    increment = 0
    for x in range(0, height):
        for y in range(0, width):
            string +=  str(increment) + " " + str(increment) + " " + str(increment) + " "
            increment += 255.0/width
        string += "\n"
        increment = 0
    return string

fd = open("hw.ppm", "w")
fd.write(str(triplets(300,300)))
fd.close()