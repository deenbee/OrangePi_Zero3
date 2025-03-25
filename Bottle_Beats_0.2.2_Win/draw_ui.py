import pygame
import os
from config.variables import Seq, Pestania, font, font_small, screen, Color, Patt, Samples, Audio, DRAW_X, STEP_WIDTH, STEP_MARGIN, STEP_HEIGHT, CHANNEL_HEIGHT, VOL_HEIGHT, VOL_WIDTH, PAN_HEIGHT, PAN_WIDTH, PLAY_BUTTON, TEMPO_BOX, MASTER_VOL_BOX, SAVE_BUTTON, LOAD_BUTTON, MENU_BUTTON, PATTERN_BOX, PATTERN_TOTAL, BNK_BUTTON, SETTING_BOX, MENU_ITEMS, MENU_WIDTH, MENU_ITEM_HEIGHT
from .handle import Botones

STP_IDX_Y = 750

def actualizar_colores_botones(local_pt):
        
        # Calcular banco y número en base a local_pt
        grupo = (local_pt - 1) // 8   # de 0 a 3
        numero = (local_pt - 1) % 8   # de 0 a 7

        # Actualizar colores de los bancos
        for i in range(4):
            if i == grupo:
                Botones.color_bank[i] = Botones.on_color
            else:
                Botones.color_bank[i] = Botones.off_color

        # Actualizar colores de los números
        for i in range(8):
            if i == numero:
                Botones.color_bank_numbers[i] = Botones.on_color
            else:
                Botones.color_bank_numbers[i] = Botones.off_color 

