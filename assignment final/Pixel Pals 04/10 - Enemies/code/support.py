from csv import reader
from pathlib import Path
import pygame

def import_csv_layout(path):
	terrain_map = []
	path = Path(path).resolve()  # 使用 pathlib 处理路径
	try:
		with path.open() as level_map:
			layout = reader(level_map, delimiter=',')
			for row in layout:
				terrain_map.append(list(row))
	except FileNotFoundError:
		print(f"File not found: {path}")
		raise
	return terrain_map

def import_folder(path):
	surface_list = []
	path = Path(path).resolve()  # 使用 pathlib 处理路径

	try:
		for image_path in path.iterdir():  # 遍历文件夹内容
			if image_path.is_file() and image_path.suffix in {'.png', '.jpg'}:  # 只加载图像文件
				image_surf = pygame.image.load(str(image_path)).convert_alpha()
				surface_list.append(image_surf)
	except FileNotFoundError:
		print(f"Folder not found: {path}")
		raise

	return surface_list