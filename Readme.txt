# Generate Docker Container
sudo docker container run -itd  --gpus '"device=0, 1"' --ipc=host --name deepAudio python:3.8
sudo docker exec -it deepAudio /bin/bash

# Setting Environment
apt update
cd root

git clone https://github.com/icns-distributed-cloud/DeepVoice.git
cd DeepVoice
bash setup.sh

# Isolate Vocal
python Isolate_Vocals.py

# Train Model
python Voice_Model_Training.py