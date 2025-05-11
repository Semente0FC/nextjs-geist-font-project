from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Qt

class VideoPreview(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.layout().addWidget(self.label) if self.layout() else None

    def update_frame(self, frame):
        # frame is a numpy array (BGR)
        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format.Format_BGR888)
        pixmap = QPixmap.fromImage(q_img)
        self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
