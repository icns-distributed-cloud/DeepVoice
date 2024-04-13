# main.py
from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from typing import List
import schemas  # schemas.py 파일에서 정의한 모델을 import
import functions
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse

import os

app = FastAPI()

# 임시로 데이터를 저장할 딕셔너리
data = {
    "models": ['test'],
    "model_name": None,
    "recordings": [],
    "text_info": None
}

# 0. 모델 리스트 받기
@app.get("/models/")
async def get_models():
    return schemas.ModelInfoResponse(models=functions.ModelInfoResponse())  

# 1. 모델 훈련 이름 정보 받기 & 2. 녹음 파일 받기 (20개) 3. 모델 훈련 시작하기
@app.post("/train_model/")
async def train_model(audios: List[UploadFile] = File(...), model_name: str = Form(...)):  
    model_name = model_name
    audios = audios
    if len(audios) < 1:
        raise HTTPException(status_code=400, detail="Minimun recordings limit exceeded")
    

    for audio_file in audios:
        file_path = f"/content/VocalRemover5-COLAB_arch/tracks/{audio_file.filename}"
        with open(file_path, "wb") as audio_writer:
            contents = await audio_file.read()
            audio_writer.write(contents)
        
        print(os.listdir('/content/VocalRemover5-COLAB_arch/tracks'))

    functions.train_model_function(model_name)
    return {
        "message": f"Model training completed for {model_name} with {len(audios)} audio files",
        "data" : {
            "train_done" : True
        }
    }

# 4. 텍스트 정보 받기 6. 모델 추론 결과 제공
@app.post("/text_info")
async def text_info(model_name: str = Form(...), text: str = Form(...)):
    if not text:
        raise HTTPException(status_code=400, detail="No text provided")

    inference_data_path = functions.Inference_with_Text(model_name, text)
    filename = inference_data_path.split('/')[-1]
    return FileResponse(inference_data_path, media_type='audio/wav', filename=filename)

# 7. 데이터 초기화
@app.post("/remove_data")
async def reset_data(models: str = Form(...)):
    if not models:
        raise HTTPException(status_code=400, detail="Missing required fields in reset data request")

    
    if models:
        functions.remove(models)
    
    return {"message": "All {}data removed".format(models)}

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
    uvicorn.run(app, host="0.0.0.0", port=8001)
