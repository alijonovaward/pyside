import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sonni 2 ga ko‘paytirish")
        self.setGeometry(200, 200, 300, 150)

        # Layout
        layout = QVBoxLayout()

        # Input
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Son kiriting...")
        layout.addWidget(self.input_field)

        # Button
        self.button = QPushButton("Ko‘paytir")
        self.button.clicked.connect(self.multiply_number)
        layout.addWidget(self.button)

        # Result
        self.result_label = QLabel("Natija: ")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def multiply_number(self):
        try:
            num = float(self.input_field.text())  # sonni olamiz
            result = num * 2
            self.result_label.setText(f"Natija: {result}")
        except ValueError:
            self.result_label.setText("Iltimos, faqat son kiriting!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
