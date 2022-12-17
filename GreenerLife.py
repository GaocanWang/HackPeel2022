import pygame
import random
import time

height = 0
width = 0
bar_length = 0
questions = ["269k tons of plastic on ocean surface", "25% of plastic is single use", "4.1k endangered species in the world", "Fast fashion = 15% of global emissions", "Methane is more potent than CO2", "Paris agreement signed in 2014", "Reusable bags should be used >35x", "One bus can replace 30-40 cars", "Coal produces 10% of electricity", "Veggies produce lots of emissions", "Glass is infinitely recyclable"]
answers = [pygame.K_t, pygame.K_f, pygame.K_t, pygame.K_f, pygame.K_t, pygame.K_f, pygame.K_t, pygame.K_t, pygame.K_f, pygame.K_f, pygame.K_t]
solutions = ["it's true", "it's false, it's 50%", "it's true", "it's false, it's 10%", "it's true", "it's false, it's 2015", "it's true", "it's true", "it's false, it's 40", "it's false, meat produce way more", "it's true"]
question = 0
answer = pygame.K_t
wrong_answer = pygame.K_f
tree_number = 1
randint = 0

pygame.init()

pygame.display.set_caption('Greener Life')
pygame.display.set_icon(pygame.image.load('icon.jpg'))

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
font = pygame.font.SysFont("monospace", 20)
text = font.render("Tree Number: " + str(tree_number), 1, (0,0,0))
screen.blit(text, (75, 565))

pygame.display.flip()

pygame.draw.rect(screen, (255,255,255), [275, 25, 300, 525])
pygame.draw.rect(screen, (255, 255, 0), [277, 523, 21, 25])
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
                bar_length = bar_length + 50
                randint = random.randint(0, 10)
                question = questions[randint]
                answer = answers[randint]
                if answer == pygame.K_t:
                    wrong_answer = pygame.K_f
                else:
                    wrong_answer = pygame.K_t

                pygame.draw.rect(screen, (255, 255, 0), [277, 523 - bar_length, 21, 25])

                if height == 240:
                    height = 0
                    width = 0
                    bar_length = 0
                    tree_number = tree_number + 1

                    screen.fill((255, 255, 255), (0, 0, 300, 25))
                    text = font.render("Tree grown!", 1, (0,0,0))
                    screen.blit(text, (0, 5))

                    pygame.display.flip()
                    time.sleep(1)

                    screen.fill((135, 206, 235))
                    screen.blit(surf, (0, 550))
                    font = pygame.font.SysFont("monospace", 20)
                    text = font.render("Tree Number: " + str(tree_number), 1, (0,0,0))
                    screen.blit(text, (75, 565))

                    pygame.display.flip()

                    pygame.draw.rect(screen, (255,255,255), [275, 25, 300, 525])
                    pygame.draw.rect(screen, (255, 255, 0), [277, 523, 21, 25])
                    pygame.draw.rect(screen, (165,42,42), [140, 450, 30, 100])

                screen.fill((255, 255, 255), (0, 0, 300, 25))
                font = pygame.font.SysFont("monospace", 14)
                text = font.render(question, 1, (0,0,0))
                screen.blit(text, (2, 5))

                pygame.display.flip()

                pygame.draw.polygon(screen, (0,255,0), [[250 - width, 450 - height], [155, 305 - height], [60 + width, 450 - height]])
                pygame.draw.polygon(screen, (0,255,0), [[240 - width, 425 - height], [155, 280 - height], [70 + width, 425 - height]])
            elif event.key == wrong_answer:
                screen.fill((255, 255, 255), (0, 0, 300, 25))
                font = pygame.font.SysFont("monospace", 14)
                text = font.render(solutions[randint], 1, (0,0,0))
                screen.blit(text, (0, 5))

                pygame.display.flip()
                time.sleep(1)

                randint = random.randint(0, 10)
                question = questions[randint]
                answer = answers[randint]
                if answer == pygame.K_t:
                    wrong_answer = pygame.K_f
                else:
                    wrong_answer = pygame.K_t

                screen.fill((255, 255, 255), (0, 0, 300, 25))
                font = pygame.font.SysFont("monospace", 14)
                text = font.render(question, 1, (0,0,0))
                screen.blit(text, (0, 5))

                pygame.display.flip()
