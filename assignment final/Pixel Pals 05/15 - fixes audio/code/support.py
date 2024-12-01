from csv import reader
from pathlib import Path
import pygame

def import_csv_layout(path):
    """从 CSV 文件中读取关卡布局"""
    path = Path(path)  # 确保路径是 Path 对象
    terrain_map = []
    with path.open() as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
    return terrain_map

def import_folder(path):
    """批量加载文件夹中的图像资源"""
    path = Path(path)  # 确保路径是 Path 对象
    surface_list = []

    for image_file in path.iterdir():
        if image_file.is_file() and image_file.suffix in ['.png', '.jpg']:  # 过滤图片文件
            image_surf = pygame.image.load(str(image_file)).convert_alpha()
            surface_list.append(image_surf)

    return surface_list