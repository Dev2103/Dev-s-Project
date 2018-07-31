import pygame
import random
import math
import time
import sys

SILVER = (192,192,192)	# FOR GUN 1 BULLET
GOLD = (255,215,0)		# FOR GUN 2 BULLET
BLUE = (18,198,236)		# FOR GUN 1 BARREL
GOLDISH = (234,154,0)	# FOR GUN 2 B

pygame.init()


# Game Settings
size = (1280,960) # so we can change later
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Skyline Defence")
background_img = pygame.image.load("img/bg.png")
clock = pygame.time.Clock()
timerFont = pygame.font.Font(None, 36)

# Global Variables
quitgame = False # as quit is a keyword and to signal when when the game is closed
meteor1_speed = 1.9
meteor2_speed = 1
meteor3_speed = 2
meteor4_speed = 1.3



# Game Assets
tall1 = pygame.transform.scale(pygame.image.load("img/tall1.png"), [65,170])#790
tall1d1 = pygame.transform.scale(pygame.image.load("img/tall1d1.png"), [65,145])
tall1d2 = pygame.transform.scale(pygame.image.load("img/tall1d2.png"), [65,83])

tall2 = pygame.transform.scale(pygame.image.load("img/tall2.png"), [125,196])#764
tall2d1 = pygame.transform.scale(pygame.image.load("img/tall2d1.png"), [125,179])#790
tall2d2 = pygame.transform.scale(pygame.image.load("img/tall2d2.png"), [125,105])#790

tall3 = pygame.transform.scale(pygame.image.load("img/tall3.png"), [125,196])#764
tall3d1 = pygame.transform.scale(pygame.image.load("img/tall3d1.png"), [125,166])#790
tall3d2 = pygame.transform.scale(pygame.image.load("img/tall3d2.png"), [125,109])#790

medium1 = pygame.transform.scale(pygame.image.load("img/medium1.png"), [116,140])#820
medium1d1 = pygame.transform.scale(pygame.image.load("img/medium1d1.png"), [116,125])#790
medium1d2 = pygame.transform.scale(pygame.image.load("img/medium1d2.png"), [116,71])#790

medium2 = pygame.transform.scale(pygame.image.load("img/medium2.png"), [116,140])#820
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


#Class Descriptions
class Meteor1(pygame.sprite.Sprite):
	# Constructor
	def __init__(self, width, height):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image = meteor1
		self.rect = self.image.get_rect()

		self.rect.x = random.randrange(0, 1200)
		# self.rect.x = 600
		self.rect.y = random.randrange(-1500, 0)
	def update(self):
		self.rect.y = self.rect.y + meteor1_speed
		self.rect.x = self.rect.x + random.randrange(-1,2)
		if self.rect.y >= 960:
			self.rect.x = random.randrange(0, 1280)
			self.rect.y = random.randrange(-1500, 0)

class Meteor2(pygame.sprite.Sprite):
	# Constructor
	def __init__(self, width, height):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image = meteor2
		self.rect = self.image.get_rect()

		self.rect.x = random.randrange(0, 1200)
		# self.rect.x = 600
		self.rect.y = random.randrange(-1500,0)
	def update(self):
		self.rect.y = self.rect.y + meteor2_speed
		self.rect.x = self.rect.x + random.randrange(-1,2)
		if self.rect.y >= 960:
			self.rect.x = random.randrange(0, 1280)
			self.rect.y = random.randrange(-1500, 0)

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
			self.rect.y = random.randrange(-1500, 0)

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
			self.rect.y = random.randrange(-1500, 0)
		
# All Meteor Sprites Group
all_meteors_group = pygame.sprite.Group()


meteor1_group = pygame.sprite.Group()
no_of_meteors = 5
for x in range (no_of_meteors):
	meteor1_sprite = Meteor1(25, 49)
	meteor1_group.add(meteor1_sprite)
	all_meteors_group.add(meteor1_sprite)

meteor2_group = pygame.sprite.Group()
no_of_meteors = 3
for x in range (no_of_meteors):
	meteor2_sprite = Meteor2(40,66)
	meteor2_group.add(meteor2_sprite)
	all_meteors_group.add(meteor2_sprite)

