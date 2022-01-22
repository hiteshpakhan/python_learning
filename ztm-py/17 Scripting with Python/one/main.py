from PIL import Image
# to run the file in which you import the Image module you have to go terminal to that specific location file and then run the python file

img = Image.open("./Pokedex/charmander.jpg")

print(img)
# it will give you the output in object

print(img.format)   #it will give you the format of that image or extention
# output:- JPEG