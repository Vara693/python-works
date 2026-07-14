"""
game_runner.py

Controls running a single user session with multiple mini-games, collects mouse events
and saves them to CSV via logger.py.

Workflow:
- Called from main.py as run_session(user, session_id).
- Runs 3–4 short pygame mini-games sequentially.
- Uses MouseLogger to track mouse movements, clicks, and timing.
- Saves events in data/{user}/session{session_id}_{game}.csv.

Dependencies: pygame
Install with: pip install pygame
"""

import pygame
import time
import random
from logger import MouseLogger

# ------------- Base Game Class -------------

class BaseGame:
    def __init__(self, name, duration_sec=60):
        self.name = name
        self.duration = duration_sec

    def run(self, screen, clock, session_id, user_id, logger):
        """Each game must implement its own run loop."""
        raise NotImplementedError


# ------------- Mini-Games -------------

class ClickCirclesGame(BaseGame):
    def __init__(self, duration_sec=60):
        super().__init__('ClickCircles', duration_sec)

    def run(self, screen, clock, session_id, user_id, logger):
        start = time.time()
        circles = []
        while time.time() - start < self.duration:
            screen.fill((240, 240, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                logger.log_event(event)   # <-- log with MouseLogger
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    for c in circles[:]:
                        if (x - c[0]) ** 2 + (y - c[1]) ** 2 < 30 ** 2:
                            circles.remove(c)

            if len(circles) < 5 and random.random() < 0.05:
                circles.append((random.randint(50, 750), random.randint(50, 550)))
            for c in circles:
                pygame.draw.circle(screen, (200, 50, 50), c, 30, 0)

            pygame.display.flip()
            clock.tick(60)


class FollowTargetGame(BaseGame):
    def __init__(self, duration_sec=60):
        super().__init__('FollowTarget', duration_sec)

    def run(self, screen, clock, session_id, user_id, logger):
        start = time.time()
        target = [400, 300]
        while time.time() - start < self.duration:
            screen.fill((250, 255, 240))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                logger.log_event(event)

            # move target slowly
            target[0] += random.choice([-3, -2, -1, 0, 1, 2, 3])
            target[1] += random.choice([-3, -2, -1, 0, 1, 2, 3])
            target[0] = max(30, min(770, target[0]))
            target[1] = max(30, min(570, target[1]))

            pygame.draw.circle(screen, (50, 100, 200), target, 25)
            pygame.display.flip()
            clock.tick(60)


class MazeGame(BaseGame):
    def __init__(self, duration_sec=60):
        super().__init__('Maze', duration_sec)

    def run(self, screen, clock, session_id, user_id, logger):
        start = time.time()
        walls = [(200, 0, 20, 500), (400, 100, 20, 500), (600, 0, 20, 500)]
        while time.time() - start < self.duration:
            screen.fill((255, 250, 240))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                logger.log_event(event)

            for w in walls:
                pygame.draw.rect(screen, (0, 0, 0), w)

            pygame.display.flip()
            clock.tick(60)


# ------------- Game Runner -------------

def run_session(user_id, session_id):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption(f"Session {session_id} — User {user_id}")
    clock = pygame.time.Clock()

    # Game sequence
    GAMES = [
        ClickCirclesGame(duration_sec=30),
        FollowTargetGame(duration_sec=30),
        MazeGame(duration_sec=30)
    ]

    for game in GAMES:
        # Create logger for each game
        logger = MouseLogger(user_id, session_id, game.name)
        game.run(screen, clock, session_id, user_id, logger)
        logger.stop()

        # Break screen
        screen.fill((230, 230, 230))
        font = pygame.font.SysFont(None, 36)
        txt = font.render(f"Next game: {game.name}", True, (0, 0, 0))
        screen.blit(txt, (250, 280))
        pygame.display.flip()
        pygame.time.wait(2000)

    pygame.quit()
