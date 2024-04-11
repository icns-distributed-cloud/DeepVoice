# main.py
from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from typing import List
import schemas  # schemas.py 파일에서 정의한 모델을 import
import functions
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse

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
        file_path = f"/content/Mangio-RVC-Fork/tracks/{audio_file.filename}"
        with open(file_path, "wb") as audio_writer:
            audio_writer.write(audio_file.file.read())
            # train_result = train_model_function(model_name, file_path)

    return {"message": f"Model training completed for {model_name} with {len(audios)} audio files"}

        

# 4. 텍스트 정보 받기 6. 모델 추론 결과 제공
@app.post("/text_info")
async def text_info(text: str = Form(...)):
    if not text:
        raise HTTPException(status_code=400, detail="No text provided")

    data["text_info"] = text
    return {"message": "Text information received"}

# 5. 모델 추론하기 - 현기코드 제공예정

# 6. 모델 추론 결과 제공 엔드포인트
@app.get("/prediction")
async def get_prediction():
    #if data["text_info"] is None:
    #    return {"error": "No text information provided"}
    
    audio_file_path = "/content/Mangio-RVC-Fork/tracks/7번_HP2-4BAND-3090_4band_arch-500m_1_Vocals.wav"
    filename = audio_file_path.split('/')[-1]
    return FileResponse(audio_file_path, media_type='audio/wav', filename=filename)

# 7. 데이터 초기화
@app.post("/reset_data")
async def reset_data(models: List[str] = None, model_name: str = None, text: str = None):
    if not reset_data.models or not reset_data.model_name or not reset_data.text:
        raise HTTPException(status_code=400, detail="Missing required fields in reset data request")

    data["models"] = reset_data.models
    data["model_name"] = reset_data.model_name
    data["recordings"] = []
    data["text_info"] = reset_data.text
    return {"message": "All data reset"}

@app.get("/")
async def main():
    content = """
    <body>
    <form action="/files/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    <form action="/train_model/" enctype="multipart/form-data" method="post">
    <input name="audios" type="file" multiple>
    <input name="model_name" type="text">
    <input type="submit">
    </form>
    <form action="/text_info/" enctype="multipart/form-data" method="post">
    <input name="text" type="text">
    <input type="submit">
    </form>
    </body>
    """
    return HTMLResponse(content=content)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)