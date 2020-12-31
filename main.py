from PIL import Image
import math

img = Image.open("image.jpg")
img = img.convert('L')

# Open output file and clear it
output = open("output.txt", "a")
output.seek(0)
output.truncate()

rep = "@%#*+=-:. "
sensitivity = 50
w, h = img.size

for heightrun in range(0, h):
    for widthrun in range (0, w):
        shade = math.floor((img.getpixel((widthrun, heightrun))) / sensitivity)
        output.write(rep[shade])
    output.write("\n")

output.close()
