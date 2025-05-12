# Models Directory

This directory is intended to store the ONNX model files required for enemy detection.

Currently, the file `yolov8.onnx` is missing, which causes the application to fail when trying to load the model.

Please download or place the appropriate YOLOv8 ONNX model file named `yolov8.onnx` in this directory before running the application.

You can obtain the YOLOv8 ONNX model from the official Ultralytics repository or export it from a trained YOLOv8 PyTorch model.

Once the model file is in place, the application should run without the missing file error.
