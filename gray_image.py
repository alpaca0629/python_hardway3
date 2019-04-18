import matplotlib.pyplot as plt 
from PIL import Image as im
import numpy as np
import math
my_gray = [' ', '.','-','~','=','O','B','M','#','$','@']


image = im.open("pp.png").convert("L")
image.show()
print(type(image))
imm = np.array(image)
print(imm)
def to_mygray(current_gray):
    return math.ceil(current_gray/255*(len(my_gray)-1))

def m_to_mygray(mm):
    rows ,cols = mm.shape
    for r in range(rows):
        for c in range(cols):
            mm[r][c] = to_mygray(mm[r][c])
    return mm
def printmygray(mm):
    rows ,cols = mm.shape
    for r in range(rows):
        for c in range(cols):
            print(my_gray[int(mm[r][c])]+'  ', end='')
            #print(str(mm[r][c])+'  ', end='')
        print('\n')


if __name__ == "__main__":
    #l = [0,1,255,165]
    #for i in l:
    #    print(to_mygray(i))
    
    printmygray(m_to_mygray(imm))
    