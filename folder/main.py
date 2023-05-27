from Enemy import *
from Character import *
from Bullet import *
from pygame import *
import random


init()
screen = display.set_mode((800, 600))
clock = time.Clock()
running = True
ship = Character("assets\\heroes\\UFO\\ufo_1.png",300,300)
enemy = Enemy("assets\\heroes\\spaceship\\rocket_3.png",300,100)

backgrounds = [
        'assets/backgrounds/city_1.png',
        'assets/backgrounds/city_2.png',
        'assets/backgrounds/city_3.png',
]
entitys = sprite.Group()
entitys.add(ship)
entitys.add(enemy)
selected_background = random.choice(backgrounds)
background_image = image.load(selected_background)
background_image = transform.scale(background_image, (800, 600))
screen.blit(background_image, (0, 0))
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    
    screen.blit(background_image, (0, 0))

    ship.update(screen)
    entitys.draw(screen)
    display.flip()
    display.update()
    dt = clock.tick(60) / 1000