import pygame
import random
import math
import time
import sys

SILVER = (192,192,192)	# FOR GUN 1 BULLET
GOLD = (255,215,0)		# FOR GUN 2 BULLET
BLUE = (18,198,236)		# FOR GUN 1 BARREL
GOLDISH = (234,154,0)	# FOR GUN 2 BARREL


pygame.init()


# Game Settings
size = (1280,960) # so we can change later
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Skyline Defence")
background_img = pygame.image.load("img/bg.png")
clock = pygame.time.Clock()
timerFont = pygame.font.Font(None, 36)

# Global Variables
# quitgame = False # as quit is a keyword and to signal when when the game is closed
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


# Meteor Class Descriptions
class Meteor1(pygame.sprite.Sprite):
	# Constructor
	def __init__(self, width, height):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image = meteor1
		self.rect = self.image.get_rect()

		self.rect.x = random.randrange(0, 1200)
		self.rect.y = random.randrange(100, 200) #-1500
	def update(self):
		self.rect.y = self.rect.y + meteor1_speed
		self.rect.x = self.rect.x + random.randrange(-1,2)
		if self.rect.y >= 960:
			self.rect.x = random.randrange(0, 1280)
			self.rect.y = random.randrange(-2000, 0)

class Meteor2(pygame.sprite.Sprite):
	# Constructor
	def __init__(self, width, height):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image = meteor2
		self.rect = self.image.get_rect()

		self.rect.x = random.randrange(0, 1200)
		# self.rect.x = 600
		self.rect.y = random.randrange(-3000,0) #-1500
	def update(self):
		self.rect.y = self.rect.y + meteor2_speed
		self.rect.x = self.rect.x + random.randrange(-1,2)
		if self.rect.y >= 960:
			self.rect.x = random.randrange(0, 1280)
			self.rect.y = random.randrange(-3000,0)

class Meteor3(pygame.sprite.Sprite):
	# Constructor
	def __init__(self, width, height):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image = meteor3
		self.rect = self.image.get_rect()

		self.rect.x = random.randrange(0, 1200)
		# self.rect.x = 600
		self.rect.y = random.randrange(-1500, 0)
	def update(self):
		self.rect.y = self.rect.y + meteor3_speed
		self.rect.x = self.rect.x + random.randrange(-1,2)
		if self.rect.y >= 960:
			self.rect.x = random.randrange(0, 1280)
			self.rect.y = random.randrange(-3000,0)

class Meteor4(pygame.sprite.Sprite):
	# Constructor
	def __init__(self, width, height):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image = meteor4
		self.rect = self.image.get_rect()

		self.rect.x = random.randrange(0, 1200)
		# self.rect.x = 600
		self.rect.y = random.randrange(-1500,0)
	def update(self):
		self.rect.y = self.rect.y + meteor4_speed
		self.rect.x = self.rect.x + random.randrange(-1,2)
		if self.rect.y >= 960:
			self.rect.x = random.randrange(0, 1280)
			self.rect.y = random.randrange(-3000,0)

# Meteor Sprite Creation
all_meteors_group = pygame.sprite.Group()
no_Meteor1 = 8
no_Meteor2 = 4
no_Meteor3 = 3
no_Meteor4 = 3

meteor1_group = pygame.sprite.Group()
for x in range (no_Meteor1):
	meteor1_sprite = Meteor1(25, 49)
	meteor1_group.add(meteor1_sprite)
	all_meteors_group.add(meteor1_sprite)

meteor2_group = pygame.sprite.Group()
for x in range (no_Meteor2):
	meteor2_sprite = Meteor2(40,66)
	meteor2_group.add(meteor2_sprite)
	all_meteors_group.add(meteor2_sprite)

meteor3_group = pygame.sprite.Group()
for x in range (no_Meteor3):
	meteor3_sprite = Meteor3(20,52)
	meteor3_group.add(meteor3_sprite)
	all_meteors_group.add(meteor3_sprite)

meteor4_group = pygame.sprite.Group()
for x in range (no_Meteor4):
	meteor4_sprite = Meteor4(45,78)
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
gun_sprite3 = Gun(80, 38, 780, 753)
gun_sprite4 = Gun(80, 38, 960, 730)
gun_sprite5 = Gun(80, 38, 1180, 730)
gun_group.add(gun_sprite1)
gun_group.add(gun_sprite2)
gun_group.add(gun_sprite3)
gun_group.add(gun_sprite4)
gun_group.add(gun_sprite5)


		# screen.blit(gun1, [27,730])
		# screen.blit(gun2, [27,730]) 

		# screen.blit(gun1, [315,753])
		# screen.blit(gun2, [315,753]) 

		

		# screen.blit(gun1, [780,753])
		# screen.blit(gun2, [780,753]) 

		# screen.blit(gun1, [960,730])
		# screen.blit(gun2, [960,730]) 
		
		# screen.blit(gun1, [1180,730])
		# screen.blit(gun2, [1180,730]) 




