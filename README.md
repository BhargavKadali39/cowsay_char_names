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
