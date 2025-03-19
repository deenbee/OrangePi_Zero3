import pygame
import os
import wiringpi
import json
from config.variables import *
from .jsncodes import save_preset
from .jsncodes import load_preset


def play_sound_and_light(channel_idx):
    global channels
    """Reproduce un sonido y enciende su LED con volumen y panorama ajustados."""
    # Selector de banco de sonidos
    if Samples.select_bank == 0: 
        sound = sound_objects[channel_idx]
    if Samples.select_bank == 1:
        sound = sound_objects_2[channel_idx]
    if Samples.select_bank == 2:
        sound = sound_objects_3[channel_idx]    
    
    vol = Seq.channel_volumes[channel_idx] * Seq.m_vol
    sound.set_volume(vol)
    pin = led_pins[channel_idx]
    wiringpi.digitalWrite(pin, 1)
    left = (1 - Seq.pan_volumes[channel_idx]) / 2
    right = (1 + Seq.pan_volumes[channel_idx]) / 2
    channels[channel_idx].set_volume(left, right)
    channels[channel_idx].play(sound)
    return pygame.time.get_ticks() + LED_DURATION

def turn_off_led(channel_idx):
    """Apaga el LED de un canal."""
    pin = led_pins[channel_idx]
    wiringpi.digitalWrite(pin, 0)

