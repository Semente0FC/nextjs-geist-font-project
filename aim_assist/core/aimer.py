import time
import math
from pynput.mouse import Controller
from loguru import logger

class Aimer:
    def __init__(self, sensitivity=1.0, smoothing=0.5):
        self.mouse = Controller()
        self.sensitivity = sensitivity
        self.smoothing = smoothing
        self.last_move_time = time.time()

    def calculate_delta(self, current_pos, target_pos):
        dx = target_pos[0] - current_pos[0]
        dy = target_pos[1] - current_pos[1]
        return dx, dy

    def smooth_move(self, dx, dy):
        # Apply smoothing factor
        smoothed_dx = dx * self.smoothing * self.sensitivity
        smoothed_dy = dy * self.smoothing * self.sensitivity
        return smoothed_dx, smoothed_dy

    def move_mouse(self, dx, dy):
        self.mouse.move(int(dx), int(dy))
        logger.debug(f"Moved mouse by dx={dx}, dy={dy}")

    def aim_at(self, current_pos, target_pos):
        dx, dy = self.calculate_delta(current_pos, target_pos)
        smoothed_dx, smoothed_dy = self.smooth_move(dx, dy)
        self.move_mouse(smoothed_dx, smoothed_dy)
