import pygame
from settings import *
from pathlib import Path

class MagicPlayer:
    def __init__(self, animation_player):
        """初始化魔法播放器"""
        self.animation_player = animation_player

        # 动态加载魔法音效
        base_audio_path = Path(__file__).resolve().parent.parent / 'audio'
        self.sounds = {
            'heal': pygame.mixer.Sound(str(base_audio_path / 'heal.wav')),
            'flame': pygame.mixer.Sound(str(base_audio_path / 'fire.wav'))
        }

        # 设置音效音量（可调整）
        for sound_name, sound in self.sounds.items():
            sound.set_volume(0.5)  # 默认音量为 50%

    def heal(self, player, strength, cost, groups):
        """创建治疗魔法"""
        if player.energy >= cost:  # 检查玩家能量是否足够
            player.energy -= cost
            player.health += strength
            if player.health > player.stats['health']:  # 血量不能超出最大值
                player.health = player.stats['health']

            # 生成治疗魔法粒子动画
            pos = player.rect.center + pygame.math.Vector2(0, -60)  # 粒子生成在玩家头顶
            self.animation_player.create_particles('aura', pos, groups)
            self.animation_player.create_particles('heal', pos, groups)

            # 播放治疗音效
            self.sounds['heal'].play()
        else:
            print("Not enough energy to cast 'heal' spell.")

    def flame(self, player, cost, groups):
        """创建火焰魔法"""
        if player.energy >= cost:  # 检查玩家能量是否足够
            player.energy -= cost

            # 播放火焰音效
            self.sounds['flame'].play()

            # 计算火焰魔法生成方向
            direction = pygame.math.Vector2()
            if player.status.split('_')[0] == 'right':
                direction = pygame.math.Vector2(1, 0)
            elif player.status.split('_')[0] == 'left':
                direction = pygame.math.Vector2(-1, 0)
            elif player.status.split('_')[0] == 'up':
                direction = pygame.math.Vector2(0, -1)
            elif player.status.split('_')[0] == 'down':
                direction = pygame.math.Vector2(0, 1)

            # 根据方向生成多个火焰粒子
            for i in range(1, 6):  # 调整粒子数量和间距
                if direction.x:  # 水平方向
                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x + direction.x * TILESIZE // 2
                    y = player.rect.centery
                    self.animation_player.create_particles('flame', (x, y), groups)
                else:  # 垂直方向
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx
                    y = player.rect.centery + offset_y + direction.y * TILESIZE // 2
                    self.animation_player.create_particles('flame', (x, y), groups)
        else:
            print("Not enough energy to cast 'flame' spell.")