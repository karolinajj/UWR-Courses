from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


#rgb_values = image.getpixel((20, 30))

def make_happier(image):
    pixels = np.array(Image.open(image))
    pixels_a = pixels[:, :, :3]
    print(pixels_a)

    
    

#image.putpixel((i,j), (250,0,0))
image = "input_image1.jpg"
make_happier(image)
#output_path = "modified_image.jpg"
#image.save(output_path)