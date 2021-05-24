# Use Docker image with singularity
Reference  
https://docs.abci.ai/ja/containers/

## Write Dockerfile
Select nvcr version from 
https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes/rel_21-05.html#rel_21-05

```
FROM nvcr.io/nvidia/pytorch:20.09-py3
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    cmake \
    curl \
    git \
    graphviz \
    less \
    libbz2-dev \
    libffi-dev \
    liblzma-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libreadline-dev \
    libsqlite3-dev \
    libssl-dev \
    llvm \
    make \
    openssh-client \
    python-openssl \
    tk-dev \
    tmux \
    unzip \
    vim \
    wget \
    xz-utils \
    zip \
    zlib1g-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip setuptools

ENV HOME /root
WORKDIR $HOME
RUN pip install pyopenjtalk spleeter jupyter wandb
```

## Build image
```
$ docker build -t {YOUR_DOCKERHUB_ACCOUNT}/{DOCKER_IMAGE_NAME} .
# for example
$ docker build -t kenoharada/abci .
```

## Register the image in DockerHub
You have to make your account in [DockerHub](https://hub.docker.com/)
```
$ docker push {YOUR_DOCKERHUB_ACCOUNT}/{DOCKER_IMAGE_NAME}
# for example
$ docker push kenoharada/abci:latest
```
## Use docker image in DockerHub with Singularity
```
[ABCI_USER_ID@es ~]$ qrsh -g $GROUP_ID -l rt_G.small=1
[ABCI_USER_ID@g**** ~]$ module load singularitypro
[ABCI_USER_ID@g**** ~]$ singularity run --nv docker://{YOUR_DOCKERHUB_ACCOUNT}/{DOCKER_IMAGE_NAME}:{tag}
# for example
[ABCI_USER_ID@g**** ~]$ SINGULARITY_TMPDIR=$SGE_LOCALDIR singularity run --nv docker://kenoharada/abci
```
