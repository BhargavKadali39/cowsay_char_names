# cowsay_char_names
This repo is about all the characters provided by cowsay.  
This repo is based on python module cowsay which has a unique way of showing output to the user.  
My favourite character is tux.Try it out yourself to find your favourites.  

Including the module cowsay I also used dictionary key-value calling integrated with eval() function.  
Time module is also used in here,so the user can have a slideshow view of all charaters.  
Some of the script is dynamically typed by the provided dictionary's keys and values and eval() .  

warning: I used eval() fun here for only learning purpose and it could potentially cause harm on your project's where the user can give his own string commands to access some authorized data or for other malicious work.


>from cowsay import *

Here I imported cowsay as * i.e all function in the module can be used without prior usage of module name ex: cowsay.FUNCTION().  
Normally eval() will not take string value inside a variable, so I declared it as a function name which belongs to the imported module(cowsay).
The only way I thought of is to import them all, so each module function can be called as a normal function inside eval() then be accessed by any loop.

>from time import sleep

Sleep() is the only thing we need from time module for slideshow view.  
After importing  

The dictionary below consists of key as the function name or command used to print the character.  
Value pair as the name of the function which needs to be printed as output.  

>cowsay_dict = {beavis : 'beavis', cheese : 'cheese', daemon : 'daemon', cow : 'cow', dragon : 'dragon', ghostbusters : 'ghostbusters', kitty : 'kitty', meow : 'meow', milk : 'milk', pig : 'pig', stegosaurus : 'stegosaurus', stimpy : 'stimpy', trex : 'trex', turkey : 'turkey', turtle : 'turtle', tux : 'tux'}

Try printing str(x) for more clean idea of what is happening.  

Here X is a key (beavis) i.e without quotations or command.  
Similarly Y is value ('beavis') i.e with quotations aka string value  

>for x, y in cowsay_dict.items():
>    eval('x(y)')
 
Inside eval x acts as a command which calls the function inside the X.  
Y is just a string variable for printing purposes.  
    
>sleep(2)

Sleep is for maintaining a time gap.  
