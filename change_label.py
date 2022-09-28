import os
import numpy as np


def get_lablist(path):
    return [os.path.join(path, f) for f in os.listdir(path)]


label_path = r"D:\smoking-calling\img_bk_train\labels\smo-cal_label"
label_path_new = r"D:\smoking-calling\img_bk_train\labels\smo-cal_label_new"
label_list = os.listdir(label_path)
count = 0


for label_file in label_list:
    if label_file.endswith(".txt"):
        with open(os.path.join(label_path, label_file), "r", encoding="utf-8") as f1, open(
                os.path.join(label_path_new, label_file), "w", encoding="utf-8") as f2:
            for line in f1:
                items = line.split(" ")
                if items[0] == "0":
                    items[0] = "9"
                elif items[0] == "1":
                    items[0] = "10"
                line = " ".join(items)
                f2.write(line)



