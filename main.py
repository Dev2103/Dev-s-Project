import pygame
import random
import math
import time
import sys
# from meteors import Meteor1
# from meteors import Meteor2
# from meteors import Meteor3
# from meteors import Meteor4

SILVER = (192,192,192)	# FOR GUN 1 BULLET
GOLD = (255,215,0)		# FOR GUN 2 BULLET
BLUE = (18,198,236)		# FOR GUN 1 BARREL
GOLDISH = (234,154,0)	# FOR GUN 2 BARREL
ANGLE = 0
USERANGLE = 0
ANGLE_R_LIMIT = 60
ANGLE_L_LIMIT = -60
SCORE = 0

pygame.init()


# Game Settings
size = (1280,960) # so we can change later
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Skyline Defence")
intro_img = pygame.image.load("img/Intro.png")
game_over_img = pygame.image.load("img/game_over.png")
background_img = pygame.image.load("img/bg.png")
clock = pygame.time.Clock()
timerFont = pygame.font.Font(None, 36)
scoreFont = pygame.font.SysFont(None, 40)

# Global Variables
QUITGAME = False 
meteor1_speed = 2.4
meteor2_speed = 1.5
meteor3_speed = 3.0
meteor4_speed = 1.7

# Game Assets
tall1 = pygame.transform.scale(pygame.image.load("img/tall1.png"), [65,170])#790
tall1d1 = pygame.transform.scale(pygame.image.load("img/tall1d1.png"), [65,170])
tall1d2 = pygame.transform.scale(pygame.image.load("img/tall1d2.png"), [65, 170])

tall2 = pygame.transform.scale(pygame.image.load("img/tall2.png"), [125,196])#764
tall2d1 = pygame.transform.scale(pygame.image.load("img/tall2d1.png"), [125,196])#790
tall2d2 = pygame.transform.scale(pygame.image.load("img/tall2d2.png"), [125,196])#790

tall3 = pygame.transform.scale(pygame.image.load("img/tall3.png"), [125,196])#764
tall3d1 = pygame.transform.scale(pygame.image.load("img/tall3d1.png"), [125,196])#790
tall3d2 = pygame.transform.scale(pygame.image.load("img/tall3d2.png"), [125,196])#790

medium1 = pygame.transform.scale(pygame.image.load("img/medium1.png"), [116,140])#820
medium1d1 = pygame.transform.scale(pygame.image.load("img/medium1d1.png"), [116,140])#790
medium1d2 = pygame.transform.scale(pygame.image.load("img/medium1d2.png"), [116,140])#790

medium2 = pygame.transform.scale(pygame.image.load("img/medium2.png"), [116,140]) #820
medium2d1 = pygame.transform.scale(pygame.image.load("img/medium2d1.png"), [116,124])#790
medium2d2 = pygame.transform.scale(pygame.image.load("img/medium2d2.png"), [116,71])#790

small1 = pygame.transform.scale(pygame.image.load("img/small1.png"), [82,70])#890
small1d1 = pygame.transform.scale(pygame.image.load("img/small1d1.png"), [82,51])#890

small2 = pygame.transform.scale(pygame.image.load("img/small2.png"), [82,70])#890
small2d1 = pygame.transform.scale(pygame.image.load("img/small2d1.png"), [82,71])#890

small3 = pygame.transform.scale(pygame.image.load("img/small3.png"), [97,100])#860
small3d1 = pygame.transform.scale(pygame.image.load("img/small3d1.png"), [97,76])#860

fusion = pygame.transform.scale(pygame.image.load("img/fusion.PNG"), [30,48])

upgrade = pygame.transform.scale(pygame.image.load("img/upgrade.PNG"), [70,22])
upgrade_faded = pygame.transform.scale(pygame.image.load("img/upgrade_faded.PNG"), [70,22])

meteor1 = pygame.transform.scale(pygame.image.load("img/meteor1.png"), [25,49])
meteor2 = pygame.transform.scale(pygame.image.load("img/meteor2.png"), [40,66])
meteor3 = pygame.transform.scale(pygame.image.load("img/meteor3.png"), [20,52])
meteor4 = pygame.transform.scale(pygame.image.load("img/meteor4.png"), [45,78])

