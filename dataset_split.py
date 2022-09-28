# coding = utf-8


"""
input：
1.img_path 数据集图片地址
2.label_path 数据集标签地址（.txt格式）
3.划分比例（0到1） split_rate
output：
--dataset
    --images
        --train
        --val
    --labels
       --train
       --val
"""
import os
import random
import shutil


def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]  # 后缀要换成自己的


def move_labels(dest_dir, path):
    label_list = get_imlist(dest_dir + f'/images/{path}')
    for names in label_list:
        name = names.split('\\')[-1:][0]
        name = name.split('.')[0]
        label = name + '.txt'
        if os.path.exists(f'{label_path}/{label}'):
            shutil.copy(f'{label_path}/{label}', dest_dir + f'/labels/{path}')
        else:
            print(f'{label} is not exists')


def main(src_path):
    dest_dir = output_path  # 这个文件夹需要提前建好
    img_list = get_imlist(src_path)
    random.shuffle(img_list)
    print(img_list)
    length1 = int(len(img_list) * split_rate)  # 这个可以修改划分比例
    length2 = int(len(img_list) * split_rate2)
    os.makedirs(dest_dir + '/images/train')
    os.makedirs(dest_dir + '/images/val')
    os.makedirs(dest_dir + '/images/test')
    os.makedirs(dest_dir + '/labels/train')
    os.makedirs(dest_dir + '/labels/val')
    os.makedirs(dest_dir + '/labels/test')

    for f in img_list[:length1]:
        shutil.copy(f, dest_dir + '/images/train')
        print(f + 'train')
    for f in img_list[length1:length1+length2]:
        shutil.copy(f, dest_dir + '/images/val')
        print(f + 'val')
    for f in img_list[length1+length2:]:
        shutil.copy(f, dest_dir + '/images/test')
        print(f + 'test')
    # 移动对应的标签到对应位置

    move_labels(dest_dir, 'train')
    move_labels(dest_dir, 'val')
    move_labels(dest_dir, 'test')
    print(f'finished')


if __name__ == '__main__':
    path_dataset = 'D:\smoking-calling\img_bk_train\smocal_data'
    img_path = path_dataset + '/images'
    label_path = path_dataset + '/labels'

    split_rate = 0.9
    split_rate2 = 0.05

    output_path = r'D:\smoking-calling\img_bk_train\smocal_data\output'

    if not os.path.exists(output_path):
        os.makedirs(output_path)
    main(img_path)


    D:\smoking-calling\img_bk_train\calling_data\output\images\train
    D:\smoking-calling\img_bk_train\HR_train_data\images\train