# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import matplotlib.cm as cm
import scipy.misc
#import Image
from PIL import Image
import scipy.io
import os


# Make sure that caffe is on the python path:
caffe_root = '../../'  # this file is expected to be in {caffe_root}/examples/hed/
#caffe_root = '../../../ocr_project_2018_02_07/ai-caffe/'  # this file is expected to be in {caffe_root}/examples/hed/
import sys
sys.path.insert(0, caffe_root + 'python')

import caffe

def plot_single_scale(scale_lst, size):
    pylab.rcParams['figure.figsize'] = size, size/2

    plt.figure()
    for i in range(0, len(scale_lst)):
        s=plt.subplot(1,5,i+1)
        plt.imshow(1-scale_lst[i], cmap = cm.Greys_r)
        s.set_xticklabels([])
        s.set_yticklabels([])
        s.yaxis.set_ticks_position('none')
        s.xaxis.set_ticks_position('none')
    plt.tight_layout()

if __name__ == '__main__':
    data_root = '../../data/FrontImages/'
    with open(data_root+'test.lst') as f:
        test_lst = f.readlines()
        print test_lst

    caffe.set_mode_gpu()
    caffe.set_device(1)

    model_root = './'
    net = caffe.Net(model_root+'deploy.prototxt', model_root+'hed_pretrained_bsds.caffemodel', caffe.TEST)

    #test_lst = [data_root+x.strip() for x in test_lst]
    #im_lst = []
    for i in range(0, len(test_lst)):
        img_path = data_root + test_lst[i].strip()
        #im = Image.open(test_lst[i])
        im = Image.open(img_path)
        (w, h) = im.size
        res_h = 800
        res_w = 800 * w / h
        im = im.resize((res_w, res_h))
        im.save("idcard_data/"+test_lst[i].strip())
        #print(im.size)
        in_ = np.array(im, dtype=np.float32)
        in_ = in_[:,:,::-1]
        in_ -= np.array((104.00698793,116.66876762,122.67891434))

        in_ = in_.transpose((2,0,1))
        net.blobs['data'].reshape(1, *in_.shape)
        net.blobs['data'].data[...] = in_
        #print in_
        net.forward()
        out1 = net.blobs['sigmoid-dsn1'].data[0][0,:,:]
        fuse = net.blobs['sigmoid-fuse'].data[0][0,:,:]
        #print fuse
        fuse = 255 - fuse * 255
        im = Image.fromarray(fuse)
        if im.mode != 'L':
            im = im.convert('L')
        print im
        im.save("idcard_gt/"+test_lst[i].strip())
        scale_lst = [fuse]
        #plot_single_scale(scale_lst, 30)
        print("forward ok")
