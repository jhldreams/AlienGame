import pygame


class Ship():
    def __init__(self, screen):
        """初始化飞船并设置其初始位置"""

        # 此处screen是父窗口传递过来的surface对象
        self.screen = screen

        # 加载飞船图像并获取其外接矩形

        # 将不规则图形按照矩形处理,rect是Ship对象的一个内部变量,用来代替image的矩形
        # screen_rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # 拿到父级窗口的的rect属性
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央

        # 屏幕中央,注意这些值是坐标
        self.rect.center = self.screen_rect.center

        print(self.rect.center)
        # 屏幕底部
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""

        # blit():draw one image onto another
        self.screen.blit(self.image, self.rect)
