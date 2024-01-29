from pygame import *


window = display.set_mode((700,500))
background = transform.scale(image.load('background.png'),(700,500))
display.set_caption('Догонялки')


sprite_1 = transform.scale(image.load('sprite1.png'),(50,50))
sprite_2= transform.scale(image.load('sprite2.png'),(50,50))
x1 = 100
x2 = 600
y1 = 400
y2 = 400

clock = time.Clock()
FPS = 30
speed = 5


game = True
while game:

    window.blit(background,(0,0))

    for i in event.get():
        if i.type == QUIT:
            game = False
    key_pressed = key.get_pressed()
    if key_pressed[K_UP] and y1 > 0:
        y1 -= speed
    if key_pressed[K_DOWN] and y1 < 450:
        y1 +=speed
    if key_pressed[K_LEFT] and x1 > 0:
        x1 -= speed
    if key_pressed[K_RIGHT] and x1 < 650:
        x1 += speed
    if key_pressed[K_s] and y2 < 450:
        y2 += speed
    if key_pressed[K_w] and y2 > 0:
        y2 -= speed
    if key_pressed[K_a] and x2 > 0:
        x2 -= speed
    if key_pressed[K_d] and x2 < 650:
        x2 += speed


    window.blit(sprite_1,(x1,y1))
    window.blit(sprite_2,(x2,y2))
    clock.tick(FPS)
    display.update()



    player.reset()
    player.rect.x = 100
    player.rect.y = 50
