import pygame
import sys
import random
def check_events(ship):
    """响应按键和鼠标事件"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydownevents(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyupevents(event, ship)


def check_keydownevents(event, ship):
    """响应按键按下"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True


def check_keyupevents(event, ship):
    """响应按键松开"""
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False
        elif event.key == pygame.K_DOWN:
            ship.moving_down = False
        elif event.key == pygame.K_UP:
            ship.moving_up = False


def update_screen(ai_settings, screen, ship):
    """更新屏幕上的头像,并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    pygame.display.flip()
