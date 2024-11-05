import pygame

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')


x = 200
y = 200
img = pygame.image.load('C:\Users\tyrel\PycharmProjects\HelloWorld\SHOOTER  GAME\Shooter-main\Shooter-main\img\player\Idle\0.png')
rect = img.get_rect()


run = True
while run:

    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False


pygame.quit()