#!/bin/bash

rm -rf idcard_data
rm -rf idcard_gt

mkdir idcard_data
mkdir idcard_gt

python test.py 2>&1| tee test.log &


