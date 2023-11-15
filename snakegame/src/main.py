import pygame
from objects import snake, wall
from levels import get_level
pygame.init()

class SnakeGame:
    def __init__(self):
        self.status = 'level_one'
        self.cell_size = 30
        self.map = get_level(self.status)
        self.display_width = len(self.map[0])
        self.display_height = len(self.map)

        self.display = pygame.display.set_mode((self.cell_size * self.display_width, self.cell_size * self.display_height))
        pygame.display.set_caption("Snake 2023")
        self.clock = pygame.time.Clock()

        self.snake = snake.Snake(10, 6, self.cell_size, self.display_width, self.display_height, self.display)
        self.sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        self.MOVE_SNAKE = pygame.USEREVENT
        pygame.time.set_timer(self.MOVE_SNAKE, 200)

        self.running = True
        self.get_sprites()
        self.loop()
    
    def get_sprites(self):
        for y in range(self.display_height):
            for x in range(self.display_width):
                cell = self.map[y][x]
                x_pos = self.cell_size * x
                y_pos = self.cell_size * y

                if cell == 1:
                    self.walls.add(wall.Wall(x_pos, y_pos))
        
        self.sprites.add(self.walls)

    def loop(self):
        while self.running:
            self.get_events()

            self.display.fill((0, 255, 0))
            self.snake.plot_snake()
            self.sprites.draw(self.display)
            if pygame.sprite.spritecollide(self.snake, self.walls, False):
                self.running = False
                print("game over")
            if self.snake.snake_hits_itself():
                self.running = False
                print("game over")
            pygame.display.update()

            self.clock.tick(60)

        pygame.quit()
    
    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_UP:
                    self.snake.change_direction('up')
                if event.key == pygame.K_DOWN:
                    self.snake.change_direction('down')
                if event.key == pygame.K_LEFT:
                    self.snake.change_direction('left')
                if event.key == pygame.K_RIGHT:
                    self.snake.change_direction('right')
                if event.key == pygame.K_g:
                    self.snake.grow_snake()
            if event.type == self.MOVE_SNAKE:
                self.snake.move_snake()

            elif event.type == pygame.QUIT:
                self.running = False

if __name__ == "__main__":
    SnakeGame()
    