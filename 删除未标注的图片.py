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
rootdir = r'D:\Datasets\No_SC_bustrain\HR_NoSC_data2\HR_NoSC_data2\images\train'
for parent, dirnames, filenames in os.walk(rootdir):
    # 遍历每一张图片
    for filename in filenames:
        # print('parent is :' + parent)
        # print('filename is :' + filename)
        currentPath = os.path.join(parent, filename)  # 目前图片的地址
        picture_number = filename[:-4]  # 图片去掉.png后的名字
        print("the picture name is:" + filename)
        # print('the full name of the file is :' + currentPath)

        # 读取图片

        # print (img.format, img.size, img.mode)
        # img.show()
        xml_path = r'D:\Datasets\No_SC_bustrain\HR_NoSC_data2\HR_NoSC_data2\labels\train'  # xml文件存放的文件夹地址
        xml_file = os.listdir(xml_path)  # 将xml文件存放在xml_file列表里面
        if picture_number + '.txt' in xml_file:  # 如果图片有对应的xml文件则跳过
            pass
        else:
            print(currentPath)
            n += 1
            os.remove(currentPath)  # 没有对应的xml文件则删除

end = time.time()
print("Execution Time:", end - start)
print("删除的照片数为：", n)
