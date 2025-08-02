from pynput import keyboard
import os
import time
import shutil
import math
import random
import sys
import termios


ascii_gradient = [" ","(",  ")", "{", "}", ".", ":", "@"]

ascii = """
                 .........  ..   ...  .. ..........                 
           :::::::::XXXXXx+++++;;;;;;++++xxXXXXX:::::::::           
           :::XXXXXXXXXXXXXxxx+++++++xxxxXXXXXXXXXXXXX:::           
          ::::: .:$$$$$$$$XXXXXXXXXXXXXXXXX$$$$$$$;  :::::          
          :$..;;;::::............ ............:::::$$$::$:          
          ::.....::$$$$$$$$$$;..    .:+$$$$$$$$$$:::::::::...       
          ::.....::::.........        .........:::::::::::........  
           ::....:::::........... ............:::::::::::    ::...  
           ::....::::::.....................:::::::::::::      :::  
            :....::::::::.................::::::::::::$:      ::::  
            ::....:$$$$$$$::::......:.::::$$$$$$$:::::::    ::::    
             ::...:::::::::::::::::::::::::::::::::::::  :::::      
              :::..:::::::::::::::::::::::::::::::::::::::::        
               :::.:::::::::::::::::::::::::::::::::::::            
                :::.::::::::::::::::::::::::::::::::                
         xxxxx;;;::::::::::::::::::::::::::::::::::;;xxxxx          
     x;;;;;;;;:;:;:::::::::::::::::::::::::::::::;;:;;;;;;;;;x      
   ;;;:;:;:;:;;::::;:::::::::::::::::::::::::::;;:::;:;:;:;:;;;;    
 ;;:;;::;::::;;;;;;;;+x::::::::::::::::::::::x+;;;;;;;;:::;;:;:;;;  
  ;::::::::::;;;;;;;+X$$$$$::::::::::::::$$$$XX+;;;;;;::::::::;:;x  
 xx  ::::::::::::::::::;;;;;;;;+++;+;;;;;;;;:::::::::::::::::: xxx  
   xxXxx  ::::::::::::::::::..:.....::::::::::::::::::::: .xxXxx    
     XxxxXxXXXXXXX     :::::::::::::::::::::     XXXXXXXXXXxXX      
         XxXXXXXXXXXXXXX$$$$$$$$$$$$$$$$$$$X$XXXXXXXXXXXXX          
                 XXX$XXX$$$$$$$$$$$$$$$$$$$$XX$XXX                  
"""

def get_terminal_size():
    cols, rows = shutil.get_terminal_size()
    return cols, rows 

def print_ascii_center(cols, rows):
    for _ in range(math.floor(rows / 2)):
        print()
    
    lines = steam(19) + ascii.strip("\n").splitlines()
    centered = [line.center(cols) for line in lines]
    print("\n".join(centered))

def steam(height):
    lines = []
    shape = gen_widths(height)
    for i in range(len(shape)):
        lines.append(steam_line(shape[i], height - i + 1))
    return lines

def steam_line(width, height) -> str:
    weights = [10 * height] + [1] * (len(ascii_gradient) - 1)
    line = ""
    for _ in range(width):
        line += random.choices(ascii_gradient, weights = weights, k = 1)[0]
    
    return line

def gen_widths(height):
    shape = []

    counter = 1
    for _ in range(height):
        shape.append(counter + 1)  
        counter += 1
    return shape
        
def on_press(key):
    try: 
        if key.char == 'q':
            return False
    except AttributeError:
        pass
        

def main():
    cols, rows = get_terminal_size() 
    
    listener = keyboard.Listener(on_press=on_press) # type: ignore
    listener.start()

    try:
        while listener.running:
            os.system("clear")
            print_ascii_center(cols, rows)
            time.sleep(0.4)
    except KeyboardInterrupt:
        pass
    
    termios.tcflush(sys.stdin, termios.TCIFLUSH)

if __name__ == "__main__":
    main()
