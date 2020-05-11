FROM ubuntu:18.04

# Install the required development packages
RUN apt-get update && apt-get install -y \
    cmake \
    gcc \
    g++ \
    git \
    curl \
    vim \
    python3 \
    python3-pip \
    protobuf-compiler \
    libprotoc-dev \
 && rm -rf /var/lib/apt/lists/*

# Set up to use python3 and pip3 as default for python and pip
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1
RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

# Upgrade pip
RUN pip install --upgrade pip

