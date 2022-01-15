# here we are going to add a package pyjokes that we will get from pipy.org
# but this time we are doing it by pycharm
import pyjokes
joke = pyjokes.get_joke("en", "neutral")
print(joke)

# here to install the pyjokes we execute the command on the terminal pip install pyjokes
# and if you want to unistall the pyjokes we use pip unistall pyjokes