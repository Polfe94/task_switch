#!/bin/bash

#how to run
#qsub ~/research/AutomatAnts/code/run_model.sh 

cd

module load Python/3.10.4-GCCcore-11.3.0

. ~/research/AntsEnv/bin/activate
python3 ~/research/task_switch/run_cluster.py --directory ~/research/CHAPTER4/results_simulations/sto/ --filename sto1 -n 100 -p "rho=1;epsilon=1" -t "tl:(10,13);(8,17)"
python3 ~/research/task_switch/run_cluster.py --directory ~/research/CHAPTER4/results_simulations/sto/ --filename sto2 -n 100 -p "rho=1;epsilon=1" -t "tl:(9,42);(11,8)"
python3 ~/research/task_switch/run_cluster.py --directory ~/research/CHAPTER4/results_simulations/sto/ --filename sto3 -n 100 -p "rho=1;epsilon=1" -t "tl:(12,29);(10,27)"
python3 ~/research/task_switch/run_cluster.py --directory ~/research/CHAPTER4/results_simulations/sto/ --filename sto4 -n 100 -p "rho=1;epsilon=1" -t "tl:(8,43);(5,14)"
python3 ~/research/task_switch/run_cluster.py --directory ~/research/CHAPTER4/results_simulations/sto/ --filename sto5 -n 100 -p "rho=1;epsilon=1" -t "tl:(9,18);(3,32)"
python3 ~/research/task_switch/run_cluster.py --directory ~/research/CHAPTER4/results_simulations/sto/ --filename sto6 -n 100 -p "rho=1;epsilon=1" -t "tl:(10,45);(6,23)"
python3 ~/research/task_switch/run_cluster.py --directory ~/research/CHAPTER4/results_simulations/sto/ --filename sto7 -n 100 -p "rho=1;epsilon=1" -t "tl:(4,35);(5,20)"
python3 ~/research/task_switch/run_cluster.py --directory ~/research/CHAPTER4/results_simulations/sto/ --filename sto8 -n 100 -p "rho=1;epsilon=1" -t "tl:(13,12);(11,12)"
python3 ~/research/task_switch/run_cluster.py --directory ~/research/CHAPTER4/results_simulations/sto/ --filename sto9 -n 100 -p "rho=1;epsilon=1" -t "tl:(13,22);(7,12)"
