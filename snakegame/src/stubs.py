import pygame
from score import Score
from snake import Snake


class StubGameEventHandler:
    def __init__(self, level):
        self.level = level

    def reset_score(self):
        print("score was reset")

    def save_final_score(self):
        print("score was submitted")


class StubScreen:
    def __init__(self, screen_type: str):
        self.type = screen_type
        self.status = None

    def draw(self, high_score=None):
        if high_score is not None:
            self.status = f"rendered {self.type} screen with high score {high_score}"
        else:
            self.status = f"rendered {self.type} screen"


class StubDatabaseHandler:
    def __init__(self):
        self.location = "nothing"

    def get_high_scores(self):
        return 1

    def update_database(self, nothing):
        return nothing


class StubImageLoader:
    def load_image(self, name: str):
        return pygame.image.load(f"src/images/{name}")


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class StubPygameEvents:
    def __init__(self, events):
        self.events = events

    def get_events(self):
        return self.events

    def update_display(self):
        return 1

    def quit(self):
        return 1


class StubRenderer:
    def __init__(self, level):
        self.level = level
        self.stub_screen = None

    def render_screen(self, name, high_scores=None):
        options = {
            "start": StubScreen("start"),
            "pause": StubScreen("pause"),
            "game_over": StubScreen("game_over"),
            "victory": StubScreen("victory"),
            "high_score_screen": StubScreen("high_score"),
        }
        if name == "high_score_screen":
            options[name].draw(high_scores)
        else:
            options[name].draw()
        self.stub_screen = options[name]

    def render_sprites(self, level_sprites):
        return level_sprites

    def display_score(self, score):
        return score

    def render_snakes_head(self, part, direction):
        return part, direction

    def render_snakes_body(self, part, another, third):
        return [part, another, third]

    def render_snakes_tail(self, tail, part):
        return tail, part


class StubClock:
    def __init__(self, fps):
        self.fps = fps

    def tick(self):
        return 1


class StubUserEvents:
    def time_to_move_snake(self):
        return 1


class StubLevelHandler:
    def __init__(self, level: str, cell_size: int):
        self.level = level
        self.cell_size = cell_size
        self.score = Score(0)
        self.snake = Snake(6, 6, 30, 30, 20)

    def get_sprites(self):
        return 1

    def reset_level_score(self):
        return 1

    def level_score(self):
        return 1

    def snake_collision(self):
        return 1

    def victory(self):
        return 1

    def snake_eats_food(self):
        return ["food"]

    def snakes_body(self):
        return [1, 2, 3, 4, 5]

    def snakes_current_direction(self):
        return self.snake.snakes_direction()

    def change_snakes_direction(self, direction: str):
        self.snake.change_direction(direction)

    def snake_move(self):
        self.snake.move_snake()

    def relocate_food(self, food):
        return food

    def grow_snake(self):
        return 1

    def increase_score(self):
        return 1
