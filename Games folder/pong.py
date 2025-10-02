import pygame

def run():
    pygame.init()
    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    paddle_width, paddle_height = 10, 60
    ball_size = 15

    player_y = HEIGHT // 2 - paddle_height // 2
    ai_y = HEIGHT // 2 - paddle_height // 2
    ball_x, ball_y = WIDTH // 2, HEIGHT // 2
    ball_speed = [4.5, 4.5]

    def draw():
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (20, player_y, paddle_width, paddle_height))
        pygame.draw.rect(screen, (255, 255, 255), (WIDTH - 30, ai_y, paddle_width, paddle_height))
        pygame.draw.ellipse(screen, (255, 255, 255), (ball_x, ball_y, ball_size, ball_size))
        pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_y -= 5
        if keys[pygame.K_DOWN]:
            player_y += 5

        # Move ball
        ball_x += ball_speed[0]
        ball_y += ball_speed[1]

        # Ball collision with top/bottom
        if ball_y <= 0 or ball_y >= HEIGHT - ball_size:
            ball_speed[1] = -ball_speed[1]

        # Ball collision with paddles
        if (20 < ball_x < 30 and player_y < ball_y < player_y + paddle_height) or \
           (WIDTH - 40 < ball_x < WIDTH - 30 and ai_y < ball_y < ai_y + paddle_height):
            ball_speed[0] = -ball_speed[0]

        # Simple AI movement
        if ai_y + paddle_height / 2 < ball_y:
            ai_y += 4
        elif ai_y + paddle_height / 2 > ball_y:
            ai_y -= 4

        # Reset ball if it goes off screen
        if ball_x < 0 or ball_x > WIDTH:
            ball_x, ball_y = WIDTH // 2, HEIGHT // 2

        draw()
        clock.tick(60)

    pygame.quit()

# ✅ This tells Python to actually start the game
if __name__ == "__main__":
    run()