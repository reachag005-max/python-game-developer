import pygame

pygame.init()
screen = pygame.display.set_mode((600,400))

class rectangle():
    def __init__(self):
        self.color = "yellow"
        self.length = 100
        self.width = 50
        self.dimention = (300,400,100,50)
        print("All rectangle properties where complete rectangle avalible to draw")

    def draw(self):
        pygame.draw.rect(screen,self.color,self.dimention)
        print("Draw function was complete")

yellowrect = rectangle()
yellowrect.draw()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.update()