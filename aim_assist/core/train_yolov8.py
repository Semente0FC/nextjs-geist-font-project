import torch
from pathlib import Path
from loguru import logger

def train_yolov8(data_yaml: str, epochs: int = 50, batch_size: int = 16, weights: str = "yolov8n.pt", save_dir: str = "runs/train/custom"):
    from ultralytics import YOLO

    logger.info("Starting YOLOv8 training")
    model = YOLO(weights)
    results = model.train(data=data_yaml, epochs=epochs, batch=batch_size, project=save_dir, name="custom_model", exist_ok=True)
    logger.info("Training completed")
    return results

if __name__ == "__main__":
    # Example usage:
    data_yaml = "data/custom_data.yaml"  # Path to dataset config file
    train_yolov8(data_yaml)
