import cv2
import os
from loguru import logger

class DataCollector:
    def __init__(self, save_dir="collected_data"):
        self.save_dir = save_dir
        os.makedirs(self.save_dir, exist_ok=True)
        self.count = 0

    def save_frame(self, frame, label="unknown"):
        filename = f"{self.save_dir}/{label}_{self.count:06d}.jpg"
        cv2.imwrite(filename, frame)
        logger.info(f"Saved frame {filename}")
        self.count += 1

    def collect_from_video(self, video_path, label="unknown", frame_skip=30):
        cap = cv2.VideoCapture(video_path)
        frame_id = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            if frame_id % frame_skip == 0:
                self.save_frame(frame, label)
            frame_id += 1
        cap.release()
