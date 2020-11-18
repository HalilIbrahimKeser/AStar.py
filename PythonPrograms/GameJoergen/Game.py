import random
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 100, 0)
RED = (255, 0, 0)


class Block(pygame.sprite.Sprite):
    """ This class represents the block. """

    def __init__(self, dude):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = dude
        self.rect = self.image.get_rect()


class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([4, 10])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3


class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(RED)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y


# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

IMAGE = pygame.image.load('are.png').convert()
IMAGE2 = pygame.image.load('asbjorn.png').convert()
IMAGE3 = pygame.image.load('halil.png').convert()

# Set the title of the window
pygame.display.set_caption("Kill em' up")

# Create the player object
player = Player(50, 50)
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)
bullet_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()

for i in range(3):
    block = Block(IMAGE)

    block.rect.x = random.randrange(800)
    block.rect.y = random.randrange(500)

    block_list.add(block)
    all_sprites_list.add(block)

for i in range(3):
    block = Block(IMAGE2)

    block.rect.x = random.randrange(800)
    block.rect.y = random.randrange(500)

    block_list.add(block)
    all_sprites_list.add(block)

for i in range(3):
    block = Block(IMAGE3)

    block.rect.x = random.randrange(800)
    block.rect.y = random.randrange(500)

    block_list.add(block)
    all_sprites_list.add(block)

clock = pygame.time.Clock()
done = False
player.rect.x = 400
player.rect.y = 550

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
            elif event.key == pygame.K_SPACE:
                bullet = Bullet()
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

    # --- Game logic

    # This calls update on all the sprites
    all_sprites_list.update()

    # Calculate mechanics for each bullet
    for bullet in bullet_list:
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    # -- Draw everything
    # Clear screen
    screen.fill(BLACK)

    # Draw sprites
    all_sprites_list.draw(screen)

    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(60)

pygame.quit()