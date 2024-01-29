from pygame import *


window = display.set_mode((700,500))
background = transform.scale(image.load('background.png'),(700,500))
display.set_caption('Догонялки')

font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, picture, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(picture),(width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP]:
            self.rect.y -= 5
        if key_pressed[K_DOWN]:
            self.rect.y += 5
        if key_pressed[K_LEFT]:
            self.rect.x -= 5
        if key_pressed[K_RIGHT]:
            self.rect.x += 5
    def say(self, phraze):
        self.text = font.SysFont('Arial', 40).render(phraze, True, (255, 0, 0))
    def draw_phraze(self):
        window.blit(self.text, (self.rect.x + 100, self.rect.y - 50))


player = Player('sprite1.png', 100, 50, 100, 100)
enemy = GameSprite('sprite2.png', 300, 250, 100, 100)
player.say("")


player.rect.y = 0

enemy.rect.x = 0


clock = time.Clock()
FPS = 30
speed = 5


game = True
while game:

    window.blit(background,(0,0))
    player.reset()
    player.update()
    enemy.reset()
    for i in event.get():
        if i.type == QUIT:
            game = False
        if i.type == KEYDOWN:
            if i.key == K_SPACE:
                player.say('Hello!')
    player.draw_phraze()
    if sprite.collide_rect(player, enemy):
        ogogo = font.SysFont('Arial', 40).render('Огого', True, (255, 0, 0))
        window.blit(ogogo, (250, 250))

    # key_pressed = key.get_pressed()
    # if key_pressed[K_UP] and y1 > 0:
    #     y1 -= speed
    # if key_pressed[K_DOWN] and y1 < 450:
    #     y1 +=speed
    # if key_pressed[K_LEFT] and x1 > 0:
    #     x1 -= speed
    # if key_pressed[K_RIGHT] and x1 < 650:
    #     x1 += speed


    clock.tick(FPS)
    display.update()