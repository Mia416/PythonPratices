'''
Created on Mar 13, 2017

@author: chen.zhang
'''

import os
from PIL import Image
from PIL.ImageFile import ImageFile
from PIL import ImageFilter

class PICAdo:

    img_path = ''
    save_path = '/home/chen.zhang/tmp/Small'  
    
    def get_image(self):
        try:
            img = Image.open(self.img_path)
            return img
        except Exception as inst:
            return ''; 
            print (inst)
            
           
    def resize(self,img_path):
        try:
            img = Image.open(img_path)
            (width,height) = img.size
            new_width = width/2
            new_height = height/2            
            out = img.resize((new_width,new_height),Image.ANTIALIAS)
            ext = os.path.splitext(img_path)[1]
            new_name = '%s%s%s' %(self.save_path,'/small',ext)
            out.save(new_name,quality=95)
         
        except Exception as inst:
             print (inst)    
     
    def thumb(self,img_path):
         size = (64,64) 
         try:
             new_name = os.path.splitext(img_path)[0] + '.thumbnail'
             img = Image.open(img_path)
             img.thumbnail(size)
             img.save(new_name,"JPEG") 
         except Exception as inst:
             print (inst)           
             
    def transpose_img(self):
        try:
            img = self.get_image()
            out_img = img.transpose(Image.ROTATE_180)
            new_name = os.path.splitext(self.img_path)[0] + '_rote' +'.JPG'
            out_img.save(new_name,"JPEG")
        except Exception as err:
             print (err)   
             
    def Filter_img(self):
        try:
            img = self.get_image()
            out_img = img.filter(ImageFilter.BLUR)
            new_name = os.path.splitext(self.img_path)[0] + '_blur' +'.JPG'
            out_img.save(new_name,"JPEG")
        except Exception as err:
             print (err)   
        
    def turnBW_img(self):
        try:
            img = self.get_image()
            out_img = img.convert('1')           
            new_name = os.path.splitext(self.img_path)[0] + '_BW' +'.JPG'
            out_img.save(new_name,"JPEG")
        except Exception as err:
             print (err)  
        
                 
    
 
