import pygame
import random

# initialize Pygame
pygame.init()

# set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong AI")

# set up the game objects
BALL_RADIUS = 10
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2
ball_speed_x = random.choice([-5, 5])
ball_speed_y = random.choice([-5, 5])
player_paddle_x = 20
player_paddle_y = WINDOW_HEIGHT // 2 - 50
player_paddle_speed = 0
ai_paddle_x = WINDOW_WIDTH - 40
ai_paddle_y = WINDOW_HEIGHT // 2 - 50
ai_paddle_speed = 0
font = pygame.font.Font(None, 30)

# set up the scores
player_score = 0
ai_score = 0
# set up the game clock
clock = pygame.time.Clock()

# main game loop
while True:
	# handle events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player_paddle_speed = -5
			elif event.key == pygame.K_DOWN:
				player_paddle_speed = 5
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				player_paddle_speed = 0

	# move the player paddle
	player_paddle_y += player_paddle_speed
	if player_paddle_y < 0:
		player_paddle_y = 0
	elif player_paddle_y > WINDOW_HEIGHT - 100:
		player_paddle_y = WINDOW_HEIGHT - 100

	# move the AI paddle
	ai_paddle_y += ai_paddle_speed
	if ai_paddle_y < 0:
		ai_paddle_y = 0
	elif ai_paddle_y > WINDOW_HEIGHT - 100:
		ai_paddle_y = WINDOW_HEIGHT - 100

	# move the ball
	ball_x += ball_speed_x
	ball_y += ball_speed_y

	# check for collision with the top or bottom of the window
	if ball_y <= BALL_RADIUS or ball_y >= WINDOW_HEIGHT - BALL_RADIUS:
		ball_speed_y += 1
		ball_speed_y = -ball_speed_y

	# check for collision with the left or right of the window
	if ball_x <= BALL_RADIUS or ball_x >= WINDOW_WIDTH - BALL_RADIUS:
		if ball_x < WINDOW_WIDTH // 2:
			ai_score += 1
		else:
			player_score += 1
		# generate a new ball with random velocity
		ball_x = WINDOW_WIDTH // 2
		ball_y = WINDOW_HEIGHT // 2
		ball_speed_x = random.choice([-5, 5])
		ball_speed_y = random.choice([-5, 5])
	if ball_x <= BALL_RADIUS or ball_x >= WINDOW_WIDTH - BALL_RADIUS:
		player_score+=1
		# generate a new ball with random velocity
		ball_x = WINDOW_WIDTH // 2
		ball_y = WINDOW_HEIGHT // 2
		ball_speed_x = random.choice([-5, 5])
		ball_speed_y = random.choice([-5, 5])

	# check for collision with the player paddle
	if ball_x <= player_paddle_x + 20 and ball_y >= player_paddle_y and ball_y <= player_paddle_y + 100:
		ball_speed_x = -ball_speed_x
		ball_speed_x += 1
		ball_speed_y += 1

	# check for collision with the AI paddle
	if ball_x >= ai_paddle_x - 20 and ball_y >= ai_paddle_y and ball_y <= ai_paddle_y + 100:
		ball_speed_x = -ball_speed_x
		ball_speed_x += 1
		ball_speed_y += 1

	# update the AI paddle position
	if ball_y < ai_paddle_y + 50:
		ai_paddle_speed = -5
	elif ball_y > ai_paddle_y + 50:
		ai_paddle_speed = 5
	else:
		ai_paddle_speed = 0

	# draw the game objects
	game_window.fill((255, 255, 255))
	pygame.draw.rect(game_window, (0, 0, 0), (player_paddle_x, player_paddle_y, 20, 100))
	pygame.draw.rect(game_window, (0, 0, 0), (ai_paddle_x, ai_paddle_y, 20, 100))
	pygame.draw.circle(game_window, (0, 0, 0), (ball_x, ball_y), BALL_RADIUS)
	# Draw the scores
	player_text = font.render("Player: "+str(player_score), True, (128, 128, 128))
	ai_text = font.render("AI: "+str(ai_score), True, (128, 128, 128))
	game_window.blit(ai_text, (WINDOW_WIDTH - 150, 10))
	game_window.blit(player_text, (50, 10))

	# update the screen
	pygame.display.update()

	# set the game clock tick rate
	clock.tick(60)  # 60 frames per second
pygame.quit()