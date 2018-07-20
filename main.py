import pygame

pygame.init()

size = (1280,960) # so we can change later
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Skyline Defence")
quitgame= False # as quit is a keyword and to signal when when the game is closed
clock = pygame.time.Clock()
background_img = pygame.image.load("img/bg.png")
while not quitgame: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quitgame = True
	screen.blit(background_img, [0,0])
	
















	pygame.display.flip()

