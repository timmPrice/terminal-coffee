import os
import time
import shutil
import math

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
    for _ in range(math.floor(rows / 2)):
        print()
    lines = ascii.splitlines()
    centered = [line.center(cols) for line in lines]
    print("\n".join(centered))

def steam(height):

def steam_line(width):
    for char in 

def main():
    cols, rows = get_terminal_size() 
    try:
        while True:
            os.system("clear")
            print_ascii_center(cols, rows)
            time.sleep(2)
    except KeyboardInterrupt:         
        print()

if __name__ == "__main__":
    main()
