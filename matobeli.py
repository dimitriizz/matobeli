import pygame

#tehdä se näyttö missä peliä pelataa
pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption('Mato Beli')

sini=(0,0,255)
red=(255,0,0)

game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    pygame.draw.rect(dis,sini,[200,150,10,10])
    pygame.display.update()

pygame.quit()
quit()