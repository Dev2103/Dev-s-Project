import pygame

SILVER = (192,192,192)	# FOR GUN 1 BULLET
GOLD = (255,215,0)		# FOR GUN 2 BULLET
BLUE = (18,198,236)		# FOR GUN 1 BARREL
GOLDISH = (234,154,0)	# FOR GUN 2 BARREL
ANGLE1 = 0
ANGLE2 = 0
USERANGLE = 0
ANGLE4 = 0
ANGLE5 = 0
ANGLE6 = 0
ANGLE_R_LIMIT = 70
ANGLE_L_LIMIT = -70
SCORE = 0
FIRED = False
DELAY = 0
READY = False
FUSION = 0

GUN_POSITIONS = [(580, 730), (27, 730), (315, 753), (780,753), (960,730), (1180, 730)]
GUNS_ACTIVE = [True, False, False, False, False, False]
GUNS_UPGRADED = [False, False, False, False, False, False]

POSITIONS = [0]
UPGRADED = []
NEXT_UPGRADE = 0

BARRELS = [(0,0,0,0), (65, 720, -60, 30), (353, 743, -60, 60), (818, 743, -60, 60), (998, 720, -60, 60), (1218, 720, -30, 60)]

ADD_GUN_MIN = 0
UPGRADE_GUN_MIN = 0

COMPUTER_HIT_SCORE = 25
USER_HIT_SCORE = 50
COMPUTER_HIT_FUSION = 1
USER_HIT_FUSION = 2