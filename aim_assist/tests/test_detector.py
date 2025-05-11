import unittest
import cv2
from core.detector import EnemyDetector

class TestEnemyDetector(unittest.TestCase):
    def setUp(self):
        self.detector = EnemyDetector(model_path="../models/yolov8.onnx")

    def test_detect_no_frame(self):
        frame = None
        with self.assertRaises(Exception):
            self.detector.detect(frame)

    def test_detect_dummy_frame(self):
        frame = cv2.imread("test_image.jpg")
        if frame is None:
            self.skipTest("Test image not found")
        detections = self.detector.detect(frame)
        self.assertIsInstance(detections, list)

if __name__ == "__main__":
    unittest.main()
