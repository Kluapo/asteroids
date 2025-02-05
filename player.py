import pygame
from constants import *
from circle_shape import CircleShape

class Player(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        pygame.sprite.Sprite.__init__(self)
        
        # Create a surface twice the size of the radius to fit the triangle
        size = PLAYER_RADIUS * 2
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)  # SRCALPHA allows transparency
        self.rect = self.image.get_rect(center=(x, y))
        self.rotation = 0
        
        # Draw initial triangle on self.image
        self.draw_triangle()

    def draw_triangle(self):
        # Clear the previous image
        self.image.fill((0,0,0,0))  # Transparent
        
        # Calculate triangle points similar to your original method
        # But adjust the points to be relative to the surface center
        center = pygame.Vector2(self.image.get_width()/2, self.image.get_height()/2)
        forward = pygame.Vector2(0, -1).rotate(-self.rotation)  # Note: negative rotation
        right = pygame.Vector2(0, -1).rotate(-self.rotation + 90) * self.radius / 1.5
        
        a = center + forward * self.radius
        b = center - forward * self.radius - right
        c = center - forward * self.radius + right
        
        # Draw on self.image
        pygame.draw.polygon(
            self.image,
            "white",
            [a, b, c],
            2
        )

    def draw(self, screen):
        pygame.draw.polygon(
            self.image,
            "white",
        [  # You'll need to adjust these points to be relative to the surface
            (PLAYER_RADIUS, 0),  # top
            (0, PLAYER_RADIUS * 2),  # bottom left
            (PLAYER_RADIUS * 2, PLAYER_RADIUS * 2)  # bottom right
    ],
    2
)
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
        self.draw_triangle()  # Add this line to update the visual 
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
<<<<<<< Updated upstream
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        
        self.rect.center = self.position
            
=======
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED



    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

>>>>>>> Stashed changes
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    