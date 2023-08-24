#!/bin/bash

dir="C:/Users/Public"

for r in {1..100}
do
   python run_atlucb.py -s $r -t 250 -m 2 -e "agri{ }" > $dir/atlucb.$r.csv
   python postprocess.py -m 2 -e "agri{ }" -c $dir/atlucb.$r.csv -s prop_of_success > "$dir/atlucb-$r.prop_of_success"
   python run_uniform.py -s $r -t 500 -m 2 -e "agri{ }" > $dir/uniform.$r.csv
   python postprocess.py -m 2 -e "agri{ }" -c $dir/uniform.$r.csv -s prop_of_success > "$dir/uniform-$r.prop_of_success"
done

python merge_results.py -d $dir -a "uniform,atlucb" -r 100 -T 500 -t prop_of_success 

python plot.py -d $dir -a "uniform,atlucb" -s 500 -t prop_of_success -o $dir/out.png 