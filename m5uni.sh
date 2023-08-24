#!/bin/bash
dir="C:\Users\Public\ouput\m=5"

for r in {36..100}
do
   
   python run_uniform.py -s $r -t 500 -m 5 -e "agri{ }" > $dir/uniform.$r.csv
   python postprocess.py -m 5 -e "agri{ }" -c $dir/uniform.$r.csv -s prop_of_success > "$dir/uniform-$r.prop_of_success"
   
done
