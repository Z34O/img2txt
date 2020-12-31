from PIL import Image
import math

print(r"""                                                                                   
                                                                                   
                   ____                   ,----,     ___                   ___     
  ,--,           ,'  , `.               .'   .' \  ,--.'|_               ,--.'|_   
,--.'|        ,-+-,.' _ |             ,----,'    | |  | :,'              |  | :,'  
|  |,      ,-+-. ;   , ||  ,----._,.  |    :  .  ; :  : ' :  ,--,  ,--,  :  : ' :  
`--'_     ,--.'|'   |  || /   /  ' /  ;    |.'  /.;__,'  /   |'. \/ .`|.;__,'  /   
,' ,'|   |   |  ,', |  |,|   :     |  `----'/  ; |  |   |    '  \/  / ;|  |   |    
'  | |   |   | /  | |--' |   | .\  .    /  ;  /  :__,'| :     \  \.' / :__,'| :    
|  | :   |   : |  | ,    .   ; ';  |   ;  /  /-,   '  : |__    \  ;  ;   '  : |__  
'  : |__ |   : |  |/     '   .   . |  /  /  /.`|   |  | '.'|  / \  \  \  |  | '.'| 
|  | '.'||   | |`-'       `---`-'| |./__;      :   ;  :    ;./__;   ;  \ ;  :    ; 
;  :    ;|   ;/           .'__/\_: ||   :    .'    |  ,   / |   :/\  \ ; |  ,   /  
|  ,   / '---'            |   :    :;   | .'        ---`-'  `---'  `--`   ---`-'   
 ---`-'                    \   \  / `---'                                          
                            `--`-'                                                 """)

print("Image to Text Art converter")
print("Type help for available commands")

while True:
    command = input("++> ").split(" ")
    output = open("output.txt", "a")

    if command[0] == "convert":
        # Clear output file
        output.seek(0)
        output.truncate()

        try:
            img = Image.open(command[1])
        except FileNotFoundError:
            print("File not found!")
            continue

        img = img.convert('L')

        rep = "@%#*+=-:. "
        sensitivity = 50 if len(command) == 2 else command[2]
        w, h = img.size

        if w > 200 or h > 200:
            print("File resolution is too big")
            print("You may opt not to resize.")
            reschoice = input("Resize? [y/n]")

        for heightrun in range(0, h):
            for widthrun in range(0, w):
                shade = math.floor((img.getpixel((widthrun, heightrun))) / sensitivity)
                output.write(rep[shade])
            output.write("\n")

        print("File saved in output.txt")

    elif command[0] == "exit":
        break

    elif command[0] == "help":
        print("\nCommand list: ")
        print("* convert [file] - convert image to text")
        print("* exit - exit the application")

    else:
        print("Unknown command")

print("Exiting...")
print("Closing files...")
output.close()
exit()
