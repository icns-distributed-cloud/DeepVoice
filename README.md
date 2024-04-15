# Deepvoice_ExperienceCenter
## 프로젝트 소개
딥보이스 체험장 웹사이트 백엔드 제작

## 기술 스택
<img src="https://github.com/yuri0329/Deepvoice_ExperienceCenter/assets/104057240/aeb61790-1584-4b4e-9628-9c118d9ee557.png" width="50%" height="50%"/>

## Getting Started (Installation)
## Generate Docker Container
```bash
sudo docker container run -itd  --gpus '"device=1, 2"' --ipc=host --name deepAudio -v /home/sun_server/jhk/WorldITShow:/content -p 10000:8080 -p 8000:8000 python:3.8
sudo docker exec -it deepAudio /bin/bash
cd root
```

## Setting Environment
apt update
cd root

````
pip install "fastapi[all]"
pip install "uvicorn[standard]"
````

## 실행 명령어
````
uvicorn main:app --reload --host 0.0.0.0
````

# Deepvoice_Model
```bash
git clone https://github.com/icns-distributed-cloud/DeepVoice.git
cd DeepVoice
bash setup.sh
```

## Isolate Vocal
```bash
python Isolate_Vocals.py
```

## Train Model
```bash
python Voice_Model_Training.py
```
