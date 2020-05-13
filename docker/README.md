## Prerequisites

Follow the instructions in [Docker Docs](https://docs.docker.com/engine/installation/) to install docker for your machine.

## Prepare the image

Switch to `docker` directory here and run (don't miss the dot at the end of the command!)

```
sudo docker build -t onnx-dev-env .
```

After the build is complete you will have `onnx-dev-env` image that you can use for your work with ONNX in this repository

## Start up a new container using the image

In this example, `onnx-dojo-lab` is the name of the new container being spawned up

```
sudo docker run -idt --name onnx-dojo-lab onnx-dev-env
```

## Get into the newly created container to start with your lab exercise

Here we start the bash shell inside the container

```
sudo docker exec -it onnx-dojo-lab /bin/bash
```

Voila! Now you are ready to start with your lab exercises.
