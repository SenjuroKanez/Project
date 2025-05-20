import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.width = 40
        self.height = 40
        self.gravity = 0.5
        self.lift = -10
        self.velocity = 0

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))

    def flap(self):
        self.velocity = self.lift

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

        # Prevent the bird from going out of bounds
        if self.y < 0:
            self.y = 0
        if self.y + self.height > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.height

# Pipe class
class Pipe:
    def __init__(self):
        self.width = 50
        self.gap = 150  # Vertical gap between pipes
        self.speed = 3
        self.pipes = []  # List to store pipe information
        self.spawn_interval = 300  # Horizontal distance between pipes

    def create_pipe(self):
        # Check if the last pipe is far enough away
        if self.pipes:
            last_pipe = self.pipes[-1]
            if last_pipe["top"].x + self.width + self.spawn_interval > SCREEN_WIDTH:
                return  # Don't spawn a new pipe yet

        gap_y = random.randint(100, SCREEN_HEIGHT - 200)  # Randomize gap position
        top_pipe = pygame.Rect(SCREEN_WIDTH, 0, self.width, gap_y)
        bottom_pipe = pygame.Rect(SCREEN_WIDTH, gap_y + self.gap, self.width, SCREEN_HEIGHT - (gap_y + self.gap))
        self.pipes.append({"top": top_pipe, "bottom": bottom_pipe, "scored": False})

    def move_pipes(self):
        for pipe in self.pipes:
            pipe["top"].x -= self.speed
            pipe["bottom"].x -= self.speed

    def draw_pipes(self):
        for pipe in self.pipes:
            pygame.draw.rect(screen, GREEN, pipe["top"])
            pygame.draw.rect(screen, GREEN, pipe["bottom"])

    def remove_offscreen_pipes(self):
        self.pipes = [pipe for pipe in self.pipes if pipe["top"].x + self.width > 0]

# Game class
class Game:
    def __init__(self):
        self.bird = Bird()
        self.pipe = Pipe()
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.flap()

            # Update game objects
            self.bird.update()
            self.pipe.move_pipes()
            self.pipe.remove_offscreen_pipes()

            # Create new pipes at a consistent distance
            self.pipe.create_pipe()

            # Check for collisions
            for pipe in self.pipe.pipes:
                if self.bird.x + self.bird.width > pipe["top"].x and self.bird.x < pipe["top"].x + self.pipe.width:
                    if self.bird.y < pipe["top"].height or self.bird.y + self.bird.height > pipe["bottom"].y:
                        self.game_over()
                        return

                # Check if bird has passed the pipe
                if not pipe["scored"] and self.bird.x > pipe["top"].x + self.pipe.width:
                    pipe["scored"] = True
                    self.score += 1

            # Draw everything
            screen.fill(WHITE)
            self.bird.draw()
            self.pipe.draw_pipes()

            # Display score
            score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
            screen.blit(score_text, (10, 10))

            pygame.display.flip()
            clock.tick(30)

    def game_over(self):
        print("Game Over! Final Score:", self.score)
        pygame.quit()
        sys.exit()

# Main function
if __name__ == "__main__":
    game = Game()
    game.run()