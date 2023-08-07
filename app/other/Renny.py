import pygame
import sys

pygame.init()

# Constants for the display window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
BG_COLOR = (255, 255, 255)  # White
SMILING_FACE_COLOR = (255, 255, 0)  # Yellow
FACE_RADIUS = 100
EYE_RADIUS = 15
MOUTH_WIDTH = 70
MOUTH_HEIGHT = 30
TEXT_COLOR = (0, 0, 0)  # Black

# Function to draw a smiling face
def draw_smiling_face(surface, x, y):
    pygame.draw.circle(surface, SMILING_FACE_COLOR, (x, y), FACE_RADIUS)
    pygame.draw.circle(surface, TEXT_COLOR, (x - FACE_RADIUS // 3, y - FACE_RADIUS // 3), EYE_RADIUS)
    pygame.draw.circle(surface, TEXT_COLOR, (x + FACE_RADIUS // 3, y - FACE_RADIUS // 3), EYE_RADIUS)
    pygame.draw.arc(surface, TEXT_COLOR, (x - MOUTH_WIDTH // 2, y, MOUTH_WIDTH, MOUTH_HEIGHT), 2.9, -0.1)

# Main function
def main():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Smiling Face with Text Input")

    text_input = ""
    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("Input Text:", text_input)
                    text_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                else:
                    text_input += event.unicode

        screen.fill(BG_COLOR)
        draw_smiling_face(screen, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        # Render text input on the screen
        text_surface = font.render(text_input, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50))
        screen.blit(text_surface, text_rect)

        pygame.display.flip()

if __name__ == "__main__":
    main()
