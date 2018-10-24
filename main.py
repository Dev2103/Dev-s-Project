import pygame
import random
import math
import time
import sys
from global_vars import *
from assets import *
from meteors import *




pygame.init()
pygame.mixer.init()


# Game Settings

QUITGAME = False
pygame.display.set_caption("Skyline Defence")
clock = pygame.time.Clock()
timerFont = pygame.font.Font(None, 36)
scoreFont = pygame.font.SysFont(None, 40)
pygame.mouse.set_visible(False)
cursor_img = pygame.transform.scale(pygame.image.load("img/cursor.png") , [12 , 20])
cursor_img_rect = cursor_img.get_rect()


# Background Music 
# pygame.mixer.music.load("music/musicbg.mp3")
# pygame.mixer.music.play(-1, 0.0)

# Building Class Descriptions

all_buildings = pygame.sprite.Group()

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
all_buildings.add(tall1_sprite1)
all_buildings.add(tall1_sprite2)

class Tall2(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.total_stages = 2
		self.stages = [tall2d2, tall2d1, tall2]
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
tall2_group = pygame.sprite.Group()
tall2_sprite1 = Tall2(0 ,764)
tall2_sprite2 = Tall2(935, 764)
tall2_group.add(tall2_sprite1)
tall2_group.add(tall2_sprite2)
all_buildings.add(tall2_sprite1)
all_buildings.add(tall2_sprite2)

class Tall3(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.total_stages = 2
		self.stages = [tall3d2, tall3d1, tall3]
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
tall3_group = pygame.sprite.Group()
tall3_sprite1 = Tall3(560 ,764)
tall3_sprite2 = Tall3(1160, 764)
tall3_group.add(tall3_sprite1)
tall3_group.add(tall3_sprite2)
all_buildings.add(tall3_sprite1)
all_buildings.add(tall3_sprite2)

class Medium1(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.total_stages = 2
		self.stages = [medium1d2, medium1d1, medium1]
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
Medium1_group = pygame.sprite.Group()
Medium1_sprite1 = Medium1(674, 820)
Medium1_group.add(Medium1_sprite1)
all_buildings.add(Medium1_sprite1)

class Medium2(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.total_stages = 2
		self.stages = [medium2d2, medium2d1, medium2]
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
Medium2_group = pygame.sprite.Group()
Medium2_sprite1 = Medium2(120, 820)
Medium2_sprite2 = Medium2(470, 820)
Medium2_sprite3 = Medium2(1050, 820)
Medium2_group.add(Medium2_sprite1)
Medium2_group.add(Medium2_sprite2)
Medium2_group.add(Medium2_sprite3)
all_buildings.add(Medium2_sprite1)
all_buildings.add(Medium2_sprite2)
all_buildings.add(Medium2_sprite3)

class Small1(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.total_stages = 1
		self.stages = [small1d1, small1]
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
small1_group = pygame.sprite.Group()
small1_sprite1 = Small1(390, 890)
small1_group.add(small1_sprite1)
all_buildings.add(small1_sprite1)

class Small2(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.total_stages = 1
		self.stages = [small2d1, small2]
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
small2_group = pygame.sprite.Group()
small2_sprite1 = Small2(854, 890)
small2_group.add(small2_sprite1)
all_buildings.add(small2_sprite1)

class Small3(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.total_stages = 1
		self.stages = [small3d1, small3]
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
small3_group = pygame.sprite.Group()
small3_sprite1 = Small3(236, 860)
small3_group.add(small3_sprite1)
all_buildings.add(small3_sprite1)



# Guns class description
class Gun(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.Surface([80, 38])
		self.image = gun1
		self.rect  = self.image.get_rect()
		self.originX = x
		self.originY = y
		self.rect.x = self.originX
		self.rect.y = self.originY
		self.upgraded = False
	def upgrade(self):
		self.image = gun2
		self.rect = self.image.get_rect(x=self.originX, y=self.originY)
		self.upgraded = True
	def upgrade_status(self):
		return self.upgraded
gun_group =  pygame.sprite.Group()
gun_sprite = Gun(580, 730)
gun_group.add(gun_sprite)

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
		self.dir = 2
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
	def __init__(self, x, y, left, right):
		super().__init__()
		self.imageMaster = barrel
		self.image = self.imageMaster
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.originX = x
		self.left_limit = left
		self.right_limit = right
		self.angle = 0
		self.dir = 5
		centerX = x + 2
		centerY = y + 13
		self.rect.center = (centerX, centerY)
	def update(self):
		global ANGLE1, ANGLE2, ANGLE4, ANGLE5, ANGLE6
		self.angle = self.angle + self.dir
		if self.angle >= self.right_limit:
			self.dir = -1
		elif self.angle <= self.left_limit:
			self.dir = 1
		if self.originX == 65:
			ANGLE1 = 0 - self.angle
		elif self.originX == 353:
			ANGLE2 = 0 - self.angle
		elif self.originX == 818:
			ANGLE4 = 0 - self.angle
		elif self.originX == 998:
			ANGLE5 = 0 - self.angle
		elif self.originX == 1218:
			ANGLE6 = 0 - self.angle
		oldCenter = self.rect.center
		self.image = pygame.transform.rotate(self.imageMaster, self.angle)
		self.rect = self.image.get_rect()
		self.rect.center = oldCenter

# Bullet Main
class User_Bullet(pygame.sprite.Sprite):
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
	
user_bullets = pygame.sprite.Group()


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
	global no_Meteor1, no_Meteor2, no_Meteor3, no_Meteor4
	global GUN1, GUN2, GUN4, GUN5, GUN6, UPGRADE_GUN_MIN, ADD_GUN_MIN
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
		if ticks >= 12:
			meteor2_group.update()
			meteor2_group.draw(screen)
		if ticks >= 18:
			meteor3_group.update()
			meteor3_group.draw(screen)
		if ticks >= 24:
			meteor4_group.update()
			meteor4_group.draw(screen)
		
		all_buildings.draw(screen)
		
		# User Bullets
		user_bullets.draw(screen)
		user_bullets.update()

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
		screen.blit(fusion ,[1120, 20])

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
		building_collision = pygame.sprite.groupcollide(all_meteors_group, all_buildings, False, False)
		if building_collision:
			building_hit = list(building_collision.values())[0].pop()
			building_hit.destroy()
			meteor_hit = list(building_collision.keys())[0]
			if meteor1_group.has(meteor_hit):
				meteor_hit.kill()
				add_meteor(Meteor1, meteor1_group)
			elif meteor2_group.has(meteor_hit):
				meteor_hit.kill()
				add_meteor(Meteor2, meteor2_group)
			elif meteor3_group.has(meteor_hit):
				meteor_hit.kill()
				add_meteor(Meteor3, meteor3_group)
			elif meteor4_group.has(meteor_hit):
				meteor_hit.kill()
				add_meteor(Meteor4, meteor4_group)

		# Bullet-Meteor Collision Detection
		user_meteor_collision = pygame.sprite.groupcollide(user_bullets, all_meteors_group, True, False)
		computer_meteor_collision = pygame.sprite.groupcollide(computer_bullets, all_meteors_group, True, False)

		if user_meteor_collision:
			meteor_hit = list(user_meteor_collision.values())[0].pop()
			health_after_hit = meteor_hit.hit()
			if health_after_hit == 0:
				if meteor1_group.has(meteor_hit):
					updated_score = SCORE + 100
					updated_fusion = FUSION + 2
					meteor_hit.kill()
					add_meteor(Meteor1, meteor1_group)
				elif meteor2_group.has(meteor_hit):
					updated_score = SCORE + 200
					updated_fusion = FUSION + 4
					meteor_hit.kill()
					add_meteor(Meteor2, meteor2_group)
				elif meteor3_group.has(meteor_hit):
					updated_score = SCORE + 250
					updated_fusion = FUSION + 6
					meteor_hit.kill()
					add_meteor(Meteor3, meteor3_group)
				elif meteor4_group.has(meteor_hit):
					updated_score = SCORE + 400
					updated_fusion = FUSION + 8
					meteor_hit.kill()
					add_meteor(Meteor4, meteor4_group)
				SCORE = updated_score
				FUSION = updated_fusion

		if computer_meteor_collision:
			meteor_hit = list(computer_meteor_collision.values())[0].pop()
			health_after_hit = meteor_hit.hit()
			if health_after_hit == 0:
				if meteor1_group.has(meteor_hit):
					updated_score = SCORE + 50
					updated_fusion = FUSION + 1
					meteor_hit.kill()
					add_meteor(Meteor1, meteor1_group)
				elif meteor2_group.has(meteor_hit):
					updated_score = SCORE + 100
					updated_fusion = FUSION + 2
					meteor_hit.kill()
					add_meteor(Meteor2, meteor2_group)
				elif meteor3_group.has(meteor_hit):
					updated_score = SCORE + 125
					updated_fusion = FUSION + 3
					meteor_hit.kill()
					add_meteor(Meteor3, meteor3_group)
				elif meteor4_group.has(meteor_hit):
					updated_score = SCORE + 200
					updated_fusion = FUSION + 4
					meteor_hit.kill()
					add_meteor(Meteor4, meteor4_group)
				SCORE = updated_score
				FUSION = updated_fusion
		
		# User Barrel Controls
		pressed_key = pygame.key.get_pressed()
		if pressed_key[pygame.K_LEFT]:
			user_barrel_sprite.turn_left()  
		if pressed_key[pygame.K_RIGHT]:
			user_barrel_sprite.turn_right()	
		
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					if len(user_bullets) <= 5:
						add_bullet(User_Bullet, USERANGLE, user_bullets)
				if FUSION >= UPGRADE_GUN_MIN:
					if event.key == pygame.K_u:
						if NEXT_UPGRADE < 6:
							upgrade_gun()
						FUSION = FUSION - UPGRADE_GUN_MIN
				if FUSION >= ADD_GUN_MIN:
					if event.key == pygame.K_p:
						if len(POSITIONS) < 6:
							add_gun()
						FUSION = FUSION - ADD_GUN_MIN
			if event.type == pygame.QUIT:
				QUITGAME = True
		
		pygame.display.flip()


def how_to_play():
	how_to_play = True
	while how_to_play:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				how_to_play = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					how_to_play = False
		screen.blit(how_to_play_img, [0,0])
		pygame.display.flip()
def game_over():
	game_over = True
	global QUITGAME
	while game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = False
				QUITGAME = True
		screen.blit(game_over_img, [0,0])
		score_total = scoreFont.render(str((FUSION * 10) + SCORE), True, (255,255,255))
		screen.blit(score_total, (670, 565))
		pygame.display.flip()
def intro_loop():
	intro =  True
	global QUITGAME
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				intro = False
				QUITGAME = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					intro = False
				if event.key == pygame.K_h:
					how_to_play()
					intro = False
		screen.blit(intro_img, [0,0])
		pygame.display.flip()
def fire_bullets():
	global ANGLE1, ANGLE2, ANGLE4, ANGLE5, ANGLE6, GUNS_ACTIVE
	if GUNS_ACTIVE[1]:
		add_bullet(Bullet1, ANGLE1, bullet1_group)
	if GUNS_ACTIVE[2]:
		add_bullet(Bullet2, ANGLE2, bullet2_group)
	if GUNS_ACTIVE[3]:
		add_bullet(Bullet4, ANGLE4, bullet4_group)
	if GUNS_ACTIVE[4]:
		add_bullet(Bullet5, ANGLE5, bullet5_group)
	if GUNS_ACTIVE[5]:
		add_bullet(Bullet6, ANGLE6, bullet6_group)
def add_bullet(Type, angle, type_group):
	bullet_sprite = Type()
	bullet_sprite.direction(angle)
	type_group.add(bullet_sprite)
	all_bullets.add(bullet_sprite)
	if type_group != user_bullets:
		computer_bullets.add(bullet_sprite)
def add_gun():
	global POSITIONS, GUN_POSITIONS, GUNS_ACTIVE
	i = random.randint(1, 5)
	while i in POSITIONS:
		i = random.randint(1, 5)
	POSITIONS.append(i)
	gun_sprite = Gun(GUN_POSITIONS[i][0], GUN_POSITIONS[i][1])
	gun_group.add(gun_sprite)
	GUNS_ACTIVE[i] = True
	add_barrel(i)
def upgrade_gun():
	global NEXT_UPGRADE, GUNS_UPGRADED
	all_guns = list(gun_group.sprites())
	all_guns[NEXT_UPGRADE].upgrade()
	# print("Iterator groing through Positions: ", NEXT_UPGRADE)
	# print("Positions array: ", POSITIONS)
	# print("Gun to be upgraded next: ", POSITIONS[NEXT_UPGRADE])
	GUNS_UPGRADED[POSITIONS[NEXT_UPGRADE]] = True
	# print("Status of guns:")
	# print("Guns Active:", GUNS_ACTIVE)
	# print("Guns Upgraded: ", GUNS_UPGRADED)
	NEXT_UPGRADE += 1
def add_barrel(i):
	global BARRELS
	barrel_sprite = Barrel(BARRELS[i][0], BARRELS[i][1], BARRELS[i][2], BARRELS[i][3])
	barrel_group.add(barrel_sprite)
intro_loop()
game_loop()
game_over()














