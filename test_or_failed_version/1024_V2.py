import pygame
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Pixel(pygame.sprite.Sprite):

    def __init__(self,position):
        super(Pixel, self).__init__()
        self.surf = pygame.Surface((75, 75)) #size of the Pixel
        self.surf.fill((255, 255, 255))  # color of the Pixel
        self.rect = self.surf.get_rect(center=position)  # get the position of the Pixel?

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


a = Pixel((100,100))
b = Pixel((300,300))


# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
pixels = pygame.sprite.Group()
pixels.add(a)
pixels.add(b)
all_sprites = pygame.sprite.Group()

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    a.update(pressed_keys)
    pixels.update(pressed_keys)
    # Fill the screen with black
    screen.fill((0, 0, 0))



    # Draw all sprites
    for entity in pixels:
        screen.blit(entity.surf, entity.rect)
    # screen.blit(a.surf, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))


    # Update the display
    pygame.display.flip()