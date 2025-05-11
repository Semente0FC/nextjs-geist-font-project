from PySide6.QtWidgets import QWidget, QFormLayout, QSlider, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

class SettingsMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        self.sensitivity_slider = QSlider(Qt.Horizontal)
        self.sensitivity_slider.setMinimum(1)
        self.sensitivity_slider.setMaximum(100)
        self.sensitivity_slider.setValue(50)
        self.layout.addRow("Sensitivity", self.sensitivity_slider)

        self.smoothing_slider = QSlider(Qt.Horizontal)
        self.smoothing_slider.setMinimum(1)
        self.smoothing_slider.setMaximum(100)
        self.smoothing_slider.setValue(50)
        self.layout.addRow("Smoothing", self.smoothing_slider)

        self.delay_slider = QSlider(Qt.Horizontal)
        self.delay_slider.setMinimum(0)
        self.delay_slider.setMaximum(100)
        self.delay_slider.setValue(0)
        self.layout.addRow("Delay (ms)", self.delay_slider)
