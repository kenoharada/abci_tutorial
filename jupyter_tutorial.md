# Use Jupyter notebook in interactive job

## Prerequisites
- [x] Create ABCI account
- [x] Log in ABCI user portal(https://portal.abci.ai/user/) and register public key
- [x] Edit ~/.ssh/config in your local machine like below
```
Host abci
     HostName es
     User {your_user_id}
     ProxyJump %r@as.abci.ai
     IdentityFile ~/.ssh/id_rsa
     ForwardX11 yes

Host as.abci.ai
     IdentityFile ~/.ssh/id_rsa
```
Now, you can access interactive node by following command  
`ssh abci`


## Set up your environment
in interactive node([ABCI_USER_ID@es ~]$ )(where you are in after ssh abci)  
### Select GPU type (V100 or A100) and nums(Full, large or small)  
https://docs.abci.ai/ja/job-execution/#available-resource-types  
Here, we use V100, 1GPU(rt_G.small)  
`[ABCI_USER_ID@es ~]$ qrsh -g $GROUP_ID -l rt_G.small=1`  
Now, you are in interactive job, you can use gpu
### Set up python env
```
[ABCI_USER_ID@g**** ~]$ module load gcc/9.3.0 python/3.8/3.8.7 cuda/11.0/11.0.3 cudnn/8.2/8.2.0 nccl/2.8/2.8.4-1 gdrcopy/2.0
[ABCI_USER_ID@g**** ~]$ python3 -m venv ~/jupyter_env
[ABCI_USER_ID@g**** ~]$ source ~/jupyter_env/bin/activate
(jupyter_env) [ABCI_USER_ID@g**** ~]$ pip install jupyter torch==1.8.0+cu111 torchvision==0.9.0+cu111 torchaudio==0.8.0 -f https://download.pytorch.org/whl/torch_stable.html
```

- [Environment Modules](https://docs.abci.ai/ja/environment-modules/)
- [Available modules related to gpu](https://docs.abci.ai/ja/gpu/)

## Access jupyter running in interacive job's node(g****) from your local browser
in interactive job  
```
[ABCI_USER_ID@g**** ~]$ jupyter notebook --ip=`hostname` --port=8888 --no-browser

[C 01:51:13.436 NotebookApp]

    To access the notebook, open this file in a browser:
        file:///home/{USER_ID}/.local/share/jupyter/runtime/nbserver-140189-open.html
    Or copy and paste one of these URLs:
        http://{g****}.abci.local:8888/?token={token}
     or http://127.0.0.1:8888/?token={token}
```

Open new local terminal window  
`ssh -i ~/.ssh/id_rsa -L 10022:es:22 -l $ABCI_USER_ID as.abci.ai`  
Open another new local terminal window  
`ssh -N -L 8888:{g****}:8888 -l $ABCI_USER_ID -i ~/.ssh/id_rsa -p 10022 localhost`  
{g****} is your interactive job's node, so it changes every time  

Finally you can access  
http://127.0.0.1:8888/?token={token}

Exit
```
[ABCI_USER_ID@g*** ~]$ exit
logout
[ABCI_USER_ID@es1 ~]$
```
## Tips
You can also run jupyter in interacive node([ABCI_USER_ID@es ~])  

You can upload files to abci  
`scp {your_file_at_local_machine} abci:`
## Reference
https://docs.abci.ai/ja/tips/jupyter-notebook/
