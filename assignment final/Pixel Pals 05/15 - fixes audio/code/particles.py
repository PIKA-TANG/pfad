import pygame
from support import import_folder
from random import choice
from settings import BASE_DIR  # 动态路径基于 BASE_DIR

class AnimationPlayer:
    def __init__(self):
        # 动态构建路径，确保兼容不同系统
        self.frames = {
            # magic
            'flame': import_folder(BASE_DIR / 'graphics' / 'particles' / 'flame' / 'frames'),
            'aura': import_folder(BASE_DIR / 'graphics' / 'particles' / 'aura'),
            'heal': import_folder(BASE_DIR / 'graphics' / 'particles' / 'heal' / 'frames'),
            
            # attacks 
            'claw': import_folder(BASE_DIR / 'graphics' / 'particles' / 'claw'),
            'slash': import_folder(BASE_DIR / 'graphics' / 'particles' / 'slash'),
            'sparkle': import_folder(BASE_DIR / 'graphics' / 'particles' / 'sparkle'),
            'leaf_attack': import_folder(BASE_DIR / 'graphics' / 'particles' / 'leaf_attack'),
            'thunder': import_folder(BASE_DIR / 'graphics' / 'particles' / 'thunder'),

            # monster deaths
            'squid': import_folder(BASE_DIR / 'graphics' / 'particles' / 'smoke_orange'),
            'raccoon': import_folder(BASE_DIR / 'graphics' / 'particles' / 'raccoon'),
            'spirit': import_folder(BASE_DIR / 'graphics' / 'particles' / 'nova'),
            'bamboo': import_folder(BASE_DIR / 'graphics' / 'particles' / 'bamboo'),
            
            # leaves 
            'leaf': (
                import_folder(BASE_DIR / 'graphics' / 'particles' / 'leaf1'),
                import_folder(BASE_DIR / 'graphics' / 'particles' / 'leaf2'),
                import_folder(BASE_DIR / 'graphics' / 'particles' / 'leaf3'),
                import_folder(BASE_DIR / 'graphics' / 'particles' / 'leaf4'),
                import_folder(BASE_DIR / 'graphics' / 'particles' / 'leaf5'),
                import_folder(BASE_DIR / 'graphics' / 'particles' / 'leaf6'),
                self.reflect_images(import_folder(BASE_DIR / 'graphics' / 'particles' / 'leaf1')),
                self.reflect_images(import_folder(BASE_DIR / 'graphics' / 'particles' / 'leaf2')),
                self.reflect_images(import_folder(BASE_DIR / 'graphics' / 'particles' / 'leaf3')),
                self.reflect_images(import_folder(BASE_DIR / 'graphics' / 'particles' / 'leaf4')),
                self.reflect_images(import_folder(BASE_DIR / 'graphics' / 'particles' / 'leaf5')),
                self.reflect_images(import_folder(BASE_DIR / 'graphics' / 'particles' / 'leaf6'))
            )
        }
    
    def reflect_images(self, frames):
        """水平翻转帧图像"""
        new_frames = []

        for frame in frames:
            flipped_frame = pygame.transform.flip(frame, True, False)
            new_frames.append(flipped_frame)
        return new_frames

    def create_grass_particles(self, pos, groups):
        """创建草地粒子效果"""
        animation_frames = choice(self.frames['leaf'])  # 随机选择一种叶子粒子
        ParticleEffect(pos, animation_frames, groups)

    def create_particles(self, animation_type, pos, groups):
        """创建通用粒子效果"""
        animation_frames = self.frames[animation_type]
        ParticleEffect(pos, animation_frames, groups)


class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.sprite_type = 'magic'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    def animate(self):
        """处理动画帧"""
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()  # 动画结束时销毁粒子
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()