import os
import time
import shutil
import math
import random

ascii_gradient = [" ", "(", ")", "1", "{", "}", "[", "]", "?", "-", "_", "+", "~", "<", ">", "i", "!", "l", "I", ";", ":", "^"]
ascii = """
                      ...  .     ..:..   . ...                      
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
    steam_block = steam(4)
    for _ in range(math.floor(rows / 2)):
        print()
    
    lines = steam(4) + ascii.splitlines()
    centered = [line.center(cols) for line in lines]
    print("\n".join(centered))

def steam(height):
    lines = []
    for line in range(height):
        lines.append(steam_line(35, height))
    return lines

def steam_line(width, height) -> str:
    line = ""
    for char in range(width):
        num = random.randint(0, len(ascii_gradient) - 1)
        line += ascii_gradient[num]
    return line

def main():
    cols, rows = get_terminal_size() 
    try:
        while True:
            os.system("clear")
            print_ascii_center(cols, rows)
            time.sleep(0.2)
    except KeyboardInterrupt:         
        print()

if __name__ == "__main__":
    main()
