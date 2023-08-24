#!/bin/bash
dir="C:\Users\Public\ouput\m=3"

for r in {1..100}
do
   
   python run_uniform.py -s $r -t 500 -m 3 -e "agri{ }" > $dir/uniform.$r.csv
   python postprocess.py -m 3 -e "agri{ }" -c $dir/uniform.$r.csv -s prop_of_success > "$dir/uniform-$r.prop_of_success"
   
done
