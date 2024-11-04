import board_comms as bc
import pygame as pg
import sys, time
from player_gui import PlayerGUI as pgui
import constants as const

pg.init()

# Constants
# WIDTH, HEIGHT = 1024, 600
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# CHALKBOARD_BLACK = (49, 52, 58) # Chalkboard Black #31343a
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# YELLOW = (255, 255, 0)
# ORANGE = (255, 128, 13)
# FONT = pg.font.Font(None, 36)
# SCORE_FONT = pg.font.Font(None, 70)
# PSCORE_FONT = pg.font.Font(None, 155)

# Set up display
screen = pg.display.set_mode((const.WIDTH, const.HEIGHT), pg.FULLSCREEN)
pg.mouse.set_visible(False)

pg.display.set_caption("Cricket Darts Game")

class CricketDarts:
    GAME_ROUND = 1
    
    def __init__(self):
        self.players = []
        self.current_player = 0
        self.rounds = []
        self.scores = []
        self.total_scores = []  # Track total scores per player

    def start_game(self):
        print("Game starting")
        
        time.sleep(2)
        self.num_players = self.get_num_players()
        for i in range(self.num_players):
            player_name = f"Player {i+1}"
            self.players.append(player_name)
            self.scores.append({num: 0 for num in range(15, 21)})
            self.scores[-1]['SB'] = 0  # bullseye
            self.total_scores.append(0)  # Initialize total score
            self.rounds.append([])

        print("Game started with players:", self.players)

    def draw_text(self, text, x, y, color=const.WHITE):
        """Render text on the screen."""
        text_surface = const.FONT.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

    def get_num_players(self):
        """Prompt for the number of players using Pygame input."""
        bc.write_serial_led("ENTER_ON")
        bc.write_serial_led("UP_ON")
        bc.write_serial_led("DOWN_ON")
        
        selected_players = 2
        max_players = 4
        min_players = 2
        
        input_active = True
        self.input_buffer = ""
        while input_active:
            screen.fill(const.CHALKBOARD_BLACK)
            self.draw_text("Select number of players", const.WIDTH // 2, const.HEIGHT // 4, const.WHITE)
            self.draw_text(f"Players: {selected_players}", const.WIDTH // 2, const.HEIGHT // 2, const.WHITE)       
            self.draw_text("Press UP or DOWN to change, Enter to select", const.WIDTH // 2, const.HEIGHT * 3 // 4, const.WHITE)     
            
            # Handle input from buttons
            # input = bc.read_board()
            # if input == "UP":
            #     if selected_players < max_players:
            #         selected_players += 1
            # if input == "DOWN":
            #     if selected_players > min_players:
            #         selected_players -= 1  
            # elif input == "ENTER":
            #     print(f"Selected Players: {selected_players}")
            #     input_active = False
            #     return int(selected_players)
            
            # Handle input from keyboard
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        if selected_players < max_players:
                            selected_players += 1
                    elif event.key == pg.K_DOWN:
                        if selected_players > min_players:
                            selected_players -= 1
                    elif event.key == pg.K_RETURN:
                        print(f"Selected Players: {selected_players}")
                        input_active = False
                        return int(selected_players)
                        # You can add code here to start the game with the selected number of players

            # for event in pg.event.get():
            #     if event.type == pg.QUIT:
            #         pg.quit()
            #         exit
            #     elif event.type == pg.KEYDOWN:
            #         if event.key == pg.K_RETURN:
            #             if self.input_buffer.isdigit() and 1 <= int(self.input_buffer) <= 8:
            #                 input_active = False
            #                 return int(self.input_buffer)
            #             else:
            #                 self.input_buffer = ""
            #         elif event.key == pg.K_BACKSPACE:
            #             self.input_buffer = self.input_buffer[:-1]
            #         elif event.unicode.isdigit():
            #             self.input_buffer += event.unicode

            pg.display.flip()

    def play_game(self):
        self.display_background()
        while True:
            player_name = self.players[self.current_player]
            #print(f"\n{player_name}'s turn!")
            self.display_game_state()
            self.turn()

            # Display the scores after each turn
            #self.display_scores()
            self.display_cricket_scoring(self.scores)

            bc.write_serial_led("ENTER_ON")
            bc.write_serial_led("RIGHT_ON")
            print(f"Press ENTER to end turn or RIGHT to delete last throw.")
            
            board_result = bc.read_board(_end = True)

            if board_result == 'ENTER':
                bc.write_serial_led("RIGHT_OFF")
                bc.write_serial_led("ENTER_OFF")
                if self.current_player + 1 == len(self.players):
                    CricketDarts.GAME_ROUND += 1
                self.current_player = (self.current_player + 1) % len(self.players)
            
            if board_result == 'RIGHT':
                bc.write_serial_led("RIGHT_OFF")
                bc.write_serial_led("ENTER_OFF")
                if self.undo_last_throw():
                    throw_count -= 1  # Revert throw count if undo successful

            if self.check_winner():
                break

    def display_background(self):
        global screen
        screen.fill(const.CHALKBOARD_BLACK)

        image = pg.image.load("assets/cricket.png")
        image.convert()
        screen.blit(image, (479, 21))

        self.display_cricket_scoring(self.scores)
        pg.draw.rect(screen, const.WHITE, pg.Rect(330, 16, 368, 516), 2, 3) # Outer box
        pg.draw.rect(screen, const.WHITE, pg.Rect(330, 70, 368, 3)) # Horizontal separator line
        pg.draw.rect(screen, const.WHITE, pg.Rect(403, 16, 3, 516)) # Left player separator vertical line
        pg.draw.rect(screen, const.WHITE, pg.Rect(476, 16, 3, 516)) # Left vertical line
        pg.draw.rect(screen, const.WHITE, pg.Rect(549, 16, 3, 516)) # Right vertical line
        pg.draw.rect(screen, const.WHITE, pg.Rect(622, 16, 3, 516)) # Right player separator vertical line
        
        px_x = 486 #865
        px_y = 83
        px_y_multi = 66

        screen.blit(const.SCORE_FONT.render("20", True, const.WHITE), (px_x, px_y))
        screen.blit(const.SCORE_FONT.render("19", True, const.WHITE), (px_x, px_y + (px_y_multi * 1)))
        screen.blit(const.SCORE_FONT.render("18", True, const.WHITE), (px_x, px_y + (px_y_multi * 2)))
        screen.blit(const.SCORE_FONT.render("17", True, const.WHITE), (px_x, px_y + (px_y_multi * 3)))
        screen.blit(const.SCORE_FONT.render("16", True, const.WHITE), (px_x, px_y + (px_y_multi * 4)))
        screen.blit(const.SCORE_FONT.render("15", True, const.WHITE), (px_x, px_y + (px_y_multi * 5))) # 66px diff
        
        # Bullseye
        pg.draw.circle(screen, const.RED,(512, 495), 19)
        pg.draw.circle(screen, const.WHITE,(512, 495), 15)
        pg.draw.circle(screen, const.RED,(512, 495), 11)
        pg.draw.circle(screen, const.WHITE,(512, 495), 7)
        pg.draw.circle(screen, const.RED,(512, 495), 3)
    
        # Current Round
        #pg.draw.rect(screen, WHITE, pg.Rect(330, 544, 368, 36), 2, 3) 
        #pg.draw.rect(screen, GREEN, pg.Rect(332, 546, 364, 32), 2, 3) 

        pg.display.flip()

    def display_cricket_scoring(self, _scores):

        for i, player in enumerate(self.players):
            self.render_scores(i, 1, _scores[i][20])
            self.render_scores(i, 2, _scores[i][19])
            self.render_scores(i, 3, _scores[i][18])
            self.render_scores(i, 4, _scores[i][17])
            self.render_scores(i, 5, _scores[i][16])
            self.render_scores(i, 6, _scores[i][15])
            self.render_scores(i, 7, _scores[i]['SB'])
    
    def render_scores(self, _player, _score_item, _score)    :
        """
        _player: player number; 0 based index
        _score_item: multiplier for positioning Y coordinate
        _score: 1, 2, or 3 indicating / X or closeout
        """
        score_px_x = 0
        score_px_y = 0
        base_px_y = 45
        y_px_diff = 66
        line_width = 6
        circle_width = 17

        if _player == 0:
            # Player 1
            score_px_x = 435
            screen.blit(const.SCORE_FONT.render("P1", True, const.WHITE), (score_px_x - 20, base_px_y - 22))
            score_px_y = base_px_y + (_score_item * y_px_diff)
            score_pixel = (score_px_x, score_px_y)
        elif _player == 1:
            # Player 2
            score_px_x = 580
            screen.blit(const.SCORE_FONT.render("P2", True, const.WHITE), (score_px_x - 20, base_px_y - 22))
            score_px_y = base_px_y + (_score_item * y_px_diff)
            score_pixel = (score_px_x, score_px_y)
        elif _player == 2:
            # Player 3
            score_px_x = 360
            screen.blit(const.SCORE_FONT.render("P3", True, const.WHITE), (score_px_x - 20, base_px_y - 22))
            score_px_y = base_px_y + (_score_item * y_px_diff)
            score_pixel = (score_px_x, score_px_y)
        elif _player == 3:
            # Player 4
            score_px_x = 655
            screen.blit(const.SCORE_FONT.render("P4", True, const.WHITE), (score_px_x - 20, base_px_y - 22))
            score_px_y = base_px_y + (_score_item * y_px_diff)
            score_pixel = (score_px_x, score_px_y)

        if _score == 1:
            start_pos = (score_pixel[0] - 10, score_pixel[1] + 10) # / First Point
            end_pos = (score_pixel[0] + 24, score_pixel[1] - 23)     # /
            pg.draw.line(screen, const.WHITE, start_pos, end_pos, line_width) # / First Point
        if _score == 2:
            start_pos = (score_pixel[0] - 10, score_pixel[1] + 10) # / First Point
            end_pos = (score_pixel[0] + 24, score_pixel[1] - 23)     # /
            pg.draw.line(screen, const.WHITE, start_pos, end_pos, line_width) # / First Point
            start_pos2 = (score_pixel[0] - 10, score_pixel[1] - 23)   # \ Second Point
            end_pos2 = (score_pixel[0] + 24, score_pixel[1] + 10)     # \
            pg.draw.line(screen, const.WHITE, start_pos2, end_pos2, line_width) # \ Second Point
        if _score >= 3:
            start_pos = (score_pixel[0] - 10, score_pixel[1] + 10) # / First Point
            end_pos = (score_pixel[0] + 24, score_pixel[1] - 23)     # /
            start_pos2 = (score_pixel[0] - 10, score_pixel[1] - 23)   # \ Second Point
            end_pos2 = (score_pixel[0] + 24, score_pixel[1] + 10)     # \
            pg.draw.circle(screen, const.ORANGE,(score_pixel[0] +7, score_pixel[1] -6), circle_width) # DRAW CIRCLE
            pg.draw.circle(screen, const.CHALKBOARD_BLACK,(score_pixel[0] +7, score_pixel[1] -6), circle_width - line_width) # DRAW CIRCLE
            pg.draw.line(screen, const.ORANGE, start_pos, end_pos, line_width)
            pg.draw.line(screen, const.ORANGE, start_pos2, end_pos2, line_width)

        pg.display.flip()

    def display_game_state(self, _throw_count=0):
        """Display the current game state."""
        global screen 
        self.display_background()
        # Display scores
        for i, player in enumerate(self.players):
            if i == 0:
                text_width = const.PSCORE_FONT.render(str(self.total_scores[i]), True, const.WHITE)
                text_width = text_width.get_width()
                score = self.total_scores[i]
                #print(f"Score is: {score}")
                pgui.player_1_score(self, screen, const.FONT, const.PSCORE_FONT, text_width, score)
            if i == 1:
                text_width = const.PSCORE_FONT.render(str(self.total_scores[i]), True, const.WHITE)
                text_width = text_width.get_width()
                score = self.total_scores[i]
                pgui.player_2_score(self, screen, const.FONT, const.PSCORE_FONT, text_width, score)
            if i == 2:
                text_width = const.PSCORE_FONT.render(str(self.total_scores[i]), True, const.WHITE)
                text_width = text_width.get_width()
                score = self.total_scores[i]
                pgui.player_3_score(self, screen, const.FONT, const.PSCORE_FONT, text_width, score)
            if i == 3:
                text_width = const.PSCORE_FONT.render(str(self.total_scores[i]), True, const.WHITE)
                text_width = text_width.get_width()
                score = self.total_scores[i]
                pgui.player_4_score(self, screen, const.FONT, const.PSCORE_FONT, text_width, score)
        
        # Darts Used
        pgui.darts_used(self, screen, const.FONT, const.SCORE_FONT)
        image = pg.image.load("assets/dart.png")
        image.convert()
        if _throw_count > 0:
            screen.blit(image, (60, 436))
        if _throw_count > 1:
            screen.blit(image, (60, 480))
        if _throw_count > 2:
            screen.blit(image, (60, 523))
        
        # Current round text
        if _throw_count >= 0 and _throw_count < 3:
            pg.draw.rect(screen, const.GREEN, pg.Rect(332, 546, 364, 32))
            pg.draw.rect(screen, const.WHITE, pg.Rect(330, 544, 368, 36), 2, 3)
            current_round_text = const.FONT.render(f"Round {CricketDarts.GAME_ROUND} - Player {self.current_player + 1} is up.", True, const.BLACK)
            for i in range(1,4):
                screen.blit(current_round_text, ((const.WIDTH//2 - current_round_text.get_width()//2) - i, (const.HEIGHT - 50) - i))
                screen.blit(current_round_text, ((const.WIDTH//2 - current_round_text.get_width()//2), (const.HEIGHT - 50) - i))
                screen.blit(current_round_text, ((const.WIDTH//2 - current_round_text.get_width()//2) + i, (const.HEIGHT - 50) - i))
                screen.blit(current_round_text, ((const.WIDTH//2 - current_round_text.get_width()//2) - i, (const.HEIGHT - 50)))
                screen.blit(current_round_text, ((const.WIDTH//2 - current_round_text.get_width()//2) + i, (const.HEIGHT - 50)))
                screen.blit(current_round_text, ((const.WIDTH//2 - current_round_text.get_width()//2) - i, (const.HEIGHT - 50) + i))
                screen.blit(current_round_text, ((const.WIDTH//2 - current_round_text.get_width()//2), (const.HEIGHT - 50) + i))
                screen.blit(current_round_text, ((const.WIDTH//2 - current_round_text.get_width()//2) + i, (const.HEIGHT - 50) + i))

            current_round_text = const.FONT.render(f"Round {CricketDarts.GAME_ROUND} - Player {self.current_player + 1} is up.", True, const.WHITE)
            screen.blit(current_round_text, (const.WIDTH//2 - current_round_text.get_width()//2, const.HEIGHT - 50))
        else:
            pg.draw.rect(screen, const.RED, pg.Rect(332, 546, 364, 32))
            pg.draw.rect(screen, const.WHITE, pg.Rect(330, 544, 368, 36), 2, 3)
            current_round_text = const.FONT.render(f"Round {CricketDarts.GAME_ROUND} - Player {self.current_player + 1} is done.", True, const.BLACK)
            for i in range(1,4):
                screen.blit(current_round_text, ((const.WIDTH//2 - current_round_text.get_width()//2) - i, (const.HEIGHT - 50) - i))
                screen.blit(current_round_text, ((const.WIDTH//2 - current_round_text.get_width()//2), (const.HEIGHT - 50) - i))
                screen.blit(current_round_text, ((const.WIDTH//2 - current_round_text.get_width()//2) + i, (const.HEIGHT - 50) - i))
                screen.blit(current_round_text, ((const.WIDTH//2 - current_round_text.get_width()//2) - i, (const.HEIGHT - 50)))
                screen.blit(current_round_text, ((const.WIDTH//2 - current_round_text.get_width()//2) + i, (const.HEIGHT - 50)))
                screen.blit(current_round_text, ((const.WIDTH//2 - current_round_text.get_width()//2) - i, (const.HEIGHT - 50) + i))
                screen.blit(current_round_text, ((const.WIDTH//2 - current_round_text.get_width()//2), (const.HEIGHT - 50) + i))
                screen.blit(current_round_text, ((const.WIDTH//2 - current_round_text.get_width()//2) + i, (const.HEIGHT - 50) + i))

            current_round_text = const.FONT.render(f"Round {CricketDarts.GAME_ROUND} - Player {self.current_player + 1} is done.", True, const.WHITE)
            screen.blit(current_round_text, (const.WIDTH//2 - current_round_text.get_width()//2, const.HEIGHT - 50))
            
            
        pg.display.flip()
    
    def turn(self, _end = False):
        throw_count = 0

        while throw_count < 3:
            
            self.check_winner() # Handle scenarios where the first or second dart thrown can be winners.
            
            if _end == True:
                throw_result = bc.read_board(_end = True)
            else:
                throw_result = bc.read_board()

            if throw_result == 'RIGHT':
                if self.undo_last_throw():
                    throw_count -= 1  # Revert throw count if undo successful7
                continue

            # Handle misses and numbers 1-14 as misses
            if throw_result == 'VIB' or self.is_miss(throw_result):
                self.rounds[self.current_player].append(throw_result)
                throw_count += 1
                #print(f"Throw '{throw_result}' counted as a miss.")

            else:
                # Handle scoring
                if self.handle_scoring(throw_result):
                    throw_count += 1
            
            pg.display.update()
            self.display_game_state(throw_count)

        # ######################### Debug code to simulate input without dartboard attached
        # while throw_count < 3:
        #     throw_result = 'T17'
        #     self.handle_scoring(throw_result)
        #     throw_count += 1
        #     throw_result = 'I19'
        #     self.handle_scoring(throw_result)
        #     throw_count += 1
        #     throw_result = 'D16'
        #     # throw_result = 'O15'
        #     # throw_result = 'O20'
        #     # throw_result = 'O18'
        #     # throw_result = 'SB'
        #     self.handle_scoring(throw_result)
        #     throw_count += 1
        #     pg.display.update()
        #     self.display_game_state(throw_count)


    def is_miss(self, throw_result):
        """Treats scores from 1 to 14 (including doubles and triples) as misses but allows recording for undo."""
        if throw_result.isdigit() and 1 <= int(throw_result) <= 14:
            return True
        if throw_result.startswith('I') and throw_result[1:].isdigit() and 1 <= int(throw_result[1:]) <= 14:
            return True
        if throw_result.startswith('O') and throw_result[1:].isdigit() and 1 <= int(throw_result[1:]) <= 14:
            return True
        if throw_result.startswith('D') and throw_result[1:].isdigit() and 1 <= int(throw_result[1:]) <= 14:
            return True
        if throw_result.startswith('T') and throw_result[1:].isdigit() and 1 <= int(throw_result[1:]) <= 14:
            return True
        return False

    def handle_scoring(self, throw_result):
        player_score = self.scores[self.current_player]
        points_to_add = 0

        # Handle different throw cases
        if throw_result.startswith('D') and throw_result != 'DB':
            num = int(throw_result[1:])
            hits = 2
        elif throw_result.startswith('T'):
            num = int(throw_result[1:])
            hits = 3
        elif throw_result.startswith('O'):
            num = int(throw_result[1:])
            hits = 1
        elif throw_result.startswith('I'):
            num = int(throw_result[1:])
            hits = 1
        elif throw_result == 'SB':
            num = 'SB'
            hits = 1
        elif throw_result == 'DB':
            num = 'SB'
            hits = 2
        else:
            try:
                num = int(throw_result)
                hits = 1
            except ValueError:
                print(f"Throw Result: {throw_result}")
                print("Invalid input! Please enter a valid throw.")
                return False

        # Add hits to the player's score
        if num in player_score:
            extra_hits = max(0, player_score[num] + hits - 3)  # Hits beyond 3 are extra
            player_score[num] += hits

            # Score points if the number is not closed for all players
            if extra_hits > 0 and not self.is_closed_for_all(num):
                points_to_add = extra_hits * (25 if num == 'SB' else num)
                self.total_scores[self.current_player] = points_to_add 

            # Add points to the total score
            #self.total_scores[self.current_player] += points_to_add 
            self.rounds[self.current_player].append(throw_result)
            # print(f"Added {extra_hits} extra hits. {points_to_add} points added.")

        return True

    def is_closed_for_all(self, num):
        """Checks if a number is closed for all players."""
        for score in self.scores:
            if score[num] < 3:
                return False
        return True

    def undo_last_throw(self):
        if not self.rounds[self.current_player]:
            print("No throws to undo!")
            return False

        last_throw = self.rounds[self.current_player].pop()
        player_score = self.scores[self.current_player]
        points_to_subtract = 0

        # Adjust the score based on the last throw
        if last_throw.startswith('D') and last_throw != 'DB':
            num = int(last_throw[1:])
            hits = 2
        elif last_throw.startswith('T'):
            num = int(last_throw[1:])
            hits = 3
        elif last_throw.startswith('O'):
            num = int(last_throw[1:])
            hits = 1
        elif last_throw.startswith('I'):
            num = int(last_throw[1:])
            hits = 1
        elif last_throw == 'SB':
            num = 'SB'
            hits = 1
        elif last_throw == 'DB':
            num = 'SB'
            hits = 2
        else:
            num = int(last_throw)
            hits = 1

        # Revert the hits
        if num in player_score:
            player_score[num] += hits  # Increment player's score

            # Check if the target is closed for all players after adding hits
            if player_score[num] > 3:
                player_score[num] = 3  # Cap at 3 hits

            if self.is_closed_for_all(num):  # Only add points if target is closed for all players
                extra_hits = max(0, player_score[num] - 3)  # Calculate extra hits beyond closure
                if extra_hits > 0:
                    points_to_add = extra_hits * (25 if num == 'SB' else num)

        # Add points to the total score only after closure verification
        self.total_scores[self.current_player] += points_to_add

        return True

    def check_winner(self):
        for i, player_score in enumerate(self.scores):
            if all(score >= 3 for score in player_score.values()): # This player has closed out all number
                if self.total_scores[i] == max(self.total_scores):
                    print(f"\n{self.players[i]} has won the game!")
                    return True
            return False

# Start the game
game = CricketDarts()
game.start_game()
game.play_game()
