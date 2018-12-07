import pygame
import random
import math
from global_vars import *
from assets import *

# Guns class description
class Gun(pygame.sprite.Sprite):
	def __init__(self, x, y, number):
		super().__init__()
		self.image = pygame.Surface([80, 38])
		self.image = gun1
		self.rect  = self.image.get_rect()
		self.originX = x
		self.originY = y
		self.rect.x = self.originX
		self.rect.y = self.originY
		self.upgraded = False
		self.number = number
	def upgrade(self):
		self.image = gun2
		self.rect = self.image.get_rect(x=self.originX, y=self.originY)
		self.upgraded = True
	def upgrade_status(self):
		return self.upgraded
	def get_number(self):
		return self.number

gun_group =  pygame.sprite.Group()
gun_sprite = Gun(580, 730, 0)
gun_group.add(gun_sprite)

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

barrel_group = pygame.sprite.Group()
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
		self.angle = USERANGLE

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
		self.angle = ANGLE1

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
		self.angle = ANGLE4
	
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
		self.angle = ANGLE5
		
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
		self.angle = ANGLE6

### Bullet Groups

# User Bullets
user_bullets = pygame.sprite.Group()
# User Upgraded Bullets
upgraded_user_bullets = pygame.sprite.Group()

# Computer Bullets
bullet1_group = pygame.sprite.Group()
bullet2_group = pygame.sprite.Group()
bullet4_group = pygame.sprite.Group()
bullet5_group = pygame.sprite.Group()
bullet6_group = pygame.sprite.Group()
# All Computer Bullets 
computer_bullets = pygame.sprite.Group()

# Upgraded Computer Bullets
upgraded_bullet1_group = pygame.sprite.Group()
upgraded_bullet2_group = pygame.sprite.Group()
upgraded_bullet4_group = pygame.sprite.Group()
upgraded_bullet5_group = pygame.sprite.Group()
upgraded_bullet6_group = pygame.sprite.Group()
# All Upgraded Computer Bullets
upgraded_computer_bullets = pygame.sprite.Group()

# All Bullets
all_bullets = pygame.sprite.Group()







