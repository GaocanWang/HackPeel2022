import pygame
import random
import time

height = 0
width = 0
questions = ["269k tons of plastic on ocean surface", "25% of plastic is single use", "4.1k endangered species in the world"]
answers = [pygame.K_t, pygame.K_f, pygame.K_t]
question = 0
answer = pygame.K_t

pygame.init()

screen = pygame.display.set_mode((300, 600))
screen.fill((135, 206, 235))

surf = pygame.Surface((300, 50))
surf.fill((181, 150, 0))
rect = surf.get_rect()

screen.blit(surf, (0, 550))
screen.fill((255, 255, 255), (0, 0, 300, 25))

font = pygame.font.SysFont("monospace", 14)
text = font.render("Are trees good (t = true, f = false)", 1, (0,0,0))
screen.blit(text, (2, 5))

pygame.display.flip()

pygame.draw.rect(screen, (165,42,42), [140, 450, 30, 100])
pygame.draw.polygon(screen, (0,255,0), [[250, 450], [155, 305], [60, 450]])
pygame.draw.polygon(screen, (0,255,0), [[240, 425], [155, 280], [70, 425]])

running = True

while running:
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == answer:
                height = height + 24
                width = width + 4
                randint = random.randint(0, 2)
                question = questions[randint]
                answer = answers[randint]
                if answer == pygame.K_t:
                    wrong_answer = pygame.K_f
                else:
                    wrong_answer = pygame.K_t

                if height == 240:
                    height = 0
                    width = 0

                    screen.fill((255, 255, 255), (0, 0, 300, 25))
                    text = font.render("Tree grown!", 1, (0,0,0))
                    screen.blit(text, (0, 5))

                    pygame.display.flip()
                    time.sleep(1)

                    screen.fill((135, 206, 235))
                    screen.blit(surf, (0, 550))

                    pygame.display.flip()

                    pygame.draw.rect(screen, (165,42,42), [140, 450, 30, 100])

                screen.fill((255, 255, 255), (0, 0, 300, 25))
                text = font.render(question, 1, (0,0,0))
                screen.blit(text, (2, 5))

                pygame.display.flip()

                pygame.draw.polygon(screen, (0,255,0), [[250 - width, 450 - height], [155, 305 - height], [60 + width, 450 - height]])
                pygame.draw.polygon(screen, (0,255,0), [[240 - width, 425 - height], [155, 280 - height], [70 + width, 425 - height]])
            elif event.key == wrong_answer:
                screen.fill((255, 255, 255), (0, 0, 300, 25))
                text = font.render("Incorrect", 1, (0,0,0))
                screen.blit(text, (0, 5))

                pygame.display.flip()
                time.sleep(1)

                randint = random.randint(0, 2)
                question = questions[randint]
                answer = answers[randint]
                if answer == pygame.K_t:
                    wrong_answer = pygame.K_f
                else:
                    wrong_answer = pygame.K_t

                screen.fill((255, 255, 255), (0, 0, 300, 25))
                text = font.render(question, 1, (0,0,0))
                screen.blit(text, (0, 5))

                pygame.display.flip()