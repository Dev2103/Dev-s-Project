import pygame
import random
import math
import time
import sys
from global_vars import *
from assets import *
from meteors import *
from skyline import *
from guns import *

pygame.init()

# Game Settings
pygame.display.set_caption("Skyline Defence")
clock = pygame.time.Clock()
timerFont = pygame.font.Font(None, 36)
scoreFont = pygame.font.SysFont(None, 40)
pauseFont = pygame.font.SysFont(None, 24)
pygame.mouse.set_visible(False)
cursor_img = pygame.transform.scale(pygame.image.load("img/cursor.png") , [12 , 20])
cursor_img_rect = cursor_img.get_rect()

# Background Music 
pygame.mixer.music.load("music/musicbg.mp3")
pygame.mixer.music.play(-1, 0.0) 

def game_loop():
	global QUITGAME, PAUSED, SCORE, FIRED, DELAY, READY, shot, FUSION
	global no_Meteor1, no_Meteor2, no_Meteor3, no_Meteor4
	global GUN1, GUN2, GUN4, GUN5, GUN6, UPGRADE_GUN_MIN, ADD_GUN_MIN
	global BUILDINGS
	t0 = time.time()
	while not QUITGAME:
		# Background Refresh
		screen.blit(background_img, [0,0])
		background = pygame.Surface(screen.get_size())
		background.fill((34, 0, 137))
		cursor_img_rect.center = pygame.mouse.get_pos()
		
		# Clock & Timer
		t1 = time.time()
		seconds = int(t1-t0)
		minutes = int(seconds/60)
		timer = "{:02d}:{:02d}".format(minutes, seconds)
		timerText = timerFont.render("Time: " + str(timer), True, (255,255,255))
		screen.blit(timerText, (10,10))
		
		# Score Display
		score = "{:06d}".format(SCORE)
		scoreText = scoreFont.render("Score: " + str(score), True, (255,255,255))
		screen.blit(scoreText, (10, 40))

		# Fusion Display
		fusionQ = "{:01d}".format(FUSION)
		fusionText = scoreFont.render(str(fusionQ), True, (255,255,255))
		screen.blit(fusionText, (1160,30))

		# Pause Display
		pauseText = pauseFont.render("PAUSE (ESC)", True, GOLD)
		screen.blit(pauseText, (1120, 80))

		# Meteor timing
		ticks = int(pygame.time.get_ticks()/1000)
		meteor1_group.update()
		meteor1_group.draw(screen)
		if ticks >= 100:
			meteor2_group.update()
			meteor2_group.draw(screen)
		if ticks >= 200:
			meteor3_group.update()
			meteor3_group.draw(screen)
		if ticks >= 300:
			meteor4_group.update()
			meteor4_group.draw(screen)
		
		# Building Placement
		all_buildings.draw(screen)
		
		# User Bullets
		user_bullets.draw(screen)
		user_bullets.update()
		upgraded_user_bullets.draw(screen)
		upgraded_user_bullets.update()

		# Computer Bullets
		DELAY = DELAY + 1
		if DELAY >= 30:
			fire_bullets()
			DELAY = 0

		computer_bullets.draw(screen)
		computer_bullets.update()
		upgraded_computer_bullets.draw(screen)
		upgraded_computer_bullets.update()

		# Guns and Barrels		
		barrel_group.clear(screen, background)
		barrel_group.update()
		barrel_group.draw(screen)
		gun_group.draw(screen)

		# Fusion Core Image
		screen.blit(fusion ,[1120, 20])

		# Cursor Image
		screen.blit(cursor_img, cursor_img_rect)

		# Gun-Meteor Collesion Detection
		gun_meteor_collision = pygame.sprite.groupcollide(all_meteors_group, gun_group, True, False)

		if gun_meteor_collision:
			gun_hit = list(gun_meteor_collision.values())[0].pop()
			destroy_defense(gun_hit)

		# Building-Meteor Collision Detection
		building_collision = pygame.sprite.groupcollide(all_meteors_group, all_buildings, False, False)
		if building_collision:
			building_hit = list(building_collision.values())[0].pop()
			building_hit.destroy()
			building = building_hit.get_number()
			if building != -1:
				buildings_with_guns.remove(building_hit)
			if building != -1 and GUNS_ACTIVE[building] == True:
				all_guns = list(gun_group.sprites())
				if len(all_guns) > 0:
					gun_hit = all_guns[0]
					for g in range(0,len(all_guns)):
						if all_guns[g].get_number() == building:
							gun_hit = all_guns[g]
					destroy_defense(gun_hit)
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
		upgraded_user_meteor_collision = pygame.sprite.groupcollide(upgraded_user_bullets, all_meteors_group, True, False)
		computer_meteor_collision = pygame.sprite.groupcollide(computer_bullets, all_meteors_group, True, False)
		upgraded_computer_meteor_collision = pygame.sprite.groupcollide(upgraded_computer_bullets, all_meteors_group, True, False)

		# Meteor Collision with User Bullets
		if user_meteor_collision:
			meteor_hit = list(user_meteor_collision.values())[0].pop()
			health_after_hit = meteor_hit.hit()
			if health_after_hit == 0:
				if meteor1_group.has(meteor_hit):
					updated_score = SCORE + (2*USER_HIT_SCORE)
					updated_fusion = FUSION + (1*USER_HIT_FUSION)
					meteor_hit.kill()
					if len(meteor1_group) < no_Meteor1:
						add_meteor(Meteor1, meteor1_group)
				elif meteor2_group.has(meteor_hit):
					updated_score = SCORE + (4*USER_HIT_SCORE)
					updated_fusion = FUSION + (2*USER_HIT_FUSION)
					meteor_hit.kill()
					add_meteor(Meteor2, meteor2_group)
				elif meteor3_group.has(meteor_hit):
					updated_score = SCORE + (5*USER_HIT_SCORE)
					updated_fusion = FUSION + (3*USER_HIT_FUSION)
					meteor_hit.kill()
					add_meteor(Meteor3, meteor3_group)
				elif meteor4_group.has(meteor_hit):
					updated_score = SCORE + (8*USER_HIT_SCORE)
					updated_fusion = FUSION + (4*USER_HIT_FUSION)
					meteor_hit.kill()
					add_meteor(Meteor4, meteor4_group)
				SCORE = updated_score
				FUSION = updated_fusion

		# Meteor Collision with Upgraded User Bullets
		if upgraded_user_meteor_collision:
			meteor_hit = list(upgraded_user_meteor_collision.values())[0].pop()
			health_after_hit = meteor_hit.upgraded_hit()
			if health_after_hit <= 0:
				if meteor1_group.has(meteor_hit):
					updated_score = SCORE + (4*USER_HIT_SCORE)
					updated_fusion = FUSION + (2*USER_HIT_FUSION)
					meteor_hit.kill()
					if len(meteor1_group) < no_Meteor1:
						add_meteor(Meteor1, meteor1_group)
				elif meteor2_group.has(meteor_hit):
					updated_score = SCORE + (8*USER_HIT_SCORE)
					updated_fusion = FUSION + (4*USER_HIT_FUSION)
					meteor_hit.kill()
					add_meteor(Meteor2, meteor2_group)
				elif meteor3_group.has(meteor_hit):
					updated_score = SCORE + (10*USER_HIT_SCORE)
					updated_fusion = FUSION + (6*USER_HIT_FUSION)
					meteor_hit.kill()
					add_meteor(Meteor3, meteor3_group)
				elif meteor4_group.has(meteor_hit):
					updated_score = SCORE + (16*USER_HIT_SCORE)
					updated_fusion = FUSION + (8*USER_HIT_FUSION)
					meteor_hit.kill()
					add_meteor(Meteor4, meteor4_group)
				SCORE = updated_score
				FUSION = updated_fusion

		# Meteor Collision with Computer Bullets
		if computer_meteor_collision:
			meteor_hit = list(computer_meteor_collision.values())[0].pop()
			health_after_hit = meteor_hit.hit()
			if health_after_hit == 0:
				if meteor1_group.has(meteor_hit):
					updated_score = SCORE + (2*COMPUTER_HIT_SCORE)
					updated_fusion = FUSION + (1*COMPUTER_HIT_FUSION)
					meteor_hit.kill()
					if len(meteor1_group) < no_Meteor1:
						add_meteor(Meteor1, meteor1_group)
				elif meteor2_group.has(meteor_hit):
					updated_score = SCORE + (4*COMPUTER_HIT_SCORE)
					updated_fusion = FUSION + (2*COMPUTER_HIT_FUSION)
					meteor_hit.kill()
					add_meteor(Meteor2, meteor2_group)
				elif meteor3_group.has(meteor_hit):
					updated_score = SCORE + (5*COMPUTER_HIT_SCORE)
					updated_fusion = FUSION + (3*COMPUTER_HIT_FUSION)
					meteor_hit.kill()
					add_meteor(Meteor3, meteor3_group)
				elif meteor4_group.has(meteor_hit):
					updated_score = SCORE + (8*COMPUTER_HIT_SCORE)
					updated_fusion = FUSION + (4*COMPUTER_HIT_FUSION)
					meteor_hit.kill()
					add_meteor(Meteor4, meteor4_group)
				SCORE = updated_score
				FUSION = updated_fusion

		# Meteor Collision with Upgraded Computer Bullets
		if upgraded_computer_meteor_collision:
			meteor_hit = list(upgraded_computer_meteor_collision.values())[0].pop()
			health_after_hit = meteor_hit.upgraded_hit()
			if health_after_hit <= 0:
				if meteor1_group.has(meteor_hit):
					updated_score = SCORE + (4*COMPUTER_HIT_SCORE)
					updated_fusion = FUSION + (2*COMPUTER_HIT_FUSION)
					meteor_hit.kill()
					if len(meteor1_group) < no_Meteor1:
						add_meteor(Meteor1, meteor1_group)
				elif meteor2_group.has(meteor_hit):
					updated_score = SCORE + (8*COMPUTER_HIT_SCORE)
					updated_fusion = FUSION + (4*COMPUTER_HIT_FUSION)
					meteor_hit.kill()
					add_meteor(Meteor2, meteor2_group)
				elif meteor3_group.has(meteor_hit):
					updated_score = SCORE + (10*COMPUTER_HIT_SCORE)
					updated_fusion = FUSION + (6*COMPUTER_HIT_FUSION)
					meteor_hit.kill()
					add_meteor(Meteor3, meteor3_group)
				elif meteor4_group.has(meteor_hit):
					updated_score = SCORE + (16*COMPUTER_HIT_SCORE)
					updated_fusion = FUSION + (8*COMPUTER_HIT_FUSION)
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
		
		# User Interaction Controls
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				# User Fire Bullets
				if event.key == pygame.K_SPACE:
					if GUNS_UPGRADED[0]:
						if len(upgraded_user_bullets) <= UPGRADED_USER_GUN_LIMIT:
							add_bullet(User_Bullet, USERANGLE, upgraded_user_bullets, True)	
					else:
						if len(user_bullets) <= USER_GUN_LIMIT:
							add_bullet(User_Bullet, USERANGLE, user_bullets, False)
				# Upgrade Guns
				if FUSION >= UPGRADE_GUN_MIN:
					if event.key == pygame.K_u:
						if NEXT_UPGRADE < len(list(gun_group.sprites())):
							upgrade_gun()
							FUSION = FUSION - UPGRADE_GUN_MIN
				# Add Guns
				if FUSION >= ADD_GUN_MIN:
					if event.key == pygame.K_p:
						if len(list(buildings_with_guns.sprites())) > 0 :
							add_gun()
							FUSION = FUSION - ADD_GUN_MIN
							print(FUSION)
				if event.key == pygame.K_ESCAPE:
					PAUSED = True
					t0 = t1
					pause()
			# Quit Game
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
def pause():
	global QUITGAME, PAUSED
	while PAUSED:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				PAUSED = False
				QUITGAME = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					PAUSED = False
		pauseText = scoreFont.render("GAME PAUSED", True, GOLD)
		pauseExtendedText = timerFont.render("Press the space bar to resume", True, GOLD)
		screen.blit(pauseText, (size[0]/2 - 130, size[1]/2))
		screen.blit(pauseExtendedText, (size[0]/2 - 200, size[1]/2 + 50))
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
	if GUNS_ACTIVE[1]:
		if GUNS_UPGRADED[1]:
			add_bullet(Bullet1, ANGLE1, upgraded_bullet1_group, True)
		else:
			add_bullet(Bullet1, ANGLE1, bullet1_group, False)
	if GUNS_ACTIVE[2]:
		if GUNS_UPGRADED[2]:
			add_bullet(Bullet2, ANGLE2, upgraded_bullet2_group, True)
		else:
			add_bullet(Bullet2, ANGLE2, bullet2_group, False)
	if GUNS_ACTIVE[3]:
		if GUNS_UPGRADED[3]:
			add_bullet(Bullet4, ANGLE4, upgraded_bullet4_group, True)
		else:
			add_bullet(Bullet4, ANGLE4, bullet4_group, False)
	if GUNS_ACTIVE[4]:
		if GUNS_UPGRADED[4]:
			add_bullet(Bullet5, ANGLE5, upgraded_bullet5_group, True)
		else:
			add_bullet(Bullet5, ANGLE5, bullet5_group, False)
	if GUNS_ACTIVE[5]:
		if GUNS_UPGRADED[5]:
			add_bullet(Bullet6, ANGLE6, upgraded_bullet6_group, True)
		else:
			add_bullet(Bullet6, ANGLE6, bullet6_group, False)
