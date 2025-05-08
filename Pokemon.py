import random,pgzrun
HEIGHT=400
WIDTH=400
TITLE="Pokemon"
ash=Actor("ash")
pikachu=Actor("pikachu")
a=[ash,pikachu]

for i in a:
    i.pos=random.randint(0,400),random.randint(0,400)


def draw():
    screen.blit("pokemonbackround",(0,0))
    # for i in a:
    #    # i.draw()


pgzrun.go()