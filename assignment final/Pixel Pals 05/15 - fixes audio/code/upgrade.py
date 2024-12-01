import pygame
from settings import *

class Upgrade:
    def __init__(self, player):
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.attribute_names = list(player.stats.keys())
        self.max_values = list(player.max_stats.values())
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # UI 配置
        self.height = self.display_surface.get_size()[1] * 0.8
        self.width = self.display_surface.get_size()[0] // 6
        self.create_items()

        # 选择状态
        self.selection_index = 0
        self.selection_time = None
        self.can_move = True

    def create_items(self):
        """创建升级菜单项"""
        self.item_list = []
        total_items = len(self.attribute_names)
        for item_index, item_name in enumerate(self.attribute_names):
            # 垂直间距
            full_width = self.display_surface.get_size()[0]
            increment = full_width // (total_items + 1)
            left = (item_index + 1) * increment - self.width // 2
            top = self.display_surface.get_size()[1] * 0.1

            # 创建 UpgradeItem 对象
            item = UpgradeItem(left, top, self.width, self.height, item_index, self.font)
            self.item_list.append(item)

    def input(self):
        """获取玩家输入"""
        keys = pygame.key.get_pressed()

        if self.can_move:
            if keys[pygame.K_RIGHT] and self.selection_index < len(self.item_list) - 1:
                self.selection_index += 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            elif keys[pygame.K_LEFT] and self.selection_index > 0:
                self.selection_index -= 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()

            if keys[pygame.K_SPACE]:
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
                self.item_list[self.selection_index].trigger(self.player)

    def selection_cooldown(self):
        """处理选择冷却时间"""
        if not self.can_move:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 300:
                self.can_move = True

    def display(self):
        """渲染升级菜单"""
        self.input()
        self.selection_cooldown()

        for index, item in enumerate(self.item_list):
            # 获取属性的名称和当前值
            name = self.attribute_names[index]
            value = self.player.stats[name]
            max_value = self.max_values[index]
            cost = self.player.upgrade_cost[name]

            # 渲染菜单项
            item.display(self.display_surface, self.player.points, name, value, max_value, cost)

        # 绘制选择高亮框
        selected_item = self.item_list[self.selection_index]
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, selected_item.rect, 4)


class UpgradeItem:
    def __init__(self, left, top, width, height, index, font):
        self.rect = pygame.Rect(left, top, width, height)
        self.index = index
        self.font = font

    def display_names(self, surface, name, cost, selected, points):
        """渲染属性名称和升级花费"""
        color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR

        # 绘制名称
        title_surf = self.font.render(name, False, color)
        title_rect = title_surf.get_rect(midtop=self.rect.midtop + pygame.Vector2(0, 20))

        # 绘制消耗
        cost_surf = self.font.render(f'Cost: {int(cost)}', False, color)
        cost_rect = cost_surf.get_rect(midbottom=self.rect.midbottom - pygame.Vector2(0, 20))

        # 检查是否有足够点数
        if cost > points:
            cost_surf = self.font.render('Not enough points', False, 'red')
            cost_rect = cost_surf.get_rect(midtop=title_rect.midbottom)

        # 绘制到屏幕
        surface.blit(title_surf, title_rect)
        surface.blit(cost_surf, cost_rect)

    def display_bar(self, surface, value, max_value, selected):
        """渲染属性进度条"""
        color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR

        # 绘制背景条
        top = self.rect.midtop + pygame.Vector2(0, 60)
        bottom = self.rect.midbottom - pygame.Vector2(0, 60)
        full_height = bottom[1] - top[1]
        relative_number = value / max_value * full_height
        bar_rect = pygame.Rect(self.rect.centerx - 15, bottom[1] - relative_number, 30, 10)

        # 绘制条
        pygame.draw.rect(surface, color, bar_rect)

    def trigger(self, player):
        """处理升级逻辑"""
        attribute = list(player.stats.keys())[self.index]
        if player.points >= player.upgrade_cost[attribute] and player.stats[attribute] < player.max_stats[attribute]:
            player.points -= player.upgrade_cost[attribute]
            player.stats[attribute] += 1
            player.upgrade_cost[attribute] *= 1.2