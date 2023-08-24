# !/bin/bash

dir="C:\Users\Public\ouput\m=5"

python merge_results.py -d $dir -a "uniform,atlucb" -r 100 -T 500 -t prop_of_success 

python plot.py -d $dir -a "uniform,atlucb" -s 500 -t prop_of_success -o $dir/out.png 