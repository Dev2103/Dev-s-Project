import pygame
import random
import math

meteor1 = pygame.transform.scale(pygame.image.load("img/meteor1.png"), [25,49])
meteor2 = pygame.transform.scale(pygame.image.load("img/meteor2.png"), [40,66])
meteor3 = pygame.transform.scale(pygame.image.load("img/meteor3.png"), [20,52])
meteor4 = pygame.transform.scale(pygame.image.load("img/meteor4.png"), [45,78])

meteor1_speed = 10     #2.4
meteor2_speed = 1.5
meteor3_speed = 3.0
meteor4_speed = 1.7

# Meteor Class Descriptions
class Meteor1(pygame.sprite.Sprite):
	# Constructor
	def __init__(self, width, height):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image = meteor1
		self.rect = self.image.get_rect()

		self.rect.x = random.randrange(0, 1200)
		self.rect.y = random.randrange(-1500, 0) #-1500
		# self.rect.x = 618
		# self.rect.y = random.randrange(0, 300)
	def update(self):
		global QUITGAME
		self.rect.y = self.rect.y + meteor1_speed
		self.rect.x = self.rect.x + random.randrange(-1,2)
		if self.rect.y >= 700: #960
			QUITGAME = True
			# self.rect.x = random.randrange(0, 1280)
			# self.rect.y = random.randrange(-2000, 0)

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
		if self.rect.y >= 500:
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
		if self.rect.y >= 500:
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
		if self.rect.y >= 500:
			self.rect.x = random.randrange(0, 1280)
			self.rect.y = random.randrange(-3000,0)