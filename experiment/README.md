# Monitor experiment's result
## Prerequisites
- [x] Create an account of [weights and biases](https://wandb.ai/home)
- [x] Clone repository https://github.com/kenoharada/abci_tutorial.git
- [x] Install wandb
```
[ABCI_USER_ID@es2 ~]$ git clone https://github.com/kenoharada/abci_tutorial.git
[ABCI_USER_ID@es2 ~]$ module load gcc/9.3.0 python/3.8/3.8.7 cuda/11.0/11.0.3 cudnn/8.2/8.2.0 nccl/2.8/2.8.4-1 gdrcopy/2.0
[ABCI_USER_ID@es2 ~]$ source ~/mnist_env/bin/activate
(mnist_env) [ABCI_USER_ID@es2 ~]$ pip install wandb
(mnist_env) [ABCI_USER_ID@es2 ~]$ wandb login
wandb: You can find your API key in your browser here: https://wandb.ai/authorize
wandb: Paste an API key from your profile and hit enter:
wandb: Appending key for api.wandb.ai to your netrc file: /home/ABCI_USER_ID/.netrc
(mnist_env) [ABCI_USER_ID@es2 ~]$ export WANDB_API_KEY={YOUR_API_KEY} >> ~/.bashrc
(mnist_env) [ABCI_USER_ID@es2 ~]$ source ~/.bashrc
```
## Run experiment and check results
```
[ABCI_USER_ID@es ~]$ qsub -g $GROUP_ID ~/abci_tutorial/experiment/simple_exp.sh
```
Now, you can monitor your results at https://wandb.ai/{$WANDB_USER_NAME}/projects

## References
- weights and biases pytorch example: https://docs.wandb.ai/guides/integrations/pytorch