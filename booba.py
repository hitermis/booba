import pygame

pygame.init()

skin = (255, 206, 180)
pink = (241, 156, 187)
red = (254, 127, 156)
runitl = True
myscreen = pygame.display.set_mode((600, 600))

pygame.draw.circle(myscreen, skin, (250, 300), 50)
pygame.draw.circle(myscreen, pink, (250, 300), 15)
pygame.draw.circle(myscreen, red, (250, 300), 5)

pygame.draw.circle(myscreen, skin, (350, 300), 50)
pygame.draw.circle(myscreen, pink, (350, 300), 15)
pygame.draw.circle(myscreen, red, (350, 300), 5)

while runitl:
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runitl = False