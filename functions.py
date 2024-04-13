import os
import json
import shutil

def ModelInfoResponse():
    all_model_list = os.listdir('/content/rvcDisconnected')
    exist_model_list = []
    weights_path = '/content/Mangio-RVC-Fork/weights'
    for model in all_model_list:
        print(os.path.join(weights_path, model+'.pth'))
        if os.path.isfile(os.path.join(weights_path, model+'.pth')):
            exist_model_list.append(model)
    print(exist_model_list)
    return exist_model_list

def train_model_function(model_name):
    # 1. Isolate_vocal.py
    print('start Isolate_Vocals.py')
    os.system('python Isolate_Vocals.py')

    # 2. Voice_Model_Training.py
    print('start Voice_Model_Training.py')
    os.system('python Voice_Model_Training.py -n {}'.format(model_name))
    
def Inference_with_Text(model_name, text):
    # 1. Config에 텍스트 저장
    with open("/root/DeepVoice/Common_Config.json", "r") as f:
        data = json.load(f)

    data['text_prompt'] = text
    
    with open("/root/DeepVoice/Common_Config.json", "w") as f:
        json.dump(data, f)


    # 2. 추론 코드 시작
    os.system('python Inference_With_Text.py -n {}'.format(model_name))
    return os.path.join('/content/dataset_Infer', f'{model_name}.wav')
    # 3. 음성 저장 경로 반환

def remove(model_name):
    # 1. 모델 pth 삭제
    if os.path.isfile(os.path.join('/content/Mangio-RVC-Fork/weights', model_name+'.pth')):
        print(os.path.join('/content/Mangio-RVC-Fork/weights', model_name+'.pth'), 'delete')
        os.remove(os.path.join('/content/Mangio-RVC-Fork/weights', model_name+'.pth'))
    
    # 2. 모델 weight 삭제
    if os.path.isdir(os.path.join('/content/rvcDisconnected', model_name)):
        print(os.path.join('/content/rvcDisconnected', model_name), 'delete')
        shutil.rmtree(os.path.join('/content/rvcDisconnected', model_name))

    # 3. dataset_Infer 정리
    if os.path.isfile(os.path.join('/content/dataset_Infer', model_name+'.wav')):
        print(os.path.join('/content/dataset_Infer', model_name+'.wav'), 'delete')
        os.remove(os.path.join('/content/dataset_Infer', model_name+'.wav'))
        
    # 4. logs 정리
    if os.path.isdir(os.path.join('/content/Mangio-RVC-Fork/logs', model_name)):
        print(os.path.join('/content/Mangio-RVC-Fork/logs', model_name), 'delete')
        shutil.rmtree(os.path.join('/content/Mangio-RVC-Fork/logs', model_name))