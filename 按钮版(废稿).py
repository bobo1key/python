# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:22:05 2019

@author: bobo1key
"""
import easygui
from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageEnhance
msg0=""
title0="图片展示"
button0="继续"
image0='D:/ptonhy/testpin.jpg'
easygui.msgbox(msg0,title0,button0,image0)
answer="0"
msg = '                   请选择一项内容'
choices = ['输出图片信息','调整图片尺寸',"45°旋转图片","图片转为灰色",\
           "显示图片轮廓","对比度10倍数","模糊处理图片","上下左右颠倒",\
           "图片添加文字","啥也不做退出"]
title = '图像管理系统'
image1=''
answer = easygui.choicebox(msg,title,choices)
img = Image.open("D:/ptonhy/testpin.jpg")
if answer=="输出图片信息":
            # 输出图片基本信息
            print(img.format)		 
            print(img.mode)
            print(img.size) 
elif answer=="调整图片尺寸":
             # 调整尺寸
            img_resize = img.resize((512,512))
            img_resize.save("testpin_resize.jpg")
elif answer=="45°旋转图片":
            # 旋转
            img_rotate = img.rotate(45)         
            img_rotate.save("testpin_rotate.jpg")
elif answer=="图片转为灰色":
            # 灰度处理
            om=img.convert('L')				
            om.save('testpin_gray.jpg')
elif answer=="显示图片轮廓":
            # 图片的轮廓
            om = img.filter(ImageFilter.CONTOUR)		
            om.save('testpin_contour.jpg')
elif answer=="对比度10倍数":
            # 对比度为初始的10倍
            om = ImageEnhance.Contrast(img).enhance(20)		
            om.save('testpin_encontrast.jpg')
elif answer=="模糊处理图片":
           #将图片模糊处理
           om = img.filter(ImageFilter.BLUR)       
           om.save('testpin_vague.jpg')
elif  answer=="上下左右颠倒":
           #将图片上下颠倒
           om = img.transpose(Image.FLIP_LEFT_RIGHT)  
           om.save('testpin_flipL&R.jpg')
           #将图片左右颠倒
           om = img.transpose(Image.FLIP_TOP_BOTTOM)  
           om.save('testpin_flipT&B.jpg')
elif answer=="图片添加文字":
            #在图片上添加文字
            ttfont = ImageFont.truetype("C:/windows/fonts/Arial.ttf",80)   
            draw = ImageDraw.Draw(img)
            draw.text((10,10),u'eve', fill=(0,0,0),font=ttfont)
            img.save("testpin_eve.jpg")