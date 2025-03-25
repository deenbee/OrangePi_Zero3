#from turtle import pos
import pygame
#import #wiringpi
from config.variables import Botones
from config.variables import Pestania, Samples, Audio, Color, Patt, Seq, channels, MENU_BUTTON, MENU_ITEMS, MENU_ITEM_HEIGHT, MENU_WIDTH, DRAW_X, STEP_WIDTH, STEP_MARGIN, STEP_HEIGHT, CHANNEL_HEIGHT, VOL_HEIGHT, VOL_WIDTH, PAN_WIDTH, PAN_HEIGHT, COLOR_BTN1, COLOR_BTN2, COLOR_BTN3, COLOR_BTN4, COLOR_BTN5, COLOR_BTN6, SAVE_BUTTON, LOAD_BUTTON, PLAY_BUTTON, BNK_BUTTON, PATTERN_TOTAL, SETTING_BOX, TEMPO_BOX, MASTER_VOL_BOX, LED_DURATION, sound_objects, sound_objects_2, sound_objects_3, led_pins
from .jsncodes import save_preset
from .jsncodes import load_preset


def samples_banks_sel(channels, channel_idx):
    
    # Selector de banco de sonidos
    if Samples.select_bank == 0: 
        sound = sound_objects[channel_idx]
    if Samples.select_bank == 1:
        sound = sound_objects_2[channel_idx]
    if Samples.select_bank == 2:
        sound = sound_objects_3[channel_idx]

    return sound

def play_step_on_stop(channel_idx, patt_in, test):
    global channels
    
    sound = samples_banks_sel(channels, channel_idx)

    if patt_in == 1 and test == True:
        channels[channel_idx].play(sound)
    
    return False



def play_sound_and_light(channel_idx):
    global channels
    """Reproduce un sonido y enciende su LED con volumen y panorama ajustados."""
    sound = samples_banks_sel(channels, channel_idx)
    
    vol = Seq.channel_volumes[channel_idx] * Seq.m_vol
    sound.set_volume(vol)
    pin = led_pins[channel_idx]
    #wiringpi.digitalWrite(pin, 1)
    left = (1 - Seq.pan_volumes[channel_idx]) / 2
    right = (1 + Seq.pan_volumes[channel_idx]) / 2
    channels[channel_idx].set_volume(left, right)
    channels[channel_idx].play(sound)
    return pygame.time.get_ticks() + LED_DURATION

def turn_off_led(channel_idx):
    """Apaga el LED de un canal."""
    #pin = led_pins[channel_idx]
    #wiringpi.digitalWrite(pin, 0)

