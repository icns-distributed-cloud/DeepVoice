import torch
import json

class Isolate_Vocals_config:
    def __init__(self):
        self.input_path = '/content/VocalRemover5-COLAB_arch/tracks'
        self.pretrained_model = "HP2-4BAND-3090_4band_arch-500m_1.pth"
        self.convertAll = True #if input_path is start http = False / else True
        self.window_size =  512
        self.parameter = "Auto detect"
        self.high_end_process = 'mirroring'
        self.aggressiveness = '0.3'
        self.postprocess = False
        self.threshold = 0.2
        self.nn_architecture = 'Auto detect'
        self.gpu = torch.cuda.is_available()
        self.deepExtraction = False
        self.isVocal = False
        self.suppress = True
        self.output_image = False
        self.tta = True
        self.useCustomArguments = False
        self.CustomArguments = "-h"
        self.download = False
        self.export_as_mp3 = False

        self.data_augmentation_speedup = True
        self.data_augmentation_slowdown = True


class Voice_Model_Training_config:
    def __init__(self):
        with open("/root/DeepVoice/Common_Config.json", "r") as f:
            data = json.load(f)
        self.experiment_name = data['experiment_name']
        self.dataset = data['dataset']
        self.pretrain_type = data['pretrain_type']
        self.path_to_training_folder = data['path_to_training_folder']
        self.model_architecture = data['model_architecture']
        self.target_sample_rate = data['target_sample_rate']
        self.cpu_threads = data['cpu_threads']
        self.speaker_id = data['speaker_id']
        self.pitch_extraction_algorithm = data['pitch_extraction_algorithm']
        self.crepe_hop_length = data['crepe_hop_length']
        self.pitch_guidance = data['pitch_guidance']
        self.save_frequency = data['save_frequency']
        self.total_epochs = data['total_epochs']
        self.batch_size = data['batch_size']
        self.save_only_latest_ckpt = data['save_only_latest_ckpt']
        self.cache_all_training_sets = data['cache_all_training_sets']
        self.save_small_final_model = data['save_small_final_model']
        self.use_manual_stepToEpoch = data['use_manual_stepToEpoch']
        self.manual_stepToEpoch = data['manual_stepToEpoch']