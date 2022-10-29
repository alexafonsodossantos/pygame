import pygame
from random import randint
from classes import Pedaco
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
collides = 0
esq = False
direita = False
cima = False
baixo = False
cobra = []
new_block = [-1,-1]
tamanho = 1
screen_collide = False
pygame.init()
screen = pygame.display.set_mode([screen_w, screen_h])

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            esq = True
            direita = False
            cima = False
            baixo = False

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            esq = False
            direita = True
            cima = False
            baixo = False

    if keys[pygame.K_UP] or keys[pygame.K_w]:
            esq = False
            direita = False
            cima = True
            baixo = False

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            esq = False
            direita = False
            cima = False
            baixo = True

    if cima:
        if circle_y != circle_r:
            circle_y -=1
            for p in cobra:
                i = cobra.index(p)
                if i == 0:
                    p.y = circle_y + circle_r * 2
                    
                else:
                    p.y = cobra[i-1].y + circle_r * 2

        else:
            screen_collide = True

    if baixo:
        if circle_y != screen_h - circle_r:
            circle_y +=1

            for p in cobra:
                i = cobra.index(p)
                if i == 0:
                    p.y = circle_y - circle_r * 2
                    
                else:
                    p.y = cobra[i-1].y - circle_r * 2
            

    if esq:
        if circle_x != circle_r:
            circle_x -=1
            for p in cobra:
                i = cobra.index(p)
                if i == 0:
                    p.x = circle_x + circle_r * 2
                    
                else:
                    p.x = cobra[i-1].x + circle_r * 2
           
        else:
            screen_collide = True


    if direita:
        if circle_x != screen_w - circle_r:
            circle_x +=1

            for p in cobra:
                i = cobra.index(p)
                if i == 0:
                    p.x = circle_x - circle_r * 2
                    
                else:
                    p.x = cobra[i-1].x - circle_r * 2
            
        else:
            screen_collide = True


    screen.fill((0, 0, 0))
    
    rect = pygame.draw.rect(screen, color , pygame.Rect(rect_x, rect_y, rect_w, rect_w))
    

    cabeca = pygame.draw.circle(screen, (0, 0, 255), (circle_x, circle_y), circle_r)

    collide = pygame.Rect.colliderect(cabeca, rect)

    if collide:
        rect_x = randint(rect_w, screen_w - rect_w)
        rect_y = randint(rect_h, screen_h - rect_h)
        collides += 1
        pdc = Pedaco(screen)
        pdc.x = circle_x
        pdc.y = circle_y
        cobra.append(pdc)

    for p in cobra:
        if p.x != circle_x + circle_r * 2 or p.y != circle_y + circle_r*2:
            p.draw()


    

    


            
    

    
    if screen_collide:
        screen.fill((0, 0, 0))
        circle_x = screen_w / 2
        circle_y = screen_h / 2 
        esq = False
        direita = False
        cima = False
        baixo = False
        collides = 0
        pygame.display.flip()
        screen_collide = False
        
    

    


    pygame.font.init()
    my_font = pygame.font.SysFont(None, 20)
    pos_x = my_font.render('Posição X: '+str(circle_x), False, (255, 255, 255))
    pos_y = my_font.render('Posição Y: '+str(circle_y), False, (255, 255, 255))
    display_rect_x = my_font.render('Posição X Rect: '+str(rect_x), False, (255, 255, 255))
    display_rect_y = my_font.render('Cobra: '+str(len(cobra)), False, (255, 255, 255))
    colisoes = my_font.render('Colisões: '+str(collides), False, (255, 255, 255))
    screen.blit(pos_x, (0,0))
    screen.blit(pos_y, (0,20))
    screen.blit(colisoes, (0,40))
    screen.blit(display_rect_x, (0,60))
    screen.blit(display_rect_y, (0,80))




    pygame.display.flip()

pygame.quit()