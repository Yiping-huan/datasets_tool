# coding = utf-8
import os

def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path)]


def readwrite(path, goal_file):
    img_list = get_imlist(path)
    for f in img_list:
        f = f.replace('\\', '/')
        file = open(goal_file, mode='a')
        file.write(f + '\n')
    file.close()


if __name__ == '__main__':

    train_img_path = './images/train'
    val_img_path = './images/val'
    test_img_path = './images/test'

    train_file_path = './train2017.txt'
    val_file_path = './val2017.txt'
    test_file_path = './test2017.txt'

    readwrite(train_img_path, train_file_path)
    readwrite(val_img_path, val_file_path)
    readwrite(test_img_path, test_file_path)



