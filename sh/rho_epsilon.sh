#!/bin/bash

#how to run
#qsub ~/research/AutomatAnts/code/run_model.sh 

cd

module load Python/3.10.4-GCCcore-11.3.0

. ~/research/AntsEnv/bin/activate
for rho in $(seq 0.001 0.1 1.001)
do
    for epsilon in $(seq 0.001 0.1 1.001)
    do
        # python3 ~/research/AutomatAnts/code/Heterogeneity/run_cluster.py --directory ~/research/AutomatAnts/results/2024/hetero_model/rho_epsilon/ --filename rho_${rho/,/.}_epsilon_${epsilon/,/.} --social_feedbacks both -n 100 -p "rho=${rho/,/.};epsilon=${epsilon/,/.}"
        python3 ~/research/AutomatAnts/VERSIONS/vHeterogenous_Movement/run_cluster.py --directory ~/research/AutomatAnts/results/2025/rho_epsilon_with_tags/ --filename rho_${rho/,/.}_epsilon_${epsilon/,/.} --social_feedbacks both -n 100 -p "rho=${rho/,/.};epsilon=${epsilon/,/.}"

    done
done