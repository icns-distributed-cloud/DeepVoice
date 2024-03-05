DATASET = "Huh_Ori_HP-KAROKEE-MSB2-3BAND-3090_arch-124m_Vocals_converted.zip"  #@param {type:"string"}


import os
import shutil
from glob import glob
import concurrent.futures
import subprocess

def sanitize_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            if filename == ".DS_Store" or filename.startswith("._") or not filename.endswith(('.wav', '.flac', '.mp3', '.ogg', '.m4a')):
                os.remove(file_path)
        elif os.path.isdir(file_path):
            sanitize_directory(file_path)

def convert_file(source_file, output_filename_converted):
    # Check if the input file is 16-bit
    probe_cmd = f'ffprobe -v error -select_streams a:0 -show_entries stream=sample_fmt -of default=noprint_wrappers=1:nokey=1 "{source_file}"'
    sample_format = subprocess.run(probe_cmd, shell=True, text=True, capture_output=True).stdout.strip()

    # Use appropriate ffmpeg command based on sample format
    if sample_format == 's16':
        # Export as 16-bit WAV
        cmd = f'ffmpeg -i "{source_file}" -c:a pcm_s16le "{output_filename_converted}"'
    else:
        # Export as 32-bit float WAV (default behavior)
        cmd = f'ffmpeg -i "{source_file}" -c:a pcm_f32le "{output_filename_converted}"'

    process = subprocess.run(cmd, shell=True)
    if process.returncode != 0:
        print(f'Failed to convert {source_file}. The file may be corrupt.')
    else:
        os.remove(source_file)

def convert_audio_files(source_dir, dest_dir):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for root, _, files in os.walk(source_dir):
            for filename in files:
                file_ext = os.path.splitext(filename)[1].lower()
                if file_ext in ['.wav', '.flac', '.mp3', '.ogg', '.m4a']:
                    source_file = os.path.join(root, filename)
                    output_filename = os.path.join(dest_dir, filename)
                    output_filename_converted = os.path.splitext(output_filename)[0] + '_converted.wav'
                    executor.submit(convert_file, source_file, output_filename_converted)

dataset_path = '/content/dataset/' + DATASET
final_directory = '/content/datasets'
temp_directory = '/content/temp_dataset'

try:
    if os.path.exists(final_directory):
        shutil.rmtree(final_directory)
        print("Dataset folder already found. Wiping clean for import operation...")
except Exception as e:
    print(f"Error in removing the final directory: {e}")

try:
    if not os.path.exists(dataset_path):
        raise Exception(f'There is no {DATASET} in {os.path.dirname(dataset_path)}')
except Exception as e:
    print(f"Error in verifying dataset: {e}")

try:
    os.makedirs(final_directory, exist_ok=True)
    os.makedirs(temp_directory, exist_ok=True)
except Exception as e:
    print(f"Error in creating directories: {e}")

try:
    # Unzip data into a temporary directory
    import zipfile
    with zipfile.ZipFile(dataset_path, 'r') as zip_ref:
        zip_ref.extractall(temp_directory)
    #!unzip -d {temp_directory} -B {dataset_path}
except Exception as e:
    print(f"Error in unzipping data: {e}")

try:
    # Sanitize temporary directory
    sanitize_directory(temp_directory)
except Exception as e:
    print(f"Error in sanitizing directory: {e}")

try:
    # Convert audio files and move them to the final directory
    convert_audio_files(temp_directory, final_directory)
except Exception as e:
    print(f"Error in converting audio files: {e}")

try:
    # Clean up temp directory
    shutil.rmtree(temp_directory)
except Exception as e:
    print(f"Error in removing temp directory: {e}")

#try:
#    # Rename files if needed
#    !rename 's/(\w+)\.(\w+)~(\d*)/$1_$3.$2/' {final_directory}/*.*~*
#except Exception as e:
#    print(f"Error in renaming files: {e}")

print('Dataset imported. You can now copy the path of the dataset folder to the training path.')
