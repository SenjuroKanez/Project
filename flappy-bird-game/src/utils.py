def load_image(file_path):
    # Function to load an image from the specified file path
    # This is a placeholder for actual image loading logic
    pass

def draw_text(text, position, font_size=20):
    # Function to draw text on the screen at the specified position
    # This is a placeholder for actual text drawing logic
    pass

def check_collision(rect1, rect2):
    # Function to check if two rectangles collide
    return (rect1[0] < rect2[0] + rect2[2] and
            rect1[0] + rect1[2] > rect2[0] and
            rect1[1] < rect2[1] + rect2[3] and
            rect1[1] + rect1[3] > rect2[1])