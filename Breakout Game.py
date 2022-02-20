import pygame


pygame.init()

# drawing the screen
size = (720, 710)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")

background = pygame.image.load("image/background.png")

block_red = (236, 28, 36)
block_orange = (255, 127, 39)
block_green = (14, 209, 69)
block_yellow = (255, 242, 0)
background_color = (0, 0, 0)

# drawing paddle
paddle = pygame.image.load("image/paddle.png")
paddle_x = 300
paddle_move_left = False
paddle_move_right = False

# ball
ball = pygame.Rect(400, 400, 15, 15)
ball_x = 400
ball_y = 400
ball_dx = 3
ball_dy = -3
ball = pygame.Rect(ball_x, ball_y, 15, 15)

block_width = 49
block_height = 20
rows = 8
cols = 14
block_list = []

def create_wall():
    block_individual = []

    for row in range(rows):
        for col in range(cols):
            block_x = col * block_width + 15
            block_y = row * block_height + 152

            if row == 0 or row == 1:
                    color = block_red
                    score = 7
            elif row == 2 or row == 3:
                    color = block_orange
                    score = 5
            elif row == 4 or row == 5:
                    color = block_green
                    score = 3
            elif row == 6 or row == 7:
                    color = block_yellow
                    score = 1

            block = pygame.Rect(block_x, block_y, block_width, block_height)
            block_individual = [block, color, score]
            block_list.append(block_individual)


def play_sounds(none):
    sounds = pygame.mixer.Sound(none)
    sounds.play()

# score text
score_font = pygame.font.Font('breakout.ttf', 44)
score_text = score_font.render('000', True, (255, 255, 255), (0, 0, 0))
score_text_rect = score_text.get_rect()
score_text_rect.center = (570, 90)

# score
score_1 = 0
score_2 = 0

# game loop
game_loop = True
game_clock = pygame.time.Clock()

create_wall()
pygame.mixer.music.load("breakout.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

while game_loop:
    
    # clear screen and set background again
    screen.fill(background_color)
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        
        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_move_left = True
            if event.key == pygame.K_RIGHT:
                paddle_move_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                paddle_move_left = False
            if event.key == pygame.K_RIGHT:
                paddle_move_right = False

    # ball movement
    ball.x += ball_dx
    ball.y += ball_dy

    for block in block_list:
        if ball.colliderect(block[0]):
            ball_dy *= -1
            score_1 += block[2]
            play_sounds("bleep.mp3")
            block_list.remove(block)

    # ball collision with the paddle
    if ball.y >= 605:
        if paddle_x < ball.x + 75:
            if paddle_x + 75 > ball.x:
                ball_dy *= -1
                ball_dx *= 1
                play_sounds("solid.wav")

    # ball´s death point
    if ball.y > 650:
        ball.x = 300
        ball.y = 300
        ball_dx *= -1
        ball_dy *= 1
        game_clock.tick(5)

    # ball collision with right wall
    if ball.x > 680:
        ball_dx *= -1
        ball_dy *= 1
        play_sounds("solid.wav")

    # ball collision with upper wall
    if ball.y <= 0:
        ball_dx *= 1
        ball_dy *= -1
        play_sounds("solid.wav")

    # ball collision with left wall
    if ball.x <= 0:
        ball_dx *= -1
        ball_dy *= 1
        play_sounds("solid.wav")

    # paddle collision with left wall
    if paddle_x <= 0:
        paddle_x = 0

    # paddle collision with right wall
    if paddle_x >= 625:
        paddle_x = 625

    # player up movement
    if paddle_move_left:
        paddle_x -= 5
    else:
        paddle_x += 0

    # player down movement
    if paddle_move_right:
        paddle_x += 5
    else:
        paddle_x += 0

    # draw objects
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    screen.blit(paddle, (paddle_x, 625))
    screen.blit(score_text, score_text_rect)

    for block in block_list:
        pygame.draw.rect(screen, block[1], block[0])
        pygame.draw.rect(screen, background_color, (block[0]), 2)
            
    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
