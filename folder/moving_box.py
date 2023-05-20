from random import randint
from pygame import *



display.set_caption("Bogdan invaders")
background = image.load("assets/backgrounds/nightlight.png")

screen = display.set_mode((800, 600))
clock = time.Clock()
running = True

class Enemy(sprite.Sprite):
    def __init__(self, image_path, x, y):
       sprite.Sprite.__init__(self) 
       self.image = image.load(image_path)
       self.image = transform.scale(self.image, (50,50)) 
       self.rect = self.image.get_rect()
       self.start_x = x
       self.start_y = y
       self.rect.x = x
       self.rect.y = y
   
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
           self.rect.x -= 5
        if keys[K_RIGHT] and self.rect.x < 740:
           self.rect.x += 5
enemy = Enemy("assets/heroes/spaceship/rocket_2.png",100,100)
while running:
    screen.blit(background, (0, 0))
    enemy.draw(screen)
    for e in event.get():
        if e.type == QUIT:
            running = False
    display.update()
    display.flip()
    dt = clock.tick(60) / 1000
