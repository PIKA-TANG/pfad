from csv import reader
from pathlib import Path
import pygame

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
    return terrain_map

def import_folder(path):
    surface_list = []

    # 将路径转换为 Path 对象，以确保兼容性
    path = Path(path)
    for image_path in path.iterdir():
        if image_path.is_file() and image_path.suffix in ['.png', '.jpg', '.jpeg']:  # 根据文件类型过滤
            image_surf = pygame.image.load(image_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list
