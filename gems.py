import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 235)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Bird class
class Bird:
    def __init__(self):
        self.image = pygame.Surface((30, 30))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (50, SCREEN_HEIGHT // 2)
        self.gravity = 0.25
        self.lift = -6
        self.velocity = 0

    def flap(self):
        self.velocity = self.lift

    def move(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity

# Pipe class
class Pipe:
    def __init__(self):
        self.width = 50
        self.gap = 150
        self.speed = 3
        self.pipes = []
        self.distance_since_last_pipe = 0
        self.pipe_distance_threshold = 200  # Distance threshold for spawning new pipes

    def create_pipe(self):
        height = random.randint(100, 400)
        top_pipe = pygame.Rect(SCREEN_WIDTH, 0, self.width, height)
        bottom_pipe = pygame.Rect(SCREEN_WIDTH, height + self.gap, self.width, SCREEN_HEIGHT - height - self.gap)
        top_pipe.scored = False  # Initialize the scored attribute
        self.pipes.append((top_pipe, bottom_pipe))
        self.distance_since_last_pipe = 0  # Reset the distance counter

    def move_pipes(self):
        for top_pipe, bottom_pipe in self.pipes:
            top_pipe.x -= self.speed
            bottom_pipe.x -= self.speed
        self.distance_since_last_pipe += self.speed

    def remove_offscreen_pipes(self, game):
        new_pipes = []
        for top_pipe, bottom_pipe in self.pipes:
            if top_pipe.x > -self.width:
                new_pipes.append((top_pipe, bottom_pipe))
            else:
                game.display_score_for_pipe()
        self.pipes = new_pipes

# Game class
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()
        self.bird = Bird()
        self.pipe = Pipe()
        self.running = True
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)
        self.score = 0

    def check_collisions(self):
        for top_pipe, bottom_pipe in self.pipe.pipes:
            if self.bird.rect.colliderect(top_pipe) or self.bird.rect.colliderect(bottom_pipe):
                self.game_over()
        if self.bird.rect.top <= 0 or self.bird.rect.bottom >= SCREEN_HEIGHT:
            self.game_over()

    def game_over(self):
        self.running = False
        self.screen.fill(SKY_BLUE)
        game_over_text = self.font.render("Game Over", True, BLACK)
        restart_text = self.small_font.render("Press SPACE to Restart", True, BLACK)
        self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 100))
        self.screen.blit(restart_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50))
        pygame.display.flip()

        while not self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.__init__()
                        self.run()

    def display_score_for_pipe(self):
        self.score += 1

    def run(self):
        self.pipe.create_pipe()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.flap()

            self.bird.move()
            self.pipe.move_pipes()
            self.pipe.remove_offscreen_pipes(self)
            self.check_collisions()

            # Increment score if bird passes through pipes
            for top_pipe, bottom_pipe in self.pipe.pipes:
                if top_pipe.x + self.pipe.width < self.bird.rect.left and not top_pipe.scored:
                    self.score += 1
                    top_pipe.scored = True

            if self.pipe.distance_since_last_pipe >= self.pipe.pipe_distance_threshold:
                self.pipe.create_pipe()

            self.screen.fill(SKY_BLUE)
            self.screen.blit(self.bird.image, self.bird.rect)
            for top_pipe, bottom_pipe in self.pipe.pipes:
                pygame.draw.rect(self.screen, GREEN, top_pipe)
                pygame.draw.rect(self.screen, GREEN, bottom_pipe)

            # Display score
            score_text = self.small_font.render(f"Score: {self.score}", True, BLACK)
            self.screen.blit(score_text, (10, 10))

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()