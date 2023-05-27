from Enemy import *
from Character import *
from Bullet import *
from pygame import *
import random


init()
screen = display.set_mode((800, 600))
clock = time.Clock()
running = True
ship = Character("assets\Images\Bogdan head 3.jpg",500,300)


backgrounds = [
        'assets/backgrounds/city_1.png',
        'assets/backgrounds/city_2.png',
        'assets/backgrounds/city_3.png',
]
entitys = sprite.Group()
entitys.add(ship)
selected_background = random.choice(backgrounds)
background_image = image.load(selected_background)
background_image = transform.scale(background_image, (800, 600))
screen.blit(background_image, (0, 0))
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    
    for e in event.get():
        if e.type == QUIT:
            running = False
    
    # screen.fill((0,0,0)) #comment this and see what hapen
    # screen.blit(background_image, (0, 0))
    screen.blit(background_image, (0, 0))
    ship.update(screen)
    entitys.draw(screen)
    display.flip()
    display.update()
    dt = clock.tick(60) / 1000