# Bullets
bullet_group = pygame.sprite.Group()
class Bullet(pygame.sprite.Sprite):
	def __init__(self, width, height, x, y, color):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(SILVER)
		self.rect = self.image.get_rect()
		self.rect.x = x - 5
		self.rect.y = y - 5
	def update(self, x, y):
		self.rect.y = self.rect.y -10
		if self.rect.y <= 0:
			self.rect.x = x
			self.rect.y = y

bullet_sprite1 = Bullet(5, 5, 27, 715, SILVER)
bullet_sprite2 = Bullet(5, 5, 315, 715, SILVER)
bullet_sprite3 = Bullet(5, 5, 780, 715, SILVER)
bullet_sprite4 = Bullet(5, 5, 960, 715, SILVER)
bullet_sprite5 = Bullet(5, 5, 1180, 715, SILVER)
bullet_sprite6 = Bullet(5, 5, 580, 715, SILVER)
bullet_group.add(bullet_sprite1)
bullet_group.add(bullet_sprite2)
bullet_group.add(bullet_sprite3)
bullet_group.add(bullet_sprite4)
bullet_group.add(bullet_sprite5)
bullet_group.add(bullet_sprite6)



# bullet_group = pygame.sprite.Group()
# class Bullet(pygame.sprite.Sprite):
# 	def __init__(self, width, height, radius, x, y, color):
# 		super().__init__()
# 		self.image = pygame.Surface([width, height])
# 		pygame.draw.circle(self.image, color, (x, y), radius, 0)
# 		self.rect = self.image.get_rect()
# 		self.rect.x = x - 5
# 		self.rect.y = y - 5
# 	def update(self, x, y):
# 		self.rect.y = self.rect.y -10
# 		if self.rect.y <= 0:
# 			self.rect.x = x
# 			self.rect.y = y

# bullet_sprite1 = Bullet(10, 10, 10, 27, 715, SILVER)

# bullet_group.add(bullet_sprite1)

		


# bullet_group = pygame.sprite.Group()
# for x in range (10):
# 	bullet_sprite = Bullet(10, 10, SILVER)
# 	bullet_group.add(bullet_sprite)




def game_loop():
	quitgame = False
	while not quitgame: 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitgame = True
		
		# Background Refresh
		screen.blit(background_img, [0,0])
		
		# Clock & Timer
		seconds = (int(pygame.time.get_ticks()/1000))%60
		minutes = int(pygame.time.get_ticks()/60000)
		timer = "{:02d}:{:02d}".format(minutes, seconds)
		timerText = timerFont.render(str(timer), True, (255,255,255))
		screen.blit(timerText, (10,10))
		
		# Meteor timing
		ticks = int(pygame.time.get_ticks()/1000)
		meteor1_group.update()
		meteor1_group.draw(screen)
		if ticks >= 45:
			meteor2_group.update()
			meteor2_group.draw(screen)
		if ticks >= 105:
			meteor3_group.update()
			meteor3_group.draw(screen)
		if ticks >= 180:
			meteor4_group.update()
			meteor4_group.draw(screen)


		allBuildings.draw(screen)
		gun_group.draw(screen)
		# gun_sprite1.draw(screen)
		bullet_group.draw(screen)
		bullet_sprite1.update(27, 715)
		bullet_sprite2.update(315, 715)
		bullet_sprite3.update(780, 715)
		bullet_sprite4.update(960, 715)
		bullet_sprite5.update(1180, 715)
		bullet_sprite6.update(580, 715)

		# Barrels
		pygame.draw.rect(screen, GOLDISH, (64,731,10,50))


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
	
		screen.blit(gun1, [580,726])  # USER CONTROLLED
		screen.blit(gun2, [580,726]) 


		pygame.display.flip()

		collision = pygame.sprite.groupcollide(meteor1_group, allBuildings, False, True)

		collision = pygame.sprite.groupcollide(meteor2_group, allBuildings, False, True)

		collision = pygame.sprite.groupcollide(meteor3_group, allBuildings, False, True)

		collision = pygame.sprite.groupcollide(meteor4_group, allBuildings, False, True)
		# print(collision)

		
 
def intro_loop():
	intro =  True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				intro = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					intro = False
					
		screen.fill(GOLD)
		introText = timerFont.render("Skyline Defence", True, (0,0,0))
		screen.blit(introText, [500,500])
		pygame.display.flip()

intro_loop()
game_loop()