# logger.py
import csv
import os
import time
from datetime import datetime
import pygame

DATA_DIR = "data"

class MouseLogger:
    def __init__(self, username: str, session_id: int, game_name: str):
        self.username = username
        self.session_id = session_id
        self.game_name = game_name

        # File path: data/{username}/session_{id}_{game}.csv
        user_dir = os.path.join(DATA_DIR, username)
        os.makedirs(user_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.file_path = os.path.join(
            user_dir, f"session{session_id}_{game_name}_{timestamp}.csv"
        )

        self.file = open(self.file_path, mode="w", newline="")
        self.writer = csv.writer(self.file)

        # CSV header
        self.writer.writerow([
            "timestamp", "event_type", "x", "y",
            "button", "duration_since_last"
        ])

        self.last_time = time.time()

    def log_event(self, event: pygame.event.Event):
        """Log mouse motion and clicks from pygame events."""
        now = time.time()
        delta = now - self.last_time
        self.last_time = now

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            self.writer.writerow([now, "motion", x, y, None, delta])

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            self.writer.writerow([now, "button_down", x, y, event.button, delta])

        elif event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            self.writer.writerow([now, "button_up", x, y, event.button, delta])

    def stop(self):
        """Close CSV file after session ends."""
        self.file.close()
        print(f"[INFO] Mouse log saved: {self.file_path}")
