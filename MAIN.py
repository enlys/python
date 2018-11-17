"""
opencv:R G B
       (253,254,255)
计算公式：0.299*R+0.587*R+0.114*B=灰度
(256 * 256 *  3)像素
  列    行  分量
R 256 * 256 *1
G 256 * 256 * 2
B 256 * 256 * 3

"""

from PIL import Image
import os
img=Image.open("13.jpg")
"""
img_mode=img.mode    #图像模式
print(img_mode)
img_size=img.size
print(img_size)
img_get=img.getpixel((0,0))
print(img_get)

"""
new=Image.new('L',img.size,255)
width,height=img.size
img.convert('L')
pen_size=3
color_diff=6

for i in range(pen_size+1,width-pen_size-1):
    for j in range(pen_size + 1, height - pen_size - 1):
        originalcolor=255
        lcolor=sum([img.getpixel((i - r, j)) for r in range(pen_size)])//pen_size
        rcolor=sum([img.getpixel((i+r,j))for r in range(pen_size)])//pen_size
        if abs(lcolor-rcolor)>color_diff:
            originalcolor-=(255-img.getpixel((i,j)))//2
            new.putpixel((i,j),originalcolor)

        acolor = sum([img.getpixel((i, j-r)) for r in range(pen_size)])//pen_size
        ccolor = sum([img.getpixel((i, j-r)) for r in range(pen_size)])//pen_size
        if abs(acolor - ccolor) > color_diff:
            originalcolor -= (255 - img.getpixel((i, j)))//2
            new.putpixel((i, j),originalcolor)



new.save('dsf.jpg')
os.system('dsf.jpg')