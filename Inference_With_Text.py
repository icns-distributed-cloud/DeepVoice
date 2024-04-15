from IPython.display import Audio
from scipy.io.wavfile import write as write_wav
import os
from bark.api import generate_audio
from bark.generation import SAMPLE_RATE, preload_models, codec_decode, generate_coarse, generate_fine, generate_text_semantic
import Config_Infer
config = Config_Infer.Inference_config()

###########################################
############################# Get arguments
###########################################
import argparse

def argparser ():
  # 1. Parser 생성
  parser = argparse.ArgumentParser(description='Parser example')
  parser.add_argument('-n', '--name', type=str, default = config.experiment_name, help='Name of model')

  return parser.parse_args()

args = argparser()
rvc_name = args.name
print('rvc_name:', rvc_name)


semantic_path = "semantic_output/pytorch_model.bin" # set to None if you don't want to use finetuned semantic
coarse_path = "coarse_output/pytorch_model.bin" # set to None if you don't want to use finetuned coarse
fine_path = "fine_output/pytorch_model.bin" # set to None if you don't want to use finetuned fine
use_rvc = True # Set to False to use bark without RVC
rvc_path = f"/content/Mangio-RVC-Fork/weights/{rvc_name}.pth"
index_path = f"/content/Mangio-RVC-Fork/logs/{rvc_name}/added_IVF256_Flat_nprobe_1_{rvc_name}_v2.index"
device="cuda:0"
is_half=True

# download and load all models
#if (not os.path.isdir(semantic_path) and os.path.isdir(coarse_path) and os.path.isdir(fine_path)):
preload_models(
    text_use_gpu=True,
    text_use_small=False,
    text_model_path=semantic_path,
    coarse_use_gpu=True,
    coarse_use_small=False,
    coarse_model_path=coarse_path,
    fine_use_gpu=True,
    fine_use_small=False,
    fine_model_path=fine_path,
    codec_use_gpu=True,
    force_reload=False,
    path="models"
)

if use_rvc:
    from rvc_infer import get_vc, vc_single
    get_vc(rvc_path, device, is_half)

    
# simple generation
text_prompt = config.text_prompt
voice_name = "speaker_0" # use your custom voice name here if you have on

infer_data_path = '/content/dataset_Infer'
if not os.path.isdir(infer_data_path):
    os.makedirs(infer_data_path, exist_ok=True)

filepath = os.path.join(infer_data_path, "audio.wav")
audio_array = generate_audio(text_prompt, history_prompt=voice_name, text_temp=0.7, waveform_temp=0.7)
write_wav(filepath, SAMPLE_RATE, audio_array)

if use_rvc:
    index_rate = 0.75
    f0up_key = -6
    filter_radius = 3
    rms_mix_rate = 0.25
    protect = 0.33
    resample_sr = SAMPLE_RATE
    f0method = "harvest" #harvest or pm
    try:
        audio_array = vc_single(0,filepath,f0up_key,None,f0method,index_path,index_rate, filter_radius=filter_radius, resample_sr=resample_sr, rms_mix_rate=rms_mix_rate, protect=protect)
    except:
        audio_array = vc_single(0,filepath,f0up_key,None,'pm',index_path,index_rate, filter_radius=filter_radius, resample_sr=resample_sr, rms_mix_rate=rms_mix_rate, protect=protect)

    
    os.makedirs(infer_data_path, exist_ok=True)
    save_data_path = os.path.join(infer_data_path, f'{rvc_name}.wav')
    write_wav(save_data_path, SAMPLE_RATE, audio_array)