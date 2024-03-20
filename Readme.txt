# Generate Docker Container
sudo docker container run -itd --gpus all --ipc=host --name deepAudio python:3.8
sudo docker exec -it deepAudio /bin/bash

# Setting Environment
apt update
cd root

git clone https://github.com/icns-distributed-cloud/DeepVoice.git
cd DeepVoice
bash setup

# Isolate Vocal
python Isolate_vocal.py

# Train Model
python Train_model.py