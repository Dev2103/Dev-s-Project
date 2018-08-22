import pygame
import random
import math
import time
import sys
from assets import *
from meteors import *

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
ANGLE_R_LIMIT = 60
ANGLE_L_LIMIT = -60
SCORE = 0
FIRED = False
DELAY = 0
READY = False
FUSION = 0


pygame.init()
pygame.mixer.init()


# Game Settings
size = (1280,960) # so we can change later
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Skyline Defence")
clock = pygame.time.Clock()
timerFont = pygame.font.Font(None, 36)
scoreFont = pygame.font.SysFont(None, 40)
pygame.mouse.set_visible(False)
cursor_img = pygame.transform.scale(pygame.image.load("img/cursor.png") , [12 , 20])
cursor_img_rect = cursor_img.get_rect()


# Global Variables
QUITGAME = False 

# Background Music
pygame.mixer.music.load("music/musicbg.mp3")
pygame.mixer.music.play(-1, 0.0)

# Building Class Descriptions

allBuildings = pygame.sprite.Group()

class Tall1(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.total_stages = 2
		self.stages = [tall1d2, tall1d1, tall1]
		self.image = self.stages[self.total_stages]
		self.rect = self.image.get_rect()
		self.originX = x
		self.originY = y
		self.rect.x = self.originX
		self.rect.y = self.originY
	def destroy(self):
		if (self.total_stages > 0):
			self.total_stages = self.total_stages - 1
			self.image = self.stages[self.total_stages]
			self.rect = self.image.get_rect(x=self.originX, y=self.originY)
		else:
			self.image = pygame.Surface([0,0])
			self.rect = self.image.get_rect(width=0, height=0)
		
tall1_group = pygame.sprite.Group()
tall1_sprite1 = Tall1(322, 790)
tall1_sprite2 = Tall1(787, 790)
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
class Barrel1(pygame.sprite.Sprite):
	def __init__(self, x, y, left_limit, right_limit):
		super().__init__()
		self.imageMaster = barrel
		self.image = self.imageMaster
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.left_limit = 0 - right_limit
		self.right_limit = 0 - left_limit
		self.angle = 0
		self.dir = 5
		centerX = x + 2
		centerY = y + 13
		self.rect.center = (centerX, centerY)	
	def update(self):
		global ANGLE1
		self.angle = self.angle + self.dir
		if self.angle >= self.right_limit:
			self.dir = -1
		elif self.angle <= self.left_limit:
			self.dir = 1
		ANGLE1 = 0 - self.angle
		oldCenter = self.rect.center
		self.image = pygame.transform.rotate(self.imageMaster, self.angle)
		self.rect = self.image.get_rect()
		self.rect.center = oldCenter

class Barrel2(pygame.sprite.Sprite):
	def __init__(self, x, y, left_limit, right_limit):
		super().__init__()
		self.imageMaster = barrel
		self.image = self.imageMaster
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.left_limit = 0 - right_limit
		self.right_limit = 0 - left_limit
		self.angle = 0
		self.dir = 5
		centerX = x + 2
		centerY = y + 13
		self.rect.center = (centerX, centerY)	
	def update(self):
		global ANGLE2
		self.angle = self.angle + self.dir
		if self.angle >= self.right_limit:
			self.dir = -1
		elif self.angle <= self.left_limit:
			self.dir = 1
		ANGLE2 = 0 - self.angle
		oldCenter = self.rect.center
		self.image = pygame.transform.rotate(self.imageMaster, self.angle)
		self.rect = self.image.get_rect()
		self.rect.center = oldCenter

class Barrel4(pygame.sprite.Sprite):
	def __init__(self, x, y, left_limit, right_limit):
		super().__init__()
		self.imageMaster = barrel
		self.image = self.imageMaster
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.left_limit = 0 - right_limit
		self.right_limit = 0 - left_limit
		self.angle = 0
		self.dir = 5
		centerX = x + 2
		centerY = y + 13
		self.rect.center = (centerX, centerY)	
	def update(self):
		global ANGLE4
		self.angle = self.angle + self.dir
		if self.angle >= self.right_limit:
			self.dir = -1
		elif self.angle <= self.left_limit:
			self.dir = 1
		ANGLE4 = 0 - self.angle
		oldCenter = self.rect.center
		self.image = pygame.transform.rotate(self.imageMaster, self.angle)
		self.rect = self.image.get_rect()
		self.rect.center = oldCenter

class Barrel5(pygame.sprite.Sprite):
	def __init__(self, x, y, left_limit, right_limit):
		super().__init__()
		self.imageMaster = barrel
		self.image = self.imageMaster
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.left_limit = 0 - right_limit
		self.right_limit = 0 - left_limit
		self.angle = 0
		self.dir = 5
		centerX = x + 2
		centerY = y + 13
		self.rect.center = (centerX, centerY)	
	def update(self):
		global ANGLE5
		self.angle = self.angle + self.dir
		if self.angle >= self.right_limit:
			self.dir = -1
		elif self.angle <= self.left_limit:
			self.dir = 1
		ANGLE5 = 0 - self.angle
		oldCenter = self.rect.center
		self.image = pygame.transform.rotate(self.imageMaster, self.angle)
		self.rect = self.image.get_rect()
		self.rect.center = oldCenter

class Barrel6(pygame.sprite.Sprite):
	def __init__(self, x, y, left_limit, right_limit):
		super().__init__()
		self.imageMaster = barrel
		self.image = self.imageMaster
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.left_limit = 0 - right_limit
		self.right_limit = 0 - left_limit
		self.angle = 0
		self.dir = 5
		centerX = x + 2
		centerY = y + 13
		self.rect.center = (centerX, centerY)	
	def update(self):
		global ANGLE6
		self.angle = self.angle + self.dir
		if self.angle >= self.right_limit:
			self.dir = -1
		elif self.angle <= self.left_limit:
			self.dir = 1
		ANGLE6 = 0 - self.angle
		oldCenter = self.rect.center
		self.image = pygame.transform.rotate(self.imageMaster, self.angle)
		self.rect = self.image.get_rect()
		self.rect.center = oldCenter

barrel_sprite1 = Barrel1(65, 720, -30, 60)
barrel_sprite2 = Barrel2(353, 743, -60, 60)
barrel_sprite4 = Barrel4(818, 743, -60, 60)
barrel_sprite5 = Barrel5(998, 720, -60, 60)
barrel_sprite6 = Barrel6(1218,720, -60, 30)
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
		self.angle = ANGLE2
		
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
computer_bullets = pygame.sprite.Group()

def game_loop():
	global QUITGAME, SCORE, FIRED, DELAY, READY, shot, FUSION
	while not QUITGAME:
		# Background Refresh
		screen.blit(background_img, [0,0])
		background = pygame.Surface(screen.get_size())
		background.fill((34, 0, 137))
		cursor_img_rect.center = pygame.mouse.get_pos()
		
		# Clock & Timer
		seconds = (int(pygame.time.get_ticks()/1000))%60
		minutes = int(pygame.time.get_ticks()/60000)
		timer = "{:02d}:{:02d}".format(minutes, seconds)
		timerText = timerFont.render("Time: " + str(timer), True, (255,255,255))
		screen.blit(timerText, (10,10))
		
		score = "{:06d}".format(SCORE)
		scoreText = scoreFont.render("Score: " + str(score), True, (255,255,255))
		screen.blit(scoreText, (10, 40))

		fusionQ = "{:01d}".format(FUSION)
		fusionText = scoreFont.render(str(fusionQ), True, (255,255,255))
		screen.blit(fusionText, (1160,30))
		



		
		# Meteor timing
		ticks = int(pygame.time.get_ticks()/1000)
		meteor1_group.update()
		meteor1_group.draw(screen)
		if ticks >= 5:
			meteor2_group.update()
			meteor2_group.draw(screen)
		if ticks >= 10:
			meteor3_group.update()
			meteor3_group.draw(screen)
		if ticks >= 20:
			meteor4_group.update()
			meteor4_group.draw(screen)


		
		allBuildings.draw(screen)
		


		# User Bullets
		bullet_main_group.draw(screen)
		bullet_main_group.update()

		# Computer Bullets
		if READY and not FIRED:
			fire_bullets()
			FIRED = True
			READY = False
		elif not READY:
			FIRED = False

		DELAY = DELAY + 1
		if DELAY >= 30:
			READY = True
			DELAY = 0
		
		computer_bullets.draw(screen)
		computer_bullets.update()

		# Guns and Barrels
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

		screen.blit(cursor_img, cursor_img_rect)


		# Building-Meteor Collision Detection
		if pygame.sprite.spritecollide(tall1_sprite1, all_meteors_group, True):
			tall1_sprite1.destroy()
		if pygame.sprite.spritecollide(tall1_sprite2, all_meteors_group, True):
			tall1_sprite2.destroy()

		# collision = pygame.sprite.groupcollide(meteor1_group, allBuildings, False, False)
		# meteor_hit = collision.keys()
		# building_hit = str(collision.values())
		# print(meteor_hit)
		# print(building_hit)
		# collision.clear()
		# meteor_hit.clear()
		# building_hit.clear()

		# pygame.sprite.groupcollide(meteor1_group, allBuildings, False, True)
		# pygame.sprite.groupcollide(meteor2_group, allBuildings, False, True)
		# pygame.sprite.groupcollide(meteor3_group, allBuildings, False, True)
		# pygame.sprite.groupcollide(meteor4_group, allBuildings, False, True)

		# Bullet-Meteor Collision Detection
		bullet_main_group_meteor1_collision = pygame.sprite.groupcollide(bullet_main_group, meteor1_group, True, True)
		bullet_main_group_meteor2_collision = pygame.sprite.groupcollide(bullet_main_group, meteor2_group, True, True)
		bullet_main_group_meteor3_collision = pygame.sprite.groupcollide(bullet_main_group, meteor3_group, True, True)
		bullet_main_group_meteor4_collision = pygame.sprite.groupcollide(bullet_main_group, meteor4_group, True, True)

		computer_bullets_meteor1_collision = pygame.sprite.groupcollide(computer_bullets, meteor1_group, True, True)
		computer_bullets_meteor2_collision = pygame.sprite.groupcollide(computer_bullets, meteor2_group, True, True)
		computer_bullets_meteor3_collision = pygame.sprite.groupcollide(computer_bullets, meteor3_group, True, True)
		computer_bullets_meteor4_collision = pygame.sprite.groupcollide(computer_bullets, meteor4_group, True, True)

		if bullet_main_group_meteor1_collision:
			SCORE = SCORE + 100
			FUSION = FUSION + 2
			add_meteor(Meteor1, meteor1_group)

		if bullet_main_group_meteor2_collision:
			SCORE = SCORE + 200
			FUSION = FUSION + 4
			meteor2_sprite = Meteor2()
			meteor2_group.add(meteor2_sprite)
			all_meteors_group.add(meteor2_sprite)

		if bullet_main_group_meteor3_collision:
			SCORE = SCORE + 250
			FUSION = FUSION + 6
			meteor3_sprite = Meteor3()
			meteor3_group.add(meteor3_sprite)
			all_meteors_group.add(meteor3_sprite)

		if bullet_main_group_meteor4_collision:
			SCORE = SCORE + 400
			FUSION = FUSION + 8
			meteor4_sprite = Meteor4()
			meteor4_group.add(meteor4_sprite)
			all_meteors_group.add(meteor4_sprite)

		if computer_bullets_meteor1_collision:
			SCORE = SCORE + 50
			FUSION = FUSION + 1
			meteor1_sprite = Meteor1()
			meteor1_group.add(meteor1_sprite)
			all_meteors_group.add(meteor1_sprite)

		if computer_bullets_meteor2_collision:
			SCORE = SCORE + 100
			FUSION = FUSION + 2
			meteor2_sprite = Meteor2()
			meteor2_group.add(meteor2_sprite)
			all_meteors_group.add(meteor2_sprite)

		if computer_bullets_meteor3_collision:
			SCORE = SCORE + 125
			FUSION = FUSION + 3
			meteor3_sprite = Meteor3()
			meteor3_group.add(meteor3_sprite)
			all_meteors_group.add(meteor3_sprite)

		if computer_bullets_meteor4_collision:
			SCORE = SCORE + 200
			FUSION = FUSION + 4
			meteor4_sprite = Meteor4()
			meteor4_group.add(meteor4_sprite)
			all_meteors_group.add(meteor4_sprite)

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					if len(bullet_main_group) <= 5:
						newBullet = Bullet_main()
						newBullet.direction(USERANGLE)
						bullet_main_group.add(newBullet)
						all_bullets.add(newBullet)

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
def fire_bullets():
	global ANGLE1, ANGLE2, ANGLE4, ANGLE5, ANGLE6
	newBullet1 = Bullet1()
	newBullet1.direction(ANGLE1)
	bullet1_group.add(newBullet1)
	all_bullets.add(newBullet1)
	computer_bullets.add(newBullet1)
	
	newBullet2 = Bullet2()
	newBullet2.direction(ANGLE2)
	bullet2_group.add(newBullet2)
	all_bullets.add(newBullet2)
	computer_bullets.add(newBullet2)

	newBullet4 = Bullet4()
	newBullet4.direction(ANGLE4)
	bullet4_group.add(newBullet4)
	all_bullets.add(newBullet4)
	computer_bullets.add(newBullet4)

	newBullet5 = Bullet5()
	newBullet5.direction(ANGLE5)
	bullet5_group.add(newBullet5)
	all_bullets.add(newBullet5)
	computer_bullets.add(newBullet5)

	newBullet6 = Bullet6()
	newBullet6.direction(ANGLE6)
	bullet6_group.add(newBullet6)
	all_bullets.add(newBullet6)
	computer_bullets.add(newBullet6)	
# intro_loop()
game_loop()
# game_over()