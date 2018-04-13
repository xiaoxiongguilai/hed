# -*- coding: utf-8 -*-

import os

TAG ='2018_04_03'

if __name__ == '__main__':
    data_path = 'idcard_data_' + TAG + '/'
    gt_path = 'idcard_gt_' + TAG + '/'
    img_list = []
    files = os.listdir(data_path)
    for file in files:
        if file.endswith('jpg'):
            img_list.append(file)
    print("Total ",len(img_list)," images")

    of = open("train_pair_" + TAG  + ".lst", "w+")
    for img_name in img_list:
        of.write(data_path + img_name + " " + gt_path + img_name + "\n")
    of.close()
