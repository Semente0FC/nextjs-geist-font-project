from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout

class ControlPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.toggle_button = QPushButton("Activate Aim Assist")
        self.toggle_button.setCheckable(True)
        self.layout.addWidget(self.toggle_button)
