from blocks import L_block, J_block, I_block, O_block, S_block, Z_block, T_block
import time
from os import system
import pygame

Display = pygame.display.set_mode((1,1))


board = []
for i in range(20) :
	board.append(["O"]*10)

# print(board)
run = True
block = T_block(board)
block.spawn()
counter = 0
rotate = 5

time=0
clock = pygame.time.Clock()

while run :
	clock.tick(30)
	system("cls")
	for every_row in board :
		print(" ".join(every_row))
	
	time +=1
	if time == 30 :
		time =0
		# print("1")
		block.move_down()
		# counter +=1
		# if counter == rotate :
		# 	block.rotate()

	for event in pygame.event.get():
		if event.type == pygame.QUIT: # Event = Press the close button
			run = False # False means the game stop running

	keys =pygame.key.get_pressed()
	if keys[pygame.K_a] :
		block.move_left()

	if keys[pygame.K_d] :
		block.move_right()

	if keys[pygame.K_w] :
		block.rotate()
