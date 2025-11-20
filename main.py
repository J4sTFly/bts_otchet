import os
from config import Config
from PyQt5.QtCore import QSize, Qt, QDate
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QGridLayout,
    QLabel,
    QLineEdit,
    QWidget,
    QCheckBox,
    QDateEdit,
    QPushButton,
    QFileDialog,
)

from styles import STYLESHEET


class App(QMainWindow):

    def __init__(self):
        super().__init__()

        self.config = Config()

        self.setWindowTitle("BHS Report App")
        self.setFixedSize(QSize(800, 600))

        self.setStyleSheet(STYLESHEET)

        self.layout = QGridLayout()

        # Report Parameters

        start_date_label = QLabel("Start Date:")
        end_date_label = QLabel("End Date:")
        today = QDate.currentDate()
        self.start_date = today.addMonths(-1)
        self.end_date = today

        self.start_date_field = QDateEdit(self.start_date)
        self.end_date_field = QDateEdit(self.end_date)

        self.start_date_field.setDisplayFormat("dd/MM/yyyy")
        self.end_date_field.setDisplayFormat("dd/MM/yyyy")

        self.start_date_field.setCalendarPopup(True)
        self.end_date_field.setCalendarPopup(True)

        self.start_date_field.dateChanged.connect(
            lambda date: self.edit_date(date, self.start_date)
        )
        self.end_date_field.dateChanged.connect(
            lambda date: self.edit_date(date, self.end_date)
        )

        self.layout.addWidget(start_date_label, 0, 0)
        self.layout.addWidget(self.start_date_field, 0, 1)

        self.layout.addWidget(end_date_label, 1, 0)
        self.layout.addWidget(self.end_date_field, 1, 1)

        # Settings
        self.input_template_path = os.path.join(os.getcwd(), "base_template.xls")
        self.output_file_path = os.path.join(os.getcwd(), "reports/output.xls")

        inp_templ_label = QLabel("Input Template:")
        self.input_templ_field = QLineEdit(self.input_template_path)
        self.input_templ_field.textChanged.connect(self.set_input_template)
        self.select_inp_templ_btn = QPushButton("Browse")
        self.select_inp_templ_btn.clicked.connect(self.select_input_template)

        of_label = QLabel("Output File:")
        self.output_file_field = QLineEdit(self.output_file_path)
        self.output_file_field.textChanged.connect(self.set_output_file)
        self.select_of_btn = QPushButton("Browse")
        self.select_of_btn.clicked.connect(self.select_output_file)

        self.layout.addWidget(inp_templ_label, 2, 0)
        self.layout.addWidget(self.input_templ_field, 2, 1)
        self.layout.addWidget(self.select_inp_templ_btn, 2, 2)

        self.layout.addWidget(of_label, 3, 0)
        self.layout.addWidget(self.output_file_field, 3, 1)
        self.layout.addWidget(self.select_of_btn, 3, 2)

        # Execution control

        self.start_btn = QPushButton("Start")
        self.start_btn.setObjectName("startButton")
        self.start_btn.clicked.connect(self.start)

        self.stop_btn = QPushButton("Stop")
        self.stop_btn.setObjectName("stopButton")
        self.stop_btn.clicked.connect(self.stop)
        self.stop_btn.setDisabled(True)

        self.pause_btn = QPushButton("Pause")
        self.pause_btn.setObjectName("pauseButton")
        self.pause_btn.clicked.connect(self.pause)
        self.pause_btn.setDisabled(True)

        self.layout.addWidget(self.start_btn, 4, 0)
        self.layout.addWidget(self.pause_btn, 4, 1)
        self.layout.addWidget(self.stop_btn, 4, 2)

        self.container = QWidget()
        self.container.setLayout(self.layout)

        self.setCentralWidget(self.container)

    def edit_date(self, date_value, date_field):
        date_field = date_value

    def select_output_file(self):
        self.select_of_dialog = QFileDialog()
        self.select_of_dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        self.select_of_dialog.setViewMode(QFileDialog.Detail)
        self.select_of_dialog.fileSelected.connect(self.set_output_file)
        self.select_of_dialog.exec_()

    def select_input_template(self):
        self.select_inp_templ_dialog = QFileDialog(self.container, "Select File")
        self.select_inp_templ_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        self.select_inp_templ_dialog.setViewMode(QFileDialog.Detail)
        self.select_inp_templ_dialog.fileSelected.connect(self.set_input_template)
        self.select_inp_templ_dialog.exec_()

    def set_input_template(self, path):
        self.input_templ_path = path
        self.input_templ_field.setText(path)

    def set_output_file(self, path):
        self.output_file_path = path
        self.output_file_field.setText(path)

    def start(self):
        self.start_btn.setDisabled(True)
        self.pause_btn.setText("Pause")
        self.pause_btn.setDisabled(False)
        self.stop_btn.setDisabled(False)
        self.pause_btn.clicked.connect(self.pause)

    def stop(self):
        self.start_btn.setDisabled(False)
        self.pause_btn.setText("Pause")
        self.pause_btn.setDisabled(True)
        self.stop_btn.setDisabled(True)

    def pause(self):
        self.start_btn.setDisabled(True)
        self.pause_btn.setText("Resume")
        self.stop_btn.setDisabled(False)
        self.pause_btn.clicked.connect(self.resume)

    def resume(self):
        self.pause_btn.setText("Pause")
        self.pause_btn.clicked.connect(self.pause)


if __name__ == "__main__":
    application = QApplication([])
    app = App()
    app.show()
    application.exec()
