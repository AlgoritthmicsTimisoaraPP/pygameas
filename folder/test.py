
from pygame import *
import random
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
       self.start_x = x
       self.start_y = y
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
    def reset_position(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
class Wall(sprite.Sprite): 
    def __init__(self, image_path, x, y):
        sprite.Sprite.__init__(self) 
        self.image = image.load(image_path)
        self.image = transform.scale(self.image, (64,64)) # resize the image
        self.rect = self.image.get_rect() #we get a rectangle from the image
        #we set its location
        self.rect.x = x
        self.rect.y = y


class Win(Wall):
    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y)
    def print_win():
        print("You win for now...")

class Enemy(Wall):
    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y)
    def move(self):
        rx = random.randint(0, 25)
        ry = random.randint(0, 25)
        dx = random.randint(-1, 1)
        dy = random.randint(-1, 1)
        self.rect.x = (rx * dx) + self.rect.x
        self.rect.y = (ry * dy) + self.rect.y

        if (self.rect.x >= 740):
            self.rect.x -= 30
        elif (self.rect.x <= 0):
            self.rect.x += 30
        elif (self.rect.y >= 540):
            self.rect.y -= 30
        elif (self.rect.y <= 0):
            self.rect.y += 30
        



def change_background():
    backgrounds = [
        'assets/backgrounds/city_1.png',
        'assets/backgrounds/city_2.png',
        'assets/backgrounds/city_3.png',
    ]
    selected_background = random.choice(backgrounds)
    background_image = image.load(selected_background)
    background_image = transform.scale(background_image, (800, 600))
    return background_image

def change_background_win():
    selected_background = "assets/backgrounds/winner_1.jpg"
    background_image = image.load(selected_background)
    background_image = transform.scale(background_image, (800, 600))
    return background_image
def change_background_lose():
    selected_background = "assets/level/NOOB.png"
    background_image = image.load(selected_background)
    background_image = transform.scale(background_image, (800, 600))
    return background_image


init()
screen = display.set_mode((800, 600))
clock = time.Clock()
running = True

levels = list()
enemies= list()

characters = sprite.Group()
character = Character('assets/level/hero.png',100,100)
characters.add(character)
win = Win("assets/level/trophy-1.png",400,400)
characters.add(win)

for i in range(3):
    levels.append(sprite.Group())



# wall1 = Wall('assets/backgrounds/cave.png',500,500)
walls1 = [
    Wall('assets/backgrounds/cave.png', 300, 0),
    Wall('assets/backgrounds/cave.png', 300, 64),
    Wall('assets/backgrounds/cave.png', 300, 128),
    Wall('assets/backgrounds/cave.png', 300, 192),
    Wall('assets/backgrounds/cave.png', 300, 256),
    Wall('assets/backgrounds/cave.png', 300, 320)
]
levels[0].add(walls1)


walls2 = list()
for i in range(5):
    walls2.append( Wall('assets/backgrounds/cave.png', 64+i*64, 320))
    walls2.append( Wall('assets/backgrounds/cave.png', 64+i*64, 320-i*64))

walls3 = list()
for i in range(5):
    walls2.append( Wall('assets/backgrounds/cave.png', 64+i*2*64, 320))
    walls2.append( Wall('assets/backgrounds/cave.png', 320-i*64,384))

enemy = Enemy("assets/level/enemy.png",600,600)
enemy1 = Enemy("assets/level/enemy.png",600,600)
enemy2 = Enemy("assets/level/enemy.png",200,200)
enemy3 = Enemy("assets/level/enemy.png",300,200)
enemy4 = Enemy("assets/level/enemy.png",400,500)

levels[1].add(walls2)
levels[2].add(walls3)

levels[0].add(enemy)
levels[1].add(enemy)
levels[2].add(enemy)
levels[2].add(enemy1)
levels[2].add(enemy2)
levels[2].add(enemy3)
levels[2].add(enemy4)
enemies.append(enemy)
enemies.append(enemy)
enemies.append(enemy)
enemies.append(enemy1)
enemies.append(enemy2)
enemies.append(enemy3)
enemies.append(enemy4)

background_image = change_background()
level_nr = 0
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for e in event.get():
        if e.type == QUIT:
            running = False
    character.update()
    screen.fill((0,0,0)) #comment this and see what hapen
    screen.blit(background_image, (0, 0))
    characters.draw(screen)
    levels[level_nr].draw(screen)
    
    for wall in levels[level_nr]:
        if sprite.collide_rect(character, wall):
            character.reset_position()
            background_image = change_background()
            screen.blit(background_image, (0, 0))
    
    for e in levels[level_nr]:
        if isinstance(e, Enemy):
            e.move()
            if sprite.collide_rect(character, e):
                change_background_lose()

    if sprite.collide_rect(character, win):
        if level_nr < 2: 
            level_nr += 1
        else:
            background_image = change_background_win()
            screen.blit(background_image, (0, 0))
            characters.remove(win)
        character.reset_position()
    # flip() the display to put your work on screen
    display.flip()
    dt = clock.tick(60) / 1000
