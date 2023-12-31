import unittest
import pygame
from objects.snake import Snake


class TestSnake(unittest.TestCase):
    def setUp(self):
        self.head_pos = {"x": 10, "y": 10}
        self.cell_size = 30
        self.width = 20
        self.height = 20
        self.snake = Snake(
            self.head_pos["x"],
            self.head_pos["y"],
            self.cell_size,
            self.width,
            self.height,
        )

    def test_snakes_initial_position_correct(self):
        self.assertEqual(self.snake.body[0].x, 300)
        self.assertEqual(self.snake.body[0].y, 300)

    def test_moving_snake_right(self):
        self.snake.change_direction("right")
        self.snake.move_snake()
        self.assertEqual(self.snake.body[0].x, 330)
        self.assertEqual(self.snake.body[0].y, 300)

    def test_moving_snake_left(self):
        self.snake.change_direction("left")
        self.snake.move_snake()
        self.assertEqual(self.snake.body[0].x, 270)
        self.assertEqual(self.snake.body[0].y, 300)

    def test_moving_snake_up(self):
        self.snake.change_direction("up")
        self.snake.move_snake()
        self.assertEqual(self.snake.body[0].x, 300)
        self.assertEqual(self.snake.body[0].y, 270)

    def test_moving_snake_down(self):
        self.snake.change_direction("right")
        self.snake.move_snake()
        self.snake.change_direction("down")
        self.snake.move_snake()
        self.assertEqual(self.snake.body[0].x, 330)
        self.assertEqual(self.snake.body[0].y, 330)

    def test_invalid_direction_change(self):
        self.snake.change_direction("right")
        self.snake.move_snake()
        self.snake.change_direction("left")
        self.snake.move_snake()
        self.assertEqual(self.snake.body[0].x, 360)
        self.assertEqual(self.snake.body[0].y, 300)
        self.assertEqual(self.snake.direction["x"], 1)
        self.assertEqual(self.snake.direction["y"], 0)

        self.snake.change_direction("down")
        self.snake.move_snake()
        self.snake.change_direction("up")
        self.snake.move_snake()
        self.assertEqual(self.snake.body[0].x, 360)
        self.assertEqual(self.snake.body[0].y, 360)
        self.assertEqual(self.snake.direction["x"], 0)
        self.assertEqual(self.snake.direction["y"], 1)

        self.snake.change_direction("left")
        self.snake.move_snake()
        self.snake.change_direction("right")
        self.snake.move_snake()
        self.assertEqual(self.snake.body[0].x, 300)
        self.assertEqual(self.snake.body[0].y, 360)
        self.assertEqual(self.snake.direction["x"], -1)
        self.assertEqual(self.snake.direction["y"], 0)

        self.snake.change_direction("up")
        self.snake.move_snake()
        self.snake.change_direction("down")
        self.snake.move_snake()
        self.assertEqual(self.snake.body[0].x, 300)
        self.assertEqual(self.snake.body[0].y, 300)
        self.assertEqual(self.snake.direction["x"], 0)
        self.assertEqual(self.snake.direction["y"], -1)

    def test_snake_can_grow(self):
        self.assertEqual(len(self.snake.body), 3)
        self.snake.grow_snake()
        self.snake.move_snake()
        self.snake.grow_snake()
        self.snake.move_snake()
        self.assertEqual(len(self.snake.body), 5)

    def test_snake_hits_itself(self):
        self.grow_snake_by(10)
        self.snake.change_direction("right")
        self.snake.move_snake()
        self.snake.move_snake()
        self.snake.change_direction("down")
        self.snake.move_snake()
        self.snake.move_snake()
        self.snake.change_direction("left")
        self.snake.move_snake()
        self.snake.move_snake()
        self.assertTrue(self.snake.snake_hits_itself())

    def test_reset_snake(self):
        intial_x_pos = self.snake.body[0].x
        intial_y_pos = self.snake.body[0].y
        self.snake.move_snake()
        self.snake.move_snake()
        self.snake.change_direction("right")
        self.snake.move_snake()
        self.snake.move_snake()
        self.snake.reset_snake()
        self.assertEqual(self.snake.body[0].x, intial_x_pos)
        self.assertEqual(self.snake.body[0].y, intial_y_pos)

    def grow_snake_by(self, number: int):
        for i in range(3, number + 3):
            snake_piece = pygame.Rect(
                self.snake.head_pos["x"] * self.cell_size,
                (self.snake.head_pos["y"] + i) * self.cell_size,
                self.cell_size,
                self.cell_size,
            )
            self.snake.body.append(snake_piece)
