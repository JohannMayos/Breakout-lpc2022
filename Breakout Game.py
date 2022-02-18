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

rows = 8
columns = 14

class blocks():
    
    # define width and height for blocks
    def __init__(self):
        self.width = 49
        self.height = 20

    # fuction to set block form, coordinate and your colors 
    def create_wall(self):
        self.blocks = []
        block_individual = []

        for row in range(rows):
            block_row = []

            for column in range(columns):
                block_x = column * self.width + 15
                block_y = row * self.height + 152
                rect = pygame.Rect(block_x, block_y, self.width, self.height)

                if row == 0 or row == 1:
                    color = 4
                elif row == 2 or row == 3:
                    color = 3
                elif row == 4 or row == 5:
                    color = 2
                elif row == 6 or row == 7:
                    color = 1

                block_individual = [rect, color]
                block_row.append(block_individual)
            self.blocks.append(block_row)


    # fuction to draw the blocks
    def draw_wall_blocks(self):
        for row in self.blocks:
            for block in row:
                if block[1] == 4:
                    block_col = block_red
                elif block[1] == 3:
                    block_col = block_orange
                elif block[1] == 2:
                    block_col = block_green
                elif block[1] == 1:
                    block_col = block_yellow
                pygame.draw.rect(screen, block_col, block[0])
                pygame.draw.rect(screen, background_color, (block[0]), 2)

wall = blocks()
wall.create_wall()

# drawing paddle
paddle = pygame.image.load("image/paddle.png")
paddle_x = 300
paddle_move_left = False
paddle_move_right = False

# ball
ball = pygame.image.load("image/Ball.png")
ball_x = 300
ball_y = 300
ball_dx = 3
ball_dy = 3

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

while game_loop:
    
    # clear screen and set background again
    screen.fill(background_color)
    screen.blit(background,(0,0))
    wall.draw_wall_blocks()

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
    if ball_y >= 605:
        if paddle_x < ball_x + 80:
            if paddle_x + 80 > ball_x:
                ball_dy *= -1
                ball_dx *= 1

    # ball´s deathpoint
    if ball_y > 650:
        ball_x = 300
        ball_y = 300
        ball_dx *= -1
        ball_dy *= 1

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
    screen.blit(ball, (ball_x, ball_y))
    screen.blit(paddle, (paddle_x, 625))
    screen.blit(score_text, score_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
