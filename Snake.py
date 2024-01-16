import pygame
import sys

pygame.init()  # Inicijalizacija pygame biblioteke

window_size = (600, 600)  # Dinamično namjestimo veličinu ekrana igre
screen = pygame.display.set_mode(window_size)  # Inicijalizacija ekrana
pygame.display.set_caption("SNAKE")   # Naziv igre

numberOfCells = 20  # Dinamično namjestimo broj redaka i stupaca

cell_size = window_size[0] // numberOfCells  # Kalkuliramo veličinu jedne čelije po veličini ekrana / broj čelija na ekranu
grid_color = (200, 200, 200)  # RGB siva boja


def drawGrid():
    # Crtamo vertikalne linije
    for x in range(cell_size, window_size[0] - 1, cell_size):
        pygame.draw.line(screen, grid_color, (x, 0), (x, window_size[1]))

    # Crtamo horizontalne linije
    for y in range(cell_size, window_size[1] - 1, cell_size):
        pygame.draw.line(screen, grid_color, (0, y), (window_size[0], y))


def draw():
    screen.fill((0, 0, 0))  # Prebojamo cijeli ekran crnom bojom (reset)

    drawGrid()

    # S novo nacrtanim elementima, ažuriramo ekran
    pygame.display.flip()


# Main game loop
while True:

    # Control the frame rate
    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw()