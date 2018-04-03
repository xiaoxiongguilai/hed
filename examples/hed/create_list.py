# -*- coding: utf-8 -*-

import os

if __name__ == '__main__':
    data_path = './idcard_data_20180403/'
    gt_path = './idcard_gt_20180403/'
    img_list = []
    files = os.listdir(data_path)
    for file in files:
        if file.endswith('jpg'):
            img_list.append(file)
    print("Total ",len(img_list)," images")

    of = open("train_pair.lst","w+")
    for img_name in img_list:
        of.write(data_path + img_name + " " + gt_path + img_name + "\n")
    of.close()
