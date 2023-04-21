import pygame
pygame.init()

window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Box walking")


x = 50
y = 50
width = 40
height = 40
speed = 5


run = True
while run:
    pygame.time.delay(100)
    #un fel de sleep dar mai precit  (acest unitati sunt in milisecunde)
    #1000 = 1s , 100 = 0.1 (face 10 verificari pe secunda, un fel de frames )
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed



    window.fill((0,0,0)) #redesenez backroundul in negru
    pygame.draw.rect(window,(255,0,0),(x,y,width,height))
    pygame.display.update()
pygame.quit()