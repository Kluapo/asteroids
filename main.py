import pygame
import os
import sys
import pygame.sprite
from constants import SCREEN_WIDTH, SCREEN_HEIGHT  # or whatever constants you need
from circle_shape import CircleShape
from player import Player

# Set display before importing pygame
os.environ['DISPLAY'] = ':0'
os.environ['LIBGL_ALWAYS_INDIRECT'] = '1'
# Add these lines
os.environ['SDL_VIDEODRIVER'] = 'x11'

<<<<<<< Updated upstream
print(f"Display settings: {os.environ.get('DISPLAY')}")
print(f"Video driver: {os.environ.get('SDL_VIDEODRIVER')}")

def main():
    print("Initializing pygame...")
    my_clock = pygame.time.Clock()
=======
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

>>>>>>> Stashed changes
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    new_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    updateable.add(new_player)
    drawable.add(new_player)
    print("Updateable group:", list(updateable))
    print("Drawable group:", list(drawable))

    try:
        pygame.init()
        print("Pygame initialized successfully!")
        
        print("Current video driver:", pygame.display.get_driver())
        
        print("Attempting to create window...")
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        print("Window created successfully!")
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Quit event received")
                    pygame.quit()
                    return
        
            screen.fill("black")
            dt = (my_clock.tick(60))/1000
            updateable.update(dt)
            drawable.draw(screen)
            pygame.display.flip()
            
            

            
    except pygame.error as e:
        print(f"Pygame error occurred: {e}")
    except Exception as e:
        print(f"Other error occurred: {e}")
        print("Error type:", type(e))
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()