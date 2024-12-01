import pygame
from pathlib import Path

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        """初始化武器"""
        super().__init__(groups)
        self.sprite_type = 'weapon'

        # 获取玩家当前方向
        direction = player.status.split('_')[0]

        # 动态生成武器资源路径
        try:
            weapon_base_path = Path(__file__).resolve().parent.parent / 'graphics' / 'weapons' / player.weapon
            full_path = weapon_base_path / f'{direction}.png'
            self.image = pygame.image.load(str(full_path)).convert_alpha()
            print(f"Weapon image loaded successfully: {full_path}")
        except FileNotFoundError as e:
            print(f"Weapon image not found for direction '{direction}': {e}")
            self.image = pygame.Surface((40, 40))  # 生成占位图像，防止程序崩溃
            self.image.fill((255, 0, 0))  # 填充红色以提示加载失败

        # 设置武器位置
        if direction == 'right':
            self.rect = self.image.get_rect(midleft=player.rect.midright + pygame.math.Vector2(0, 16))
        elif direction == 'left':
            self.rect = self.image.get_rect(midright=player.rect.midleft + pygame.math.Vector2(0, 16))
        elif direction == 'down':
            self.rect = self.image.get_rect(midtop=player.rect.midbottom + pygame.math.Vector2(-10, 0))
        else:  # 默认方向为向上
            self.rect = self.image.get_rect(midbottom=player.rect.midtop + pygame.math.Vector2(-10, 0))