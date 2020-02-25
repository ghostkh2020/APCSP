import matplotlib.pyplot as plt
import os.path
import numpy as np

from PIL import image
def combine_image():
    front = image.open("dream.png")
    back = image.open("mroad.jpg")
    width = front.size[0] + back.size[0]
    hight = front.size[1]
    
    new_image = Image.new("RGB", (width, hight))
    new_image.paste(front, (0,0))
    new_image.paste(back, (front.size[0], 0))
    new_image.save("combined.png")
    return image 

