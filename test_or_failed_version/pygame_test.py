# Simple pygame program

# Import and initialize the pygame library
import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

player = Player()
# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
                running = False

    # Fill the background with white
    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)

    screen.fill((0,0,0))
    surf = pygame.Surface((50, 50))
    surf.fill((0, 0, 0))
    rect = surf.get_rect()
    surf_center = (
        (SCREEN_WIDTH - surf.get_width()) / 2,
        (SCREEN_HEIGHT - surf.get_height()) / 2
    )

    # Draw surf at the new coordinates
    (screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)))
    # screen.blit(player.surf, player.rect)
    pygame.display.flip()
    # Draw a solid blue circle in the center
    # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    #
    # pygame.draw.rect(screen,(0, 0, 255),[50,50,50,50])
    # pygame.draw.rect(screen,(0, 0, 255),[50,50,50,50])
    # pygame.draw.rect(screen,(0, 0, 255),[0,200,50,200])
    # # Flip the display
    # pygame.display.flip()

# Done! Time to quit.
pygame.quit()