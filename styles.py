# styles.py
STYLESHEET = """
QMainWindow {
    background-color: #f0f0f0;
    font-family: Arial, sans-serif;
}

QLabel {
    font-weight: bold;
    color: #333333;
    padding: 4px;
}

QLineEdit {
    padding: 8px;
    border: 1px solid #cccccc;
    border-radius: 4px;
    background-color: white;
    font-size: 14px;
}

QLineEdit:focus {
    border: 1px solid #0078d4;
    outline: none;
}

QDateEdit {
    padding: 8px;
    border: 1px solid #cccccc;
    border-radius: 4px;
    background-color: white;
    font-size: 14px;
}

QDateEdit:focus {
    border: 1px solid #0078d4;
}

QDateEdit::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    border-left: 1px solid #cccccc;
}

QPushButton {
    background-color: #0078d4;
    color: white;
    border: none;
    padding: 8px 12px;
    border-radius: 4px;
    font-weight: bold;
    font-size: 13px;
    min-width: 70px;
    max-width: 100px;
}

QPushButton:hover {
    background-color: #106ebe;
}

QPushButton:pressed {
    background-color: #005a9e;
}

QPushButton:disabled {
    background-color: #cccccc;
    color: #666666;
}

QPushButton#startButton {
    background-color: #107c10;
}

QPushButton#startButton:hover {
    background-color: #0e6b0e;
}

QPushButton#stopButton {
    background-color: #d83b01;
}

QPushButton#stopButton:hover {
    background-color: #b32d00;
}

QPushButton#pauseButton {
    background-color: #ffb900;
    color: #000000;
    min-width: 60px;
    max-width: 80px;
}

QPushButton#pauseButton:hover {
    background-color: #d19d00;
}

QGridLayout {
    margin: 20px;
    spacing: 10px;
}

QWidget#mainContainer {
    background-color: white;
    border-radius: 8px;
    margin: 10px;
    padding: 15px;
}
"""
