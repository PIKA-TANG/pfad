import pygame, sys
import os
from settings import *  # 导入所有设置
from level import Level
from pathlib import Path  # 动态路径管理

# 切换工作目录到 main.py 所在目录
os.chdir(Path(__file__).resolve().parent)

class Game:
	def __init__(self):
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGTH))  # 使用 settings.py 中的 WIDTH 和 HEIGTH
		pygame.display.set_caption('Zelda')
		self.clock = pygame.time.Clock()

		self.level = Level()

		# sound
		base_path = Path(__file__).resolve().parent.parent  # 定位到 "15 - fixes audio" 文件夹
		main_sound = pygame.mixer.Sound(base_path / 'audio' / 'main.ogg')  # 调整路径
		main_sound.set_volume(0.5)
		main_sound.play(loops=-1)  # 循环播放
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_m:
						self.level.toggle_menu()

			self.screen.fill(WATER_COLOR)  # 使用 settings.py 中的 WATER_COLOR
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()