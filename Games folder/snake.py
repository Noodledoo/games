import pygame
import random

def run():
    pygame.init()
    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    block_size = 20
    snake = [(100, 100)]
    direction = (block_size, 0)
    food = (random.randint(0, (WIDTH - block_size) // block_size) * block_size,
            random.randint(0, (HEIGHT - block_size) // block_size) * block_size)

    def draw_snake():
        for segment in snake:
            pygame.draw.rect(screen, (0, 255, 0), (*segment, block_size, block_size))

    def draw_food():
        pygame.draw.rect(screen, (255, 0, 0), (*food, block_size, block_size))

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, block_size):
                    direction = (0, -block_size)
                elif event.key == pygame.K_DOWN and direction != (0, -block_size):
                    direction = (0, block_size)
                elif event.key == pygame.K_LEFT and direction != (block_size, 0):
                    direction = (-block_size, 0)
                elif event.key == pygame.K_RIGHT and direction != (-block_size, 0):
                    direction = (block_size, 0)

        if not running:
            break

        # Move snake
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, new_head)

        # Check collision
        if new_head == food:
            food = (random.randint(0, (WIDTH - block_size) // block_size) * block_size,
                    random.randint(0, (HEIGHT - block_size) // block_size) * block_size)
        else:
            snake.pop()

        if (new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in snake[1:]):
            running = False

        draw_snake()
        draw_food()
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    
if __name__ == "__main__":
    run()