from cowsay import *
from time import sleep


cowsay_dict = {beavis : 'beavis', cheese : 'cheese', daemon : 'daemon', cow : 'cow', dragon : 'dragon', ghostbusters : 'ghostbusters', kitty : 'kitty', meow : 'meow', milk : 'milk', pig : 'pig', stegosaurus : 'stegosaurus', stimpy : 'stimpy', trex : 'trex', turkey : 'turkey', turtle : 'turtle', tux : 'tux'}

for x, y in cowsay_dict.items():
    eval('x(y)')
    sleep(2)

