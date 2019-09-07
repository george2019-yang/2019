import pygame

class GameSprites(pygame.sprite.Sprite):
    '''定义游戏精灵类'''
    def __init__(self,image_name,speed = 1):
        super().__init__()
        self.speed = speed
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += self.speed


class HeroSprites(GameSprites):
    pass