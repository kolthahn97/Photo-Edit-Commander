#!/usr/bin/env python
# coding: utf-8

# In[36]:


from PIL import Image
import numpy as np
import sys
from configparser import ConfigParser
import argparse
import os

# class ImageModifier:
#     def __init__(self, image_path):
#         self.image_path = image_path
#         self.image = Image.open(image_path)
#         #self.image = Image.new(io.mode, io.size)
        
#     def show(self):
#         return self.image.show()
        
#     def rotate_90_deg(self, rotate_count = 1):
#         width, height = self.image.size
#         if(rotate_count % 4 == 0):
#             return self
#         elif(rotate_count % 4 == 1):
#             self.image = self.image.transpose(Image.ROTATE_90).rotate(180)
#         elif(rotate_count % 4 == 2):
#             self.image = self.image.rotate(180)
#         else:
#             self.image = self.image.transpose(Image.ROTATE_90)
#         return self
    
#     def filter(self, amount, rgb='r'):
#         pixels = self.image.load()
        
#         for i in range(self.image.size[0]):
#             for j in range(self.image.size[1]):
#                 pixels[i,j] = (
#                     pixels[i,j][0] if 'r' not in rgb else int(pixels[i,j][0] * amount),
#                     pixels[i,j][1] if 'g' not in rgb else int(pixels[i,j][1] * amount),
#                     pixels[i,j][2] if 'b' not in rgb else int(pixels[i,j][2] * amount)
#                 )
#         return self  
    
#     def set_color(self, value, rgb='r'):
#         pixels = self.image.load()
        
#         for i in range(self.image.size[0]):
#             for j in range(self.image.size[1]):
#                 pixels[i,j] = (
#                     pixels[i,j][0] if 'r' not in rgb else value,
#                     pixels[i,j][1] if 'g' not in rgb else value,
#                     pixels[i,j][2] if 'b' not in rgb else value
#                 )
#         return self 
    
#     def rotate_color(self):
#         pixels = self.image.load()
        
#         for i in range(self.image.size[0]):
#             for j in range(self.image.size[1]):
#                 pixels[i,j] = (
#                     pixels[i,j][1],
#                     pixels[i,j][2],
#                     pixels[i,j][0]
#                 )
#         return self 
    
#     def invert(self, rgb='r'):
#         pixels = self.image.load()
        
#         for i in range(self.image.size[0]):
#             for j in range(self.image.size[1]):
#                 pixels[i,j] = (
#                     pixels[i,j][0] if 'r' not in rgb else 255-pixels[i,j][0],
#                     pixels[i,j][1] if 'g' not in rgb else 255-pixels[i,j][1],
#                     pixels[i,j][2] if 'b' not in rgb else 255-pixels[i,j][2]
#                 )
#         return self 
    
#     def grayscale_red(self):
#         pixels = self.image.load()
        
#         for i in range(self.image.size[0]):
#             for j in range(self.image.size[1]):
#                 pixels[i,j] = (
#                     pixels[i,j][0],
#                     pixels[i,j][0],
#                     pixels[i,j][0]
#                 )
#         return self 
    
#     def grayscale_green(self):
#         pixels = self.image.load()
        
#         for i in range(self.image.size[0]):
#             for j in range(self.image.size[1]):
#                 pixels[i,j] = (
#                     pixels[i,j][1],
#                     pixels[i,j][1],
#                     pixels[i,j][1]
#                 )
#         return self 
    
#     def grayscale_blue(self):
#         pixels = self.image.load()
        
#         for i in range(self.image.size[0]):
#             for j in range(self.image.size[1]):
#                 pixels[i,j] = (
#                     pixels[i,j][2],
#                     pixels[i,j][2],
#                     pixels[i,j][2]
#                 )
#         return self 
    
#     def grayscale(self):
#         pixels = self.image.load()
        
#         for i in range(self.image.size[0]):
#             for j in range(self.image.size[1]):
#                 pixels[i,j] = (
#                     int((pixels[i,j][0] + pixels[i,j][1] + pixels[i,j][2])/3),
#                     int((pixels[i,j][0] + pixels[i,j][1] + pixels[i,j][2])/3),
#                     int((pixels[i,j][0] + pixels[i,j][1] + pixels[i,j][2])/3)
#                 )
#         return self 


# In[37]:


# img = ImageModifier(r"C:\Users\kolth\Downloads\IMG_20191108_090307.jpg")
# img.grayscale().show()


# In[39]:


if not os.path.exists('config.ini'):
    config = ConfigParser()

    config.read('config.ini')
    config.add_section('settings')
    config.set('settings', 'destination', './')

    with open('config.ini', 'w') as f:
        config.write(f)


# In[40]:


args = ".\ImageModifier.py -h".split()
# for arg in sys.argv:
for arg in args:
    print(arg)


# In[43]:


parser = argparse.ArgumentParser(prog='.\ImageModifier')
parser.add_argument('--active-destination', nargs=1, help='set the default image / folder location for future commands without a destination specified')
args = parser.parse_args(args)
args


# In[ ]:




