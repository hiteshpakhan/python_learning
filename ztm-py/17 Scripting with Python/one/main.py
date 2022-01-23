from PIL import Image, ImageFilter
# PIL is the Python Imaging Library
# to run the file in which you import the Image module you have to go terminal to that specific location file and then run the python file
# and the ImageFilter that help to filter the image



# Image.open()
img1 = Image.open("./Pokedex/charmander.jpg")

print(img1)
# it will give you the output in object

# .format
print(img1.format)   #it will give you the format of that image or extention
# output:- JPEG

# .size 
print(img1.size)
# output:- (260, 240)

# .mode
print(img1.mode)
# output:- RGB

# dir()
# we can use the dir command to find out how many methods specific term have
# print(dir(img1))
# you can see that because we assign the Image class on the img1 so it has many methods now
# print(dir(Image))


# .filter()
# ImageFilter.BLUR
# .save()
img_filtered = img1.filter(ImageFilter.BLUR)
img_filtered.save("blurcharmander.png", "png")  #you can give any type of extention but to give .jpg you have to actiualy give .jpeg 


# ImageFilter.SMOOTH
img_smooth = img1.filter(ImageFilter.SMOOTH)
img_smooth.save("smoothcharmender.jpeg", "jpeg")


# ImageFilter.SHARPEN
img_sharpen = img1.filter(ImageFilter.SHARPEN)
img_sharpen.save("sharpencharmender.png")


# .convert()
img_convert = img1.convert("1")         #there are more like : "1"
img_convert.save("converted.png")