gun1 = pygame.transform.scale(pygame.image.load("img/gun1.png"), [80,38])
gun2 = pygame.transform.scale(pygame.image.load("img/gun2.png"), [80,42])

barrel = pygame.image.load("img/barrel.png")

pygame.mixer.music.load("music/musicbg.mp3")
pygame.mixer.music.play(-1, 0.0)

# Meteor Class Descriptions
class Meteor1(pygame.sprite.Sprite):
	# Constructor
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([25, 49])
		self.image = meteor1
		self.rect = self.image.get_rect()

		self.rect.x = random.randrange(0, 1200)
		self.rect.y = random.randrange(-500, 0)
	def update(self):
		global QUITGAME
		self.rect.y = self.rect.y + meteor1_speed
		self.rect.x = self.rect.x + random.randrange(-1,2)
		if self.rect.y >= 960: #960
			# QUITGAME = True
			# game_over()
			self.rect.x = random.randrange(0, 1280)
			self.rect.y = random.randrange(-2000, 0)

class Meteor2(pygame.sprite.Sprite):
	# Constructor
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([40,66])
		self.image = meteor2
		self.rect = self.image.get_rect()

		self.rect.x = random.randrange(0, 1200)
		# self.rect.x = 600
		self.rect.y = random.randrange(-3000,0) #-1500
	def update(self):
		self.rect.y = self.rect.y + meteor2_speed
		self.rect.x = self.rect.x + random.randrange(-1,2)
		if self.rect.y >= 500:
			self.rect.x = random.randrange(0, 1280)
			self.rect.y = random.randrange(-3000,0)

class Meteor3(pygame.sprite.Sprite):
	# Constructor
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([20,52])
		self.image = meteor3
		self.rect = self.image.get_rect()

		self.rect.x = random.randrange(0, 1200)
		# self.rect.x = 600
		self.rect.y = random.randrange(-1500, 0)
	def update(self):
		self.rect.y = self.rect.y + meteor3_speed
		self.rect.x = self.rect.x + random.randrange(-1,2)
		if self.rect.y >= 500:
			self.rect.x = random.randrange(0, 1280)
			self.rect.y = random.randrange(-3000,0)

class Meteor4(pygame.sprite.Sprite):
	# Constructor
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([45,78])
		self.image = meteor4
		self.rect = self.image.get_rect()

		self.rect.x = random.randrange(0, 1200)
		# self.rect.x = 600
		self.rect.y = random.randrange(-1500,0)
	def update(self):
		self.rect.y = self.rect.y + meteor4_speed
		self.rect.x = self.rect.x + random.randrange(-1,2)
		if self.rect.y >= 500:
			self.rect.x = random.randrange(0, 1280)
			self.rect.y = random.randrange(-3000,0)

# Meteor Sprite Creation
all_meteors_group = pygame.sprite.Group()
no_Meteor1 = 8
no_Meteor2 = 5
no_Meteor3 = 5
no_Meteor4 = 5

meteor1_group = pygame.sprite.Group()
for x in range (no_Meteor1):
	meteor1_sprite = Meteor1()
	meteor1_group.add(meteor1_sprite)
	all_meteors_group.add(meteor1_sprite)

meteor2_group = pygame.sprite.Group()
for x in range (no_Meteor2):
	meteor2_sprite = Meteor2()
	meteor2_group.add(meteor2_sprite)
	all_meteors_group.add(meteor2_sprite)

meteor3_group = pygame.sprite.Group()
for x in range (no_Meteor3):
	meteor3_sprite = Meteor3()
	meteor3_group.add(meteor3_sprite)
	all_meteors_group.add(meteor3_sprite)

meteor4_group = pygame.sprite.Group()
for x in range (no_Meteor4):
	meteor4_sprite = Meteor4()
	meteor4_group.add(meteor4_sprite)
	all_meteors_group.add(meteor4_sprite)

# Building Class Descriptions

allBuildings = pygame.sprite.Group()

