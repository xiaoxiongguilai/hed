#!/bin/bash
rm train.log -rf
rm training_data -rf

mkdir training_data

python solve.py 2>&1| tee train.log &
