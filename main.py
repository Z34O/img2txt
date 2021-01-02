# 0.7

from PIL import Image
import re
import requests
import math
from io import BytesIO

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

    if command[0] == "convert":
        # Clear output file
        output = open("output.txt", "a")
        output.seek(0)
        output.truncate()

        if re.match("^http(s)?://.*", command[1]):
            response = requests.get(command[1])
            img = Image.open(BytesIO(response.content))
        else:
            try:
                img = Image.open(command[1])
            except FileNotFoundError:
                print("File not found")
                continue

        img = img.convert('L')

        rep = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
        sensitivity = 50 if len(command) == 2 else int(command[2])
        w, h = img.size

        if w > 300 or h > 300:
            print("Image dimesion too large")
            print("You may opt not to resize but, your file viewer")
            print("may word-wrap the output file.")

            choice = input("Resize (auto)? [y/n/(w, h)]: ")
            if choice == "y":
                for optimize in range(1, 50):
                    if w/optimize < 300 and h/optimize < 300:
                        w = math.floor(w/optimize)
                        h = math.floor(h/optimize)
                        img = img.resize((w, h))
                        break

            elif choice == "n":
                pass

            else:
                newdimension = choice.split(", ")
                w = int(newdimension[0])
                h = int(newdimension[1])
                img = img.resize((w, h))

        for heightrun in range(0, h):
            for widthrun in range(0, w):
                shade = math.floor((img.getpixel((widthrun, heightrun))) / sensitivity)
                output.write(rep[shade])
            output.write("\n")

        print("File saved in output.txt")
        output.close()

    elif command[0] == "exit":
        break

    elif command[0] == "help":
        print("\nCommand list: ")
        print("* convert [file] - convert image to text")
        print("* exit - exit the application")

    elif command[0] == "result":
        res = open("output.txt", "r")
        print(res.read())

    else:
        print("Unknown command")

print("Exiting...")
exit()
