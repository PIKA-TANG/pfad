from pathlib import Path

# 动态设置项目根目录
BASE_DIR = Path(__file__).resolve().parent.parent  # 定位到 "15 - fixes audio" 文件夹

# 游戏窗口设置
WIDTH = 1280
HEIGTH = 720
FPS = 60
TILESIZE = 64

# 碰撞盒偏移量
HITBOX_OFFSET = {
	'player': -26,
	'object': -40,
	'grass': -10,
	'invisible': 0
}

# UI 设置
UI_FONT = BASE_DIR / 'graphics' / 'font' / 'joystix.ttf'
UI_FONT_SIZE = 18
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80

# 颜色设置
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# 升级菜单颜色
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# 武器数据
weapon_data = {
	'sword': {'cooldown': 100, 'damage': 15, 'graphic': BASE_DIR / 'graphics' / 'weapons' / 'sword' / 'full.png'},
	'lance': {'cooldown': 400, 'damage': 30, 'graphic': BASE_DIR / 'graphics' / 'weapons' / 'lance' / 'full.png'},
	'axe': {'cooldown': 300, 'damage': 20, 'graphic': BASE_DIR / 'graphics' / 'weapons' / 'axe' / 'full.png'},
	'rapier': {'cooldown': 50, 'damage': 8, 'graphic': BASE_DIR / 'graphics' / 'weapons' / 'rapier' / 'full.png'},
	'sai': {'cooldown': 80, 'damage': 10, 'graphic': BASE_DIR / 'graphics' / 'weapons' / 'sai' / 'full.png'}
}

# 魔法数据
magic_data = {
	'flame': {'strength': 5, 'cost': 20, 'graphic': BASE_DIR / 'graphics' / 'particles' / 'flame' / 'fire.png'},
	'heal': {'strength': 20, 'cost': 10, 'graphic': BASE_DIR / 'graphics' / 'particles' / 'heal' / 'heal.png'}
}

# 怪物数据
monster_data = {
	'squid': {'health': 100, 'exp': 100, 'damage': 20, 'attack_type': 'slash', 
	          'attack_sound': BASE_DIR / 'audio' / 'attack' / 'slash.wav', 
	          'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	'raccoon': {'health': 300, 'exp': 250, 'damage': 40, 'attack_type': 'claw', 
	            'attack_sound': BASE_DIR / 'audio' / 'attack' / 'claw.wav', 
	            'speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	'spirit': {'health': 100, 'exp': 110, 'damage': 8, 'attack_type': 'thunder', 
	           'attack_sound': BASE_DIR / 'audio' / 'attack' / 'fireball.wav', 
	           'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
	'bamboo': {'health': 70, 'exp': 120, 'damage': 6, 'attack_type': 'leaf_attack', 
	           'attack_sound': BASE_DIR / 'audio' / 'attack' / 'slash.wav', 
	           'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}
}