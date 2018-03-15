import numpy
import matplotlib.pyplot as plt
from copy import deepcopy
from PIL import Image
from math import cos, sin
import math

def getGrayColor(rgb):
    gray = int((int(rgb[0])+int(rgb[1])+int(rgb[2]))/3)
    return gray

def setGrayColor(color):
    color = int(color)
    return [color, color, color]


sizeShow = [2,5]

size = 3
limit = int((size-1)/2)

midSize = size*size
midlo  = int((midSize-1)/2)

# pic = input("input boardSaltPepper.bmp pepperNoise.bmp SaltNoise.bmp and gaussianNoise.bmp :")
pic = 'SaltNoise.bmp'

# q = input("input q for Contraharmonic Mean Filter :")
q = -2
d = 2

img = Image.open(pic)
img = numpy.asarray(img)


# copy list not reference
Contra = deepcopy(img)
MaxFilter = deepcopy(img)
MinFilter = deepcopy(img)
MidFilter = deepcopy(img)
Alpha = deepcopy(img)




for i in range(0+limit,len(img)-limit):
    for j in range(0+limit, len(img[i])-limit):
        max = 0
        min = 256
        num = [0]*midSize
        c = 0
        s1 = 0
        s2 = 0
        for k in range(i-limit, i+limit+1):
            for l in range(j-limit, j+limit+1):
                nC = getGrayColor(img[k][l])
                num[c] = nC
                c += 1

                if nC > max:
                    max = nC

                if nC < min:
                    min = nC

                # print nC,s2,q
                
                if nC is 0 and q+1.0 < 0:
                    s1 += 0
                else:
                    s1 += nC**(q+1.0)

                if nC is 0 and q < 0:
                    s2 += 0
                else:
                    s2 += nC**q
                
        # print(s1 , ' ', s2)
        if s2==0 :
            Contra[i][j] = setGrayColor(0)
        else : 
            Contra[i][j] = setGrayColor(s1/s2)
        # print(Contra[i][j],'  ',img[i][j])

        MaxFilter[i][j] = setGrayColor(max)
        MinFilter[i][j] = setGrayColor(min)
        MidFilter[i][j] = setGrayColor(1/2.0*(max+min))

        num.sort()
        num.pop(0)
        num.pop(len(num)-1)
        num = sum(num)
        Alpha[i][j] = setGrayColor(num/((size*size)-d))

plt.subplot(sizeShow[0], sizeShow[1], 1)
plt.gca().set_title(pic)
plt.imshow(img)


plt.subplot(sizeShow[0], sizeShow[1], 2)
plt.gca().set_title('Contra')
plt.imshow(Contra)

plt.subplot(sizeShow[0], sizeShow[1], 3)
plt.gca().set_title('Max Filter')
plt.imshow(MaxFilter)

plt.subplot(sizeShow[0], sizeShow[1], 4)
plt.gca().set_title('Min Filter')
plt.imshow(MinFilter)

plt.subplot(sizeShow[0], sizeShow[1], 5)
plt.gca().set_title('Midpoint Filter')
plt.imshow(MidFilter)

plt.subplot(sizeShow[0], sizeShow[1], 6)
plt.gca().set_title('Alpha-trimmed Mean Filter ')
plt.imshow(Alpha)

plt.show()
