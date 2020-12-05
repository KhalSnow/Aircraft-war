# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 22:25:16 2020

@author: Wyh
"""

import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

# Respond to keydown events. 
def respond_keydown_events(event, setting, screen, rocket, bullets):
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_UP:
        rocket.moving_up = True
        rocket.heading_up = True
        rocket.heading_down = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = True
        rocket.heading_up = False
        rocket.heading_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(setting, screen, rocket, bullets)
    elif event.key == pygame.K_q:
        pygame.quit()

# Respond to keyup events. 
def respond_keyup_events(event, rocket):
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False
    elif event.key == pygame.K_UP:
        rocket.moving_up = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = False

# Respond to keypresses and mouse events. 
def respond_events(setting, screen, states, scoreboard, rocket, aliens, bullets, play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            respond_keydown_events(event, setting, screen, rocket, bullets)
        elif event.type == pygame.KEYUP:
            respond_keyup_events(event, rocket)
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            mouse_x, mouse_y = pygame.mouse.get_pos() 
            check_play_button(setting, screen, states, scoreboard, play_button, rocket, aliens, bullets, mouse_x, mouse_y)

# Update screen. 
def screen_update(setting, screen, states, scoreboard, rocket, aliens, bullets, play_button):
    screen.fill(setting.background_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    rocket.blit()
    aliens.draw(screen)
    scoreboard.show_score()
    if not states.game_active:
        play_button.draw_button()
    pygame.display.flip()

# Update bullets. 
def update_bullets(setting, screen, states, scoreboard, rocket, aliens, bullets):
    bullets.update(rocket)
    # Delete missing bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0 or bullet.rect.bottom >= rocket.screen_rect.bottom:
            bullets.remove(bullet)
    check_bullet_alien_collisions(setting, screen, states, scoreboard, rocket, aliens, bullets)

def check_bullet_alien_collisions(setting, screen, states, scoreboard, rocket, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            states.score += setting.alien_points * len(aliens)
            scoreboard.prep_score()
        check_highest_score(states, scoreboard)
    if len(aliens) == 0:
        bullets.empty()
        create_aliens(setting, screen, rocket, aliens)

# Fire bullets. 
def fire_bullet(setting, screen, rocket, bullets):
    if len(bullets) < setting.bullets_max:
        new_bullet = Bullet(setting, screen, rocket)
        bullets.add(new_bullet)

# Get number of aliens each row. 
def get_number_aliens_x(setting, alien_width):
    available_space_x = setting.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

# Create an alien. 
def create_alien(setting, screen, aliens, alien_number, row_number):
    alien = Alien(setting, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 10 * alien.rect.height * row_number
    aliens.add(alien)

# Create aliens. 
def create_aliens(setting, screen, rocket, aliens): 
    alien = Alien(setting, screen)
    number_aliens_x = get_number_aliens_x(setting, alien.rect.width)

    number_rows = alien.row_number
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(setting, screen, aliens, alien_number, row_number)

# Check aliens edge. 
def check_aliens_edge(setting, aliens):
    for alien in aliens.sprites():
        if alien.check_edge():
            change_aliens_direction(setting, aliens)
            break

# Change aliens direction. 
def change_aliens_direction(setting, aliens):
    for alien in aliens.sprites():
        if alien.rect.y <= setting.screen_height / 2:
            alien.rect.y += setting.aliens_drop_speed
        else:
            alien.rect.y -= setting.aliens_drop_speed
    setting.aliens_direction *= -1

# Update aliens. 
def update_aliens(setting, screen, states, scoreboard, rocket, aliens, bullets):
    check_aliens_edge(setting, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(rocket, aliens):
        rocket_hit(setting, screen, states, scoreboard, rocket, aliens, bullets)
    check_alien_bottom(setting, screen, states, scoreboard, rocket, aliens, bullets)
    
# Rocket hit. 
def rocket_hit(setting, screen, states, scoreboard, rocket, aliens, bullets):
    if states.rocket_left > 0:
        states.rocket_left -= 1
        
        scoreboard.prep_rockets()
    
        aliens.empty()
        bullets.empty()
        
        create_aliens(setting, screen, rocket, aliens)
        rocket.center_rocket()
        
        sleep(0.5)
    else:
        states.game_active = False
        pygame.mouse.set_visible(True)

# Check alien bottom. 
def check_alien_bottom(setting, screen, states, scoreboard, rocket, aliens, bullets):
    # screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.y == setting.screen_height / 2:
        # if alien.rect.bottom >= screen_rect.bottom:
            rocket_hit(setting, screen, states, scoreboard, rocket, aliens, bullets)
            break
        
# Check play button. 
def check_play_button(setting, screen, states, scoreboard, play_button, rocket, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not states.game_active:
        pygame.mouse.set_visible(False)
        
        states.reset_states()
        states.game_active = True
        
        scoreboard.prep_score()
        scoreboard.prep_highest_score()
        scoreboard.prep_rockets()
        
        aliens.empty()
        bullets.empty()
        
        create_aliens(setting, screen, rocket, aliens)
        rocket.center_rocket()
        
# Check highest score. 
def check_highest_score(states, scoreboard):
    if states.score > states.highest_score:
        states.highest_score = states.score
        scoreboard.prep_highest_score()