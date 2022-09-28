# coding=UTF-8
import os


class ImageRename():
    def __init__(self):
        self.path = 'D://smoking-calling//img_bk_train//labels//smo-cal_label//smoking_calling'

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)

        i = 0
        for item in filelist:
            if item.endswith('.txt'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), "SmoCal_"+'0' + format(str(i), '0>4s') + '.txt')
                os.rename(src, dst)
                print('converting %s to %s ...' % (src, dst))
                i = i + 1
        print('total %d to rename & converted %d txts' % (total_num, i))


if __name__ == '__main__':
    newname = ImageRename()
    newname.rename()