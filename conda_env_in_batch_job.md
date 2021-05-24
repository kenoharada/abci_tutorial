# Use conda env in batch job
Reference: https://qiita.com/h1sat0r1/items/24d4a6f4405e23096347

## Write like this in shell script
```
#!/bin/bash

#$ -l rt_M.small=1
#$ -l h_rt=72:00:00
#$ -j y
#$ -m e
#$ -cwd

## >>> conda init >>>

__conda_setup="$(CONDA_REPORT_ERRORS=false '$HOME/anaconda3/bin/conda' shell.bash hook 2> /dev/null)"

if [ $? -eq 0 ]; then
    \eval "$__conda_setup"
else
    if [ -f "$HOME/anaconda3/etc/profile.d/conda.sh" ]; then
        . "$HOME/anaconda3/etc/profile.d/conda.sh"
        CONDA_CHANGEPS1=false conda activate base
    else
        \export PATH="$PATH:$HOME/anaconda3/bin"
    fi
fi
unset __conda_setup
## <<< conda init <<<
conda activate tts
# move to the directory
cd ~/tts/tts/data
# CAUTION: you have to re-install library installled by pip
pip install spleeter
# run main.py
python main.py
```
