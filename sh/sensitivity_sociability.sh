#!/bin/bash

#how to run
#qsub ~/research/AutomatAnts/code/run_model.sh 

cd

module load Python/3.10.4-GCCcore-11.3.0

. ~/research/AntsEnv/bin/activate

# relative density
PEAK=3

for p in $(LC_NUMERIC=C seq 0.1 0.1 1)
do
    # awk to calculate beta shapes
    params=$(awk -v p="$p" -v peak="$PEAK" 'BEGIN { printf "%.2f %.2f", 1 + (peak - 1) * p, 1 + (peak - 1) * (1 - p) }')
    
    # get values
    a_clean=$(echo $params | cut -d' ' -f1)
    b_clean=$(echo $params | cut -d' ' -f2)

    # echo "Running: Progress=$p -> Alpha=$a_clean, Beta=$b_clean"
    
    # sociability
    for epsilon in $(LC_NUMERIC=C seq 0.1 0.1 1)
    do

        # deterministic experiments
        python3 ~/research/task_switch/run_cluster.py --directory  ~/research/CHAPTER4/results_simulations/sensitivity_sociability/det/ --filename det_resistance_${p}_sociability_${epsilon} --social_feedbacks both -n 100 -p "rho=1;epsilon=${epsilon}" -g "100,B,${a_clean},${b_clean}"

        # stochastic experiments
        python3 ~/research/task_switch/run_cluster.py --directory  ~/research/CHAPTER4/results_simulations/sensitivity_sociability/sto/ --filename sto1_resistance_${p}_sociability_${epsilon} --social_feedbacks both -n 100 -p "rho=1;epsilon=${epsilon}" -g "100,B,${a_clean},${b_clean}" -t "tl:(10,13);(8,17)"
        python3 ~/research/task_switch/run_cluster.py --directory  ~/research/CHAPTER4/results_simulations/sensitivity_sociability/sto/ --filename sto2_resistance_${p}_sociability_${epsilon} --social_feedbacks both -n 100 -p "rho=1;epsilon=${epsilon}" -g "100,B,${a_clean},${b_clean}" -t "tl:(9,42);(11,8)"
        python3 ~/research/task_switch/run_cluster.py --directory  ~/research/CHAPTER4/results_simulations/sensitivity_sociability/sto/ --filename sto3_resistance_${p}_sociability_${epsilon} --social_feedbacks both -n 100 -p "rho=1;epsilon=${epsilon}" -g "100,B,${a_clean},${b_clean}" -t "tl:(12,29);(10,27)"
        python3 ~/research/task_switch/run_cluster.py --directory  ~/research/CHAPTER4/results_simulations/sensitivity_sociability/sto/ --filename sto4_resistance_${p}_sociability_${epsilon} --social_feedbacks both -n 100 -p "rho=1;epsilon=${epsilon}" -g "100,B,${a_clean},${b_clean}" -t "tl:(8,43);(5,14)"
        python3 ~/research/task_switch/run_cluster.py --directory  ~/research/CHAPTER4/results_simulations/sensitivity_sociability/sto/ --filename sto5_resistance_${p}_sociability_${epsilon} --social_feedbacks both -n 100 -p "rho=1;epsilon=${epsilon}" -g "100,B,${a_clean},${b_clean}" -t "tl:(9,18);(3,32)"
        python3 ~/research/task_switch/run_cluster.py --directory  ~/research/CHAPTER4/results_simulations/sensitivity_sociability/sto/ --filename sto6_resistance_${p}_sociability_${epsilon} --social_feedbacks both -n 100 -p "rho=1;epsilon=${epsilon}" -g "100,B,${a_clean},${b_clean}" -t "tl:(10,45);(6,23)"
        python3 ~/research/task_switch/run_cluster.py --directory  ~/research/CHAPTER4/results_simulations/sensitivity_sociability/sto/ --filename sto7_resistance_${p}_sociability_${epsilon} --social_feedbacks both -n 100 -p "rho=1;epsilon=${epsilon}" -g "100,B,${a_clean},${b_clean}" -t "tl:(4,35);(5,20)"
        python3 ~/research/task_switch/run_cluster.py --directory  ~/research/CHAPTER4/results_simulations/sensitivity_sociability/sto/ --filename sto8_resistance_${p}_sociability_${epsilon} --social_feedbacks both -n 100 -p "rho=1;epsilon=${epsilon}" -g "100,B,${a_clean},${b_clean}" -t "tl:(13,12);(11,12)"
        python3 ~/research/task_switch/run_cluster.py --directory  ~/research/CHAPTER4/results_simulations/sensitivity_sociability/sto/ --filename sto9_resistance_${p}_sociability_${epsilon} --social_feedbacks both -n 100 -p "rho=1;epsilon=${epsilon}" -g "100,B,${a_clean},${b_clean}" -t "tl:(13,22);(7,12)"

        # random placements
        python3 ~/research/task_switch/run_cluster.py --directory  ~/research/CHAPTER4/results_simulations/sensitivity_sociability/rand/ --filename rand1_resistance_${p}_sociability_${epsilon} --social_feedbacks both -n 100 -p "rho=1;epsilon=${epsilon}" -g "100,B,${a_clean},${b_clean}" -t "rand:(8,24);(9,1);(13,7);(4,8);(1,4);(5,43);(10,10);(11,36);(9,13);(4,38);(1,30);(6,35)"
        python3 ~/research/task_switch/run_cluster.py --directory  ~/research/CHAPTER4/results_simulations/sensitivity_sociability/rand/ --filename rand2_resistance_${p}_sociability_${epsilon} --social_feedbacks both -n 100 -p "rho=1;epsilon=${epsilon}" -g "100,B,${a_clean},${b_clean}" -t "rand:(10,26);(1,1);(4,5);(7,5);(0,16);(7,13);(1,10);(11,45);(2,42);(11,27);(9,43);(11,34)"
        python3 ~/research/task_switch/run_cluster.py --directory  ~/research/CHAPTER4/results_simulations/sensitivity_sociability/rand/ --filename rand3_resistance_${p}_sociability_${epsilon} --social_feedbacks both -n 100 -p "rho=1;epsilon=${epsilon}" -g "100,B,${a_clean},${b_clean}" -t "rand:(11,41);(5,41);(1,16);(12,0);(5,16);(12,20);(0,18);(8,35);(9,25);(4,37);(11,0);(5,7)"


    done
done