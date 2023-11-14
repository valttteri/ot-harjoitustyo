import pygame
from pygame.math import Vector2
import os

pygame.init()

class Snake(pygame.sprite.Sprite):
    def __init__(self, head_x:int, head_y:int, cell_size:int, width:int, height:int):
        super().__init__()
        self.body = [Vector2(head_x, head_y), Vector2(10, head_y+1), Vector2(10, head_y+2)]
        self.direction = Vector2(0, -1)
        self.width = width
        self.height = height
        self.max_x_pos = cell_size * width
        self.max_y_pos = cell_size * height
        self.grow = False
    
    def plot_snake(self):
        for part in self.body:
            x_pos = int(part.x * cell_size)
            y_pos = int(part.y * cell_size)
            part_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(display, (0, 0, 255), part_rect)
    
    def move_snake(self):
        new_head = Vector2(self.body[0].x, self.body[0].y) + self.direction
        if new_head.x < 0:
            new_head = Vector2(self.width, self.body[0].y) + self.direction
        if new_head.x >= self.width:
            new_head = Vector2(-1, self.body[0].y) + self.direction

        if new_head.y < 0:
            new_head = Vector2(self.body[0].x, self.height) + self.direction
        if new_head.y >= self.height:
            new_head = Vector2(self.body[0].x, -1) + self.direction

        self.body.insert(0, new_head)
        if self.grow:
            self.grow = False
        else:
            self.body.pop()
    
    def change_direction(self, direction:str):
        if direction == 'up':
            if self.direction == Vector2(0, 1):
                return
            self.direction = Vector2(0, -1)
        if direction == 'down':
            if self.direction == Vector2(0, -1):
                return
            self.direction = Vector2(0, 1)
        if direction == 'left':
            if self.direction == Vector2(1, 0):
                return
            self.direction = Vector2(-1, 0)
        if direction == 'right':
            if self.direction == Vector2(-1, 0):
                return
            self.direction = Vector2(1, 0)
    
    def grow_snake(self):
        self.grow = True

cell_size = 40
display_width = 20
display_height = 15

display = pygame.display.set_mode((cell_size * display_width, cell_size * display_height))
clock = pygame.time.Clock()
snake = Snake(10, 6, cell_size, display_width, display_height)

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
    