class Tall1(pygame.sprite.Sprite):
	def __init__(self, width, height, x, y):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image = tall1
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
tall1_group = pygame.sprite.Group()
tall1_sprite1 = Tall1(125, 196, 322, 790)
tall1_sprite2 = Tall1(116, 140, 787, 790)
tall1_group.add(tall1_sprite1)
tall1_group.add(tall1_sprite2)
allBuildings.add(tall1_sprite1)
allBuildings.add(tall1_sprite2)

class Tall2(pygame.sprite.Sprite):
	def __init__(self, width, height, x, y):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image = tall2
		self.rect = self.image.get_rect()
		self.rect.x = x 
		self.rect.y = y
tall2_group = pygame.sprite.Group()
tall2_sprite1 = Tall2(125, 196, 0 ,764)
tall2_sprite2 = Tall2(116, 140, 935, 764)
tall2_group.add(tall2_sprite1)
tall2_group.add(tall2_sprite2)
allBuildings.add(tall2_sprite1)
allBuildings.add(tall2_sprite2)

class Tall3(pygame.sprite.Sprite):
	def __init__(self, width, height, x, y):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image = tall3
		self.rect = self.image.get_rect()
		self.rect.x = x 
		self.rect.y = y
tall3_group = pygame.sprite.Group()
tall3_sprite1 = Tall3(125, 196, 560 ,764)
tall3_sprite2 = Tall3(116, 140, 1160, 764)
tall3_group.add(tall3_sprite1)
tall3_group.add(tall3_sprite2)
allBuildings.add(tall3_sprite1)
allBuildings.add(tall3_sprite2)

class Medium1(pygame.sprite.Sprite):
	def __init__(self, width, height, x, y):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image = medium1
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
Medium1_group = pygame.sprite.Group()
Medium1_sprite1 = Medium1(116, 140, 674, 820)
Medium1_group.add(Medium1_sprite1)
allBuildings.add(Medium1_sprite1)

class Medium2(pygame.sprite.Sprite):
	def __init__(self, width, height, x, y):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image = medium2
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
Medium2_group = pygame.sprite.Group()
Medium2_sprite1 = Medium2(116, 140, 120, 820)
Medium2_sprite2 = Medium2(116, 140, 470, 820)
Medium2_sprite3 = Medium2(116, 140, 1050, 820)
Medium2_group.add(Medium2_sprite1)
Medium2_group.add(Medium2_sprite2)
Medium2_group.add(Medium2_sprite3)
allBuildings.add(Medium2_sprite1)
allBuildings.add(Medium2_sprite2)
allBuildings.add(Medium2_sprite3)

class Small1(pygame.sprite.Sprite):
	def __init__(self, width, height, x, y):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image = small1
		self.rect = self.image.get_rect()
		self.rect.x = x 
		self.rect.y = y
small1_group = pygame.sprite.Group()
small1_sprite1 = Small1(82, 70, 390, 890)
small1_group.add(small1_sprite1)
allBuildings.add(small1_sprite1)

class Small2(pygame.sprite.Sprite):
	def __init__(self, width, height, x, y):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image = small2
		self.rect = self.image.get_rect()
		self.rect.x = x 
		self.rect.y = y
small2_group = pygame.sprite.Group()
small2_sprite1 = Small2(82, 70, 854, 890)
small2_group.add(small2_sprite1)
allBuildings.add(small2_sprite1)

class Small3(pygame.sprite.Sprite):
	def __init__(self, width, height, x, y):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image = small3
		self.rect = self.image.get_rect()
		self.rect.x = x 
		self.rect.y = y
small3_group = pygame.sprite.Group()
small3_sprite1 = Small3(97, 77, 236, 860)
small3_group.add(small3_sprite1)
allBuildings.add(small3_sprite1)



# Guns class description
class Gun(pygame.sprite.Sprite):
	def __init__(self, width, height, x, y):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image = gun1
		self.rect  = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
	def update(self):
 		self.image = gun2
