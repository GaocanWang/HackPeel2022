import pygame

pygame.init()

screen = pygame.display.set_mode((300, 600))

screen.fill((135, 206, 235))

surf = pygame.Surface((300, 50))

surf.fill((181, 150, 0))

rect = surf.get_rect()

screen.blit(surf, (0, 550))

pygame.display.flip()

pygame.draw.rect(screen, (165,42,42), [140, 450, 30, 100])
pygame.draw.polygon(screen, (0,255,0), [[250, 450], [155, 305], [60, 450]])
pygame.draw.polygon(screen, (0,255,0), [[240, 425], [155, 280], [70, 425]])

height = 0
width = 0

running = True

while running:
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                height = height + 24
                width = width + 4

                if height == 240:
                    height = 0
                    width = 0
                    screen.fill((135, 206, 235))
                    screen.blit(surf, (0, 550))
                    pygame.display.flip()
                    pygame.draw.rect(screen, (165,42,42), [140, 450, 30, 100])

                pygame.draw.polygon(screen, (0,255,0), [[250 - width, 450 - height], [155, 305 - height], [60 + width, 450 - height]])
                pygame.draw.polygon(screen, (0,255,0), [[240 - width, 425 - height], [155, 280 - height], [70 + width, 425 - height]])
