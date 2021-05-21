# Hyperparameter search using wandb sweep function
- Sweep: https://docs.wandb.ai/guides/sweeps
## Prerequisites
Following this step: https://github.com/wandb/examples/tree/master/examples/pytorch/pytorch-cnn-fashion
You set configuration of sweep in dashboard, and get sweeep agent
Here is my configuration  
```
program: main.py
method: grid
metric:
  goal: maximize
  name: best_acc
parameters:
  test-batch-size:
    value: 1000
  log-interval:
    value: 100
  batch-size:
    values: [16, 32, 64, 128]
  epochs:
    value: 14
  gamma:
    values: [0.7, 0.8, 0.9, 0.95, 0.99]
  seed:
    values: [1, 2, 3, 4, 5, 6, 7]
  lr:
    values: [0.0001, 0.001, 0.01, 0.1, 1.0]
```
CAUTION
I fixed test_batch_size to test-batch-size, log_interval to log-interval, batch_size to batch-size, removed check
It is necessary to run wandb agent

## Write shell script for batch job in multi_sweep.sh
```
#!/bin/bash

#$ -l rt_G.large=1
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
# wandb agent
pids=()
CUDA_VISIBLE_DEVICES=0 wandb agent {SWEEP_ID} &
pids[$!]=$!
CUDA_VISIBLE_DEVICES=1 wandb agent {SWEEP_ID} &
pids[$!]=$!
CUDA_VISIBLE_DEVICES=2 wandb agent {SWEEP_ID} &
pids[$!]=$!
CUDA_VISIBLE_DEVICES=3 wandb agent {SWEEP_ID} &
pids[$!]=$!
wait ${pids[@]}
deactivate
```

## Run experiment and check results
```
[ABCI_USER_ID@es ~]$ qsub -g $GROUP_ID ~/abci_tutorial/multi_gpu/multi_sweep.sh
```
Now, you can monitor your results at https://wandb.ai/{WANDB_USER_NAME}/SimpleNet-mnist/sweeps

