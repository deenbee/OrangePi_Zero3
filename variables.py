import pygame
import wiringpi
import os
import json

class Samples:
    
    select_bank = 0
    
    # Lista de archivos WAV
    wav_files = [
        "samples/808/Kick Basic.wav", "samples/808/Kick Long.wav",
        "samples/808/Kick Mid.wav", "samples/808/Kick Short.wav",
        "samples/808/Snare Mid.wav", "samples/808/Snare Low.wav",
        "samples/808/Snare High.wav", "samples/808/Snare Bright.wav",
        "samples/808/Rimshot.wav", "samples/808/Open Hat Short.wav",
        "samples/808/Open Hat Long.wav", "samples/808/Hihat.wav",
        "samples/808/Cymbal.wav", "samples/808/Cowbell.wav",
        "samples/808/Clap.wav", "samples/808/Conga Mid.wav",
        "samples/808/Conga Low.wav", "samples/808/Conga High.wav",
        "samples/808/Claves.wav", "samples/808/Maracas.wav",
        "samples/808/Tom Mid.wav", "samples/808/Tom Low.wav",
        "samples/808/Tom High.wav", "samples/808/808.wav"
    ]
    
    T909 = [
        "samples/909/bd01.wav", "samples/909/bd02.wav",
        "samples/909/bd03.wav", "samples/909/bd04.wav",
        "samples/909/bd05.wav", "samples/909/bd06.wav",
        "samples/909/cp01.wav", "samples/909/cr01.wav",
        "samples/909/cp02.wav", "samples/909/cr02.wav",
        "samples/909/rd01.wav", "samples/909/rs01.wav",
        "samples/909/hh01.wav", "samples/909/rs02.wav",
        "samples/909/rd03.wav", "samples/909/hh02.wav",
        "samples/909/rd04.wav", "samples/909/mt03.wav",
        "samples/909/sd01.wav", "samples/909/oh01.wav",
        "samples/909/sd02.wav", "samples/909/oh02.wav",
        "samples/909/mt01.wav", "samples/909/mt02.wav"
    ]
    
    C64 = [
        "samples/c64/kick1.wav", "samples/c64/clap.wav",
        "samples/c64/kick2.wav", "samples/c64/cowbell.wav",
        "samples/c64/kick3.wav", "samples/c64/hihat1.wav",
        "samples/c64/kick4.wav", "samples/c64/hihat2.wav",
        "samples/c64/kick5.wav", "samples/c64/snare1.wav",
        "samples/c64/kick6.wav", "samples/c64/snare2.wav",
        "samples/c64/kick7.wav", "samples/c64/snare3.wav",
        "samples/c64/kick8.wav", "samples/c64/snare4.wav",
        "samples/808/Tom High.wav", "samples/c64/snare6.wav",
        "samples/808/Conga Low.wav", "samples/c64/snare7.wav",
        "samples/808/Hihat.wav", "samples/c64/snare8.wav",
        "samples/c64/tom1.wav", "samples/c64/tom2.wav", 
    ]
    
    
    

class Audio:
    freq = 44100
    bits = -16
    chan = 2
    buffer = 512

class Color:
    g = (150, 150, 150)
    r = (255, 0, 0) 
    w = (255, 255, 255)
    bg = (0, 0, 0)
    gn = (0, 0, 0)

class Patt:
    mtx_p = [[[0] * 16 for _ in range(24)] for _ in range(32)]  # Matrix de 32 patterns

        
# Configuración del secuenciador
class Seq:
    tempo = 100
    tpo_txt = str(tempo)  # tempo_text
    m_vol = 1.0           # master_volume: Volumen master
    m_opn = False # menu_open
    playing = False
    lstime = 0 # last_step_time
    s_idx = 0 # step_index
    tpt = 1    # total_patt : Total numbers of patterns (máximo 32)
    apt = 1   # Active pattern number (1 a 32)   
    act_chs = {} # Active channels
    s_mem = 1 # Selected_memory
    channel_volumes = [1.0] * 24  # Volumen por canal (0.0 a 1.0)
    pan_volumes = [0.0] * 24      # Panorama por canal (-1.0 a 1.0)
    


# Inicializar Pygame y wiringpi
pygame.init()
pygame.mixer.pre_init(Audio.freq, Audio.bits, Audio.chan, Audio.buffer)  # 44.1kHz, 16-bit, estéreo, buffer 512
pygame.mixer.init()
pygame.mixer.set_num_channels(24)
wiringpi.wiringPiSetup()

