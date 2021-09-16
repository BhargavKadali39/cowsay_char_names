from cowsay import *
# Here I imported cowsay by * because normally eval() will not take string value inside a variable declared as a function name belonging inside the imported module.
# The only way I thought of is to import them all,so each module function can be called as a normal function inside eval().
from time import sleep
# Sleep() is the only thing we need from time module for slideshow view.

# The dictionary below consists of key as the function name or command used to print the character.
# Value pair as the name of the function which needs to be printed as output.
cowsay_dict = {beavis : 'beavis', cheese : 'cheese', daemon : 'daemon', cow : 'cow', dragon : 'dragon', ghostbusters : 'ghostbusters', kitty : 'kitty', meow : 'meow', milk : 'milk', pig : 'pig', stegosaurus : 'stegosaurus', stimpy : 'stimpy', trex : 'trex', turkey : 'turkey', turtle : 'turtle', tux : 'tux'}
# Try printing str(x) for more clean idea of what is happening.

# X is a key (beavis) i.e without quotations or command.
# Y is value ('beavis') i.e with quotations aka string value
for x, y in cowsay_dict.items():
    eval('x(y)')
    # Inside eval x acts as a command which calls the function inside the X.
    # Y is just a string variable for printing purposes.
    sleep(2)

