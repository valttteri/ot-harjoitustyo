import pygame
from pygame.math import Vector2

pygame.init()

class Snake(pygame.sprite.Sprite):
    def __init__(self, head_x:int, head_y:int, cell_size:int, width:int, height:int, display):
        super().__init__()
        self.cell_size = cell_size
        self.direction_x = 0
        self.direction_y = -1
        self.display = display
        self.width = width
        self.height = height
        self.max_x_pos = self.cell_size * width
        self.max_y_pos = self.cell_size * height
        self.grow = False

        self.body = [
                pygame.Rect(head_x * self.cell_size, head_y * self.cell_size, self.cell_size, self.cell_size),
                pygame.Rect(head_x * self.cell_size, (head_y + 1) * self.cell_size, self.cell_size, self.cell_size),
                pygame.Rect(head_x * self.cell_size, (head_y + 2) * self.cell_size, self.cell_size, self.cell_size)
            ]
    
    def plot_snake(self):
        for part in self.body:
            pygame.draw.rect(self.display, (0, 0, 255), part)

    def move_snake(self):
        new_head = pygame.Rect(self.body[0].x, self.body[0].y, self.cell_size, self.cell_size)
        new_head.move_ip(self.cell_size * self.direction_x, self.cell_size * self.direction_y)
        #if new_head.x < 0:
        #    new_head = Vector2(self.width, self.body[0].y) + self.direction
        #if new_head.x >= self.width:
        #    new_head = Vector2(-1, self.body[0].y) + self.direction
#
        #if new_head.y < 0:
        #    new_head = Vector2(self.body[0].x, self.height) + self.direction
        #if new_head.y >= self.height:
        #    new_head = Vector2(self.body[0].x, -1) + self.direction

        self.body.insert(0, new_head)

        if self.snake_hits_itself():
            print("game over")

        if self.grow:
            self.grow = False
        else:
            self.body.pop()
    
    def change_direction(self, direction:str):
        if direction == 'up':
            if self.direction_y == 1:
                return
            self.direction_y = -1
            self.direction_x = 0
        if direction == 'down':
            if self.direction_y == -1:
                return
            self.direction_y = 1
            self.direction_x = 0
        if direction == 'left':
            if self.direction_x == 1:
                return
            self.direction_x = -1
            self.direction_y = 0
        if direction == 'right':
            if self.direction_x == -1:
                return
            self.direction_x = 1
            self.direction_y = 0

    def grow_snake(self):
        self.grow = True

    def snake_hits_itself(self):
        return self.body[0].collidelistall(self.body[1:])

def main():
    cell_size = 30
    display_width = 30
    display_height = 20

    display = pygame.display.set_mode((cell_size * display_width, cell_size * display_height))
    pygame.display.set_caption("Snake 2023")
    clock = pygame.time.Clock()
    snake = Snake(10, 6, cell_size, display_width, display_height, display)

    sprites = pygame.sprite.Group()

    MOVE_SNAKE = pygame.USEREVENT
    pygame.time.set_timer(MOVE_SNAKE, 200)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_UP:
                    snake.change_direction('up')
                if event.key == pygame.K_DOWN:
                    snake.change_direction('down')
                if event.key == pygame.K_LEFT:
                    snake.change_direction('left')
                if event.key == pygame.K_RIGHT:
                    snake.change_direction('right')
                if event.key == pygame.K_g:
                    snake.grow_snake()
            if event.type == MOVE_SNAKE:
                snake.move_snake()
            
            elif event.type == pygame.QUIT:
                running = False

        display.fill((0, 255, 0))
        snake.plot_snake()
        pygame.display.update()

        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
    