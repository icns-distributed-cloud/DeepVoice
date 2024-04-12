# Deepvoice_ExperienceCenter

## 프로젝트 소개
딥보이스 체험장 웹사이트 백엔드 제작

## 기술 스택
<img src="https://github.com/yuri0329/Deepvoice_ExperienceCenter/assets/104057240/aeb61790-1584-4b4e-9628-9c118d9ee557.png" width="50%" height="50%"/>

## Getting Started (Installation)
````
pip install "fastapi[all]"
pip install "uvicorn[standard]"
````

## 실행 명령어
````
uvicorn main:app --reload
````

# Deepvoice_Model
## Generate Docker Container
sudo docker container run -itd  --gpus '"device=0, 1"' --ipc=host --name deepAudio python:3.8
sudo docker exec -it deepAudio /bin/bash

## Setting Environment
apt update
cd root

git clone https://github.com/icns-distributed-cloud/DeepVoice.git
cd DeepVoice
bash setup.sh

## Isolate Vocal
python Isolate_Vocals.py

## Train Model
python Voice_Model_Training.py