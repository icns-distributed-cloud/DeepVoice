import os

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

#def train_model_function(model_name, file_path):
    # 1. Isolate_vocal.py
    # 2. Voice_Model_Training.py
    # 3. 