# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 20:14:51 2019

@author: bobo1key
"""

#图片处理：
from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageEnhance
img = Image.open("D:/ptonhy/testpin.jpg")
def menu(): 
        print('\n\n        **********************')
        print('        *欢迎来到图像管理系统*')
        print('        **********************\n')
        print('**************************************')
        print('**********  1：输出图片信息  **********')
        print('**********  2：调整图片尺寸  **********')
        print('**********  3：45°旋转图片   **********')
        print('**********  4：图片转为灰色  **********')
        print('**********  5：显示图片轮廓  **********')
        print('**********  6：对比度10倍数  **********')
        print('**********  7：模糊处理图片  **********')
        print('**********  8：上下左右颠倒  **********')
        print('**********  9：图片添加文字  **********')
        print('**********  0：啥也不做退出  **********')
        print('***************************************')
        v=input('请输入对应的数字：')
        if v=="1":
            print(img.format)		 # 输出图片基本信息
            print(img.mode)
            print(img.size)
        elif v=="2":
            img_resize = img.resize((256,256)) # 调整尺寸
            img_resize.save("testpin_resize.jpg")
        elif v=="3":
            img_rotate = img.rotate(45)         # 旋转
            img_rotate.save("testpin_rotate.jpg")
        elif v=="4":
            om=img.convert('L')				# 灰度处理
            om.save('testpin_gray.jpg')
        elif v=="5":
            om = img.filter(ImageFilter.CONTOUR)		# 图片的轮廓
            om.save('testpin_contour.jpg')
        elif v=="6":
            om = ImageEnhance.Contrast(img).enhance(20)		# 对比度为初始的10倍
            om.save('testpin_encontrast.jpg')
        elif v=="7":
           om = img.filter(ImageFilter.BLUR)       #将图片模糊处理
           om.save('testpin_vague.jpg')
        elif  v=="8":
           om = img.transpose(Image.FLIP_LEFT_RIGHT)  #将图片上下颠倒
           om.save('testpin_flipL&R.jpg')
           om = img.transpose(Image.FLIP_TOP_BOTTOM)  #将图片左右颠倒
           om.save('testpin_flipT&B.jpg')
        elif v=="9":
            ttfont = ImageFont.truetype("C:/windows/fonts/Arial.ttf",80)  #在图片上添加文字；Arial是我电脑里fonts里第一个，不知道其他电脑有没有这个字体 
            draw = ImageDraw.Draw(img)
            draw.text((10,10),u'eve', fill=(0,0,0),font=ttfont)
            img.save("testpin_eve.jpg")

menu()
