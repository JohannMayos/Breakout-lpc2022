import pygame
import pygame.locals

pygame.init()


# define run game function to reload game
def run_game():

    # drawing the screen
    size = (720, 710)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Breakout Game")

    background = pygame.image.load("image/background.png")

    # colors rgb coord
    block_red = (236, 28, 36)
    block_orange = (255, 127, 39)
    block_green = (14, 209, 69)
    block_yellow = (255, 242, 0)
    background_color = (0, 0, 0)
    white_color = (255, 255, 255)
    blue_color = (58, 219, 240)

    # drawing paddle
    paddler_width = 50
    paddle = pygame.Rect(300, 625, paddler_width, 20)
    paddle_move_left = False
    paddle_move_right = False

    # ball
    ball = pygame.Rect(400, 400, 15, 15)
    ball_dx = 3
    ball_dy = -3

    block_width = 49
    block_height = 20
    rows = 8
    cols = 14
    block_list = []
    wall_break = 0
    collision_tresh = 5

    # define draw lines color function
    def draw_line_blocks():

        # draw lines left
        pygame.draw.line(screen, block_red, (0, 192), (0, 152), 25)
        pygame.draw.line(screen, block_orange, (0, 232), (0, 192), 25)
        pygame.draw.line(screen, block_green, (0, 272), (0, 232), 25)
        pygame.draw.line(screen, block_yellow, (0, 312), (0, 272), 25)

        # draw lines right
        pygame.draw.line(screen, block_red, (705, 192), (705, 152), 20)
        pygame.draw.line(screen, block_orange, (705, 232), (705, 192), 20)
        pygame.draw.line(screen, block_green, (705, 272), (705, 232), 20)
        pygame.draw.line(screen, block_yellow, (705, 312), (705, 272), 20)

    # define the wall blocks function
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

                block = pygame.Rect(block_x, block_y, block_width,
                                    block_height)
                block_individual = [block, color, score]
                block_list.append(block_individual)

    # define the sounds function
    def play_sounds(none):
        sounds = pygame.mixer.Sound(none)
        sounds.play()

    # score
    score_1 = 0
    life_points_1 = 1
    life_points_2 = 1
    first_time_red_line = True
    first_time_orange_line = True

    # score text
    score_font = pygame.font.Font('breakout.ttf', 44)

    # define the score function
    def show_score():
        if score_1 < 10:
            score_text_1 = score_font.render("00" + str(score_1), True,
                                             white_color, background_color)
        elif score_1 >= 10 and score_1 < 100:
            score_text_1 = score_font.render("0" + str(score_1), True,
                                             white_color, background_color)
        else:
            score_text_1 = score_font.render(str(score_1), True,
                                             white_color, background_color)

        score_text_2 = score_font.render("000", True,
                                         white_color, background_color)

        screen.blit(score_text_1, (170, 90))
        screen.blit(score_text_2, (570, 90))

    # define life points fuction and your draw
    def show_life_point():
        life_points_text_1 = score_font.render(str(life_points_1), True,
                                               white_color, background_color)
        life_points_text_2 = score_font.render(str(life_points_2), True,
                                               white_color, background_color)

        screen.blit(life_points_text_1, (450, 5))
        screen.blit(life_points_text_2, (150, 5))

    # define the pause and lose screen function
    def pause():

        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False

                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_r:
                        run_game()

            screen.fill(background_color)
            font = pygame.font.Font('breakout.ttf', 44)

            if life_points_1 != 4:
                pause = font.render("Paused", True, white_color)
                pause_text = font.render("Press C to continue", True,
                                         white_color)
                quit_text = font.render("Press Q to quit", True,
                                        white_color)

                screen.blit(pause, (150, 150))
                screen.blit(pause_text, (150, 250))
                screen.blit(quit_text, (150, 350))

            pygame.display.update()
            game_clock.tick(15)

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
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False
            
            #  keystroke events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddle_move_left = True
                elif event.key == pygame.K_RIGHT:
                    paddle_move_right = True
                elif event.key == pygame.K_p:
                    pause()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_r:
                    run_game()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    paddle_move_left = False
                elif event.key == pygame.K_RIGHT:
                    paddle_move_right = False

        # ball movement
        ball.x += ball_dx
        ball.y += ball_dy

        # reduction of the paddler by half and increase speed ball after
        # passing the red line
        if ball.y < 152 and first_time_red_line:
            paddler_width = 25
            paddle = pygame.Rect(300, 625, paddler_width, 20)
            ball_dy *= 1.1
            ball_dx *= 1.1
            first_time_red_line = False

        # increase speed ball after passing the orange line
        if ball.y < 192 and first_time_orange_line:
            ball_dy *= 1.1
            ball_dx *= 1.1
            first_time_orange_line = False

        # block collision and scoring up
        for block in block_list:
            if ball.colliderect(block[0]):
                # checking the collision side
                if abs(block[0].top - ball.bottom) < collision_tresh \
                        and ball_dy > 0:
                    ball_dy *= -1
                elif abs(block[0].bottom - ball.top) < collision_tresh \
                        and ball_dy < 0:
                    ball_dy *= -1
                elif abs(block[0].right - ball.left) < collision_tresh \
                        and ball_dx < 0:
                    ball_dx *= -1
                elif abs(block[0].left - ball.right) < collision_tresh \
                        and ball_dx > 0:
                    ball_dx *= -1

                score_1 += block[2]
                play_sounds("bleep.mp3")

                if life_points_1 != 4:
                    block_list.remove(block)

                wall_break += 1

        # ball speed up after 4 blocks destroyed
        if wall_break == 4:
            ball_dy *= -1.02
            ball_dx *= 1.02

        # ball speed up after 12 blocks destroyed
        if wall_break == 12:
            ball_dy *= -1.03
            ball_dx *= 1.03

        # ball speed up after 60 blocks destroyed
        if wall_break == 60:
            ball_dy *= -1.04
            ball_dx *= 1.04

        # checks if the wall has been destroyed and start phase two
        if wall_break == 112:
            create_wall()
            wall_break = 0

        # ball collision with the paddle
        if ball.colliderect(paddle):
            if abs(ball.bottom - paddle.top) < collision_tresh:
                ball_dy *= -1
                ball_dx *= 1
                play_sounds("solid.wav")
            elif abs(ball.left - paddle.right) < collision_tresh or \
                    abs(ball.right - paddle.left) < collision_tresh:
                ball_dy *= -1
                ball_dx *= -1
                play_sounds("solid.wav")

        # ball´s death point
        if ball.y > 650:
            if life_points_1 < 4:
                life_points_1 += 1
                ball.x = 400
                ball.y = 400
                ball_dx *= -1
                ball_dy *= 1
                game_clock.tick(5)

            # End game screen
            else:
                paddler_width = 720
                paddle = pygame.Rect(0, 625, paddler_width, 20)
                font = pygame.font.Font('breakout.ttf', 44)
                restart_text = font.render("Press R to restart", True,
                                           white_color)
                quit_text = font.render("Press Q to quit", True,
                                        white_color)

                screen.blit(quit_text, (150, 450))
                screen.blit(restart_text, (150, 550))

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
        if paddle.x <= 0:
            paddle.x = 0

        # paddle collision with right wall
        if paddle.x >= 655:
            paddle.x = 655

        # player up movement
        if paddle_move_left:
            paddle.x -= 7
        else:
            paddle.x += 0

        # player down movement
        if paddle_move_right:
            paddle.x += 7
        else:
            paddle.x += 0

        # draw objects
        pygame.draw.ellipse(screen, white_color, ball)
        pygame.draw.rect(screen, blue_color, paddle)
        show_score()
        show_life_point()
        draw_line_blocks()

        for block in block_list:
            pygame.draw.rect(screen, block[1], block[0])
            pygame.draw.rect(screen, background_color, (block[0]), 2)
                
        # update screen
        pygame.display.flip()
        game_clock.tick(60)

    pygame.quit()


run_game()
