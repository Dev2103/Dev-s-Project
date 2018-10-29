import pygame
import random
import math
from global_vars import *
from assets import *

# Building Classes
class Tall1(pygame.sprite.Sprite):
	def __init__(self, x, y, number):
		super().__init__() 
		self.total_stages = 2
		self.stages = [tall1d2, tall1d1, tall1]
		self.image = self.stages[self.total_stages]
		self.rect = self.image.get_rect()
		self.originX = x
		self.originY = y
		self.rect.x = self.originX
		self.rect.y = self.originY
		self.number = number
		self.destroyed = False
	def destroy(self):
		if (self.total_stages > 0):
			self.total_stages = self.total_stages - 1
			self.image = self.stages[self.total_stages]
			self.rect = self.image.get_rect(x=self.originX, y=self.originY)
		else:
			self.image = pygame.Surface([0,0])
			self.rect = self.image.get_rect(width=0, height=0)
		self.destroyed = True
	def get_number(self):
		return self.number
	def check_state(self):
		return self.destroyed

class Tall2(pygame.sprite.Sprite):
	def __init__(self, x, y, number):
		super().__init__()
		self.total_stages = 2
		self.stages = [tall2d2, tall2d1, tall2]
		self.image = self.stages[self.total_stages]
		self.rect = self.image.get_rect()
		self.originX = x
		self.originY = y
		self.rect.x = self.originX
		self.rect.y = self.originY
		self.number = number
		self.destroyed = False
	def destroy(self):
		if (self.total_stages > 0):
			self.total_stages = self.total_stages - 1
			self.image = self.stages[self.total_stages]
			self.rect = self.image.get_rect(x=self.originX, y=self.originY)
		else:
			self.image = pygame.Surface([0,0])
			self.rect = self.image.get_rect(width=0, height=0)
		self.destroyed = True
	def get_number(self):
		return self.number
	def check_state(self):
		return self.destroyed

class Tall3(pygame.sprite.Sprite):
	def __init__(self, x, y, number):
		super().__init__()
		self.total_stages = 2
		self.stages = [tall3d2, tall3d1, tall3]
		self.image = self.stages[self.total_stages]
		self.rect = self.image.get_rect()
		self.originX = x
		self.originY = y
		self.rect.x = self.originX
		self.rect.y = self.originY
		self.number = number
		self.destroyed = False
	def destroy(self):
		if (self.total_stages > 0):
			self.total_stages = self.total_stages - 1
			self.image = self.stages[self.total_stages]
			self.rect = self.image.get_rect(x=self.originX, y=self.originY)
		else:
			self.image = pygame.Surface([0,0])
			self.rect = self.image.get_rect(width=0, height=0)
		self.destroyed = True
	def get_number(self):
		return self.number
	def check_state(self):
		return self.destroyed

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
	def get_number(self):
		return -1

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
	def get_number(self):
		return -1

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
	def get_number(self):
		return -1

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
	def get_number(self):
		return -1

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
	def get_number(self):
		return -1

# Building Groups
all_buildings = pygame.sprite.Group()
buildings_with_guns = pygame.sprite.Group()

# Building Sprites
tall1_sprite1 = Tall1(322, 790, 2)
tall1_sprite2 = Tall1(787, 790, 3)
tall2_sprite1 = Tall2(0 ,764, 1)
tall2_sprite2 = Tall2(935, 764, 4)
tall3_sprite1 = Tall3(560 ,764, 0)
tall3_sprite2 = Tall3(1160, 764, 5)
Medium1_sprite1 = Medium1(674, 820)
Medium2_sprite1 = Medium2(120, 820)
Medium2_sprite2 = Medium2(470, 820)
Medium2_sprite3 = Medium2(1050, 820)
small1_sprite1 = Small1(390, 890)
small2_sprite1 = Small2(854, 890)
small3_sprite1 = Small3(236, 860)

all_buildings.add(tall1_sprite1)
all_buildings.add(tall1_sprite2)
all_buildings.add(tall2_sprite1)
all_buildings.add(tall2_sprite2)
all_buildings.add(tall3_sprite1)
all_buildings.add(tall3_sprite2)
all_buildings.add(Medium1_sprite1)
all_buildings.add(Medium2_sprite1)
all_buildings.add(Medium2_sprite2)
all_buildings.add(Medium2_sprite3)
all_buildings.add(small1_sprite1)
all_buildings.add(small2_sprite1)
all_buildings.add(small3_sprite1)
buildings_with_guns.add(tall1_sprite1)
buildings_with_guns.add(tall1_sprite2)
buildings_with_guns.add(tall2_sprite1)
buildings_with_guns.add(tall2_sprite2)
buildings_with_guns.add(tall3_sprite2)