# Train CNN on MNIST with batch job
- Batch job: https://docs.abci.ai/ja/job-execution/#batch-jobs
- MNIST example repository: https://github.com/pytorch/examples/tree/master/mnist
## Clone repository and check the environment setting in interacive job
```
# At your local machine
~ ssh abci
# now you are at interactive node
[ABCI_USER_ID@es ~]$ git clone https://github.com/pytorch/examples pytorch_examples
# enter interactive job to check the environment setting
[ABCI_USER_ID@es ~]$ qrsh -g $GROUP_ID -l rt_G.small=1
# make env for training
[ABCI_USER_ID@g**** ~]$ module load gcc/9.3.0 python/3.8/3.8.7 cuda/11.0/11.0.3 cudnn/8.2/8.2.0 nccl/2.8/2.8.4-1 gdrcopy/2.0
[ABCI_USER_ID@g**** ~]$ python3 -m venv ~/mnist_env
[ABCI_USER_ID@g**** ~]$ source ~/mnist_env/bin/activate
(mnist_env) [ABCI_USER_ID@g**** ~]$ pip install torch==1.8.0+cu111 torchvision==0.9.0+cu111 torchaudio==0.8.0 -f https://download.pytorch.org/whl/torch_stable.html
# check if gpu is enabled
(mnist_env) [ABCI_USER_ID@g**** ~]$ python -c "import torch; print(torch.cuda.is_available())"
True
(mnist_env) [ABCI_USER_ID@g**** ~]$ cd pytorch_examples/mnist
# install libraries needed to run main.py
(mnist_env) [ABCI_USER_ID@g**** mnist]$ pip install requests
# download MNIST data
(mnist_env) [ABCI_USER_ID@g**** mnist]$ wget www.di.ens.fr/~lelarge/MNIST.tar.gz
(mnist_env) [ABCI_USER_ID@g**** mnist]$ tar -zxvf MNIST.tar.gz -C ../data
# run main.py and save trained model
(mnist_env) [ABCI_USER_ID@g**** mnist]$ python main.py --save-model
```
Now, you checked main.py successfully ran.

## Write shell script for batch job
write following shell script in ~/pytorch_examples/mnist/mnist.sh  
More details about job-execution-options: https://docs.abci.ai/ja/job-execution/#job-execution-options
```
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
cd ~/pytorch_examples/mnist
# run main.py
python main.py --save-model
```
## Execute batch job from interactive node([ABCI_USER_ID@es ~])
```
# execute job
[ABCI_USER_ID@es ~]$ qsub -g $GROUP_ID ~/pytorch_examples/mnist/mnist.sh
Your job {job-ID} ("mnist.sh") has been submitted
# check status
[ABCI_USER_ID@es ~]$ qstat
job-ID     prior   name       user         state submit/start at     queue                          jclass                         slots ja-task-ID
------------------------------------------------------------------------------------------------------------------------------------------------
   {job-ID} 0.25586 mnist.sh   {ABCI_USER_ID}   r     05/21/2021 15:11:02 gpu@g****                                                        10
```
More details about job status: https://docs.abci.ai/ja/job-execution/#show-the-status-of-batch-jobs
