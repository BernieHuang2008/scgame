import pygame

def main():
    # Initialize pygame
    pygame.init()
    pygame.display.set_caption("My Game")

    # Set up the display
    screen = pygame.display.set_mode((800, 600))

    # Load the sprite image
    sprite_image = pygame.image.load("test/src/e6ddc55a6ddd9cc9d84fe0b4c21e016f.svg")

    # Create a sprite object
    sprite = pygame.sprite.Sprite()

    # Set the sprite's image
    sprite.image = sprite_image

    # Set the sprite's position
    sprite.rect = sprite.image.get_rect()
    sprite.rect.center = (400, 300)

    # Create a sprite group
    all_sprites = pygame.sprite.Group()
    all_sprites.add(sprite)

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill((225, 225, 225))

        # Draw the sprites on the screen
        all_sprites.draw(screen)

        # Update the display
        pygame.display.flip()

    # Quit the game
    pygame.quit()

if __name__ == "__main__":
    main()