meteor3_group = pygame.sprite.Group()
no_of_meteors = 3
for x in range (no_of_meteors):
	meteor3_sprite = Meteor3(20,52)
	meteor3_group.add(meteor3_sprite)
	all_meteors_group.add(meteor3_sprite)

meteor4_group = pygame.sprite.Group()
no_of_meteors = 3
for x in range (no_of_meteors):
	meteor4_sprite = Meteor4(45,78)
	meteor4_group.add(meteor4_sprite)
	all_meteors_group.add(meteor4_sprite)


# Main Loop
while not quitgame: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quitgame = True
	
	# Background Refresh
	screen.blit(background_img, [0,0])
	
	#Clock & Timer
	clock.tick()
	seconds = (int(pygame.time.get_ticks()/1000))%60
	minutes = int(pygame.time.get_ticks()/60000)
	timer = "{:02d}:{:02d}".format(minutes, seconds)
	timerText = timerFont.render(str(timer), True, (255,255,255))
	screen.blit(timerText, (80,60))
	
	#all_meteors_group.update()
	meteor1_group.update()
	meteor2_group.update()
	meteor3_group.update()
	meteor4_group.update()

	# Game Logic
	
	#all_meteors_group.draw(screen)
	meteor1_group.draw(screen)
	meteor2_group.draw(screen)
	meteor3_group.draw(screen)
	meteor4_group.draw(screen)
	

	# Game Assset Placement

	#skyline
	screen.blit(tall2,[0,764])			#1 WEAPON
	#screen.blit(tall2d1,[0,781])
	#screen.blit(tall2d2,[0,855])
	
	screen.blit(medium2,[120,820])		#2
	#screen.blit(medium2d1,[120,835])
	#screen.blit(medium2d2,[120,889])
	
	screen.blit(small3,[235,860])		#3
	#screen.blit(small3d1,[235,884])

	screen.blit(tall1, [322,790])		#4 WEAPON
	#screen.blit(tall1d1, [322,815])
	#screen.blit(tall1d2, [322,877])

	screen.blit(small1, [390,890])		#5
	#screen.blit(small1d1, [390,909])

	screen.blit(medium2, [470,820 ])	#6
	#screen.blit(medium2d1, [470,836])
	#screen.blit(medium2d2, [470,889])

	screen.blit(tall3,  [560,764])		#7 WEAPON
	#screen.blit(tall3d1, [560,794])
	#screen.blit(tall3d2, [560,851])

	screen.blit(medium1,  [674,820])	#8
	#screen.blit(medium1d1, [674,835])
	#screen.blit(medium1d2, [674,889])

	screen.blit(tall1,  [787,790])		#9 WEAPON
	#screen.blit(tall1d1, [787,815])
	#screen.blit(tall1d2, [787,877])

	screen.blit(small2,[854,890])		#10
	#screen.blit(small2d1, [854,889])

	screen.blit(tall2, [935,764])		#11 WEAPON
	#screen.blit(tall2d1, [935,781])
	#screen.blit(tall2d2, [935,855])

	screen.blit(medium2,[1050, 820])	#12
	#screen.blit(medium2d1, [1050,836])
	#screen.blit(medium2d2, [1050,889])

	screen.blit(tall3,[1160, 764] )		#13 WEAPON
	#screen.blit(tall3d1, [1160,794])
	#screen.blit(tall3d2, [1160,851])

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
	screen.blit(gun1, [27,730])
	screen.blit(gun2, [27,730]) 

	screen.blit(gun1, [315,753])
	screen.blit(gun2, [315,753]) 

	screen.blit(gun1, [580,726])
	screen.blit(gun2, [580,726]) 

	screen.blit(gun1, [780,753])
	screen.blit(gun2, [780,753]) 

	screen.blit(gun1, [960,730])
	screen.blit(gun2, [960,730]) 
	
	screen.blit(gun1, [1180,730])
	screen.blit(gun2, [1180,730]) 

	# def is_collided_with(self, sprite):
 #    	return self.rect.colliderect(sprite.rect)
	
	# 		if meteor1_group.is_collided_with(tall2):
				
 #    		meteor1_group.kill()
 #    		tall2.kill()


 	# hit = pygame.sprite.spritecollide(tall2,meteor1_group,True)
 	# if hit:
 	# 	screen.fill(255,255,255)
	


	
	

	pygame.display.flip()