# Configuración de la ventana
WINDOW_WIDTH = 830
WINDOW_HEIGHT = 850

# Configurar ventana
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Bottle Beats 0.2.0 Alpha")

# Fuentes
font = pygame.font.SysFont("Arial", 16)
font_small = pygame.font.SysFont("Arial", 12)


# Pines GPIO para 24 LEDs
led_pins = [0, 7, 14, 15, 9, 6, 12, 10, 8, 4, 11, 2] * 2
for pin in led_pins:
    wiringpi.pinMode(pin, 1)

# Pre-cargar sonidos y configurar volúmenes/paneo
channels = [pygame.mixer.Channel(i) for i in range(24)]
sound_objects = [pygame.mixer.Sound(file) for file in Samples.wav_files] # Default Sound Bank
sound_objects_2 = [pygame.mixer.Sound(file) for file in Samples.T909]
sound_objects_3 = [pygame.mixer.Sound(file) for file in Samples.C64]
sound_objects_4 = [pygame.mixer.Sound(file) for file in Samples.wav_files]





## - CONSTANTES - ##

# Configuración de los pasos, volúmenes y paneo
STEP_WIDTH = 20
STEP_HEIGHT = 25
STEP_MARGIN = 5
COLOR_SIZE = 20
CHANNEL_HEIGHT = STEP_HEIGHT + STEP_MARGIN
VOL_WIDTH = 40
VOL_HEIGHT = 20
PAN_WIDTH = 60  # Definimos ancho para el paneo
PAN_HEIGHT = 20
DRAW_X = 150  # Posición inicial x de steps

# Botones y cuadros

PLAY_BUTTON = pygame.Rect(10, WINDOW_HEIGHT - 61, 80, 40)
STOP_BUTTON = pygame.Rect(100, WINDOW_HEIGHT - 61, 80, 40)
TEMPO_BOX = pygame.Rect(200, WINDOW_HEIGHT - 61, 117, 40)
MASTER_VOL_BOX = pygame.Rect(320, WINDOW_HEIGHT - 61, 130, 40)
PATTERN_BOX = pygame.Rect(700, 152, 95, 40)
PATTERN_TOTAL = pygame.Rect(700, 190, 95, 40)
SETTING_BOX = pygame.Rect(PATTERN_TOTAL.x, PATTERN_TOTAL.y + 150, 95, 60)


# Botones load/save y menú desplegable para las memorias
SAVE_BUTTON = pygame.Rect(690, WINDOW_HEIGHT - 61, 80, 40)
LOAD_BUTTON = pygame.Rect(690, WINDOW_HEIGHT - 105, 80, 40)
MENU_BUTTON = pygame.Rect(690, WINDOW_HEIGHT - 155, 100, 40)

COLOR_BTN1 = pygame.Rect(700, 32, COLOR_SIZE, COLOR_SIZE)
COLOR_BTN2 = pygame.Rect(730, 32, COLOR_SIZE, COLOR_SIZE)
COLOR_BTN3 = pygame.Rect(760, 32, COLOR_SIZE, COLOR_SIZE)
COLOR_BTN4 = pygame.Rect(700, 62, COLOR_SIZE, COLOR_SIZE)
COLOR_BTN5 = pygame.Rect(730, 62, COLOR_SIZE, COLOR_SIZE)
COLOR_BTN6 = pygame.Rect(760, 62, COLOR_SIZE, COLOR_SIZE)

BNK_BUTTON = pygame.Rect(690, WINDOW_HEIGHT - 205, 95, 40)

T1V1 = (700, 160 - 30) # Vertices
T1V2 = (730, 170 - 30) # Vertices
T1V3 = (730, 150 - 30) # Vertices
TRI_BL = [T1V1, T1V2, T1V3]  # Triangulo izquierdo
T2V1 = (790, 160 - 30) # Vertices
T2V2 = (760, 170 - 30) # Vertices
T2V3 = (760, 150 - 30) # Vertices
TRI_BR = [T2V1, T2V2, T2V3] # Triangulo derecho

RF_T1 = pygame.Rect(700, 160 - 60, 40, 45) # Botones de ref. triangulo 1
RF_T2 = pygame.Rect(760, 160 - 60, 40, 45) # Botones de ref. triangulo 2


MENU_WIDTH = 100
MENU_ITEM_HEIGHT = 30
MENU_ITEMS = 10  # 10 memorias (1 a 10)

# Variable para el nombre del preset
current_preset = "default_preset"

LED_DURATION = 50