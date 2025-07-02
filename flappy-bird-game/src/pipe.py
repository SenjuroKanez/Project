class Pipe:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, turtle):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.setheading(90)  # Point upwards
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)  # Reset heading

    def update(self, speed):
        self.x -= speed

    def is_collision(self, bird):
        if (self.x < bird.x < self.x + self.width) and (bird.y < self.y + self.height):
            return True
        return False

    @staticmethod
    def generate_pipes(screen_width, gap_size):
        import random
        height = random.randint(50, 300)
        return Pipe(screen_width, height, 50, screen_height - height - gap_size)