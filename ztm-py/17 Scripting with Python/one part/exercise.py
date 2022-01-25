# jpg to png convertor


# os.path.exists()
# os.makedirs()


from distutils.command.clean import clean
import sys  #sys help you to get the parameters with the running the file
import os   
from PIL import Image

img_folder = sys.argv[1]
output_folder = sys.argv[2]

print(img_folder, output_folder)

# now we have to check if the new foldfer is exist if not then we have to create it
# by importing the os module you can check if the specific path present or not #there is another module that you can use to check if the file is present or not that is pathlib
if not os.path.exists(output_folder): #it will return true if it exist or it will return the false # also we assign the not at the front the condition if it return the flase then only it will execute
    os.makedirs(output_folder)        # it will create the new folder name new
    print(f"the new file {output_folder} has been created")

for each_file in os.listdir(img_folder):    # os.listdir gives you the list of each item in the list for example ['astro.jpg', 'bulbasaur.jpg', 'charmander.jpg', 'pikachu.jpg', 'squirtle.jpg'] 
    if each_file == "astro.jpg":    #it will not contain the astro img
        continue    
    img = Image.open(f"{img_folder}{each_file}")
    clean_name = os.path.splitext(each_file)[0]
    img.save(f"{output_folder}{clean_name}.png", "png")
    print("all done")



# you can search about the open cv
# this is an very important topic