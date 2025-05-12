import torch
from ultralytics import YOLO
from loguru import logger

def export_to_onnx(weights_path: str, onnx_path: str, input_size=(640, 640)):
    logger.info(f"Loading model from {weights_path}")
    model = YOLO(weights_path)
    logger.info(f"Exporting model to ONNX at {onnx_path}")
    model.export(format="onnx", imgsz=input_size, opset=12, simplify=True, dynamic=True, output=onnx_path)
    logger.info("Export completed")

if __name__ == "__main__":
    weights_path = "runs/train/custom_model/weights/best.pt"
    onnx_path = "models/yolov8_custom.onnx"
    export_to_onnx(weights_path, onnx_path)
