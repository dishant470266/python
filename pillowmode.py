
# installation of pillow library 
# change the image extension 
# resize image files
# resize multiple images using for loop  
# Sharpness 
# Brightess 
# Color
# Contrast 
# Image blur , GaussianBlur

from PIL import Image, ImageEnhance, ImageFilter
import os 


# img1.save('dog1.pdf')
# img1.show()
# 250
# MAX_SIZE = (250,250)
# img1.thumbnail(MAX_SIZE)
# img1.save('dog1small.jpg')

# for item in os.listdir():
#     if item.endswith('.jpg'):
#         img1 = Image.open(item)
#         filename,extension = os.path.splitext(item)
#         img1.save(f'{filename}.png')
# img1 = Image.open('dog1.jpg')
# enhancer = ImageEnhance.Sharpness(img1)
# enhancer.enhance(5).save('dog1edited.jpg')
# 0 : blurry 
# 1: original image 
# 2 : image with increased sharpness 

# -------color ---------
# img1 = Image.open('dog1.jpg')
# enhancer = ImageEnhance.Color(img1)
# enhancer.enhance(2).save('dog1edited.jpg')

# --------brightness -----------
# img1 = Image.open('dog1.jpg')
# enhancer = ImageEnhance.Brightness(img1)
# enhancer.enhance(1.5).save('dog1edited.jpg')


img1 = Image.open('dog1.jpg')
enhancer = ImageEnhance.Contrast(img1)
enhancer.enhance(1.5).save('dog1edited.jpg')

# image blur 

# img1.filter(ImageFilter.GaussianBlur(radius=4)).save('dog1edited.jpg')





# from PIL import Image,ImageFilter, ImageEnhance
# image = Image.open('cute.jpg')
# image.filter(ImageFilter.MaxFilter(size=0)).show()
# # enhancer = ImageEnhance.Brightness(image)
# # enhancer.enhance(4).show()
