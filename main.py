import pygame
from random import randint
from pygame.locals import (

    K_UP,

    K_DOWN,

    K_LEFT,

    K_RIGHT,

    K_ESCAPE,

    KEYDOWN,

    QUIT,

)

color = (255,255,255)
screen_w = 800
screen_h = 600
circle_x = screen_w / 2 
circle_y = screen_h / 2
circle_r = 20
rect_w  = 20
rect_h = 20
rect_x = randint(rect_w, screen_w - rect_w)
rect_y = randint(rect_h, screen_h - rect_h)
percorrido = 0
collides = 0


pygame.init()
screen = pygame.display.set_mode([screen_w, screen_h])

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if circle_x != circle_r:
            circle_x -= 1
            percorrido += 1

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if circle_x != screen_w - circle_r:
            circle_x += 1
            percorrido += 1

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        if circle_y != circle_r:
            circle_y -= 1
            percorrido += 1

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if circle_y != screen_h - circle_r:
            circle_y += 1
            percorrido += 1
        #else:
        #    if circle_r >=20:
        #        circle_r -=10
        #        circle_y = circle_y
        #    else:    
        #        circle_y = circle_y

    screen.fill((0, 0, 0))
    
    rect = pygame.draw.rect(screen, color , pygame.Rect(rect_x, rect_y, rect_w, rect_w))
    circle = pygame.draw.circle(screen, (0, 0, 255), (circle_x, circle_y), circle_r)
    collide = pygame.Rect.colliderect(circle, rect)

    if collide:
        rect_x = randint(rect_w, screen_w - rect_w)
        rect_y = randint(rect_h, screen_h - rect_h)
        collides += 1
        circle_r += 10
    




    pygame.draw.circle(screen, (0, 0, 255), (circle_x, circle_y), circle_r)


    pygame.font.init()
    my_font = pygame.font.SysFont(None, 20)
    pos_x = my_font.render('Posição X: '+str(circle_x), False, (255, 255, 255))
    pos_y = my_font.render('Posição Y: '+str(circle_y), False, (255, 255, 255))
    percorrido_value = my_font.render('Distância percorrida: '+str(percorrido), False, (255, 255, 255))
    colisoes = my_font.render('Colisões: '+str(collides), False, (255, 255, 255))
    screen.blit(pos_x, (0,0))
    screen.blit(pos_y, (0,20))
    screen.blit(percorrido_value, (0,40))
    screen.blit(colisoes, (0,60))




    pygame.display.flip()

pygame.quit()