def pattern_control():
    #global Patt.mtx_p
    
    print("Step actual:", Seq.s_idx)
    
    if Seq.s_idx >= 16 * Seq.tpt:
        Seq.s_idx = 0
        Seq.apt = 1
        patterns = [row[:] for row in Patt.mtx_p[Seq.apt - 1]] # Copia explicita para evitar sobrescritura
        print("Reset step:", Seq.s_idx, "and active patt:", Seq.apt)
    
    current_pattern_idx = (Seq.s_idx // 16) % Seq.tpt
    if current_pattern_idx >= 0 and current_pattern_idx < Seq.tpt:
        Seq.apt = current_pattern_idx + 1
        if Seq.apt != Seq.apt:
            Seq.apt = new_Seq.apt
            patterns = [row[:] for row in Patt.mtx_p[Seq.apt - 1]] # Copia explicita al cambiar pattern
            # Reiniciar Seq.s_idx al inicio del nuevo pattern            
            Seq.s_idx = (Seq.apt - 1) * 16
            print("Active PATT:", Seq.apt, "Patterns: ", patterns)    
                
                
def handle_input(pos):
    #global patterns, Patt.mtx_p
        
    if MENU_BUTTON.collidepoint(pos):
        Seq.m_opn = not Seq.m_opn
        return

    if Seq.m_opn:
        for i in range(MENU_ITEMS):
            menu_item_rect = pygame.Rect(MENU_BUTTON.x, MENU_BUTTON.y - (i + 1) * MENU_ITEM_HEIGHT, MENU_WIDTH, MENU_ITEM_HEIGHT)
            if menu_item_rect.collidepoint(pos):
                Seq.s_mem = i + 1
                Seq.m_opn = False
                print(f"Memoria seleccionada: {Seq.s_mem}")
                return
    
    for channel_idx in range(24): # Recorre la matrix de las patterns
        for step_idx in range(16):
            x = DRAW_X + step_idx * (STEP_WIDTH + STEP_MARGIN)
            y = 30 + channel_idx * CHANNEL_HEIGHT
            rect = pygame.Rect(x, y, STEP_WIDTH, STEP_HEIGHT)
            if rect.collidepoint(pos):
                #patterns[channel_idx][step_idx] = 1 - patterns[channel_idx][step_idx]
                Patt.mtx_p[Seq.apt - 1][channel_idx][step_idx] = 1 - Patt.mtx_p[Seq.apt - 1][channel_idx][step_idx] # Guarda los cambios en Patt.mtx_p
                for i in range(16):
                     print("Channel1 STEP ", i + 1,"Patt.mtx_p", Patt.mtx_p[0][0][i], " Pattern active: ", Seq.apt)
                   
        
        vol_x = DRAW_X + 16 * (STEP_WIDTH + STEP_MARGIN) + 10
        vol_y = 30 + channel_idx * CHANNEL_HEIGHT + (STEP_HEIGHT - VOL_HEIGHT) // 2
        vol_rect = pygame.Rect(vol_x, vol_y, VOL_WIDTH, VOL_HEIGHT)
        if vol_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                Seq.channel_volumes[channel_idx] = min(1.0, Seq.channel_volumes[channel_idx] + 0.05)
            elif pygame.mouse.get_pressed()[2]:
                Seq.channel_volumes[channel_idx] = max(0.0, Seq.channel_volumes[channel_idx] - 0.05)
        
        pan_x = vol_x + VOL_WIDTH + 10
        pan_rect = pygame.Rect(pan_x, vol_y, PAN_WIDTH, PAN_HEIGHT)
        if pan_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                Seq.pan_volumes[channel_idx] = min(1.0, Seq.pan_volumes[channel_idx] + 0.1)
            elif pygame.mouse.get_pressed()[2]:
                Seq.pan_volumes[channel_idx] = max(-1.0, Seq.pan_volumes[channel_idx] - 0.1)
    
    if COLOR_BTN1.collidepoint(pos):
        Color.bg = (0, 0, 0)
        Color.w = (255, 255, 255)
        Color.g = (150, 150, 150)
        Color.gn = (0, 255, 0)
        Color.r = (255, 0, 0)
        print("Color 1")
    if COLOR_BTN2.collidepoint(pos):
        Color.bg = (153, 255, 51)
        Color.w = (0, 0, 0)
        Color.g = (0, 0, 0)
        Color.gn = (255, 0, 0)
        Color.r = (255, 0, 0)
        print("Color 2")
    if COLOR_BTN3.collidepoint(pos):
        Color.bg = (210, 237, 255)
        Color.w = (0, 0, 0)
        Color.g = (110, 110, 110)
        Color.gn = (255, 0, 0)
        Color.r = (255, 255, 0)
        print("Color 3")
    if COLOR_BTN4.collidepoint(pos):
        Color.bg = (60, 60, 60)
        Color.w = (255, 255, 255)
        Color.g = (150, 150, 150)
        Color.gn = (0, 255, 0)
        Color.r = (255, 0, 0)
    if COLOR_BTN5.collidepoint(pos):
        Color.bg = (76, 0, 153)
        Color.w = (255, 255, 255)
        Color.g = (150, 150, 150)
        Color.gn = (255, 0, 0)
        Color.r = (255, 255, 0)
    if COLOR_BTN6.collidepoint(pos):
        Color.bg = (255, 229, 204)
        Color.w = (0, 0, 0)
        Color.g = (150, 150, 150)
        Color.gn = (0, 0, 0)
        Color.r = (0, 0, 0)
    
    if SAVE_BUTTON.collidepoint(pos):
        save_preset()
    if LOAD_BUTTON.collidepoint(pos):
        load_preset()
    
    if PLAY_BUTTON.collidepoint(pos):
        Seq.playing = True
    if STOP_BUTTON.collidepoint(pos):
        Seq.playing = False
    
    if Seq.playing == False:
        if BNK_BUTTON.collidepoint(pos):
           if pygame.mouse.get_pressed()[0]:
               Samples.select_bank = min(2, Samples.select_bank + 1)
        if BNK_BUTTON.collidepoint(pos):
            if pygame.mouse.get_pressed()[2]:
               Samples.select_bank = max(0, Samples.select_bank - 1)
        
        if RF_T1.collidepoint(pos) and Seq.apt > 1 : # Triangulo izquierdo
            if pygame.mouse.get_pressed()[0]:
               Seq.apt -= 1
         
        if RF_T2.collidepoint(pos) and Seq.apt < 32: # Triangulo derecho
            if pygame.mouse.get_pressed()[0]:
                Seq.apt += 1
              
                
        
        if PATTERN_TOTAL.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                Seq.tpt = min(32, Seq.tpt + 1)
                if Seq.apt > Seq.tpt:
                    Seq.apt = Seq.tpt
                    patterns = Patt.mtx_p[Seq.apt - 1]
            elif pygame.mouse.get_pressed()[2]:
                Seq.tpt = max(1, Seq.tpt - 1)
                if Seq.apt > Seq.tpt:
                    Seq.apt = Seq.tpt
                    patterns = Patt.mtx_p[Seq.apt - 1]
        if SETTING_BOX.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                Audio.freq = min(44100, Audio.freq + 22050)
                Audio.chan = min(2, Audio.chan + 1)
                Audio.buffer = min(1024, Audio.buffer + 256)
                Audio.bits = -16
            elif pygame.mouse.get_pressed()[2]:
                Audio.freq = max(22050, Audio.freq - 22050)
                Audio.chan = max(1, Audio.chan - 1)
                Audio.buffer = max(256, Audio.buffer - 256)
                Audio.bits = -8
        
    
    if TEMPO_BOX.collidepoint(pos):
        if pygame.mouse.get_pressed()[0]:
            Seq.tempo = min(200, Seq.tempo + 2)
        elif pygame.mouse.get_pressed()[2]:
            Seq.tempo = max(20, Seq.tempo - 2)
        Seq.tpo_txt = str(Seq.tempo)
    if MASTER_VOL_BOX.collidepoint(pos):
        if pygame.mouse.get_pressed()[0]:
            Seq.m_vol = min(1.0, Seq.m_vol + 0.05)
        elif pygame.mouse.get_pressed()[2]:
            Seq.m_vol = max(0.0, Seq.m_vol - 0.05)

def update_sequencer():
    
    if not Seq.playing:
        return
    
    current_time = pygame.time.get_ticks()
    beat_duration = 60.0 / Seq.tempo * 1000
    step_duration = beat_duration / 4
    
    expired_channels = [ch for ch, off_time in Seq.act_chs.items() if current_time >= off_time]
    for channel_idx in expired_channels:
        turn_off_led(channel_idx)
        del Seq.act_chs[channel_idx]
    
    if current_time >= Seq.lstime + step_duration:
        # Calcular el paso dentro del pattern activo
        pattern_offset = (Seq.apt - 1) * 16
        local_step = Seq.s_idx - pattern_offset
        
        if local_step >= 0 and local_step < 16:
            for channel_idx, pattern in enumerate(Patt.mtx_p[Seq.apt - 1]):
                if pattern[local_step] == 1:
                    if channel_idx not in Seq.act_chs:
                        off_time = play_sound_and_light(channel_idx)
                        Seq.act_chs[channel_idx] = off_time
        else:
           # Reiniciar Seq.s_idx si excede el rango del pattern actual 
            Seq.s_idx = pattern_offset        
        
        Seq.lstime = current_time
        Seq.s_idx += 1
#         print("Seq.s_idx / STEP index ", Seq.s_idx)
        
    pattern_control()
