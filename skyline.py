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


