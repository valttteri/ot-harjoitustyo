import pygame

pygame.init()

class Snake(pygame.sprite.Sprite):
    def __init__(self, head_x:int, head_y:int, cell_size:int, width:int, height:int, display):
        super().__init__()
        self.cell_size = cell_size
        self.direction_x = 0
        self.direction_y = -1
        self.display = display
        self.max_x_pos = self.cell_size * width
        self.max_y_pos = self.cell_size * height
        self.grow = False

        self.body = [
                pygame.Rect(head_x * self.cell_size, head_y * self.cell_size, self.cell_size, self.cell_size),
                pygame.Rect(head_x * self.cell_size, (head_y + 1) * self.cell_size, self.cell_size, self.cell_size),
                pygame.Rect(head_x * self.cell_size, (head_y + 2) * self.cell_size, self.cell_size, self.cell_size)
            ]

        self.rect = self.body[0]
    
    def plot_snake(self):
        for part in self.body:
            pygame.draw.rect(self.display, (0, 0, 255), part)

    def move_snake(self):
        new_head = pygame.Rect(self.body[0].x, self.body[0].y, self.cell_size, self.cell_size)
        new_head.move_ip(self.cell_size * self.direction_x, self.cell_size * self.direction_y)
        if new_head.x < 0:
            new_head = pygame.Rect(self.max_x_pos-self.cell_size, self.body[0].y, self.cell_size, self.cell_size)
        if new_head.x >= self.max_x_pos:
            new_head = pygame.Rect(0, self.body[0].y, self.cell_size, self.cell_size)

        if new_head.y < 0:
            new_head = pygame.Rect(self.body[0].x, self.max_y_pos-self.cell_size, self.cell_size, self.cell_size)
        if new_head.y >= self.max_y_pos:
            new_head = pygame.Rect(self.body[0].x, 0, self.cell_size, self.cell_size)

        self.body.insert(0, new_head)
        self.rect = new_head

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

    def rect_list(self):
        return self.body

class Wall(pygame.sprite.Sprite):
    def __init__(self, x_pos=0, y_pos=0):
        super().__init__()
        
        self.image = pygame.transform.scale(
            pygame.image.load('images/grass.png').convert_alpha(),
            (30, 30))

        self.rect = self.image.get_rect()

        self.rect.x = x_pos
        self.rect.y = y_pos

def form_walls(map_level, width, height):
    walls = pygame.sprite.Group()

    for y in range(height):
        for x in range(width):
            cell = map_level[y][x]
            x_pos = 30 * x
            y_pos = 30 * y

            if cell == 1:
                walls.add(Wall(x_pos, y_pos))
    
    return walls
    


map_level = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

def main():
    cell_size = 30
    display_width = len(map_level[0])
    display_height = len(map_level)

    display = pygame.display.set_mode((cell_size * display_width, cell_size * display_height))
    pygame.display.set_caption("Snake 2023")
    clock = pygame.time.Clock()
    snake = Snake(10, 6, cell_size, display_width, display_height, display)

    walls = pygame.sprite.Group()
    sprites = pygame.sprite.Group()

    walls = form_walls(map_level, display_width, display_height)
    sprites.add(walls)

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
        sprites.draw(display)
        if pygame.sprite.spritecollide(snake, walls, False):
            print("bonk")
        pygame.display.update()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
    