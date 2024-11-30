import pygame
from sys import exit
import os
from random import randint


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

text_surface = test_font.render('My game', False, 'Black')
text_rect = text_surface.get_rect(center=(400, 30))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()

fly_surf = pygame.image.load('graphics/fly/fly1.png').convert_alpha()

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(100, 0))

player_stand = pygame.image.load('graphics/player/player_stand.png')
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

menu_title_surf = test_font.render('Roman\'s game', True, 'White')
menu_title_rect = menu_title_surf.get_rect(center = (400, 50))

menu_hint_surf = test_font.render('Press \"SPACE\" to start the game', True, 'White')
menu_hint_rect = menu_hint_surf.get_rect(center=(400, 350))

obstacle_timer = pygame.USEREVENT = 1
pygame.time.set_timer(obstacle_timer, 1500)

jump_h = 8
player_gravity = 0
game_active = False
start_time = 0


def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = test_font.render(f'Score: {current_time // 1000}', False, (0, 0, 0))
    score_rect = score_surf.get_rect(center= (400, 30))
    screen.blit(score_surf, score_rect)

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 6
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)
            obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.right >= 0]
    return obstacle_list

obstacle_rect_list = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('\nGame over!')
            pygame.quit()
            exit()
        if not game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:                    
                    start_time = pygame.time.get_ticks()
                    player_rect.bottom = 0
                    game_active = True
        if game_active:
            if event.type == obstacle_timer:
                if randint(0, 2):
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright=(randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright=(randint(900, 1100), 210)))

            if event.type == pygame.KEYDOWN:            
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = jump_h
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom == 300:
                if player_rect.collidepoint(event.pos):                
                    player_gravity = jump_h
        
    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))        
        display_score()
        
        player_gravity -= 0.3
        player_rect.bottom -= player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        game_active = collisions(player_rect, obstacle_rect_list)
        
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(menu_title_surf, menu_title_rect)
        screen.blit(menu_hint_surf, menu_hint_rect)
        obstacle_rect_list = []
        player_gravity = 0

    
    
    
    pygame.display.update()
    clock.tick(60) 
