
from pygame import *

#main player class—Characters
class Character(sprite.Sprite): #in the parentheses it is indicated that the class inherits from the Sprite class
    #creating the constructor
    def __init__(self, image_path, x, y):
       sprite.Sprite.__init__(self) #mandatory calling of the constructor of the parent class
       # each sprite should store the image property—its image
       self.image = image.load(image_path)
       self.image = transform.scale(self.image, (64,64)) # resize the image
 
       # each sprite should store the rect property—the rectangle into which it is inscribed
       self.rect = self.image.get_rect() #we get a rectangle from the image
       #we set its location
       self.rect.x = x
       self.rect.y = y
   #method defining the sprite’s movement
    def update(self):

        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
           self.rect.x -= 5
        if keys[K_RIGHT] and self.rect.x < 740:
           self.rect.x += 5
        if keys[K_UP] and self.rect.y > 0:
           self.rect.y -= 5
        if keys[K_DOWN] and self.rect.y < 540:
           self.rect.y += 5

class Wall(sprite.Sprite): 
    def __init__(self, image_path, x, y):
        sprite.Sprite.__init__(self) 
        self.image = image.load(image_path)
        self.image = transform.scale(self.image, (64,64)) # resize the image
        self.rect = self.image.get_rect() #we get a rectangle from the image
        #we set its location
        self.rect.x = x
        self.rect.y = y

init()
screen = display.set_mode((800, 600))
clock = time.Clock()
running = True


character = Character('assets/level/hero.png',100,100)

sprite_group = sprite.Group()
sprite_group.add(character)
sprite_group.draw(screen)


wall1 = Wall('assets/backgrounds/cave.png',500,500)
sprite_group.add(wall1)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for e in event.get():
        if e.type == QUIT:
            running = False
    character.update()
    screen.fill((0,0,0)) #comment this and see what hapen
    sprite_group.draw(screen)

    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")
    if sprite.collide_rect(character, wall1):
        print("touch")

    # flip() the display to put your work on screen
    display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