def add_bullet(Type, angle, type_group, upgraded):
	bullet_sprite = Type()
	bullet_sprite.direction(angle)
	type_group.add(bullet_sprite)
	all_bullets.add(bullet_sprite)
	if type_group != user_bullets and type_group != upgraded_user_bullets:
		if upgraded == True:
			upgraded_computer_bullets.add(bullet_sprite)
		else:
			computer_bullets.add(bullet_sprite)	
def add_gun():
	global POSITIONS, GUNS_ACTIVE
	buildings = list(buildings_with_guns.sprites())
	building = buildings[random.randrange(len(buildings))]
	gun = building.get_number()
	buildings_with_guns.remove(building)
	POSITIONS.append(gun)
	gun_sprite = Gun(GUN_POSITIONS[gun][0], GUN_POSITIONS[gun][1], gun)
	gun_group.add(gun_sprite)
	GUNS_ACTIVE[gun] = True
	add_barrel(gun)
def upgrade_gun():
	global NEXT_UPGRADE, GUNS_UPGRADED
	all_guns = list(gun_group.sprites())
	all_guns[NEXT_UPGRADE].upgrade()
	GUNS_UPGRADED[POSITIONS[NEXT_UPGRADE]] = True
	NEXT_UPGRADE += 1
def add_barrel(i):
	global BARRELS
	barrel_sprite = Barrel(BARRELS[i][0], BARRELS[i][1], BARRELS[i][2], BARRELS[i][3])
	barrel_group.add(barrel_sprite)
def destroy_defense(gun_hit):
	global QUITGAME	
	all_guns = list(gun_group.sprites())
	all_barrels = list(barrel_group.sprites())
	gun = all_guns.index(gun_hit)
	if gun == 0:
		QUITGAME = True
	else:
		GUNS_ACTIVE[POSITIONS[gun]] = False
		all_guns[gun].kill()
		all_barrels[gun].kill()



intro_loop()
game_loop()
game_over()