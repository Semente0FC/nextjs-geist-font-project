import time
from core.capture import ScreenCapture
from core.detector import EnemyDetector

def benchmark_capture(fps_target=60, duration=10):
    capture = ScreenCapture(target_fps=fps_target)
    frame_count = 0
    start_time = time.time()

    def on_frame(frame):
        nonlocal frame_count
        frame_count += 1

    import threading
    t = threading.Thread(target=capture.start_capture, args=(on_frame,), daemon=True)
    t.start()

    time.sleep(duration)
    elapsed = time.time() - start_time
    print(f"Captured {frame_count} frames in {elapsed:.2f} seconds. FPS: {frame_count/elapsed:.2f}")

def benchmark_detection(model_path="../models/yolov8.onnx", duration=10):
    detector = EnemyDetector(model_path=model_path)
    import cv2
    frame = cv2.imread("test_image.jpg")
    if frame is None:
        print("Test image not found, skipping detection benchmark.")
        return
    start_time = time.time()
    count = 0
    while time.time() - start_time < duration:
        detector.detect(frame)
        count += 1
    elapsed = time.time() - start_time
    print(f"Ran {count} detections in {elapsed:.2f} seconds. FPS: {count/elapsed:.2f}")

if __name__ == "__main__":
    benchmark_capture()
    benchmark_detection()
