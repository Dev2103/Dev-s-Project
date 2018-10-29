import pygame
import random
import math
from global_vars import *
from assets import *

normal_hit = 1
upgraded_hit = 2

# Meteor Class Descriptions
class Meteor1(pygame.sprite.Sprite):
	# Constructor
	def __init__(self):
		super().__init__()
		self.image = meteor1
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(0, 1200)
		self.rect.y = random.randrange(-1500, 0)
		self.speed = 2
		self.health = 2
	def update(self):
		self.rect.y = self.rect.y + self.speed
		self.rect.x = self.rect.x + random.randrange(-1,2)
		if self.rect.y >= 960:
			self.rect.x = random.randrange(0, 1280)
			self.rect.y = random.randrange(-2000, 0)
	def hit(self):
		self.health = self.health - normal_hit
		return self.health
	def upgraded_hit(self):
		self.health = self.health - upgraded_hit
		return self.health
	def check_y(self):
		return self.rect.y

class Meteor2(pygame.sprite.Sprite):
	# Constructor
	def __init__(self):
		super().__init__()
		self.image = meteor2
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(0, 1200)
		self.rect.y = random.randrange(-3000,0)
		self.speed = 1.4
		self.health = 4
	def update(self):
		self.rect.y = self.rect.y + self.speed
		self.rect.x = self.rect.x + random.randrange(-1,2)
		if self.rect.y >= 960:
			self.rect.x = random.randrange(0, 1280)
			self.rect.y = random.randrange(-3000,0)
	def hit(self):
		self.health = self.health - normal_hit
		return self.health
	def upgraded_hit(self):
		self.health = self.health - upgraded_hit
		return self.health
	def check_y(self):
		return self.rect.y

class Meteor3(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([20,52])
		self.image = meteor3
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(0, 1200)
		self.rect.y = random.randrange(-1500, 0)
		self.speed = 3
		self.health = 1
	def update(self):
		self.rect.y = self.rect.y + self.speed
		self.rect.x = self.rect.x + random.randrange(-1,2)
		if self.rect.y >= 960:
			self.rect.x = random.randrange(0, 1280)
			self.rect.y = random.randrange(-3000,0)
	def hit(self):
		self.health = self.health - normal_hit
		return self.health
	def upgraded_hit(self):
		self.health = self.health - upgraded_hit
		return self.health
	def check_y(self):
		return self.rect.y

class Meteor4(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([45,78])
		self.image = meteor4
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(0, 1200)
		self.rect.y = random.randrange(-1500,0)
		self.speed = 1.7
		self.health = 8
	def update(self):
		self.rect.y = self.rect.y + self.speed
		self.rect.x = self.rect.x + random.randrange(-1,2)
		if self.rect.y >= 960:
			self.rect.x = random.randrange(0, 1280)
			self.rect.y = random.randrange(-3000,0)
	def hit(self):
		self.health = self.health - normal_hit
		return self.health
	def upgraded_hit(self):
		self.health = self.health - upgraded_hit
		return self.health
	def check_y(self):
		return self.rect.y

def add_meteor(Type, type_group):
	meteor_sprite = Type()
	type_group.add(meteor_sprite)
	all_meteors_group.add(meteor_sprite)

# Meteor Sprite Creation
no_Meteor1 = 10
no_Meteor2 = 3
no_Meteor3 = 3
no_Meteor4 = 3
all_meteors_group = pygame.sprite.Group()
meteor1_group = pygame.sprite.Group()
meteor2_group = pygame.sprite.Group()
meteor3_group = pygame.sprite.Group()
meteor4_group = pygame.sprite.Group()
for x in range (no_Meteor1):
	add_meteor(Meteor1, meteor1_group)
for x in range (no_Meteor2):
	add_meteor(Meteor2, meteor2_group)
for x in range (no_Meteor3):
	add_meteor(Meteor3, meteor3_group)
for x in range (no_Meteor4):
	add_meteor(Meteor4, meteor4_group)