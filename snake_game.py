"""Jeu Snake pédagogique avec pygame.

Lancez le jeu avec :
    python snake_game.py
"""

import random
import sys

import pygame

# -----------------------------
# Configuration générale
# -----------------------------
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELL_SIZE = 20  # Taille d'une case de la grille

# La fenêtre est une grille : toutes les positions sont des multiples de CELL_SIZE
GRID_WIDTH = WINDOW_WIDTH // CELL_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // CELL_SIZE

FPS = 10  # Vitesse du serpent (images / déplacements par seconde)

# Couleurs (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (220, 30, 30)


# Directions possibles (déplacement en cases)
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


def random_food_position(snake):
    """Retourne une position aléatoire qui n'est pas sur le serpent."""
    while True:
        position = (random.randrange(GRID_WIDTH), random.randrange(GRID_HEIGHT))
        if position not in snake:
            return position


def draw_cell(screen, color, position):
    """Dessine une case de la grille à la position donnée."""
    x, y = position
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect)


def draw_text(screen, text, font, color, x, y):
    """Affiche du texte à l'écran."""
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


def reset_game():
    """Initialise / réinitialise toutes les données d'une partie.

    Retourne :
        snake (list[tuple[int, int]]): positions des segments
        direction (tuple[int, int]): direction actuelle
        food (tuple[int, int]): position de la nourriture
        score (int): score du joueur
    """
    # Le serpent démarre avec 3 segments au centre de l'écran
    center_x = GRID_WIDTH // 2
    center_y = GRID_HEIGHT // 2
    snake = [(center_x, center_y), (center_x - 1, center_y), (center_x - 2, center_y)]

    direction = RIGHT
    food = random_food_position(snake)
    score = 0
    return snake, direction, food, score


def handle_direction_change(current_direction, event_key):
    """Calcule la nouvelle direction après un appui sur une flèche.

    Empêche les demi-tours instantanés (ex: RIGHT -> LEFT), car cela
    provoquerait une collision immédiate sur le corps.
    """
    new_direction = current_direction

    if event_key == pygame.K_UP and current_direction != DOWN:
        new_direction = UP
    elif event_key == pygame.K_DOWN and current_direction != UP:
        new_direction = DOWN
    elif event_key == pygame.K_LEFT and current_direction != RIGHT:
        new_direction = LEFT
    elif event_key == pygame.K_RIGHT and current_direction != LEFT:
        new_direction = RIGHT

    return new_direction


def move_snake(snake, direction, food):
    """Fait avancer le serpent et gère la nourriture.

    Retourne :
        snake (list[tuple[int, int]]): nouveau serpent
        ate_food (bool): True si nourriture mangée
    """
    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = (head_x + dx, head_y + dy)

    new_snake = [new_head] + snake

    if new_head == food:
        # Le serpent grandit : on garde toute la liste
        ate_food = True
    else:
        # Déplacement normal : on retire la queue
        new_snake.pop()
        ate_food = False

    return new_snake, ate_food


def is_collision(snake):
    """Détecte si la tête touche un mur ou le corps du serpent."""
    head_x, head_y = snake[0]

    # Collision mur
    if head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT:
        return True

    # Collision corps
    if snake[0] in snake[1:]:
        return True

    return False


def draw_game(screen, font, snake, food, score):
    """Dessine l'état courant de la partie."""
    screen.fill(BLACK)

    # Dessin du serpent
    for segment in snake:
        draw_cell(screen, GREEN, segment)

    # Dessin de la nourriture
    draw_cell(screen, RED, food)

    # Affichage du score
    draw_text(screen, f"Score : {score}", font, WHITE, 10, 10)

    pygame.display.flip()


def game_over_screen(screen, font, big_font, score):
    """Affiche l'écran de fin et attend une décision du joueur.

    Retourne :
        True  -> relancer une partie
        False -> quitter le jeu
    """
    screen.fill(BLACK)

    title = big_font.render("GAME OVER", True, RED)
    score_text = font.render(f"Score final : {score}", True, WHITE)
    hint_text = font.render("Appuyez sur R pour rejouer ou Echap pour quitter", True, WHITE)

    screen.blit(title, title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 40)))
    screen.blit(score_text, score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 10)))
    screen.blit(hint_text, hint_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50)))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                if event.key == pygame.K_ESCAPE:
                    return False


def run_game():
    """Point d'entrée principal du jeu Snake."""
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake - Version pédagogique")

    font = pygame.font.SysFont("arial", 24)
    big_font = pygame.font.SysFont("arial", 44, bold=True)
    clock = pygame.time.Clock()

    running = True

    while running:
        snake, direction, food, score = reset_game()
        game_active = True

        # Boucle d'une partie
        while game_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    direction = handle_direction_change(direction, event.key)

            snake, ate_food = move_snake(snake, direction, food)

            if ate_food:
                score += 1
                food = random_food_position(snake)

            if is_collision(snake):
                game_active = False

            draw_game(screen, font, snake, food, score)
            clock.tick(FPS)

        # Fin de partie : proposer de rejouer
        running = game_over_screen(screen, font, big_font, score)

    pygame.quit()


if __name__ == "__main__":
    run_game()
