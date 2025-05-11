import onnxruntime as ort
import numpy as np
import cv2
from loguru import logger

class EnemyDetector:
    def __init__(self, model_path: str, use_tensorrt: bool = False):
        providers = ['CUDAExecutionProvider', 'CPUExecutionProvider']
        if use_tensorrt:
            providers = ['TensorrtExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider']
        self.session = ort.InferenceSession(model_path, providers=providers)
        self.input_name = self.session.get_inputs()[0].name
        self.input_shape = self.session.get_inputs()[0].shape
        logger.info(f"Loaded model {model_path} with providers {providers}")

    def preprocess(self, frame):
        # Resize and normalize frame to model input size
        input_h, input_w = self.input_shape[2], self.input_shape[3]
        img = cv2.resize(frame, (input_w, input_h))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = img.astype(np.float32) / 255.0
        img = np.transpose(img, (2, 0, 1))
        img = np.expand_dims(img, axis=0)
        return img

    def postprocess(self, outputs, conf_threshold=0.5):
        # Placeholder for postprocessing logic to extract bounding boxes and class ids
        # This depends on the model output format
        # For demonstration, return empty list
        return []

    def detect(self, frame):
        input_tensor = self.preprocess(frame)
        outputs = self.session.run(None, {self.input_name: input_tensor})
        detections = self.postprocess(outputs)
        return detections
