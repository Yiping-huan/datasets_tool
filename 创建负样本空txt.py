# coding=UTF-8
import os


def main():


    imagepath = r"D:\Datasets\sc\normal" #图片目录
    filelist = os.listdir(imagepath)
    total_num = len(filelist)
    print(total_num)
    i = 0
    for file_name in filelist:
        txt_path = r"D:\Datasets\sc\labels" #生成的txt文件夹路径
        if file_name.endswith('.jpg'):
            image_name = file_name[:-4]
            full_path = txt_path + '\\' + image_name + '.txt'
            open(full_path, 'w')
            print('make' + '' + full_path)
            i = i + 1
 
if __name__ == '__main__':
    main()
    print('finish')
