import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
GRID_WIDTH = 10
GRID_HEIGHT = 20
CELL_SIZE = 30
GRID_X_OFFSET = 50
GRID_Y_OFFSET = 50

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
GRAY = (128, 128, 128)

# Tetris pieces (tetrominoes)
PIECES = [
    # I piece
    [['.....',
      '..#..',
      '..#..',
      '..#..',
      '..#..'],
     ['.....',
      '.....',
      '####.',
      '.....',
      '.....']],
    
    # O piece
    [['.....',
      '.....',
      '.##..',
      '.##..',
      '.....']],
    
    # T piece
    [['.....',
      '.....',
      '.#...',
      '###..',
      '.....'],
     ['.....',
      '.....',
      '.#...',
      '.##..',
      '.#...'],
     ['.....',
      '.....',
      '.....',
      '###..',
      '.#...'],
     ['.....',
      '.....',
      '.#...',
      '##...',
      '.#...']],
    
    # S piece
    [['.....',
      '.....',
      '.##..',
      '##...',
      '.....'],
     ['.....',
      '.#...',
      '.##..',
      '..#..',
      '.....']],
    
    # Z piece
    [['.....',
      '.....',
      '##...',
      '.##..',
      '.....'],
     ['.....',
      '..#..',
      '.##..',
      '.#...',
      '.....']],
    
    # J piece
    [['.....',
      '.#...',
      '.#...',
      '##...',
      '.....'],
     ['.....',
      '.....',
      '#....',
      '###..',
      '.....'],
     ['.....',
      '.##..',
      '.#...',
      '.#...',
      '.....'],
     ['.....',
      '.....',
      '###..',
      '..#..',
      '.....']],
    
    # L piece
    [['.....',
      '..#..',
      '..#..',
      '.##..',
      '.....'],
     ['.....',
      '.....',
      '###..',
      '#....',
      '.....'],
     ['.....',
      '##...',
      '.#...',
      '.#...',
      '.....'],
     ['.....',
      '.....',
      '..#..',
      '###..',
      '.....']]
]

PIECE_COLORS = [CYAN, YELLOW, PURPLE, GREEN, RED, BLUE, ORANGE]

class TetrisPiece:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.piece_type = random.randint(0, len(PIECES) - 1)
        self.rotation = 0
        self.color = PIECE_COLORS[self.piece_type]
    
    def get_rotated_piece(self):
        return PIECES[self.piece_type][self.rotation % len(PIECES[self.piece_type])]
    
    def get_cells(self):
        cells = []
        piece = self.get_rotated_piece()
        for row in range(5):
            for col in range(5):
                if piece[row][col] == '#':
                    cells.append((self.x + col, self.y + row))
        return cells

