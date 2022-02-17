import pygame

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BLUE = (58, 219, 240)

# drawing the screen
size = (720, 710)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")

background = pygame.image.load("background.png")

# drawing the box area of the game
game_box_line_left = pygame.draw.line(screen, COLOR_WHITE, (0, 710), (0, -710), 25)
game_box_line_up = pygame.draw.line(screen, COLOR_WHITE, (720, 0), (-720, 0), 40)
game_box_line_right = pygame.draw.line(screen, COLOR_WHITE, (720, 710), (720, -710), 25)

# drawing the hud lines of the score (1p - 2p scores)
game_box_line_hud_1 = pygame.draw.line(screen, COLOR_WHITE, (50, 75), (50, -720), 10)
game_box_line_hud_2 = pygame.draw.line(screen, COLOR_WHITE, (450, 75), (450, -720), 10)

# drawing the paddle marks on box
paddle_mark_left = pygame.draw.line(screen, COLOR_BLUE, (0, 670), (0, 640), 25)
paddle_mark_right = pygame.draw.line(screen, COLOR_BLUE, (720, 670), (720, 640), 25)

# drawing paddle
paddle = pygame.image.load("paddle.jpg")
paddle_x = 300
paddle_move_left = False
paddle_move_right = False

# ball
ball = pygame.image.load("ball.jpg")
ball_x = 300
ball_y = 300
ball_dx = 3
ball_dy = 3

# score text
score_font = pygame.font.Font('breakout.ttf', 44)
score_text = score_font.render('000', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (570, 90)

# score
score_1 = 0
score_2 = 0

# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:
    
    screen.fill(COLOR_BLACK)
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
    ball_x = ball_x + ball_dx
    ball_y = ball_y + ball_dy

    # ball collision with the paddle
    if ball_y >= 600:
        if paddle_x < ball_y + 75:
            if paddle_x + 75 > ball_y:
                ball_dy *= -1
                ball_dx *= 1

    # ball collision with right wall
    if ball_x > 680:
        ball_dx *= -1
        ball_dy *= 1

    # ball collision with upper wall
    if ball_y <= 0:
        ball_dx *= 1
        ball_dy *= -1

    # ball collision with left wall
    if ball_x == 0:
        ball_dx *= -1
        ball_dy *= 1

    # paddle collision with left wall
    if paddle_x <= 0:
        paddle_x = 0

    # paddle collision with right wall
    if paddle_x >= 610:
        paddle_x = 610

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

    screen.blit(ball, (ball_x, ball_y))
    screen.blit(paddle, (paddle_x, 640))
    screen.blit(score_text, score_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()