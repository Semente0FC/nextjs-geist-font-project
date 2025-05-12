import cv2
import numpy as np
import mss
import time
from loguru import logger
import pygetwindow as gw

class ScreenCapture:
    def __init__(self, target_fps=60):
        self.sct = mss.mss()
        self.target_fps = target_fps
        self.frame_time = 1.0 / target_fps
        self.last_time = time.time()
        self.capture_region = None

    def find_fullscreen_window(self):
        windows = gw.getAllWindows()
        for w in windows:
            if w.isVisible and w.width == w.screen.width and w.height == w.screen.height:
                logger.info(f"Found fullscreen window: {w.title}")
                return w
        logger.warning("No fullscreen window found")
        return None

    def update_capture_region(self):
        window = self.find_fullscreen_window()
        if window:
            self.capture_region = {
                "top": window.top,
                "left": window.left,
                "width": window.width,
                "height": window.height
            }
        else:
            # Fallback to primary monitor
            self.capture_region = self.sct.monitors[1]

    def grab_frame(self):
        if self.capture_region is None:
            self.update_capture_region()
        img = np.array(self.sct.grab(self.capture_region))
        # Convert BGRA to BGR
        frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        return frame

    def start_capture(self, frame_callback):
        logger.info("Starting screen capture")
        while True:
            start_time = time.time()
            frame = self.grab_frame()
            frame_callback(frame)
            elapsed = time.time() - start_time
            sleep_time = self.frame_time - elapsed
            if sleep_time > 0:
                time.sleep(sleep_time)
