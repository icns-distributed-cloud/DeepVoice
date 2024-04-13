# main.py
from fastapi import FastAPI, File, UploadFile, HTTPException, Form, BackgroundTasks
from typing import List
import schemas  # schemas.py 파일에서 정의한 모델을 import
import functions
from fastapi.responses import HTMLResponse, FileResponse
import multiprocessing
import requests
import json
import os
import time

app = FastAPI()

# 임시로 데이터를 저장할 딕셔너리
data = {
    "models": ['test'],
    "model_name": None,
    "recordings": [],
    "text_info": None
}

with open("/root/DeepVoice/Common_Config.json", "r") as f:
            data = json.load(f)
local_address = data['local_address']

# 1. 모델 리스트 받기
@app.get("/models/")
async def get_models():
    return {
        "success" : 1,
        "data" : {
                "models":functions.ModelInfoResponse()
            },
        "message": "Return model list"
        }

# 2. 모델 훈련 이름 정보 받기 & 녹음 파일 받기 (20개) 모델 훈련 시작하기
@app.post("/train_model/")
async def train_model(audios: List[UploadFile] = File(...), model_name: str = Form(...), background_tasks: BackgroundTasks = None):
    if len(audios) < 1:
        raise HTTPException(status_code=400, detail="Minimun recordings limit exceeded")
    

    for audio_file in audios:
        file_path = f"/root/DeepVoice/tracks/{audio_file.filename}"
        with open(file_path, "wb") as audio_writer:
            contents = await audio_file.read()
            audio_writer.write(contents)
    
    print('Train Start')
    functions.train_model_function(model_name)
    send_model_to_local_server(model_name)
    print('Train end')

        #send_model_to_local_server(model_name)

    return {
        "success" : 1,
        "data" : {},
        "message": f"Model training start for {model_name} with {len(audios)} audio files",
    }

# 3. 텍스트 정보 받기 and 모델 추론 결과 제공
@app.post("/text_info")
async def text_info(model_name: str = Form(...), text: str = Form(...), gender: int = Form(...)):
    if not text:
        raise HTTPException(status_code=400, detail="No text provided")

    inference_data_path = functions.Inference_with_Text(model_name, text)
    filename = inference_data_path.split('/')[-1]
    return {
        "success" : 1,
        "data" : {
            "inference_data" : FileResponse(inference_data_path, media_type='audio/wav', filename=filename)
        },
        "message": f"Model training completed for {model_name} with {len(audios)} audio files",
    }

# 4. 데이터 초기화
@app.post("/remove_data")
async def reset_data(models: str = Form(...)):
    if not models:
        raise HTTPException(status_code=400, detail="Missing required fields in reset data request")

    
    if models:
        functions.remove(models)
    
    return {
        "success" : 1,
        "data" : {},
        "message": "All {}data removed".format(models),
    }


# 훈련된 모델 송싱
def send_model_to_local_server(model_name):
    pth_file_path = os.path.join('/content/Mangio-RVC-Fork/weights', model_name+'.pth')
    with open(pth_file_path, "rb") as f:
        pth_contents = f.read()

    weight_file_path = f"/content/rvcDisconnected/{model_name}"
    weight_file_path = os.path.join(weight_file_path, os.listdir(weight_file_path)[0])
    with open(weight_file_path, "rb") as f:
        weight_contents = f.read()

    data = {
        "pth" : pth_contents,
        "weight" : weight_contents,
        'model_name' : model_name
    }

    url = local_address+"/send_trained_model"
    response = requests.post(url, files=data)
    print(response)


# 5. 훈련된 모델 수신
@app.post("/send_trained_model")
async def reset_data(pth: UploadFile = Form(...), weight: UploadFile = Form(...), model_name: str = Form(...)):
    pth_file_path = os.path.join('/content/Mangio-RVC-Fork/weights', model_name+'.pth')
    with open(pth_file_path, "wb") as f:
        contents = await pth.read()
        f.write(contents)

    weight_file_path = f"/content/rvcDisconnected/{model_name}/added_IVF386_Flat_nprobe_1_{model_name}_v2.index"
    with open(file_path, "wb") as f:
        contents = await weight.read()
        f.write(contents)

    return {
        "success" : 1,
        "data" : {},
        "message": "Model received"
    }

@app.get("/")
async def main():
    content = """
    <body>
    <form action="/models/" enctype="multipart/form-data" method="get">
    <input type="submit">
    </form>
    <form action="/train_model/" enctype="multipart/form-data" method="post">
    <input name="audios" type="file" multiple>
    <input name="model_name" type="text">
    <input type="submit">
    </form>
    <form action="/text_info/" enctype="multipart/form-data" method="post">
    <input name="text" type="text">
    <input name="model_name" type="text">
    <input type="submit">
    </form>
    </form>
    <form action="/remove_data/" enctype="multipart/form-data" method="post">
    <input name="models" type="text">
    <input type="submit">
    </form>
    </body>
    """
    return HTMLResponse(content=content)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
