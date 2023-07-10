import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QHBoxLayout, QVBoxLayout, QComboBox, QCheckBox, QRadioButton, QSlider, QProgressBar, QSpinBox, QDial, QCalendarWidget, QGroupBox, QScrollBar, QListWidget, QTabWidget, QInputDialog, QFontDialog, QColorDialog, QMessageBox, QFileDialog
from PyQt6.QtCore import QFile, QTextStream, Qt

class ExampleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):

        def set_style_sheet(filename):
            with open(filename, "r") as f:
                style = f.read()
                app.setStyleSheet(style)

        set_style_sheet('Material.css')

        # QLabel
        label = QLabel("This is a label")

        # QLineEdit
        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Q Line Edit")

        # QTextEdit
        text_edit = QTextEdit()

        # QPushButton
        button = QPushButton("Click Me!")

        # QHBoxLayout and QVBoxLayout
        hbox = QHBoxLayout()
        hbox.addWidget(label)
        hbox.addWidget(line_edit)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(text_edit)
        vbox.addWidget(button)

        # QLabel
        label = QLabel("This is a label")

        # QPushButton
        button = QPushButton("Click Me!")

        
        # QComboBox
        combo_box = QComboBox()
        combo_box.addItem("Option 1")
        combo_box.addItem("Option 2")
        combo_box.addItem("Option 3")

        # QCheckBox
        check_box = QCheckBox("Check Box")

        # QRadioButton
        radio_button = QRadioButton("Radio Button")

        # QSlider
        vertical_slider = QSlider(Qt.Orientation.Vertical)
        vertical_slider.setRange(0, 100)
        vertical_slider.setValue(0)
        vertical_slider.setFixedWidth(32)
        horizontal_slider = QSlider(Qt.Orientation.Horizontal)
        horizontal_slider.setRange(0, 100)
        horizontal_slider.setValue(0)
        horizontal_slider.setFixedHeight(32)

        # QProgressBar
        progress_bar = QProgressBar()

        # QSpinBox
        spin_box = QSpinBox()

        # QDial
        dial = QDial()

        # QCalendarWidget
        calendar = QCalendarWidget()

        # QGroupBox
        group_box = QGroupBox("Group Box")

        # QScrollBar
        scroll_bar = QScrollBar()
        scroll_bar.setOrientation(Qt.Orientation.Horizontal)

        # QListWidget
        list_widget = QListWidget()
        list_widget.addItems(["Item 1", "Item 2", "Item 3"])

        # QTabWidget
        tab_widget = QTabWidget()
        tab_widget.addTab(QWidget(), "Tab 1")
        tab_widget.addTab(QWidget(), "Tab 2")

        # QInputDialog
        input_dialog = QInputDialog()

        # QFontDialog
        font_dialog = QFontDialog()

        # QColorDialog
        color_dialog = QColorDialog()

        # QMessageBox
        message_box = QMessageBox()
        message_box.setText("This is a message box")

        # QFileDialog
        file_dialog = QFileDialog()

        # Adding all the widgets to the main layout
        main_layout = QVBoxLayout()
        # main_layout.addWidget(combo_box)
        # main_layout.addWidget(check_box)
        # main_layout.addWidget(radio_button)
        main_layout.addWidget(vertical_slider)
        main_layout.addWidget(horizontal_slider)
        main_layout.addWidget(label)
        main_layout.addWidget(button)
        main_layout.addWidget(line_edit)
        # main_layout.addWidget(progress_bar)
        # main_layout.addWidget(spin_box)
        # main_layout.addWidget(dial)
        # main_layout.addWidget(calendar)
        # main_layout.addWidget(group_box)
        main_layout.addWidget(scroll_bar)
        # main_layout.addWidget(list_widget)
        # main_layout.addWidget(tab_widget)
        # main_layout.addWidget(input_dialog)
        # main_layout.addWidget(font_dialog)
        # main_layout.addWidget(color_dialog)
        # main_layout.addWidget(message_box)
        # main_layout.addWidget(file_dialog)

        self.setLayout(main_layout)
        self.setWindowTitle("PyQt6 Widgets Example")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExampleApp()
    sys.exit(app.exec())
