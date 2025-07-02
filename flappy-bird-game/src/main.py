# filepath: /flappy-bird-game/flappy-bird-game/src/main.py

import turtle
from bird import Bird
from pipe import Pipe
from game import Game

def main():
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Flappy Bird")
    screen.bgcolor("skyblue")
    screen.setup(width=400, height=600)
    screen.tracer(0)  # Turns off the screen updates

    # Create game objects
    bird = Bird(x=0, y=0)  # Provide initial x and y positions for the bird
    pipes = Pipe()
    game = Game(bird, pipes)

    # Main game loop
    while True:
        screen.update()
        game.update()
        turtle.delay(20)  # Control the frame rate

    screen.mainloop()

if __name__ == "__main__":
    main()