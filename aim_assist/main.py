import sys
import threading
from PySide6.QtWidgets import QApplication
from core.capture import ScreenCapture
from core.detector import EnemyDetector
from core.aimer import Aimer
from core.gpu_monitor import GPUMonitor
from core.config import Config
from core.logger import setup_logger
from gui.main_window import MainWindow
from queue import Queue
from loguru import logger

def main():
    logger = setup_logger()
    config = Config()
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    frame_queue = Queue(maxsize=5)
    detection_queue = Queue(maxsize=5)

    capture = ScreenCapture(target_fps=60)
    detector = EnemyDetector(model_path="models/yolov8.onnx")
    aimer = Aimer(sensitivity=config.get("sensitivity"), smoothing=config.get("smoothing"))
    gpu_monitor = GPUMonitor()

    def capture_thread():
        def on_frame(frame):
            if not frame_queue.full():
                frame_queue.put(frame)
        capture.start_capture(on_frame)

    def detection_thread():
        while True:
            frame = frame_queue.get()
            detections = detector.detect(frame)
            if not detection_queue.full():
                detection_queue.put(detections)

    def aim_thread():
        while True:
            detections = detection_queue.get()
            # Placeholder: calculate aim and move mouse
            # For now, just log detections
            logger.info(f"Detections: {detections}")

    threading.Thread(target=capture_thread, daemon=True).start()
    threading.Thread(target=detection_thread, daemon=True).start()
    threading.Thread(target=aim_thread, daemon=True).start()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
