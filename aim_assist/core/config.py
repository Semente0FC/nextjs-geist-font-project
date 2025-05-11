import json
from pathlib import Path

class Config:
    def __init__(self, config_path: str = "config.json"):
        self.config_path = Path(config_path)
        self.data = {
            "mode": "default",
            "sensitivity": 1.0,
            "smoothing": 0.5,
            "delay": 0,
            "model": "yolov8.onnx",
            "presets": {
                "CS2": {"sensitivity": 1.2, "smoothing": 0.4, "delay": 0},
                "Valorant": {"sensitivity": 1.0, "smoothing": 0.5, "delay": 0},
                "Warzone": {"sensitivity": 1.5, "smoothing": 0.3, "delay": 0},
            }
        }
        self.load()

    def load(self):
        if self.config_path.exists():
            with open(self.config_path, "r") as f:
                self.data.update(json.load(f))

    def save(self):
        with open(self.config_path, "w") as f:
            json.dump(self.data, f, indent=4)

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
        self.save()
