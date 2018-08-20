import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('music/musicbg.mp3')
pygame.mixer.music.play(-1, 0.0)