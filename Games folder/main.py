import pygame
import sys
from games import snake, pong, space

def init_menu():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Game Hub")
    font = pygame.font.SysFont("Arial", 40)
    return screen, font

def main():
    screen, FONT = init_menu()
    clock = pygame.time.Clock()

    while True:
        screen.fill((30, 30, 30))
        buttons = []
        labels = ["Play Snake", "Play Pong", "Play Space Invaders", "Quit"]
        functions = [snake.run, pong.run, space.run, sys.exit]

        for i, label in enumerate(labels):
            text = FONT.render(label, True, (255, 255, 255))
            rect = text.get_rect(center=(600 // 2, 100 + i * 60))
            screen.blit(text, rect)
            buttons.append({"rect": rect, "function": functions[i]})

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button["rect"].collidepoint(event.pos):
                        pygame.quit()  # Clean exit before switching games
                        button["function"]()
                        return main()  # Restart menu after game ends

        clock.tick(60)

if __name__ == "__main__":
    main()
