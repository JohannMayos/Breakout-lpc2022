import pygame

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

# drawing the screen
size = (720, 710)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")

# drawing the box area of the game
game_box_line_left = pygame.draw.line(screen, COLOR_WHITE, (0, 720), (0, -720), 20)
game_box_line_up = pygame.draw.line(screen, COLOR_WHITE, (720, 0), (-720, 0), 40)
game_box_line_right = pygame.draw.line(screen, COLOR_WHITE, (720, 720), (720, -720), 20)

# drawing the hud lines of the score (1p - 2p scores)
game_box_line_hud_1 = pygame.draw.line(screen, COLOR_WHITE, (50, 75), (50, -720), 10)
game_box_line_hud_2 = pygame.draw.line(screen, COLOR_WHITE, (450, 75), (450, -720), 10)

# score text
score_font = pygame.font.Font('PressStart2P-vaV7.ttf', 44)
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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

    screen.blit(score_text, score_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()