apt update

echo "install torch"
pip3 install torch torchvision torchaudio

echo "git clone RVC2"
git clone https://github.com/kalomaze/externalcolabcode.git /content/Retrieval-based-Voice-Conversion-WebUI/utils

echo "setting environments"
pip install fastapi==0.88.0
cd /content/Retrieval-based-Voice-Conversion-WebUI
mkdir csvdb 
wget https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/rmvpe.pt -P /content/Retrieval-based-Voice-Conversion-WebUI
wget https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/hubert_base.pt -P /content/Retrieval-based-Voice-Conversion-WebUI
python install_settings.py
pip install -q stftpitchshift==1.5.1
pip install gradio==3.34.0
pip install tensorboard
pip install encodec
pip install funcy
pip install transformers

echo "load files"
python load_files.py

echo "Preprocess data"
python preprocess_data.py

echo "Extract features"
pip install torchcrepe
python extract_f0_print.py /content/Retrieval-based-Voice-Conversion-WebUI/logs/HUH_TEST3 1 rmvpe 64
python extract_feature_print.py cuda 1 0 0 /content/Retrieval-based-Voice-Conversion-WebUI/logs/HUH_TEST3 v2

echo "Training"
pthon train_nsf_sim_cache_sid_load_pretrain.py -e HUH_TEST3 -sr 48k -f0 1 -bs 8 -g 0 -te 3000 -se 100   -l 0 -c 0 -sw 0 -v v2 -li 76
#python train_nsf_sim_cache_sid_load_pretrain.py -e HUH_TEST3 -sr 48k -f0 1 -bs 8 -g 0-2 -te 300 -se 100   -l 0 -c 0 -sw 0 -v v2 -li 11