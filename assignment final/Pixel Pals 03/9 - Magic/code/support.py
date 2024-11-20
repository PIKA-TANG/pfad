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
	path = Path(path)

	for img_file in path.glob('*'):
		image_surf = pygame.image.load(str(img_file)).convert_alpha()
		surface_list.append(image_surf)

	return surface_list