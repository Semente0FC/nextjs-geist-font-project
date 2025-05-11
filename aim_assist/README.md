# Aim Assist with AI and Professional Panel

This project is a professional Aim Assist AI built in Python 3.10+ with GPU RTX 2060+ acceleration. It features real-time screen capture, enemy detection using YOLOv8 ONNX with GPU acceleration, smooth aim calculation, and a modern PySide6 graphical user interface.

## Features

- Real-time screen capture compatible with fullscreen and borderless games at 60+ FPS.
- Enemy detection using YOLOv8 ONNX or Faster R-CNN with CUDA GPU acceleration.
- Smooth aim calculation with configurable sensitivity and smoothing.
- Modern PySide6 UI with dark theme, rounded borders, real-time preview, logs, and settings.
- GPU monitoring with pynvml.
- Thread management for capture, detection, and UI.
- Logging and metrics with local log files and UI visualization.
- Configuration profiles and presets for different games.
- Test and benchmark scripts for FPS, latency, and stress testing.

## Requirements

- Python 3.10+
- GPU: RTX 2060 or higher
- Libraries: See requirements.txt

## Installation

1. Create a virtual environment and activate it.
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the main application:

```
python main.py
```

## Project Structure

- `core/`: Core modules for capture, detection, aiming, GPU monitoring, config, and logging.
- `gui/`: PySide6 GUI components.
- `models/`: ONNX model files.
- `tests/`: Test and benchmark scripts.
- `assets/`: UI stylesheets.
- `main.py`: Main entry point.

## License

This project is built from scratch and free to use.
