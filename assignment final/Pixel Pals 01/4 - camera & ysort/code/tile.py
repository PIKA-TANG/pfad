import pygame
from pathlib import Path

# 获取 `4 - camera & ysort` 目录
current_file = Path(__file__).resolve().parent.parent  # 定位到 `4 - camera & ysort` 目录

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # 使用相对 `4 - camera & ysort` 的路径加载图片
        self.image = pygame.image.load(current_file / "graphics/test/rock.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, *args):
        # 任何其他更新逻辑都在这里继续使用
        pass
