import math
from typing import Match
from PIL import Image

# parameters
image = Image.open("test.JPG")
displayRingLEDs = [60,48,40,32,24,16,12,8,1] #LEDS in the rings
pictureSharpner =0.85 #to reduce blur in the pixels overlapse and to sharpen the picture (0 - 1.0)

# output
imageOutput = [] # output is in terminal not in file yet

processRing=len(displayRingLEDs) # how many rings are there
pictureCenterX =image.width/2
pictureCenterY = image.height/2
pictureProcessPixels = min(image.width,image.height) #process just the square in the middel
pictureDivider = pictureProcessPixels/((processRing*2)-1) #calulate how long the steps are for each ring
pictureEpsilon = int(pictureDivider*pictureSharpner/2.0) #to reduce overlapse and to sharpen the picture



processCenterY = 0
processCenterX = 0 
processRing=len(displayRingLEDs)

for ring in displayRingLEDs:
    processRing = processRing-1
    for pixel in range(ring):
        processCenterY = int(pictureCenterY - (processRing * pictureDivider)* math.cos(pixel/ring*2*math.pi))
        processCenterX = int(pictureCenterX - (processRing * pictureDivider) * math.sin(pixel/ring*2*math.pi))
        color = [0,0,0]
        getPixel = [0,0,0]
        pixelCounter = 0
        for sectorY in range(processCenterY-pictureEpsilon,processCenterY+pictureEpsilon+1):
            for sectorX in range(processCenterX-pictureEpsilon,processCenterX+pictureEpsilon+1):
                pixelCounter = pixelCounter + 1                
                for idx, colorPart in enumerate(image.getpixel((sectorX ,sectorY))):
                    getPixel[idx] = getPixel[idx] + colorPart
        for putPixelColor in range(len(getPixel)):
            getPixel[putPixelColor] = round(getPixel[putPixelColor]/pixelCounter)
        imageOutput.append(getPixel)
    

#print("---------------")
#print(pictureProcessPixels)
#print("------------------------------")

print(imageOutput)

