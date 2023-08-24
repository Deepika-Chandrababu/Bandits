#!/bin/bash

dir="C:\Users\Public\ouput\m=3"

for r in {1..100}
do
   python run_atlucb.py -s $r -t 250 -m 3 -e "agri{ }" > $dir/atlucb.$r.csv
   python postprocess.py -m 3 -e "agri{ }" -c $dir/atlucb.$r.csv -s prop_of_success > "$dir/atlucb-$r.prop_of_success"
  
done
