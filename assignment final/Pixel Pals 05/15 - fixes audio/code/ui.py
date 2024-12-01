import pygame
from settings import *
from pathlib import Path

class UI:
    def __init__(self):
        """初始化 UI 元素"""
        # 初始化显示表面
        self.display_surface = pygame.display.get_surface()
        print("Display surface initialized.")

        # 打印字体路径以调试
        print(f"Resolved font path: {UI_FONT}")
        try:
            self.font = pygame.font.Font(str(UI_FONT), UI_FONT_SIZE)  # 加载字体
            print("Font loaded successfully!")
        except FileNotFoundError as e:
            print(f"Font not found: {e}")
        except Exception as e:
            print(f"Unexpected error loading font: {e}")
        
        # 血条和能量条
        self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(10, 34, ENERGY_BAR_WIDTH, BAR_HEIGHT)

        # 动态加载武器图像
        self.weapon_graphics = []
        weapon_base_path = Path(__file__).resolve().parent.parent / 'graphics' / 'weapons'
        for weapon in weapon_data.values():
            # 修复路径重复问题
            path = Path(weapon['graphic'])
            final_path = (weapon_base_path / path).resolve()  # 拼接路径并解析为绝对路径
            print(f"Loading weapon graphic from: {final_path}")  # 打印路径进行调试
            try:
                weapon_image = pygame.image.load(str(final_path)).convert_alpha()
                self.weapon_graphics.append(weapon_image)
            except FileNotFoundError as e:
                print(f"Weapon graphic not found: {final_path}, error: {e}")

        # 动态加载魔法图像
        self.magic_graphics = []
        magic_base_path = Path(__file__).resolve().parent.parent / 'graphics' / 'particles'
        for magic in magic_data.values():
            # 修复路径重复问题
            path = Path(magic['graphic'])
            final_path = (magic_base_path / path).resolve()  # 拼接路径并解析为绝对路径
            print(f"Loading magic graphic from: {final_path}")  # 打印路径进行调试
            try:
                magic_image = pygame.image.load(str(final_path)).convert_alpha()
                self.magic_graphics.append(magic_image)
            except FileNotFoundError as e:
                print(f"Magic graphic not found: {final_path}, error: {e}")

    def show_bar(self, current, max_amount, bg_rect, color):
        """渲染血条或能量条"""
        # 绘制背景
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        # 将数值转换为像素宽度
        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        # 绘制条
        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)

    def show_exp(self, exp):
        """显示玩家当前的经验值"""
        text_surf = self.font.render(str(int(exp)), False, TEXT_COLOR)
        x = self.display_surface.get_size()[0] - 20
        y = self.display_surface.get_size()[1] - 20
        text_rect = text_surf.get_rect(bottomright=(x, y))

        pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(20, 20))
        self.display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(20, 20), 3)

    def selection_box(self, left, top, has_switched):
        """渲染物品选择框"""
        bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
        if has_switched:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, bg_rect, 3)
        else:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)
        return bg_rect

    def weapon_overlay(self, weapon_index, has_switched):
        """渲染当前武器的覆盖图"""
        bg_rect = self.selection_box(10, 630, has_switched)
        weapon_surf = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surf.get_rect(center=bg_rect.center)

        self.display_surface.blit(weapon_surf, weapon_rect)

    def magic_overlay(self, magic_index, has_switched):
        """渲染当前魔法的覆盖图"""
        bg_rect = self.selection_box(80, 635, has_switched)
        magic_surf = self.magic_graphics[magic_index]
        magic_rect = magic_surf.get_rect(center=bg_rect.center)

        self.display_surface.blit(magic_surf, magic_rect)

    def display(self, player):
        """渲染所有 UI 元素"""
        # 血条和能量条
        self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOR)
        self.show_bar(player.energy, player.stats['energy'], self.energy_bar_rect, ENERGY_COLOR)

        # 经验值
        self.show_exp(player.exp)

        # 武器和魔法覆盖图
        self.weapon_overlay(player.weapon_index, not player.can_switch_weapon)
        self.magic_overlay(player.magic_index, not player.can_switch_magic)