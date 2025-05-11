import cv2
import numpy as np
import mss
import time
from loguru import logger

class ScreenCapture:
    def __init__(self, monitor_number=1, target_fps=60):
        self.sct = mss.mss()
        self.monitor = self.sct.monitors[monitor_number]
        self.target_fps = target_fps
        self.frame_time = 1.0 / target_fps
        self.last_time = time.time()

    def grab_frame(self):
        img = np.array(self.sct.grab(self.monitor))
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
