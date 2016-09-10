import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""

        # 此处screen是父窗口传递过来的surface对象
        self.screen = screen

        self.ai_settings = ai_settings
        # 加载飞船图像并获取其外接矩形,不规则图形按照矩形处理,rect是Ship对象的一个内部变量,用来代替image的矩形
        self.image = pygame.image.load_basic('images/ship.bmp')
        self.rect = self.image.get_rect()
        # 拿到父级窗口的的rect属性
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央

        # 屏幕中央,注意centerx是int类型数据,center是整数类型
        self.rect.centerx = self.screen_rect.centerx
        self.centernumber = float(self.rect.centerx)

        # 屏幕底部
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update_moving(self):
        """根据移动标志来调整飞船的位置"""

        # 先得判断是否越界
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # warning: centerx为int类型, center为元组类型,元组不能加减
            self.centernumber += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.centernumber -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += 1
        if self.moving_up and self.rect.top > 0:
            self.rect.bottom -= 1

        self.rect.centerx = self.centernumber

    def blitme(self):
        """在指定位置绘制飞船"""

        # blit():draw one image onto another
        self.screen.blit(self.image, self.rect)
