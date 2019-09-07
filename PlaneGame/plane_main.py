import pygame
from plane_sprites import *


class PlaneGame(object):
    '''飞机大战游戏类'''
    #初始化对象
    def __init__(self):
        # 初始化设置游戏窗口
        pygame.init()
        self.screen = pygame.display.set_mode((480, 800))
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 创建游戏精灵和精灵组
        self.__create_sprite()

    def __create_sprite(self):
        self.screen_sprite = GameSprites("./images/bg_01.png")
        self.screen_sprite.rect = pygame.Rect(0, 0, 480, 800)
        self.screen_spritegroup = pygame.sprite.Group(self.screen_sprite)

        self.hero_sprite = GameSprites("./images/hero.png", 0)
        self.hero_sprite.rect = pygame.Rect(150, 500, 72, 72)
        self.hero_spritegroup = pygame.sprite.Group(self.hero_sprite)

        self.enemy = GameSprites("./images/enemy-1.png")
        self.enemy1 = GameSprites("./images/enemy-1.png")
        self.enemy_spritegroup = pygame.sprite.Group(self.enemy, self.enemy1)

    def start_game(self):
        while True:
            # 设置刷新频率
            self.clock.tick(60)
            # 事件监听
            self.__event_handle()
            

    def __event_handle(self):
        '''事件监听'''
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()




# 开发飞机大战步骤：
# 1 pip3 install pygame 安装pygame
# 2 python -m pygame.examples.aliens 检查是否安装成功
# 3 pygame 主要方法
# 绘制一个游戏画布SCREEN  Rect(x,y,width,height)
# 加载精灵图片,使用screen.blit(hero, (140, 500))添加到画布
# pygame.display.update()方法刷新荧幕
# 4 游戏固定模式：
# 初始化游戏（1设置游戏窗口2绘制图像初始位置3设置游戏时钟）
#游戏循环（1 设置刷新频率 2 检测用户交互 3 更新所有图像位置 4 更新荧幕显示）





    screen_spritegroup.update()
    screen_spritegroup.draw(screen)
    hero_spritegroup.update()
    hero_spritegroup.draw(screen)
    enemy_spritegroup.update()
    enemy_spritegroup.draw(screen)
    pygame.display.update()

