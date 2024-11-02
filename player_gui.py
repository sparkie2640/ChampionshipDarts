import pygame as pg
import sys, time

# Constants
WIDTH, HEIGHT = 1024, 600
WHITE = (255, 255, 255)
CHALKBOARD_BLACK = (49, 52, 58) # Chalkboard Black #31343a
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 13)

score_box_x = 55
score_box_y = 70
score_box_width = 200
score_box_height = 160
score_box_y_multi = 170
score_box_x_multi = 718
inner_box_multi = 3
inner_box_multi_wh = inner_box_multi * 2

ulx = 65
uly = 107
llx = 65
lly = 221
urx = 246
ury = 107
lrx = 246
lry = 221

p_x = 65
p_y = 115
pwidth = 182
pheight = 115

text_offset_x = 53
text_offset_y = 5
#current_round_text = FONT.render(f"Round {CricketDarts.GAME_ROUND} - Player {self.current_player + 1} is up.", True, BLACK)
#screen.blit(current_round_text, (WIDTH//2 - current_round_text.get_width()//2, HEIGHT - 50))

class PlayerGUI:

    def player_1_score(self, screen, FONT, SCORE_FONT, _text_width, _score):
        pg.draw.rect(screen, WHITE, pg.Rect(score_box_x, score_box_y, score_box_width, score_box_height), 2, 3)
        pg.draw.rect(screen, CHALKBOARD_BLACK, pg.Rect(score_box_x + inner_box_multi, score_box_y + inner_box_multi, score_box_width - inner_box_multi_wh, score_box_height - inner_box_multi_wh), 2, 3)
        screen.blit(FONT.render(f"Player 1", True, WHITE), (score_box_x + text_offset_x, score_box_y + text_offset_y))
        
        for i in range(1,4):
            PlayerGUI.background_text(self, screen, SCORE_FONT, _score, _text_width, p_x, p_y)
        
        screen.blit(SCORE_FONT.render(str(_score), True, WHITE), ((pwidth//2 - _text_width//2) + p_x, p_y))
    
    def player_2_score(self, screen, FONT, SCORE_FONT, _text_width, _score = 0):
        pg.draw.rect(screen, WHITE, pg.Rect((score_box_x + score_box_x_multi), score_box_y, score_box_width, score_box_height), 2, 3)
        pg.draw.rect(screen, CHALKBOARD_BLACK, pg.Rect((score_box_x + score_box_x_multi) + inner_box_multi, score_box_y + inner_box_multi, score_box_width - inner_box_multi_wh, score_box_height - inner_box_multi_wh), 2, 3)
        screen.blit(FONT.render(f"Player 2", True, WHITE), (score_box_x + score_box_x_multi + inner_box_multi + text_offset_x, score_box_y + inner_box_multi + text_offset_y))
        
        for i in range(1,4):
            PlayerGUI.background_text(self, screen, SCORE_FONT, _score, _text_width, p_x + score_box_x_multi, p_y)
        
        screen.blit(SCORE_FONT.render(str(_score), True, WHITE), ((pwidth//2 - _text_width//2) + p_x + score_box_x_multi, p_y))
    
    def player_3_score(self, screen, FONT, SCORE_FONT, _text_width, _score = 0):
        pg.draw.rect(screen, WHITE, pg.Rect(score_box_x, (score_box_y + score_box_y_multi), score_box_width, score_box_height), 2, 3)
        pg.draw.rect(screen, CHALKBOARD_BLACK, pg.Rect(score_box_x + inner_box_multi, (score_box_y + score_box_y_multi + inner_box_multi), score_box_width - inner_box_multi_wh, score_box_height - inner_box_multi_wh), 2, 3)
        screen.blit(FONT.render(f"Player 3", True, WHITE), (score_box_x + text_offset_x, score_box_y + text_offset_y + score_box_y_multi))
 
        for i in range(1,4):
            PlayerGUI.background_text(self, screen, SCORE_FONT, _score, _text_width, p_x, p_y + score_box_y_multi)
        
        screen.blit(SCORE_FONT.render(str(_score), True, WHITE), ((pwidth//2 - _text_width//2) + p_x, p_y + score_box_y_multi))

    def player_4_score(self, screen, FONT, SCORE_FONT, _text_width, _score = 0):
        pg.draw.rect(screen, WHITE, pg.Rect((score_box_x + score_box_x_multi), (score_box_y + score_box_y_multi), score_box_width, score_box_height), 2, 3)
        pg.draw.rect(screen, CHALKBOARD_BLACK, pg.Rect((score_box_x + score_box_x_multi) + inner_box_multi, (score_box_y + score_box_y_multi) + inner_box_multi, score_box_width - inner_box_multi_wh, score_box_height - inner_box_multi_wh), 2, 3)
        screen.blit(FONT.render(f"Player 4", True, WHITE), (score_box_x + score_box_x_multi + inner_box_multi + text_offset_x, score_box_y + inner_box_multi + text_offset_y + score_box_y_multi))
 
        for i in range(1,4):
            PlayerGUI.background_text(self, screen, SCORE_FONT, _score, _text_width, p_x + score_box_x_multi, p_y + score_box_y_multi)

        screen.blit(SCORE_FONT.render(str(_score), True, WHITE), ((pwidth//2 - _text_width//2) + p_x + score_box_x_multi, p_y + score_box_y_multi))

    def darts_used(self, screen, FONT, SCORE_FONT):
        pg.draw.rect(screen, WHITE, pg.Rect(score_box_x, (score_box_y + (score_box_y_multi * 2)), score_box_width, score_box_height), 2, 3)
        pg.draw.rect(screen, CHALKBOARD_BLACK, pg.Rect(score_box_x + inner_box_multi, (score_box_y + (score_box_y_multi * 2)) + inner_box_multi, score_box_width - inner_box_multi_wh, score_box_height - inner_box_multi_wh), 2, 3)
        screen.blit(FONT.render(f"Darts Used", True, WHITE), (88, 415))

    def current_round_score(self, screen, FONT, SCORE_FONT, _score = 0):
        pg.draw.rect(screen, WHITE, pg.Rect((score_box_x + score_box_x_multi), (score_box_y + (score_box_y_multi * 2)), score_box_width, score_box_height), 2, 3)
        pg.draw.rect(screen, CHALKBOARD_BLACK, pg.Rect((score_box_x + score_box_x_multi) + inner_box_multi, (score_box_y + (score_box_y_multi * 2)) + inner_box_multi, score_box_width - inner_box_multi_wh, score_box_height - inner_box_multi_wh), 2, 3)

    def background_text(self, screen, SCORE_FONT, _score, _text_width, p_x, p_y):
        for i in range(1,4):
            screen.blit(SCORE_FONT.render(str(_score), True, BLACK), ((pwidth//2 - _text_width//2) + p_x - i, p_y -i))
            screen.blit(SCORE_FONT.render(str(_score), True, BLACK), ((pwidth//2 - _text_width//2) + p_x, p_y - i))
            screen.blit(SCORE_FONT.render(str(_score), True, BLACK), ((pwidth//2 - _text_width//2) + p_x + i, p_y - i))
            screen.blit(SCORE_FONT.render(str(_score), True, BLACK), ((pwidth//2 - _text_width//2) + p_x - i, p_y))
            screen.blit(SCORE_FONT.render(str(_score), True, BLACK), ((pwidth//2 - _text_width//2) + p_x + i, p_y))
            screen.blit(SCORE_FONT.render(str(_score), True, BLACK), ((pwidth//2 - _text_width//2) + p_x -i, p_y + i))
            screen.blit(SCORE_FONT.render(str(_score), True, BLACK), ((pwidth//2 - _text_width//2) + p_x, p_y + i))
            screen.blit(SCORE_FONT.render(str(_score), True, BLACK), ((pwidth//2 - _text_width//2) + p_x +i, p_y + i))