import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象

    pygame.init()
    ai_settings = Settings()  # 屏幕大小和背景色的设置

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船

    ship = Ship(ai_settings, screen)

    # 开始游戏的主循环

    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ship)

        ship.update_moving()
        # 重绘屏幕,背景色填充
        # 让最近绘制的屏幕可见
        gf.update_screen(ai_settings, screen, ship)


run_game()
