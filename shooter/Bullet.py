from pygame import *

class Bullet(sprite.Sprite): #in the parentheses it is indicated that the class inherits from the Sprite class

    image_path = ""
    def __init__(self, x, y):
       sprite.Sprite.__init__(self) #mandatory calling of the constructor of the parent class
       # each sprite should store the image property—its image
       self.image = image.load(self.image_path)
       self.image = transform.scale(self.image, (64,64)) # resize the image
 
       # each sprite should store the rect property—the rectangle into which it is inscribed
       self.rect = self.image.get_rect() #we get a rectangle from the image
       #we set its location
       self.rect.x = x
       self.rect.y = y
   #method defining the sprite’s movement
    def update(self):
        self.rect.y += 1

    
    