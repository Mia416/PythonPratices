'''
Created on Mar 21, 2017

@author: chenz
'''

from PIL import ImageFont, ImageDraw ,ImageFilter
from PIL import Image
import random 
import math, string 


number = 5

def gene_text():
    
    source = list(string.ascii_letters)
    for index in range(0,10):
        source.append(str(index))
    return ''.join(random.sample(source,number))

def gene_code():
    size = (255, 255)
    bgColor = (255, 255, 255)
    width,height = size #宽和高
    fontPath = 'd:\OpenSans-Bold.ttf'
    bgColor = (255, 255, 255,110)
    fontSize = 60    
    font = ImageFont.truetype(fontPath,fontSize)
    image = Image.new('RGB',(width,height),bgColor) #创建图片
    
    draw = ImageDraw.Draw(image)  #创建画笔
    text = gene_text() #生成字符串
    print (text)
    font_width, font_height = (100,100)
    #draw.text(((width - font_width) / number, (height - font_height) / number),text) #填充字符串
    draw.text((10,10),text,font=font,fill=(248,248,255)) #填充字符串
    draw.text((10,100),text,font=font,fill=(248,248,10)) #填充字符串
     
    gene_line(draw,80,80)
    image = image.transform((width+20,height+10), Image.AFFINE, (1,-0.3,0,-0.1,1,0),Image.BILINEAR)  #创建扭曲
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE) #滤镜，边界加强
    image.save('idencode.png') #保存验证码图片
    
def gene_line(draw,width,height):
        begin = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([begin, end])
        
