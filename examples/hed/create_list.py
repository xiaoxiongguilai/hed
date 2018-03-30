# -*- coding: utf-8 -*-

if __name__ == '__main__':
    data_root = './idcard_gt_1100/'
    of = open("train_pair.lst","w+")
    with open(data_root+'image.lst') as f:
        test_lst = f.readlines()
    for i in range(0, len(test_lst)):
        image_name = test_lst[i].strip()
        of.write("idcard_data_1100/"+image_name+" "+"idcard_gt_1100/"+image_name+"\n")
    of.close()
