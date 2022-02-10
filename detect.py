import keyboard
import time
import sys
import pyautogui as py
import cv2
import numpy
from PIL import Image, ImageGrab
from playsound import playsound
import random

# program is not well optimized(idk why) so it can cause high cpu usage and on low-end pc lags

print("Ultimate Detector Machine                                                                          Copyright by MarkSon")
time.sleep(1)
print("Loading Overwatch Verison...")
time.sleep(1)

# waiting till assets will load (Just in case)

print()

time.sleep(2) 

print("Script is ready now. You can go back to game. Press 'z' hotkey to stop program")

while True:     # loop that makes program detect ultimate always                                                        

    try:
        if keyboard.is_pressed('q'):                     
            imgr = ImageGrab.grab()            
            imgr_rgb = imgr.convert("RGB")                     # doing "screenshot", converting it to rgb to specify the color, taking rgb from specific pixel
            rgb_pixel_value = imgr_rgb.getpixel((948, 1003))                                                  
            print(rgb_pixel_value)                                              
            if rgb_pixel_value >= (230, 230, 230):                  
                ttt = random.randint(1, 3)
                print(ttt)                        
                print("ULTIMATE DETECTED!!!") 
                if ttt == 1:          
                    playsound('C:\\Users\\jamal\\Desktop\\code\\music\\sound1.mp3')
                
                if ttt == 2:
                    playsound('C:\\Users\\jamal\\Desktop\\code\\music\\sound2.mp3') # randomize playable sounds | playsound('PATH FOR SOUND') | mp3 works i am not sure about others
                                                                                    # if sound won't play try to import it and export as mp3 with music editor like Audacity
                if ttt == 3:
                    playsound('C:\\Users\\jamal\\Desktop\\code\\music\\sound3.mp3')
                    
                                     
            if rgb_pixel_value <= (230, 230, 230):              
                print("NOT BRIGHT!!!")              # sends message if ultimate is not ready(or not detected) and go back to step where program waits to user to press hotkey
            
        if keyboard.is_pressed('z'):
            sys.exit(0)


    except:
        break  
        

 