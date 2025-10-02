import pygame
import random

def run():
    pygame.init()
    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 40, 50, 10)
    bullets = []
    enemies = [pygame.Rect(x * 60 + 40, 40, 40, 20) for x in range(8)]

    def draw():
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 255, 0), player)
        for bullet in bullets:
            pygame.draw.rect(screen, (255, 255, 0), bullet)
        for enemy in enemies:
            pygame.draw.rect(screen, (255, 0, 0), enemy)
        pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.move_ip(-5, 0)
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.move_ip(5, 0)
        if keys[pygame.K_SPACE] and len(bullets) < 5:
            bullets.append(pygame.Rect(player.centerx - 2, player.top - 10, 4, 10))

        # Move bullets
        for bullet in bullets[:]:
            bullet.move_ip(0, -8)
            if bullet.bottom < 0:
                bullets.remove(bullet)

        # Check for collisions
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.colliderect(enemy):
                    enemies.remove(enemy)
                    bullets.remove(bullet)
                    break

        draw()
        clock.tick(60)

    pygame.quit()
    
if __name__ == "__main__":
    run()