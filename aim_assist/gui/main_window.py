from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QHBoxLayout
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtGui import QPixmap, QImage
from .video_preview import VideoPreview
from .control_panel import ControlPanel
from .settings_menu import SettingsMenu
from loguru import logger

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aim Assist Professional")
        self.setMinimumSize(800, 600)
        self.setStyleSheet("background-color: #121212; color: white; border-radius: 10px;")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.video_preview = VideoPreview()
        self.control_panel = ControlPanel()
        self.settings_menu = SettingsMenu()

        self.log_panel = QTextEdit()
        self.log_panel.setReadOnly(True)
        self.log_panel.setStyleSheet("background-color: #1e1e1e; border-radius: 5px;")

        self.layout.addWidget(self.video_preview)
        self.layout.addWidget(self.control_panel)
        self.layout.addWidget(self.settings_menu)
        self.layout.addWidget(QLabel("Logs:"))
        self.layout.addWidget(self.log_panel)

        self.control_panel.toggle_button.clicked.connect(self.toggle_aim_assist)

    @Slot()
    def toggle_aim_assist(self):
        if self.control_panel.toggle_button.isChecked():
            logger.info("Aim Assist Activated")
        else:
            logger.info("Aim Assist Deactivated")
