import sys
import threading
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit
from fastapi import FastAPI, Request
import uvicorn

# --- FastAPI qismi ---
app = FastAPI()
log_messages = []  # FastAPI va GUI o'rtasida umumiy log

@app.post("/event")
async def event_listener(request: Request):
    data = await request.json()
    message = f"Event kelib tushdi: {data}"
    log_messages.append(message)
    return {"status": "ok"}

# --- GUI qismi ---
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 + FastAPI Demo")

        self.layout = QVBoxLayout()

        self.label = QLabel("Event loglari:")
        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.text_area)
        self.setLayout(self.layout)

        # Timer orqali loglarni tekshirish
        from PySide6.QtCore import QTimer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_logs)
        self.timer.start(1000)  # har 1 sekundda yangilaydi

    def update_logs(self):
        while log_messages:
            msg = log_messages.pop(0)
            self.text_area.append(msg)

# --- FastAPI serverni boshqa threadda ishga tushirish ---
def start_fastapi():
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")

if __name__ == "__main__":
    # FastAPI serverni boshqa threadda ishga tushiramiz
    server_thread = threading.Thread(target=start_fastapi, daemon=True)
    server_thread.start()

    # PySide6 GUI
    qt_app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(qt_app.exec())
