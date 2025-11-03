from config import Config
from PyQt5.QtCore import QSize, Qt, QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QLabel, QWidget, QCheckBox, QDateEdit, QPushButton, QFileDialog

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BHS Report App")
        self.setFixedSize(QSize(800, 600))

        self.layout = QGridLayout()
        
        # Report Parameters

        start_date_label = QLabel("Start Date:")
        end_date_label = QLabel("End Date:")
        today = QDate.currentDate()

        self.start_date_field = QDateEdit(today.addMonths(-1))
        self.end_date_field = QDateEdit(today)

        self.layout.addWidget(start_date_label)
        self.layout.addWidget(self.start_date_field)

        self.layout.addWidget(end_date_label)
        self.layout.addWidget(self.end_date_field)
        
        # Settings
        
        inp_templ_label = QLabel("Input Template")
        self.select_inp_templ_btn = QPushButton("Browse")
        self.select_inp_templ_btn.clicked.connect(self.select_output_file)

        of_label = QLabel("Output File")
        self.of_slct_dialog = QFileDialog()
        self.of_slct_dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        self.slct_of_btn = QPushButton("Browse")
        
        self.layout.addWidget(inp_templ_label)
        self.layout.addWidget(self.select_inp_templ_btn)
        self.layout.addWidget(of_label)
        self.layout.addWidget(self.select_of_btn)
        #self.layout.addWidget(self.output_file_selection_dialog)

        self.container = QWidget()
        self.container.setLayout(self.layout)

        self.setCentralWidget(self.container)

        start = QPushButton("Start")
        start.clicked.connect(self.start)

        stop = QPushButton("Stop")
        stop.clicked.connect(self.stop)
        
        pause = QPushButton("Pause")
        pause.clicked.connect(self.pause)

        resume = QPushButton("Resume")
        resume.clicked.connect(self.resume)

    def select_output_file(self):
        pass

    def select_input_template(self):
        self.select_inp_templ_dialog = QFileDialog()
        self.select_inp_templ_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)

    def start(self):
        pass

    def stop(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

if __name__ == "__main__":
    application = QApplication([])
    app = App()
    app.show()
    application.exec()