def draw_steps():
    
          # Si se esta reproduciendo
    if Seq.playing == True:
        Seq.patt = Seq.patt_state[Seq.apt - 1]   # Si se reproduce solo se actualiza segun la posicion
        Seq.pattern_num = Seq.patt               # Cuando se esta reproduciendo se iguala la variable del numeros de patterns
        actualizar_colores_botones(Seq.patt)
    else: # Si NO se esta reproducciondo:

       # Si esta en modo escritura y no se esta reproduciendo se graba
        if Botones.write_mode == True and Seq.pulsador_stop == False:
            Seq.patt_state[Seq.apt - 1] = Seq.pattern_num  # Write selected pattern in the song position
            Seq.patt = Seq.patt_state[Seq.apt - 1]
            actualizar_colores_botones(Seq.patt)
     
        if Botones.pulsador_patt_num == True  and Botones.pulsador == False and Seq.pulsador_stop == False:
            Seq.patt = Seq.pattern_num       # Como no se esta escribiendo solo se muestra la pattern segun la posicion
            actualizar_colores_botones(Seq.patt)
            Botones.color_write = Botones.off_color
            Botones.pulsador_patt_num = False   # Se restablece
            Botones.write_mode = False          # Se restablece

        if Botones.pulsador_bank_num == True  and Botones.pulsador == False and Seq.pulsador_stop == False:
            Seq.patt = Seq.pattern_num       # Como no se esta escribiendo solo se muestra la pattern segun la posicion
            actualizar_colores_botones(Seq.patt)
            Botones.color_write = Botones.off_color
            Botones.pulsador_bank_num = False   # Se restablece
            Botones.write_mode = False          # Se restablece    
            

        if Botones.pulsador == True and Seq.pulsador_stop == False:
            Seq.patt = Seq.patt_state[Seq.apt - 1]   # Si se presiona las flechas de la posicion se actualiza el estado sin grabar
            Seq.pattern_num = Seq.patt               # Cuando se esta reproduciendo se iguala la variable del numeros de patterns
            actualizar_colores_botones(Seq.patt)
            Botones.pulsador = False     # Se restablece el estado a false

        if Seq.pulsador_stop == True:                # Cuando se presiona stop actualiza el estado segun la posicion 
            Seq.patt = Seq.patt_state[Seq.apt - 1]
            actualizar_colores_botones(Seq.patt)
            Seq.pulsador_stop = False    # Se restablece el estado a false


             
   

    step_on = Seq.s_idx % 16
    
    if Pestania.confirm_close == False:

        for i in range(16): # Draw Index steps of leds - (Dibuja los leds de los steps del indice superior e inferior)
            num_text = font_small.render(str(i + 1), True, Color.w)
            screen.blit(num_text, (DRAW_X + i * (STEP_WIDTH + STEP_MARGIN) + STEP_WIDTH // 2 - 5, 5))
            screen.blit(num_text, (DRAW_X + i * (STEP_WIDTH + STEP_MARGIN) + STEP_WIDTH // 2 - 5, STP_IDX_Y + 10))
                    
            if step_on == i:
                pygame.draw.rect(screen, Color.gn, (DRAW_X + i * (STEP_WIDTH + STEP_MARGIN) + STEP_WIDTH // 2 - 10, 20, STEP_WIDTH, STEP_HEIGHT / 4))
                pygame.draw.rect(screen, Color.gn, (DRAW_X + i * (STEP_WIDTH + STEP_MARGIN) + STEP_WIDTH // 2 - 10, STP_IDX_Y, STEP_WIDTH, STEP_HEIGHT / 4))
            else:    
                pygame.draw.rect(screen, Color.g, (DRAW_X + i * (STEP_WIDTH + STEP_MARGIN) + STEP_WIDTH // 2 - 10, 20, STEP_WIDTH, STEP_HEIGHT / 4))
                pygame.draw.rect(screen, Color.g, (DRAW_X + i * (STEP_WIDTH + STEP_MARGIN) + STEP_WIDTH // 2 - 10, STP_IDX_Y, STEP_WIDTH, STEP_HEIGHT / 4))
        
        # Draw Samples Names (Sound Bank)
        for channel_idx, pattern in enumerate(Patt.mtx_p[Seq.patt - 1]): # Seq.patt - 1 # Seq.apt - 1
            if Samples.select_bank == 0:
                wav_name = os.path.basename(Samples.wav_files[channel_idx]).replace(".wav", "")
            if Samples.select_bank == 1:
                wav_name = os.path.basename(Samples.T909[channel_idx]).replace(".wav", "")
            if Samples.select_bank == 2:
                wav_name = os.path.basename(Samples.C64[channel_idx]).replace(".wav", "")    
            text = font.render(wav_name, True, Color.w)
            screen.blit(text, (10, 30 + channel_idx * CHANNEL_HEIGHT))
        
    
    if Pestania.confirm_close == False:

        # Draw Steps status (Active or Inactive), Channel Volumes and Panning
        for channel_idx, pattern in enumerate(Patt.mtx_p[Seq.patt - 1]): # Seq.apt - 1 
            for step_idx, value in enumerate(pattern):
                
                x = DRAW_X + step_idx * (STEP_WIDTH + STEP_MARGIN)
                y = 30 + channel_idx * CHANNEL_HEIGHT
                color = Color.r if value == 1 else Color.g # Evalua el color del step
                pygame.draw.rect(screen, color, (x, y, STEP_WIDTH, STEP_HEIGHT))
            
            vol_x = DRAW_X + 16 * (STEP_WIDTH + STEP_MARGIN) + 10
            vol_y = 30 + channel_idx * CHANNEL_HEIGHT + (STEP_HEIGHT - VOL_HEIGHT) // 2
            pygame.draw.rect(screen, Color.g, (vol_x, vol_y, VOL_WIDTH, VOL_HEIGHT))
            vol_text = font_small.render(f"{int(Seq.channel_volumes[channel_idx] * 100)}%", True, Color.bg)
            screen.blit(vol_text, (vol_x + 5, vol_y + 2))
            
            pan_x = vol_x + VOL_WIDTH + 10
            pan_y = vol_y
            pygame.draw.rect(screen, Color.g, (pan_x, pan_y, PAN_WIDTH, PAN_HEIGHT))
            pan_text = font_small.render(f"P: {int(Seq.pan_volumes[channel_idx] * 100)}", True, Color.r)
            screen.blit(pan_text, (pan_x + 5, pan_y + 2))


def draw_ui():
       
          
    play_color = Color.gn if Seq.playing else Color.g
    pygame.draw.rect(screen, play_color, PLAY_BUTTON)
    
    pygame.draw.rect(screen, Color.w, TEMPO_BOX, 2)
    pygame.draw.rect(screen, Color.w, MASTER_VOL_BOX, 2)
    pygame.draw.rect(screen, Color.g, SAVE_BUTTON)
    pygame.draw.rect(screen, Color.g, LOAD_BUTTON)
    pygame.draw.rect(screen, Color.g, MENU_BUTTON)
    
    pygame.draw.rect(screen, Color.w, PATTERN_BOX, 1)
    pygame.draw.rect(screen, Color.w, PATTERN_TOTAL, 1)
    
    pygame.draw.rect(screen, Color.g, BNK_BUTTON)

         
    
    
    Botones.draw()
    Botones.text()    # Resetea los colores de las flechas de la posicion de la cancion
    Botones.show()
           
    
    if Samples.select_bank == 0:
       bank_txt = font.render(f"Bank: 808", True, Color.w)
    if Samples.select_bank == 1:
       bank_txt = font.render(f"Bank: 909", True, Color.w)
    if Samples.select_bank == 2:
       bank_txt = font.render(f"Bank: C64", True, Color.w)
        
    freq_text = font_small.render(f"Sample: {Audio.freq}", True, Color.w)
    bits_text = font_small.render(f"Audio.bits: {Audio.bits}", True, Color.w)
    chan_text = font_small.render(f"Stereo {Audio.chan}:", True, Color.w)
    buffer_text = font_small.render(f"Audio.buffer {Audio.buffer}", True, Color.w)
    pattern_text = font.render(f"{Seq.apt}", True, Color.w)
    total_text = font.render(f"Total: {Seq.tpt}", True, Color.w)
    play_text = font.render("Play", True, Color.bg)
    
    tempo_label = font.render(f"Tempo: {Seq.tpo_txt}", True, Color.w)
    master_vol_text = font.render(f"Master: {int(Seq.m_vol * 100)}%", True, Color.w)
    save_text = font.render("Save", True, Color.bg)
    load_text = font.render("Load", True, Color.bg)
    menu_text = font.render(f"Mem: {Seq.s_mem}", True, Color.bg)
    
    # Textos
    screen.blit(bank_txt, (BNK_BUTTON.x + 10, BNK_BUTTON.y + 10))
    screen.blit(freq_text, (SETTING_BOX.x, SETTING_BOX.y + 0))
    screen.blit(bits_text, (SETTING_BOX.x, SETTING_BOX.y + 20))
    screen.blit(chan_text, (SETTING_BOX.x, SETTING_BOX.y + 40))
    screen.blit(buffer_text, (SETTING_BOX.x, SETTING_BOX.y + 60))
    screen.blit(pattern_text, (PATTERN_BOX.x + 50, PATTERN_BOX.y + 10))
    screen.blit(total_text, (PATTERN_TOTAL.x + 10, PATTERN_TOTAL.y + 10))
    screen.blit(play_text, (PLAY_BUTTON.x + 10, PLAY_BUTTON.y + 10))
    
    screen.blit(tempo_label, (TEMPO_BOX.x + 10, TEMPO_BOX.y + 10))
    screen.blit(master_vol_text, (MASTER_VOL_BOX.x + 10, MASTER_VOL_BOX.y + 10))
    screen.blit(save_text, (SAVE_BUTTON.x + 10, SAVE_BUTTON.y + 10))
    screen.blit(load_text, (LOAD_BUTTON.x + 10, LOAD_BUTTON.y + 10))
    screen.blit(menu_text, (MENU_BUTTON.x + 10, MENU_BUTTON.y + 10))
    
    # Draw menu items (Memory)
    if Seq.m_opn:
        for i in range(MENU_ITEMS):
            menu_item_rect = pygame.Rect(MENU_BUTTON.x, MENU_BUTTON.y - (i + 1) * MENU_ITEM_HEIGHT, MENU_WIDTH, MENU_ITEM_HEIGHT)
            pygame.draw.rect(screen, Color.g, menu_item_rect)
            menu_item_text = font.render(f"Mem: {i + 1}", True, Color.bg)
            screen.blit(menu_item_text, (menu_item_rect.x + 10, menu_item_rect.y + 5))
