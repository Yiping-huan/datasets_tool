# -!- coding: utf-8 -!-
from PIL import Image
import os
import os.path
import numpy as np
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import time

start = time.time()
n = 0
# 指明被遍历的文件夹
rootdir = r'D:\Datasets\sc_normal\output\labels\test'  #lables文件夹
for parent, dirnames, filenames in os.walk(rootdir):
    # 遍历每一张图片
    for filename in filenames:
        # print('parent is :' + parent)
        # print('filename is :' + filename)
        currentPath = os.path.join(parent, filename)  # 目前图片的地址
        label_number = filename[:-4]  # 图片去掉.txt后的名字
        print("the label name is:" + filename)
        # print('the full name of the file is :' + currentPath)

        # 读取图片

        # print (img.format, img.size, img.mode)
        # img.show()
        img_path = r'D:\Datasets\sc_normal\output\images\test'  #图片文件存放的文件夹地址
        img_file = os.listdir(img_path)  # 将xml文件存放在xml_file列表里面
        if label_number + '.jpg' in img_file:  # 如果图片有对应的xml文件则跳过
            pass
        else:
            print(currentPath)
            n += 1
            os.remove(currentPath)  # 没有对应的xml文件则删除

end = time.time()
print("Execution Time:", end - start)
print("删除的labels数为：", n)
