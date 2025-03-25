import json
import pygame
from config.variables import Audio, Color, Seq, Samples, Patt, channels


def load_settings():
        
    m_file = f"settings.json"
    try:
        with open(m_file, "r") as f:
            settings_data = json.load(f)
            Audio.freq = settings_data["Audio.freq"]
            Audio.bits = settings_data["Audio.bits"]
            Audio.chan = settings_data["Audio.chan"]
            Audio.buffer = settings_data["Audio.buffer"]
            Color.g = settings_data["Color.g"]
            Color.r = settings_data["Color.r"]
            Color.w = settings_data["Color.w"]
            Color.gn = settings_data["Color.gn"]
            Color.bg = settings_data["Color.bg"]
            print(f"Load settings ok")
    except FileNotFoundError:
            print(f"No find settings file")
            Audio.freq = 44100
            Audio.bits = -16
            Audio.chan = 2
            Audio.buffer = 512
            Color.g = (150, 150, 150)  # Color de botones
            Color.r = (255, 0, 0)  
            Color.w = (255, 255, 255) 
            Color.gn = (0, 255, 0)  
            Color.bg = (0, 0, 0)    
    except Exception as e:
            print(f"Error load settings file")
            Audio.freq = 44100
            Audio.bits = -16
            Audio.chan = 2
            Audio.buffer = 512
            Color.g = (150, 150, 150)  
            Color.r = (255, 0, 0) 
            Color.w = (255, 255, 255) 
            Color.gn = (0, 255, 0)   
            Color.bg = (0, 0, 0)

def save_settings():
        
    settings_data = {
        "Audio.freq": Audio.freq,
        "Audio.chan": Audio.chan,
        "Audio.buffer": Audio.buffer,
        "Audio.bits": Audio.bits,
        "Color.g": Color.g,
        "Color.r": Color.r,
        "Color.w": Color.w,
        "Color.gn": Color.gn,
        "Color.bg": Color.bg
    }
    m_file = f"settings.json"
    with open(m_file, "w") as f:
        json.dump(settings_data, f)
    print("Settings saved")    
    
def save_preset():
    #global Samples.wav_files, Patt.mtx_p
    try:
        preset_data = {
            "Patt.mtx_p": Patt.mtx_p,
            "Seq.apt": Seq.apt,
            "Seq.tpt": Seq.tpt,
            "Seq.patt_state": Seq.patt_state,
            "Samples.wav_files": Samples.wav_files,
            "Seq.channel_volumes": Seq.channel_volumes,
            "Seq.pan_volumes": Seq.pan_volumes,
            "Seq.m_vol": Seq.m_vol,
            "Seq.tempo": Seq.tempo,
            "Color.g": Color.g,
            "Color.r": Color.r,
            "Color.w": Color.w,
            "Color.gn": Color.gn,
            "Color.bg": Color.bg,
            "Samples.select_bank": Samples.select_bank
        }
        memory_file = f"presets/memory_{Seq.s_mem}.json"
        with open(memory_file, "w") as f:
            json.dump(preset_data, f)
        print(f"Preset guardado en memoria {Seq.s_mem} ({memory_file})")
    except FileNotFoundError:
            print(f"No se encontró un preset")
    except Exception as e:
            print(f"Error al cargar el preset")
    
def load_preset():
    #Seq.load_data_file()
        #global Patt.mtx_p, Samples.wav_files, channels, Seq.channel_volumes, Seq.pan_volumes    
    memory_file = f"presets/memory_{Seq.s_mem}.json"
    try:
        with open(memory_file, "r") as f:
            preset_data = json.load(f)
            Patt.mtx_p = preset_data["Patt.mtx_p"]
            Seq.apt = preset_data["Seq.apt"]
            Seq.tpt = preset_data["Seq.tpt"]
            Seq.patt_state = preset_data["Seq.patt_state"]
            Samples.wav_files = preset_data["Samples.wav_files"]
            Seq.channel_volumes = preset_data.get("Seq.channel_volumes", [1.0] * 24)
            Seq.pan_volumes = preset_data.get("Seq.pan_volumes", [0.0] * 24)
            Seq.m_vol = preset_data.get("Seq.m_vol", 1.0)
            Seq.tempo = preset_data["Seq.tempo"]
            Color.g = preset_data["Color.g"]
            Color.r = preset_data["Color.r"]
            Color.w = preset_data["Color.w"]
            Color.bg = preset_data["Color.bg"]
            Samples.select_bank = preset_data["Samples.select_bank"]
            
            Seq.tpo_txt = str(Seq.tempo)
                
            sound_objects = [pygame.mixer.Sound(file) for file in Samples.wav_files]
            for idx, sound in enumerate(sound_objects):
                sound.set_volume(Seq.channel_volumes[idx] * Seq.m_vol)
                channels[idx].set_volume((1 - Seq.pan_volumes[idx]) / 2, (1 + Seq.pan_volumes[idx]) / 2)

            print(f"Preset cargado desde memoria {Seq.s_mem} ({memory_file})")
    except FileNotFoundError:
            print(f"No se encontró un preset en la memoria {Seq.s_mem}. Se creará uno al guardar.")
    except Exception as e:
            print(f"Error al cargar el preset desde memoria {Seq.s_mem}: {e}")

    