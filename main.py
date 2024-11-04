#import board_comms as bc
import pygame as pg
import sys, time, random
import subprocess
import constants as const

pg.init()

screen = pg.display.set_mode((const.WIDTH, const.HEIGHT)) #, pg.FULLSCREEN)
#pg.mouse.set_visible(False)
pg.display.set_caption("Championship Darts Game Selection")

# Fonts
font = pg.font.Font(None, 36)

# Game names
#game_names = [f"Game{random.randint(1, 100)}" for _ in range(10)]
game_names = ["Cricket",
              "Wildcard Cricket",
              "Cut-Throat Cricket",
              "301",
              "501",
              "701",
              "Tic Tac Toe"] 

# Grid settings
cols, rows = 1, 7
cell_width, cell_height = const.WIDTH // cols, const.HEIGHT // rows 

# Selection
selected_index = 0

def draw_selection_screen():
    screen.fill(const.CHALKBOARD_BLACK)
    for i, game in enumerate(game_names):
        col = i % cols
        row = i // cols
        x, y = col * cell_width, row * cell_height
        
        # Highlight selected game
        if i == selected_index:
            pg.draw.rect(screen, const.HIGHLIGHT_COLOR, (x, y, cell_width, cell_height))

        # Draw game name
        text = font.render(game, True, const.WHITE)
        text_rect = text.get_rect(center=(x + cell_width // 2, y + cell_height // 2))
        screen.blit(text, text_rect)

def move_selection(direction):
    global selected_index
    if direction == "up" and selected_index >= cols:
        selected_index -= cols
    elif direction == "down" and selected_index < len(game_names) - cols:
        selected_index += cols
    elif direction == "left" and selected_index % cols > 0:
        selected_index -= 1
    elif direction == "right" and selected_index % cols < cols - 1:
        selected_index += 1

#def game_selection(self):
    # """Prompt for the number of players using Pygame input."""
    # bc.write_serial_led("ENTER_ON")
    # bc.write_serial_led("UP_ON")
    # bc.write_serial_led("DOWN_ON")   

def begin():
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    move_selection("up")
                elif event.key == pg.K_DOWN:
                    move_selection("down")
                elif event.key == pg.K_LEFT:
                    move_selection("left")
                elif event.key == pg.K_RIGHT:
                    move_selection("right")
                elif event.key == pg.K_RETURN:
                    if game_names[selected_index] == "Cricket":
                        subprocess.run(["python", "cricket.py"])
                    print(f"Selected Game: {game_names[selected_index]}")

        # Draw the screen
        draw_selection_screen()
        pg.display.flip()

    # Quit Pygame
    pg.quit()
    sys.exit()

if __name__ == '__main__':
    begin()