gun_group =  pygame.sprite.Group()
gun_sprite1 = Gun(80, 38, 27, 730)
gun_sprite2 = Gun(80, 38, 315, 753)
gun_sprite3 = Gun(80,38, 580, 730)
gun_sprite4 = Gun(80, 38, 780, 753)
gun_sprite5 = Gun(80, 38, 960, 730)
gun_sprite6 = Gun(80, 38, 1180, 730)
gun_group.add(gun_sprite1)
gun_group.add(gun_sprite2)
gun_group.add(gun_sprite3)
gun_group.add(gun_sprite4)
gun_group.add(gun_sprite5)
gun_group.add(gun_sprite6)



barrel_group = pygame.sprite.Group()

# User Barrel
class User_barrel(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.imageMaster = barrel
		self.image = self.imageMaster
		self.rect = self.image.get_rect()
		self.rect.x = 618
		self.rect.y = 720
		self.angle = 0
		self.dir = 10
		centerX = 620
		centerY = 733
		self.rect.center = (centerX, centerY)
	def update(self):
		oldCenter = self.rect.center
		self.image = pygame.transform.rotate(self.imageMaster, (-self.angle))
		self.rect = self.image.get_rect()
		self.rect.center = oldCenter
	def turn_right(self):
		global USERANGLE, ANGLE_R_LIMIT
		if self.angle <= ANGLE_R_LIMIT:
			self.angle = self.angle + self.dir
			USERANGLE = self.angle
	def turn_left(self):
		global USERANGLE, ANGLE_L_LIMIT
		if self.angle >= ANGLE_L_LIMIT:
			self.angle = self.angle - self.dir
			USERANGLE = self.angle

user_barrel_sprite = User_barrel()
barrel_group.add(user_barrel_sprite)

# Computer Barrels
class Barrel(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.imageMaster = barrel
		self.image = self.imageMaster
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.angle = 0
		self.dir = 2
		centerX = x + 2
		centerY = y + 13
		self.rect.center = (centerX, centerY)	
	def update(self):
		global ANGLE, ANGLE_R_LIMIT, ANGLE_L_LIMIT
		if self.angle >= ANGLE_R_LIMIT:
			self.dir = -2
		elif self.angle <= ANGLE_L_LIMIT:
			self.dir = 2
		self.angle = self.angle + self.dir
		ANGLE = 0 - self.angle
		oldCenter = self.rect.center
		self.image = pygame.transform.rotate(self.imageMaster, self.angle)
		self.rect = self.image.get_rect()
		self.rect.center = oldCenter

barrel_sprite1 = Barrel(65, 720) 
barrel_sprite2 = Barrel(353, 743)
barrel_sprite4 = Barrel(818, 743)
barrel_sprite5 = Barrel(998, 720)
barrel_sprite6 = Barrel(1218,720)
barrel_group.add(barrel_sprite1)
barrel_group.add(barrel_sprite2)
barrel_group.add(barrel_sprite4)
barrel_group.add(barrel_sprite5)
barrel_group.add(barrel_sprite6)

# Bullet Main
class Bullet_main(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([5, 5])
		self.image.fill(SILVER)
		self.rect = self.image.get_rect()
		self.rect.x = 620
		self.rect.y = 733
		self.originX = self.rect.x
		self.originY = self.rect.y
		self.angle = 0
	def update(self):
		self.rect.y = self.rect.y - 15
		self.rect.x = self.rect.x + (15 * math.tan(math.radians(self.angle)))
		
		if self.rect.y <= 0:	
			self.kill()
	def direction(self, angle):
		self.angle = angle
	
bullet_main_group = pygame.sprite.Group()


class Bullet1(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([5, 5])
		self.image.fill(SILVER)
		self.rect = self.image.get_rect()
		self.rect.x = 65
		self.rect.y = 733
		self.originX = self.rect.x
		self.originY = self.rect.y
		self.angle = 0
	def update(self):
		self.rect.y = self.rect.y - 15
		self.rect.x = self.rect.x + (15 * math.tan(math.radians(self.angle)))
		
		if self.rect.y <= 0:	
			self.kill()
	def direction(self, angle):
		self.angle = angle
		
bullet1_group = pygame.sprite.Group()


class Bullet2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([5, 5])
		self.image.fill(SILVER)
		self.rect = self.image.get_rect()
		self.rect.x = 353
		self.rect.y = 750
		self.originX = self.rect.x
		self.originY = self.rect.y
		self.angle = 0
	def update(self):
		self.rect.y = self.rect.y - 15
		self.rect.x = self.rect.x + (15 * math.tan(math.radians(self.angle)))
		
		if self.rect.y <= 0:	
			self.kill()
	def direction(self, angle):
		self.angle = angle
		
bullet2_group = pygame.sprite.Group()


class Bullet4(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([5, 5])
		self.image.fill(SILVER)
		self.rect = self.image.get_rect()
		self.rect.x = 818
		self.rect.y = 750
		self.originX = self.rect.x
		self.originY = self.rect.y
		self.angle = 0
	def update(self):
		self.rect.y = self.rect.y - 15
		self.rect.x = self.rect.x + (15 * math.tan(math.radians(self.angle)))
		if self.rect.y <= 0:	
			self.kill()
	def direction(self, angle):
		self.angle = angle
	
bullet4_group = pygame.sprite.Group()


class Bullet5(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([5, 5])
		self.image.fill(SILVER)
		self.rect = self.image.get_rect()
		self.rect.x = 998
		self.rect.y = 733
		self.originX = self.rect.x
		self.originY = self.rect.y
		self.angle = 0
	def update(self):
		self.rect.y = self.rect.y - 15
		self.rect.x = self.rect.x + (15 * math.tan(math.radians(self.angle)))
		if self.rect.y <= 0:	
			self.kill()
	def direction(self, angle):
		self.angle = angle
		
bullet5_group = pygame.sprite.Group()


class Bullet6(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([5, 5])
		self.image.fill(SILVER)
		self.rect = self.image.get_rect()
		self.rect.x = 1218
		self.rect.y = 733
		self.originX = self.rect.x
		self.originY = self.rect.y
		self.angle = 0
	def update(self):
		self.rect.y = self.rect.y - 15
		self.rect.x = self.rect.x + (15 * math.tan(math.radians(self.angle)))
		
		if self.rect.y <= 0:	
			self.kill()
	def direction(self, angle):
		self.angle = angle
		
bullet6_group = pygame.sprite.Group()

all_bullets = pygame.sprite.Group()

def game_loop():
	global QUITGAME, SCORE
	while not QUITGAME:
		# Background Refresh
		screen.blit(background_img, [0,0])
		background = pygame.Surface(screen.get_size())
		background.fill((34, 0, 137))
		
		# Clock & Timer
		seconds = (int(pygame.time.get_ticks()/1000))%60
		minutes = int(pygame.time.get_ticks()/60000)
		timer = "{:02d}:{:02d}".format(minutes, seconds)
		timerText = timerFont.render("Time: " + str(timer), True, (255,255,255))
		screen.blit(timerText, (10,10))
		score = "{:05d}".format(SCORE)
		scoreText = scoreFont.render("Score: " + str(score), True, (255,255,255))
		screen.blit(scoreText, (10, 40))
		
		# Meteor timing
		ticks = int(pygame.time.get_ticks()/1000)
		meteor1_group.update()
		meteor1_group.draw(screen)
		if ticks >= 5:
			meteor2_group.update()
			meteor2_group.draw(screen)
		if ticks >= 105:
			meteor3_group.update()
			meteor3_group.draw(screen)
		if ticks >= 180:
			meteor4_group.update()
			meteor4_group.draw(screen)


		
		allBuildings.draw(screen)
		bullet_main_group.draw(screen)
		bullet_main_group.update()

		bullet1_group.draw(screen)
		bullet1_group.update()

		bullet2_group.draw(screen)
		bullet2_group.update()

		bullet4_group.draw(screen)
		bullet4_group.update()

		bullet5_group.draw(screen)
		bullet5_group.update()

		bullet6_group.draw(screen)
		bullet6_group.update()
		barrel_group.clear(screen, background)
		barrel_group.update()
		barrel_group.draw(screen)
		gun_group.draw(screen)

		#coin
		screen.blit(fusion , [1120, 20])

		#buttons
		screen.blit(upgrade_faded, [20,780])
		screen.blit(upgrade, [20,780])

		screen.blit(upgrade_faded, [580,780])
		screen.blit(upgrade, [580,780])

		screen.blit(upgrade_faded, [955,780])
		screen.blit(upgrade, [955,780])

		screen.blit(upgrade_faded, [1180,780])
		screen.blit(upgrade, [1180,780])

		screen.blit(upgrade_faded, [330,805])
		screen.blit(upgrade, [330,805])

		screen.blit(upgrade_faded, [795,805])
		screen.blit(upgrade, [795,805])
		
		#Guns
	
		# screen.blit(gun1, [580,726])  # USER CONTROLLED
		# screen.blit(gun2, [580,726]) 


		

		pygame.sprite.groupcollide(meteor1_group, allBuildings, False, True)
		pygame.sprite.groupcollide(meteor2_group, allBuildings, False, True)
		pygame.sprite.groupcollide(meteor3_group, allBuildings, False, True)
		pygame.sprite.groupcollide(meteor4_group, allBuildings, False, True)

		# Collision Detection
		all_bullets_meteor1_collision = pygame.sprite.groupcollide(all_bullets, meteor1_group, True, True)
		all_bullets_meteor2_collision = pygame.sprite.groupcollide(all_bullets, meteor2_group, True, True)
		all_bullets_meteor3_collision = pygame.sprite.groupcollide(all_bullets, meteor3_group, True, True)
		all_bullets_meteor4_collision = pygame.sprite.groupcollide(all_bullets, meteor4_group, True, True)

		if all_bullets_meteor1_collision:
			SCORE = SCORE + 100
			meteor1_sprite = Meteor1()
			meteor1_group.add(meteor1_sprite)
			all_meteors_group.add(meteor1_sprite)

		if all_bullets_meteor2_collision:
			SCORE = SCORE + 200
			meteor2_sprite = Meteor2()
			meteor2_group.add(meteor2_sprite)
			all_meteors_group.add(meteor2_sprite)



		if all_bullets_meteor3_collision:
			SCORE = SCORE + 250
			meteor3_sprite = Meteor3()
			meteor3_group.add(meteor3_sprite)
			all_meteors_group.add(meteor3_sprite)



		if all_bullets_meteor4_collision:
			SCORE = SCORE + 400
			meteor4_sprite = Meteor4()
			meteor4_group.add(meteor4_sprite)
			all_meteors_group.add(meteor4_sprite)




		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					newBullet = Bullet_main()
					newBullet.direction(USERANGLE)
					bullet_main_group.add(newBullet)
					all_bullets.add(newBullet)
					
					newBullet1 = Bullet1()
					newBullet1.direction(ANGLE)
					bullet1_group.add(newBullet1)
					all_bullets.add(newBullet1)
					
					newBullet2 = Bullet2()
					newBullet2.direction(ANGLE)
					bullet2_group.add(newBullet2)
					all_bullets.add(newBullet2)

					newBullet4 = Bullet4()
					newBullet4.direction(ANGLE)
					bullet4_group.add(newBullet4)
					all_bullets.add(newBullet4)
					
					newBullet5 = Bullet5()
					newBullet5.direction(ANGLE)
					bullet5_group.add(newBullet5)
					all_bullets.add(newBullet5)
					
					newBullet6 = Bullet6()
					newBullet6.direction(ANGLE)
					bullet6_group.add(newBullet6)
					all_bullets.add(newBullet6)

				if event.key == pygame.K_LEFT:
					user_barrel_sprite.turn_left()
				if event.key == pygame.K_RIGHT:
					user_barrel_sprite.turn_right()
					
			elif event.type == pygame.QUIT:
				QUITGAME = True

		pygame.display.flip()
def game_over():
	game_over = True
	while game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = False
		screen.blit(game_over_img, [0,0])
		score = scoreFont.render(str(SCORE), True, (255,255,255))
		screen.blit(score, (670, 565))
		pygame.display.flip()
def intro_loop():
	intro =  True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				intro = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					intro = False
		screen.blit(intro_img, [0,0])
		pygame.display.flip()

intro_loop()
game_loop()
game_over()