import pygame
import random
import math

pygame.init()


# Game Settings
size = (1280,960) # so we can change later
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Skyline Defence")

# Global Variables
quitgame = False # as quit is a keyword and to signal when when the game is closed
clock = pygame.time.Clock()
background_img = pygame.image.load("img/bg.png")


# Game Assets
tall1 = pygame.transform.scale(pygame.image.load("img/tall1.png"), [65,170])#790
tall2 = pygame.transform.scale(pygame.image.load("img/tall2.png"), [125,196])#764
tall3 = pygame.transform.scale(pygame.image.load("img/tall3.png"), [125,196])#764
medium1 = pygame.transform.scale(pygame.image.load("img/medium1.png"), [116,140])#820
medium2 = pygame.transform.scale(pygame.image.load("img/medium2.png"), [116,140])#820
small1 = pygame.transform.scale(pygame.image.load("img/small1.png"), [82,70])#890
small2 = pygame.transform.scale(pygame.image.load("img/small2.png"), [82,70])#890
small3 = pygame.transform.scale(pygame.image.load("img/small3.png"), [97,100])#860
coins = pygame.transform.scale(pygame.image.load("img/coins.PNG"), [28,45])
#coin = pygame.transform.scale(pygame.image.load("img/coin.PNG") [])
#upgrade = pygame.transform.scale(pygame.image.load("img/upgrade.PNG"), [x])
upgrade_faded = pygame.transform.scale(pygame.image.load("img/upgrade_faded.PNG"), [70,22])
meteor1 = pygame.transform.scale(pygame.image.load("img/meteor1.png"), [25,49])
meteor2 = pygame.transform.scale(pygame.image.load("img/meteor2.png"), [40,66])
meteor3 = pygame.transform.scale(pygame.image.load("img/meteor3.png"), [20,52])



while not quitgame: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quitgame = True
	
	# Game Logic

	# Game Refresh
	screen.blit(background_img, [0,0])
	
	# Game Assset Placement

	#skyline
	screen.blit(tall2, [0,764])
	screen.blit(medium2, [120,820])
	screen.blit(small3, [235,860])
	screen.blit(tall1, [322,790])
	screen.blit(small1, [390,890])
	screen.blit(medium2, [470,820 ])
	screen.blit(tall3,  [560,764])
	screen.blit(medium1,  [674,820])
	screen.blit(tall1,  [787,790])
	screen.blit(small2,[854,890] )
	screen.blit(tall2, [935,764])
	screen.blit(medium2,[1050, 820])
	screen.blit(tall3,[1160, 764] )
	
	screen.blit(coins, [1120, 20])

	#buttons
	screen.blit(upgrade_faded, [20,780])
	screen.blit(upgrade_faded, [580,780])
	screen.blit(upgrade_faded, [955,780])
	screen.blit(upgrade_faded, [1180,780])
	screen.blit(upgrade_faded, [330,805])
	screen.blit(upgrade_faded, [ 795,805])

	#meteor
	screen.blit(meteor1, [500,500])
	screen.blit(meteor2, [550,550])
	screen.blit(meteor3, [300,200])
	#class meteor(pygame.sprite)
	




	pygame.display.flip()

