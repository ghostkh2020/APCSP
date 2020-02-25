import matplotlib.pyplot as plt
import os.path
import numpy as np

def cutBackground(image):
    img = PIL.image.new('RGBA',(columns, rows))
    image = np.array(img)
    numRows = len(image)
    numcols = len(image[0])   
    for row in range(numRows):
       for col in range (numcols):
            currentPixel = image[row][col]
            currentRed = currentPixel[0]
            currentGreen = currentPixel[1]
            currentBlue = currentPixel[2]
            averageIntensity = (currentRed / 3 + currentGreen/3 + currentBlue/3)
        
            if averageIntensity < 50:
                img[row][col] = [0,0,0,255]
                
            else:
                img[row][col] = averageIntensity
    return image
def commbine(img_front, img_back):
    img = PIL.image.new('RGBA',(columns, rows))
    image = np.array(img)
    numRows = len(image_front)
    numcols = len(image_front[0])   
    for row in range(numRows):
       for col in range (numcols):
           new_image = image_back  + [row][col]
    return new_image
           
        
directory = os.path.dirname(os.path.abspath(__file__))
image_front = os.path.join(directory, "dream.png")
image_back = os.path.join(directory, "mroad.jpg")
img = plt.imread(commbine)

fig, ax = plt.subplots(1,1)

ax[0].imshow(img, interpolation = "none")      
 
    
fig.show()

            
                    
                    

