import os
import time
import shutil
import math
import random

# ascii_gradient = [" ", "(", ")", "1", "{", "}", "[", "]", "?", "-", "_", "+", "~", "<", ">", "i", "!", "l", "I", ";", ":", "^"]
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
    shape = gen_widths(height, 45)
    for i in range(len(shape)):
        lines.append(steam_line(shape[i], height - i + 1))
    return lines

def steam_line(width, height) -> str:
    weights = [10 * height] + [1] * (len(ascii_gradient) - 1)
    line = ""
    for char in range(width):
        line += random.choices(ascii_gradient, weights = weights, k = 1)[0]
    
    return line

# could make this a nicer shape later... looks nice for now (I think the centering may be saving it)
def gen_widths(height, width):
    shape = []

    counter = 1
    for i in range(height):
        shape.append(counter + 1)  
        counter += 1
    return shape
         

def main():
    cols, rows = get_terminal_size() 
    try:
        while True:
            os.system("clear")
            print_ascii_center(cols, rows)
            time.sleep(0.4)
    except KeyboardInterrupt:         
        print()

if __name__ == "__main__":
    main()