class TetrisGame:
    def __init__(self):
        self.grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = None
        self.next_piece = None
        self.score = 0
        self.lines_cleared = 0
        self.fall_time = 0
        self.fall_speed = 500  # milliseconds
        self.game_over = False
        self.spawn_new_piece()
    
    def spawn_new_piece(self):
        if self.next_piece is None:
            self.next_piece = TetrisPiece(GRID_WIDTH // 2 - 2, 0)
        
        self.current_piece = self.next_piece
        self.next_piece = TetrisPiece(GRID_WIDTH // 2 - 2, 0)
        
        # Check if game is over
        if self.check_collision(self.current_piece):
            self.game_over = True
    
    def check_collision(self, piece):
        cells = piece.get_cells()
        for x, y in cells:
            if (x < 0 or x >= GRID_WIDTH or 
                y >= GRID_HEIGHT or 
                (y >= 0 and self.grid[y][x] != BLACK)):
                return True
        return False
    
    def move_piece(self, dx, dy):
        piece = TetrisPiece(self.current_piece.x + dx, self.current_piece.y + dy)
        piece.piece_type = self.current_piece.piece_type
        piece.rotation = self.current_piece.rotation
        piece.color = self.current_piece.color
        
        if not self.check_collision(piece):
            self.current_piece = piece
            return True
        return False
    
    def rotate_piece(self):
        piece = TetrisPiece(self.current_piece.x, self.current_piece.y)
        piece.piece_type = self.current_piece.piece_type
        piece.rotation = self.current_piece.rotation + 1
        piece.color = self.current_piece.color
        
        if not self.check_collision(piece):
            self.current_piece = piece
            return True
        return False
    
    def drop_piece(self):
        if self.move_piece(0, 1):
            return True
        else:
            self.place_piece()
            self.clear_lines()
            self.spawn_new_piece()
            return False
    
    def place_piece(self):
        cells = self.current_piece.get_cells()
        for x, y in cells:
            if 0 <= y < GRID_HEIGHT and 0 <= x < GRID_WIDTH:
                self.grid[y][x] = self.current_piece.color
    
    def clear_lines(self):
        lines_to_clear = []
        for y in range(GRID_HEIGHT):
            if all(self.grid[y][x] != BLACK for x in range(GRID_WIDTH)):
                lines_to_clear.append(y)
        
        for y in lines_to_clear:
            del self.grid[y]
            self.grid.insert(0, [BLACK for _ in range(GRID_WIDTH)])
        
        if lines_to_clear:
            self.lines_cleared += len(lines_to_clear)
            self.score += len(lines_to_clear) * 100 * (len(lines_to_clear) + 1)
            # Increase speed
            self.fall_speed = max(50, self.fall_speed - 10)
    
    def update(self, dt):
        if self.game_over:
            return
        
        self.fall_time += dt
        if self.fall_time >= self.fall_speed:
            self.drop_piece()
            self.fall_time = 0

class TetrisRenderer:
    def __init__(self):
        self.screen_width = GRID_WIDTH * CELL_SIZE + 2 * GRID_X_OFFSET + 200
        self.screen_height = GRID_HEIGHT * CELL_SIZE + 2 * GRID_Y_OFFSET
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Tetris")
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
    
    def draw_cell(self, x, y, color):
        rect = pygame.Rect(
            GRID_X_OFFSET + x * CELL_SIZE,
            GRID_Y_OFFSET + y * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE
        )
        pygame.draw.rect(self.screen, color, rect)
        pygame.draw.rect(self.screen, WHITE, rect, 1)
    
    def draw_grid(self, game):
        # Draw background grid
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                self.draw_cell(x, y, game.grid[y][x])
        
        # Draw current piece
        if game.current_piece:
            cells = game.current_piece.get_cells()
            for x, y in cells:
                if 0 <= y < GRID_HEIGHT and 0 <= x < GRID_WIDTH:
                    self.draw_cell(x, y, game.current_piece.color)
    
    def draw_next_piece(self, game):
        if game.next_piece:
            next_x = GRID_X_OFFSET + GRID_WIDTH * CELL_SIZE + 20
            next_y = GRID_Y_OFFSET + 50
            
            # Draw "Next:" label
            text = self.small_font.render("Next:", True, WHITE)
            self.screen.blit(text, (next_x, next_y - 30))
            
            # Draw next piece
            piece = game.next_piece.get_rotated_piece()
            for row in range(5):
                for col in range(5):
                    if piece[row][col] == '#':
                        rect = pygame.Rect(
                            next_x + col * 20,
                            next_y + row * 20,
                            20,
                            20
                        )
                        pygame.draw.rect(self.screen, game.next_piece.color, rect)
                        pygame.draw.rect(self.screen, WHITE, rect, 1)
    
    def draw_info(self, game):
        info_x = GRID_X_OFFSET + GRID_WIDTH * CELL_SIZE + 20
        info_y = GRID_Y_OFFSET + 200
        
        # Score
        score_text = self.small_font.render(f"Score: {game.score}", True, WHITE)
        self.screen.blit(score_text, (info_x, info_y))
        
        # Lines cleared
        lines_text = self.small_font.render(f"Lines: {game.lines_cleared}", True, WHITE)
        self.screen.blit(lines_text, (info_x, info_y + 30))
        
        # Game over
        if game.game_over:
            game_over_text = self.font.render("GAME OVER", True, RED)
            text_rect = game_over_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            self.screen.blit(game_over_text, text_rect)
            
            restart_text = self.small_font.render("Press R to restart", True, WHITE)
            restart_rect = restart_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 40))
            self.screen.blit(restart_text, restart_rect)
    
    def draw_controls(self):
        controls_x = GRID_X_OFFSET + GRID_WIDTH * CELL_SIZE + 20
        controls_y = GRID_Y_OFFSET + 300
        
        controls = [
            "Controls:",
            "A/D - Move left/right",
            "S - Soft drop",
            "W - Rotate",
            "SPACE - Hard drop",
            "R - Restart"
        ]
        
        for i, control in enumerate(controls):
            color = WHITE if i == 0 else GRAY
            text = self.small_font.render(control, True, color)
            self.screen.blit(text, (controls_x, controls_y + i * 20))
    
    def render(self, game):
        self.screen.fill(BLACK)
        self.draw_grid(game)
        self.draw_next_piece(game)
        self.draw_info(game)
        self.draw_controls()
        pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    game = TetrisGame()
    renderer = TetrisRenderer()
    
    running = True
    while running:
        dt = clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if game.game_over:
                    if event.key == pygame.K_r:
                        game = TetrisGame()
                else:
                    if event.key == pygame.K_a:  # Move left
                        game.move_piece(-1, 0)
                    elif event.key == pygame.K_d:  # Move right
                        game.move_piece(1, 0)
                    elif event.key == pygame.K_s:  # Soft drop
                        game.drop_piece()
                    elif event.key == pygame.K_w:  # Rotate
                        game.rotate_piece()
                    elif event.key == pygame.K_SPACE:  # Hard drop
                        while game.drop_piece():
                            pass
        
        game.update(dt)
        renderer.render(game)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()