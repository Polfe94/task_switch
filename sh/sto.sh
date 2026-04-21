#!/bin/bash

#how to run
#qsub ~/research/AutomatAnts/code/run_model.sh 

cd

export PATH=/home/soft/python-3.9.5/bin:$PATH
export LD_LIBRARY_PATH=/home/soft/python-3.9.5/bin/$LD_LIBRARY_PATH

. ~/research/automatenv/bin/activate
python3 ~/research/AutomatAnts/code/Heterogeneity/run_cluster.py --directory ~/research/AutomatAnts/results/2024/hetero_model/default/ --filename sto1 -n 100 -p "rho=1;epsilon=1" -t "tl:(10,13);(8,17)"
python3 ~/research/AutomatAnts/code/Heterogeneity/run_cluster.py --directory ~/research/AutomatAnts/results/2024/hetero_model/default/ --filename sto2 -n 100 -p "rho=1;epsilon=1" -t "tl:(9,42);(11,8)"
python3 ~/research/AutomatAnts/code/Heterogeneity/run_cluster.py --directory ~/research/AutomatAnts/results/2024/hetero_model/default/ --filename sto3 -n 100 -p "rho=1;epsilon=1" -t "tl:(12,29);(10,27)"
python3 ~/research/AutomatAnts/code/Heterogeneity/run_cluster.py --directory ~/research/AutomatAnts/results/2024/hetero_model/default/ --filename sto4 -n 100 -p "rho=1;epsilon=1" -t "tl:(8,43);(5,14)"
python3 ~/research/AutomatAnts/code/Heterogeneity/run_cluster.py --directory ~/research/AutomatAnts/results/2024/hetero_model/default/ --filename sto5 -n 100 -p "rho=1;epsilon=1" -t "tl:(9,18);(3,32)"
python3 ~/research/AutomatAnts/code/Heterogeneity/run_cluster.py --directory ~/research/AutomatAnts/results/2024/hetero_model/default/ --filename sto6 -n 100 -p "rho=1;epsilon=1" -t "tl:(10,45);(6,23)"
python3 ~/research/AutomatAnts/code/Heterogeneity/run_cluster.py --directory ~/research/AutomatAnts/results/2024/hetero_model/default/ --filename sto7 -n 100 -p "rho=1;epsilon=1" -t "tl:(4,35);(5,20)"
python3 ~/research/AutomatAnts/code/Heterogeneity/run_cluster.py --directory ~/research/AutomatAnts/results/2024/hetero_model/default/ --filename sto8 -n 100 -p "rho=1;epsilon=1" -t "tl:(13,12);(11,12)"
python3 ~/research/AutomatAnts/code/Heterogeneity/run_cluster.py --directory ~/research/AutomatAnts/results/2024/hetero_model/default/ --filename sto9 -n 100 -p "rho=1;epsilon=1" -t "tl:(13,22);(7,12)"
