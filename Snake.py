import pygame
import sys

pygame.init()  # Inicijalizacija pygame biblioteke

window_size = (800, 800)  # Dinamično namjestimo veličinu ekrana igre
screen = pygame.display.set_mode(window_size)  # Inicijalizacija ekrana
pygame.display.set_caption("SNAKE")  # Naziv igre

numberOfCells = 20  # Dinamično namjestimo broj redaka i stupaca

cell_size = window_size[
                0] // numberOfCells  # Kalkuliramo veličinu jedne čelije po veličini ekrana / broj čelija na ekranu
grid_color = (200, 200, 200)  # RGB siva boja
snake_color = (0, 200, 0)  # RGB zelena boja

snake = []  # Snake ce reprezentirati lista čelija koje snake zauzima
prvaPozicija = (numberOfCells / 2, numberOfCells / 2)  # Prvobitna vrijednost će biti na sredini
snake.append(prvaPozicija)  # dodajemo u listu "glavu"
snake.append((numberOfCells / 2 + 1, numberOfCells / 2))  # dodajemo u listu rep
snake.append((numberOfCells / 2 + 2, numberOfCells / 2))
snake.append((numberOfCells / 2 + 3, numberOfCells / 2))

#  direkcije (x, y)
gore = {'x': 0, 'y': -1}
dolje = {'x': 0, 'y': 1}
lijevo = {'x': -1, 'y': 0}
desno = {'x': 1, 'y': 0}

snakeDirection = lijevo


def drawGrid():
    # Crtamo vertikalne linije
    for x in range(cell_size, window_size[0] - 1, cell_size):
        pygame.draw.line(screen, grid_color, (x, 0), (x, window_size[1]))

    # Crtamo horizontalne linije
    for y in range(cell_size, window_size[1] - 1, cell_size):
        pygame.draw.line(screen, grid_color, (0, y), (window_size[0], y))


def drawSnake():
    for cell in snake:
        x, y = cell
        pygame.draw.rect(screen, snake_color, (x * cell_size + 1, y * cell_size + 1, cell_size - 2, cell_size - 2))
        #  početni x, početni y, width, height


def draw():
    screen.fill((0, 0, 0))  # Prebojamo cijeli ekran crnom bojom (reset)

    drawGrid()

    drawSnake()

    # S novo nacrtanim elementima, ažuriramo ekran
    pygame.display.flip()


def moveSnake():
    head = snake[0]
    new_head = ((head[0] + snakeDirection['x']) % numberOfCells,
                (head[1] + snakeDirection['y']) % numberOfCells)  # Novu glavu zapišemo kao prijašnju plus direkcija

    snake.insert(0, new_head)  # Ubacimo novu glavu na početak liste, time pomičemo cijelu listu za jedan u iza

    snake.pop()  # Zadnja čelija (rep) zmije "nestane"


while True:

    pygame.time.Clock().tick(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # osposobit X gumb za zatvoriti igricu
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # Provjeravamo ako je bilo koji gumb na tipkownici stisnut
            if event.key == pygame.K_UP:  # Postavljamo smjer zmije ovisno o stisnutom gumbu
                snakeDirection = gore
            elif event.key == pygame.K_DOWN:
                snakeDirection = dolje
            elif event.key == pygame.K_LEFT:
                snakeDirection = lijevo
            elif event.key == pygame.K_RIGHT:
                snakeDirection = desno

    moveSnake()
    draw()