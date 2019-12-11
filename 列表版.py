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
            a=img.format
            b=img.mode
            c=img.size
            msg1="图像格式:",a,"图像模式:",b,"图像大小:",c
            title1="图像信息"
            button1="继续"
            easygui.msgbox(msg1,title1,button1)
            print(img.format)		 
            print(img.mode)
            print(img.size) 
elif answer=="调整图片尺寸":
             # 调整尺寸
            img_resize = img.resize((400,400))
            img_resize.save("testpin_resize.jpg")
            msg2=""
            title2="图片展示"
            button2="继续"
            image2='D:/ptonhy/testpin_resize.jpg'
            easygui.msgbox(msg2,title2,button2,image2)
elif answer=="45°旋转图片":
            # 旋转
            img_rotate = img.rotate(45)         
            img_rotate.save("testpin_rotate.jpg")
            msg3=""
            title3="图片展示"
            button3="继续"
            image3='D:/ptonhy/testpin_rotate.jpg'
            easygui.msgbox(msg3,title3,button3,image3)
elif answer=="图片转为灰色":
            # 灰度处理
            om=img.convert('L')				
            om.save('testpin_gray.jpg')
            msg4=""
            title4="图片展示"
            button4="继续"
            image4='D:/ptonhy/testpin_gray.jpg'
            easygui.msgbox(msg4,title4,button4,image4)
elif answer=="显示图片轮廓":
            # 图片的轮廓
            om = img.filter(ImageFilter.CONTOUR)		
            om.save('testpin_contour.jpg')
            msg5=""
            title5="图片展示"
            button5="继续"
            image5='D:/ptonhy/testpin_contour.jpg'
            easygui.msgbox(msg5,title5,button5,image5)
elif answer=="对比度10倍数":
            # 对比度为初始的10倍
            om = ImageEnhance.Contrast(img).enhance(20)		
            om.save('testpin_encontrast.jpg')
            msg6=""
            title6="图片展示"
            button6="继续"
            image6='D:/ptonhy/testpin_encontrast.jpg'
            easygui.msgbox(msg6,title6,button6,image6)
elif answer=="模糊处理图片":
           #将图片模糊处理
           om = img.filter(ImageFilter.BLUR)       
           om.save('testpin_vague.jpg')
           msg7=""
           title7="图片展示"
           button7="继续"
           image7='D:/ptonhy/testpin_vague.jpg'
           easygui.msgbox(msg7,title7,button7,image7)
elif  answer=="上下左右颠倒":
           #将图片上下颠倒
           om = img.transpose(Image.FLIP_LEFT_RIGHT)  
           om.save('testpin_flipL&R.jpg')
           #将图片左右颠倒
           om = img.transpose(Image.FLIP_TOP_BOTTOM)  
           om.save('testpin_flipT&B.jpg')
           msg8=""
           title8="图片展示"
           button8="继续"
           image8='D:/ptonhy/testpin_flipL&R.jpg'
           image82='D:/ptonhy/testpin_flipT&B.jpg'
           easygui.msgbox(msg8,title8,button8,image8)
           easygui.msgbox(msg8,title8,button8,image82)
           
elif answer=="图片添加文字":
            #在图片上添加文字
            ttfont = ImageFont.truetype("C:/windows/fonts/Arial.ttf",30)   
            draw = ImageDraw.Draw(img)
            draw.text((10,10),u'eve', fill=(0,0,0),font=ttfont)
            img.save("testpin_eve.jpg")
            msg9=""
            title9="图片展示"
            button9="继续"
            image9='D:/ptonhy/testpin_eve.jpg'
            easygui.msgbox(msg9,title9,button9,image9)