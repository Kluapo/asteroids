import pygame
import os
import sys
from constants import *

# Set display before importing pygame
os.environ['DISPLAY'] = ':0'
os.environ['LIBGL_ALWAYS_INDIRECT'] = '1'
# Add these lines
os.environ['SDL_VIDEODRIVER'] = 'x11'

print(f"Display settings: {os.environ.get('DISPLAY')}")
print(f"Video driver: {os.environ.get('SDL_VIDEODRIVER')}")

def main():
    print("Initializing pygame...")
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