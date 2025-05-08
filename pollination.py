import random,pgzrun
HEIGHT=400
WIDTH=400
TITLE="Pollination game"
bee=Actor("bee")
flower=Actor("flower")
d=[bee,flower]
score=0
gameover=False
for i in d:
    i.pos=random.randint(0,400),random.randint(0,400)

def draw():
    screen.blit("bgforrest",(0,0))
    for i in d:
        i.draw()
    print(score)
def on_key_down(key):
    global score
    if key==keys.LEFT:
        bee.x-=5
    elif key==keys.RIGHT:
        bee.x+=5
    elif key==keys.UP:
        bee.y-=5
    elif key==keys.DOWN:
        bee.y+=5
    
    if bee.colliderect(flower):
       score+=1
       for i in d:
         i.pos=random.randint(0,400),random.randint(0,400)

def timer ():
    global gameover
    gameover=True
    print(gameover)

clock.schedule(timer,10)
pgzrun.go()