def pattern_control():
    #print("Step actual > > > > > > > ----->", Seq.s_idx)

    # Si llegamos al final de la secuencia completa, reseteamos
    if Seq.s_idx >= 16 * Seq.tpt:
        Seq.s_idx = 0
        Seq.apt = 1
               
                
        print("Reset step:", Seq.s_idx, "and active patt:", Seq.apt)
        
        # Mostrar bancos activos
        for i in range(4):
            print("Bank selected ", Botones.state[i])

        # Mostrar patrones activos
        for i in range(8):
            print("Pattern selected ", Botones.number_state[i])

    # Calcular el índice de pattern actual según s_idx
    current_pattern_idx = (Seq.s_idx // 16) % Seq.tpt
    if 0 <= current_pattern_idx < Seq.tpt:
        nuevo_apt = current_pattern_idx + 1

        # Si el pattern activo cambia
        if nuevo_apt != Seq.apt:
            Seq.apt = nuevo_apt
           
            Seq.s_idx = (Seq.apt - 1) * 16  # Ajustar el paso al inicio del nuevo pattern

            #Botones.update_pattern_state()
            #print("Active PATT:", Seq.apt, "Patterns: ", patterns)
 
        
                
def handle_input(pos):
    

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
    
    if Pestania.confirm_close == False:

        for channel_idx in range(24): # Recorre la matrix de las patterns
            for step_idx in range(16):
                test_play = False
                x = DRAW_X + step_idx * (STEP_WIDTH + STEP_MARGIN)
                y = 30 + channel_idx * CHANNEL_HEIGHT
                rect = pygame.Rect(x, y, STEP_WIDTH, STEP_HEIGHT)
                if rect.collidepoint(pos):
                    test_play = True
                    # Seq.patt - 1
                    Patt.mtx_p[Seq.patt - 1][channel_idx][step_idx] = 1 - Patt.mtx_p[Seq.patt - 1][channel_idx][step_idx] # Guarda los cambios en Patt.mtx_p
                    test_play = play_step_on_stop(channel_idx, Patt.mtx_p[Seq.patt - 1][channel_idx][step_idx], test_play)
                    for i in range(16):
                        print("Channel1 STEP ", i + 1,"Patt.mtx_p", Patt.mtx_p[0][0][i], " Pattern active: ", Seq.patt)
            
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
                    Seq.pan_volumes[channel_idx] = min(1.0, Seq.pan_volumes[channel_idx] + 0.05)
                elif pygame.mouse.get_pressed()[2]:
                    Seq.pan_volumes[channel_idx] = max(-1.0, Seq.pan_volumes[channel_idx] - 0.05)
    
    
    if COLOR_BTN1.collidepoint(pos):
        Color.bg = (0, 0, 0)
        Color.w = (255, 255, 255)
        Color.g = (150, 150, 150)
        Color.gn = (0, 255, 0)
        Color.r = (255, 0, 0)
        Botones.skin_color[0] = Botones.on_color
        for i in range(6):
            if i != 0:
                Botones.skin_color[i] = Botones.off_color
        print("Color 1")
    if COLOR_BTN2.collidepoint(pos):
        Color.bg = (153, 255, 51)
        Color.w = (0, 0, 0)
        Color.g = (0, 0, 0)
        Color.gn = (255, 0, 0)
        Color.r = (255, 0, 0)
        Botones.skin_color[1] = Botones.on_color
        for i in range(6):
            if i != 1:
                Botones.skin_color[i] = Botones.off_color
        print("Color 2")
    if COLOR_BTN3.collidepoint(pos):
        Color.bg = (210, 237, 255)
        Color.w = (0, 0, 0)
        Color.g = (110, 110, 110)
        Color.gn = (255, 0, 0)
        Color.r = (255, 255, 0)
        Botones.skin_color[2] = Botones.on_color
        for i in range(6):
            if i != 2:
                Botones.skin_color[i] = Botones.off_color
        print("Color 3")
    if COLOR_BTN4.collidepoint(pos):
        Color.bg = (60, 60, 60)
        Color.w = (255, 255, 255)
        Color.g = (150, 150, 150)
        Color.gn = (0, 255, 0)
        Color.r = (255, 0, 0)
        Botones.skin_color[3] = Botones.on_color
        for i in range(6):
            if i != 3:
                Botones.skin_color[i] = Botones.off_color
    if COLOR_BTN5.collidepoint(pos):
        Color.bg = (76, 0, 153)
        Color.w = (255, 255, 255)
        Color.g = (150, 150, 150)
        Color.gn = (255, 0, 0)
        Color.r = (255, 255, 0)
        Botones.skin_color[4] = Botones.on_color
        for i in range(6):
            if i != 4:
                Botones.skin_color[i] = Botones.off_color
    if COLOR_BTN6.collidepoint(pos):
        Color.bg = (255, 229, 204)
        Color.w = (0, 0, 0)
        Color.g = (150, 150, 150)
        Color.gn = (0, 0, 0)
        Color.r = (0, 0, 0)
        Botones.skin_color[5] = Botones.on_color
        for i in range(6):
            if i != 5:
                Botones.skin_color[i] = Botones.off_color

        
    
       
         
    
    if SAVE_BUTTON.collidepoint(pos):
        save_preset()
    if LOAD_BUTTON.collidepoint(pos):
        load_preset()
    
    if PLAY_BUTTON.collidepoint(pos):
        Seq.playing = True
        Botones.write_mode = False               # Quita el modo de escritura
        Botones.color_write = Botones.off_color  # Quita el color de escritura
        
    Botones.stop_song_(pos)
               
    if Seq.playing == False:
        if BNK_BUTTON.collidepoint(pos):
           if pygame.mouse.get_pressed()[0]:
               Samples.select_bank = min(2, Samples.select_bank + 1)
        if BNK_BUTTON.collidepoint(pos):
            if pygame.mouse.get_pressed()[2]:
               Samples.select_bank = max(0, Samples.select_bank - 1)
        
        Botones.handle_botones_triangulo(pos) # Si la secuencia esta detenida puede manejar los botones del triangulo
              
                
        
        if PATTERN_TOTAL.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                Seq.tpt = min(32, Seq.tpt + 1)

                #Botones.update_pattern_state()
                if Seq.apt > Seq.tpt:
                    Seq.apt = Seq.tpt
                    
            elif pygame.mouse.get_pressed()[2]:
                #Botones.update_pattern_state()
                Seq.tpt = max(1, Seq.tpt - 1)
                if Seq.apt > Seq.tpt:
                    Seq.apt = Seq.tpt
                    
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
    
    #pat = Seq.patt_state[Seq.apt - 1] if Seq.playing else Seq.patt

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
            for channel_idx, pattern in enumerate(Patt.mtx_p[Seq.patt - 1]): #pat - # Seq.apt - 1
                if pattern[local_step] == 1:
                    if channel_idx not in Seq.act_chs:
                        off_time = play_sound_and_light(channel_idx)
                        Seq.act_chs[channel_idx] = off_time
        else:
           # Reiniciar Seq.s_idx si excede el rango del pattern actual 
            Seq.s_idx = pattern_offset        
        
        Seq.lstime = current_time
        Seq.s_idx += 1
    #   print("Seq.s_idx / STEP index ", Seq.s_idx)
        
    pattern_control() # Control de avance de los patterns
