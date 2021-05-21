#!/bin/bash

#$ -l rt_G.small=1
#$ -l h_rt=72:00:00
#$ -j y
#$ -m e
#$ -cwd

# initialize Environment Modules
source /etc/profile.d/modules.sh
# set up environment
module load gcc/9.3.0 python/3.8/3.8.7 cuda/11.0/11.0.3 cudnn/8.2/8.2.0 nccl/2.8/2.8.4-1 gdrcopy/2.0
source ~/mnist_env/bin/activate
# move to the directory
cd ~/abci_tutorial/multi_gpu
# run main.py
python main.py
