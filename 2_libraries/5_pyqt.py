########################################################################################################################
# TODO интерфейс на pyqt

import sys
import threading
import multiprocessing
from PyQt6 import QtWidgets, QtCore, QtGui


# from PyQt6.QtWidgets import (
#     QApplication,
#     QCheckBox,
#     QComboBox,
#     QDateEdit,
#     QDateTimeEdit,
#     QDial,
#     QDoubleSpinBox,
#     QFontComboBox,
#     QLabel,
#     QLCDNumber,
#     QLineEdit,
#     QMainWindow,
#     QProgressBar,
#     QPushButton,
#     QRadioButton,
#     QSlider,
#     QSpinBox,
#     QTimeEdit,
#     QVBoxLayout,
#     QWidget, QGridLayout,
# )


class PyQtWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QGridLayout(self)

        # self.layout = QtWidgets.QVBoxLayout(self)
        # self.ui_window = QtWidgets.QHBoxLayout(self)

        self.label_path = QtWidgets.QLabel("...")
        self.layout.addWidget(self.label_path, 0, 0)

        self.line_edit_path = QtWidgets.QLineEdit("Hello World!")
        # self.line_edit.textChanged.connect(self.line_edit_text_changed)
        self.layout.addWidget(self.line_edit_path, 0, 1)

        self.check_box_is_equal = QtWidgets.QCheckBox("")
        self.layout.addWidget(self.check_box_is_equal, 1, 0)

        self.button = QtWidgets.QPushButton("request")
        self.button.clicked.connect(self.start)
        self.layout.addWidget(self.button, 1, 1)

        # self.temp_box = QtWidgets.QDoubleSpinBox()

        # self.combo_box_filter = QComboBox()
        # self.combo_box_filter.addItem("usd")
        # self.combo_box_filter.addItem("eur")
        # self.combo_box_filter.addItems(["gbp", "cny", "pln", "rub"])

        # self.slider_quality = QSlider(Qt.Horizontal)
        # self.slider_quality = QSlider()
        # self.slider_quality.setMinimum(1)
        # self.slider_quality.setMaximum(100)
        # self.slider_quality.setValue(95)
        # self.layout.addWidget(self.slider_quality, 4, 5)

        # self.pixmap = QPixmap('python.jpeg')
        # self.label2.setPixmap(self.pixmap)

        self.setWindowTitle("Create user in Django")
        self.resize(640, 480)
        self.show()

    def start(self):
        url = self.line_edit_path.text()
        self.label_path.setText(url[::-1])

    def closeEvent(self, event: QtGui.QCloseEvent):
        reply = QtWidgets.QMessageBox.question(self, 'Внимание', 'Вы действительно хотите выйти?',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def get_speed_video_stream_button(self):
        widget = self.speed_video_stream
        value, success = QtWidgets.QInputDialog.getDouble(self, f'Set {widget.text().split(":")[0].strip()}',
                                                          f'{widget.text().split(":")[0].strip()} value:',
                                                          1.0, 0.01, 50.0, 2)
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_sensitivity_analysis_button(self):
        widget = self.sensitivity_analysis
        value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                        f'{widget.text().split(":")[0].strip()} value:',
                                                        text=f'{widget.text().split(":")[1].strip()}')
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')


if __name__ == "__main__":
    pyqt_app = QtWidgets.QApplication([])
    pyqt_ui = PyQtWindow()
    sys.exit(pyqt_app.exec())


########################################################################################################################

########################################################################################################################
# TODO машинное зрение

class AppContainerClass:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.widget = None

    def create_ui(self, title, width, height, icon, play_f, stop_f, quit_f, snapshot_f):
        self.widget = MainWidgetClass(title, width, height, icon, play_f, stop_f, quit_f, snapshot_f)
        return self.widget

    @staticmethod
    def create_qlable(text: str, _parent, background=False):
        _widget = QtWidgets.QLabel(text)
        if background:
            _widget.setAutoFillBackground(True)
            _widget.setStyleSheet("QLabel { background-color: rgba(0, 0, 0, 255); color : white; }")
        _parent.addWidget(_widget)
        return _widget

    @staticmethod
    def create_qpushbutton(_parent, _connect_func, _text='set'):
        _widget = QtWidgets.QPushButton(_text)
        _parent.addWidget(_widget)
        _widget.clicked.connect(_connect_func)
        return _widget

    @staticmethod
    def create_qcheckbox(_parent, _text='check?', default=False):
        _widget = QtWidgets.QCheckBox(_text)
        _widget.setChecked(default)
        _parent.addWidget(_widget)
        return _widget

    @staticmethod
    def create_qcombobox(_parent, _text: list, default=None):
        _widget = QtWidgets.QComboBox()
        _widget.addItems([x for x in _text])
        _widget.setCurrentText(default)
        _parent.addWidget(_widget)
        return _widget

    @staticmethod
    def create_qradiobutton(_parent, _text: str, default=False):
        _widget = QtWidgets.QRadioButton(_text)
        _widget.setChecked(default)
        _parent.addWidget(_widget)
        return _widget


class MainWidgetClass(QtWidgets.QWidget):
    def __init__(self, title="APP", width=640, height=480, icon="", play_f=None, stop_f=None, quit_f=None,
                 snapshot_f=None):
        super().__init__()

        self.play_f = play_f
        self.snapshot_f = snapshot_f
        self.resize(width, height)
        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(icon))
        self.resolution_debug = []
        self.v_layout_m = QtWidgets.QVBoxLayout(self)

        # MANAGEMENT
        self.h_layout_g_management = QtWidgets.QHBoxLayout()
        self.v_layout_m.addLayout(self.h_layout_g_management)
        self.g_management_set = AppContainerClass.create_qlable('MANAGEMENT', self.h_layout_g_management,
                                                                background=True)
        self.h_layout_management_1 = QtWidgets.QHBoxLayout()
        self.v_layout_m.addLayout(self.h_layout_management_1)
        self.play_QPushButton = AppContainerClass.create_qpushbutton(self.h_layout_management_1,
                                                                     self.play_btn_func,
                                                                     'play')
        self.stop_QPushButton = AppContainerClass.create_qpushbutton(self.h_layout_management_1, stop_f, 'stop')
        self.quit_QPushButton = AppContainerClass.create_qpushbutton(self.h_layout_management_1, quit_f, 'quit')
        # CAMERAS
        self.h_layout_g_cam = QtWidgets.QHBoxLayout()
        self.v_layout_m.addLayout(self.h_layout_g_cam)
        self.g_cam_set = AppContainerClass.create_qlable('CAMERAS', self.h_layout_g_cam, background=True)
        self.h_layout_cam_1 = QtWidgets.QHBoxLayout()
        self.v_layout_m.addLayout(self.h_layout_cam_1)
        self.protocol_cam_type = AppContainerClass.create_qlable('PROTOCOL TYPE : http', self.h_layout_cam_1)
        self.set_protocol_cam_type = AppContainerClass.create_qpushbutton(self.h_layout_cam_1,
                                                                          self.get_protocol_cam_type_button)
        self.port_cam = AppContainerClass.create_qlable('PORT CAM : 80', self.h_layout_cam_1)
        self.set_port_cam = AppContainerClass.create_qpushbutton(self.h_layout_cam_1, self.get_port_cam_button)
        self.login_cam = AppContainerClass.create_qlable('LOGIN CAM : admin', self.h_layout_cam_1)
        self.set_login_cam = AppContainerClass.create_qpushbutton(self.h_layout_cam_1,
                                                                  self.get_login_cam_button)
        self.password_cam = AppContainerClass.create_qlable('PASSWORD CAM : q1234567', self.h_layout_cam_1)
        self.set_password_cam = AppContainerClass.create_qpushbutton(self.h_layout_cam_1,
                                                                     self.get_password_cam_button)
        self.h_layout_cam_2 = QtWidgets.QHBoxLayout()
        self.v_layout_m.addLayout(self.h_layout_cam_2)
        self.alias_device = AppContainerClass.create_qlable(
            'ALIAS DEVICE : 16/1 | 16/2 | 16/3 | 16/4 | 16/5 | 16/6 '
            '| 16/7 | 16/8 | 16/9 | 16/10', self.h_layout_cam_2)
        self.set_alias_device = AppContainerClass.create_qpushbutton(self.h_layout_cam_2,
                                                                     self.get_alias_device_button)
        self.h_layout_cam_3 = QtWidgets.QHBoxLayout()
        self.v_layout_m.addLayout(self.h_layout_cam_3)
        self.ip_cam = AppContainerClass.create_qlable(
            'IP CAM : 15.202 | 15.206 | 15.207 | 15.208 | 15.209 | 15.210 '
            '| 15.211 | 15.203 | 15.204 | 15.205', self.h_layout_cam_3)
        self.set_ip_cam = AppContainerClass.create_qpushbutton(self.h_layout_cam_3, self.get_ip_cam_button)
        self.h_layout_cam_4 = QtWidgets.QHBoxLayout()
        self.v_layout_m.addLayout(self.h_layout_cam_4)
        self.mask_cam = AppContainerClass.create_qlable(
            'MASK CAM : m_16_1.jpg | m_16_2.jpg | m_16_3.jpg | m_16_4.jpg '
            '| m_16_5.jpg | m_16_6.jpg | m_16_7.jpg | m_16_8.jpg '
            '| m_16_9.jpg | m_16_10.jpg', self.h_layout_cam_4)
        self.set_mask_cam = AppContainerClass.create_qpushbutton(self.h_layout_cam_4, self.get_mask_cam_button)
        self.h_layout_cam_5 = QtWidgets.QHBoxLayout()
        self.v_layout_m.addLayout(self.h_layout_cam_5)
        self.sensitivity_analysis = AppContainerClass.create_qlable(
            'SENSITIVITY ANALYSIS : 115 | 115 | 115 | 115 '
            '| 115 | 115 | 115 | 115 | 115 | 115',
            self.h_layout_cam_5)
        self.set_sensitivity_analysis = AppContainerClass.create_qpushbutton(self.h_layout_cam_5,
                                                                             self.get_sensitivity_analysis_button)
        self.h_layout_cam_6 = QtWidgets.QHBoxLayout()
        self.v_layout_m.addLayout(self.h_layout_cam_6)
        self.alarm_level = AppContainerClass.create_qlable('ALARM LEVEL : 30 | 30 | 30 | 30 '
                                                           '| 30 | 30 | 30 | 30 | 30 | 30',
                                                           self.h_layout_cam_6)
        self.set_alarm_level = AppContainerClass.create_qpushbutton(self.h_layout_cam_6,
                                                                    self.get_alarm_level_button)
        self.h_layout_cam_7 = QtWidgets.QHBoxLayout()
        self.v_layout_m.addLayout(self.h_layout_cam_7)
        self.correct_coefficient = AppContainerClass.create_qlable(
            'CORRECT COEFFICIENT : 1.0 | 1.0 | 1.0 | 1.0 | 1.0 '
            '| 1.0 | 1.0 | 1.0 | 1.0 | 1.0', self.h_layout_cam_7)
        self.set_correct_coefficient = AppContainerClass.create_qpushbutton(self.h_layout_cam_7,
                                                                            self.get_correct_coefficient_button)
        # SQL
        self.h_layout_g_sql = QtWidgets.QHBoxLayout()
        self.v_layout_m.addLayout(self.h_layout_g_sql)
        self.g_sql_set = AppContainerClass.create_qlable('SQL', self.h_layout_g_sql, background=True)
        self.h_layout_sql_1 = QtWidgets.QHBoxLayout()
        self.v_layout_m.addLayout(self.h_layout_sql_1)
        self.sql_write = AppContainerClass.create_qcheckbox(self.h_layout_sql_1, 'CONNECT TO SQL?')
        self.ip_sql = AppContainerClass.create_qlable('IP SQL SERVER : 192.168.15.87', self.h_layout_sql_1)
        self.set_ip_sql = AppContainerClass.create_qpushbutton(self.h_layout_sql_1, self.get_ip_sql_button)
        self.server_sql = AppContainerClass.create_qlable(r'SERVER SQL : DESKTOP-SM7K050\COMPUTER_VISION',
                                                          self.h_layout_sql_1)
        self.set_server_sql = AppContainerClass.create_qpushbutton(self.h_layout_sql_1,
                                                                   self.get_server_sql_button)
        self.port_sql = AppContainerClass.create_qlable('PORT SQL SERVER : 1433', self.h_layout_sql_1)
        self.set_port_sql = AppContainerClass.create_qpushbutton(self.h_layout_sql_1, self.get_port_sql_button)
        self.h_layout_sql_2 = QtWidgets.QHBoxLayout()
        self.v_layout_m.addLayout(self.h_layout_sql_2)
        self.database_sql = AppContainerClass.create_qlable('DATABASE SQL : analiz_16grohot',
                                                            self.h_layout_sql_2)
        self.set_database_sql = AppContainerClass.create_qpushbutton(self.h_layout_sql_2,
                                                                     self.get_database_sql_button)
        self.user_sql = AppContainerClass.create_qlable('USER SQL : computer_vision', self.h_layout_sql_2)
        self.set_user_sql = AppContainerClass.create_qpushbutton(self.h_layout_sql_2, self.get_user_sql_button)
        self.h_layout_sql_3 = QtWidgets.QHBoxLayout()
        self.v_layout_m.addLayout(self.h_layout_sql_3)
        self.password_sql = AppContainerClass.create_qlable('PASSWORD SQL : vision12345678',
                                                            self.h_layout_sql_2)
        self.set_password_sql = AppContainerClass.create_qpushbutton(self.h_layout_sql_2,
                                                                     self.get_password_sql_button)
        self.sql_now_check = AppContainerClass.create_qcheckbox(self.h_layout_sql_3, 'WRITE NOW SQL?')
        self.table_now_sql = AppContainerClass.create_qlable('TABLE NOW SQL : grohot16_now_table',
                                                             self.h_layout_sql_3)
        self.set_table_now_sql = AppContainerClass.create_qpushbutton(self.h_layout_sql_3,
                                                                      self.get_table_now_sql_button)
        self.rows_now_sql = AppContainerClass.create_qlable('ROWS NOW SQL : device_row | value_row | alarm_row '
                                                            '| datetime_row', self.h_layout_sql_3)
        self.set_rows_now_sql = AppContainerClass.create_qpushbutton(self.h_layout_sql_3,
                                                                     self.get_rows_now_sql_button)
        self.h_layout_sql_4 = QtWidgets.QHBoxLayout()
        self.v_layout_m.addLayout(self.h_layout_sql_4)
        self.sql_data_check = AppContainerClass.create_qcheckbox(self.h_layout_sql_4, 'WRITE DATA SQL?')
        self.table_data_sql = AppContainerClass.create_qlable('TABLE DATA SQL : grohot16_data_table',
                                                              self.h_layout_sql_4)
        self.set_table_data_sql = AppContainerClass.create_qpushbutton(self.h_layout_sql_4,
                                                                       self.get_table_data_sql_button)
        self.rows_data_sql = AppContainerClass.create_qlable(
            'ROWS DATA SQL : device_row | value_row | alarm_row '
            '| datetime_row', self.h_layout_sql_4)
        self.set_rows_data_sql = AppContainerClass.create_qpushbutton(self.h_layout_sql_4,
                                                                      self.get_rows_data_sql_button)
        # DEBUG
        self.h_layout_g_debug = QtWidgets.QHBoxLayout()
        self.v_layout_m.addLayout(self.h_layout_g_debug)
        self.g_debug_set = AppContainerClass.create_qlable('DEBUG', self.h_layout_g_debug, background=True)
        self.h_layout_debug_1 = QtWidgets.QHBoxLayout()
        self.v_layout_m.addLayout(self.h_layout_debug_1)
        self.auto_import_check = AppContainerClass.create_qcheckbox(self.h_layout_debug_1, 'AUTO IMPORT?')
        self.auto_play_check = AppContainerClass.create_qcheckbox(self.h_layout_debug_1, 'AUTO PLAY?')
        self.speed_analysis = AppContainerClass.create_qlable('SPEED ANALYSIS : 1.0', self.h_layout_debug_1)
        self.set_speed_analysis = AppContainerClass.create_qpushbutton(self.h_layout_debug_1,
                                                                       self.get_speed_analysis_button)
        self.speed_video_stream = AppContainerClass.create_qlable('SPEED VIDEO-STREAM : 1.0',
                                                                  self.h_layout_debug_1)
        self.set_speed_video_stream = AppContainerClass.create_qpushbutton(self.h_layout_debug_1,
                                                                           self.get_speed_video_stream_button)
        self.h_layout_debug_2 = QtWidgets.QHBoxLayout()
        self.v_layout_m.addLayout(self.h_layout_debug_2)
        self.widget_data_value = AppContainerClass.create_qlable('0.00%', self.h_layout_debug_2)
        self.h_layout_debug_2.addStretch()
        self.widget_write = AppContainerClass.create_qcheckbox(self.h_layout_debug_2, 'WRITE TO WIDGET?')
        self.text_write = AppContainerClass.create_qcheckbox(self.h_layout_debug_2, 'WRITE TO TEXT?')
        self.source_win_type = AppContainerClass.create_qlable('SOURCE TYPE :', self.h_layout_debug_2)
        self.source_type = AppContainerClass.create_qcombobox(self.h_layout_debug_2,
                                                              ['image-http', 'video-rtsp', 'video-file'],
                                                              'image-http')
        self.compute_win_debug = AppContainerClass.create_qlable('COMPUTE TYPE :', self.h_layout_debug_2)
        self.compute_debug = AppContainerClass.create_qcombobox(self.h_layout_debug_2,
                                                                ['sync', 'async', 'multithread',
                                                                 'multiprocess', 'complex'],
                                                                'complex')
        self.process_cores = AppContainerClass.create_qlable('PROCESS CORES : 4', self.h_layout_debug_2)
        self.set_process_cores = AppContainerClass.create_qpushbutton(self.h_layout_debug_2,
                                                                      self.get_process_cores_button)
        self.h_layout_debug_3 = QtWidgets.QHBoxLayout()
        self.v_layout_m.addLayout(self.h_layout_debug_3)
        self.render_win_debug = AppContainerClass.create_qlable('Render windows :', self.h_layout_debug_3)
        self.render_debug = AppContainerClass.create_qcombobox(self.h_layout_debug_3,
                                                               ['none', 'source', 'final', 'extended',
                                                                'all'], 'none')
        self.resolution_debug_1 = AppContainerClass.create_qradiobutton(self.h_layout_debug_3, '320x240',
                                                                        default=True)
        # self.resolution_debug_1.toggled.connect(self.set_resolution_debug(self.resolution_debug_1, 320, 240))
        # self.resolution_debug_2 = AppContainerClass.create_qradiobutton(self.h_layout_debug_3, '640x480')
        # self.resolution_debug_2.toggled.connect(self.set_resolution_debug(self.resolution_debug_2, 640, 480))
        # self.resolution_debug_3 = AppContainerClass.create_qradiobutton(self.h_layout_debug_3, '1280x720')
        # self.resolution_debug_3.toggled.connect(self.set_resolution_debug(self.resolution_debug_3, 1280, 720))
        # self.resolution_debug_4 = AppContainerClass.create_qradiobutton(self.h_layout_debug_3, '1920x1080')
        # self.resolution_debug_4.toggled.connect(self.set_resolution_debug(self.resolution_debug_4, 1920, 1080))
        # self.resolution_debug_5 = AppContainerClass.create_qradiobutton(self.h_layout_debug_3, '2560x1600')
        # self.resolution_debug_5.toggled.connect(self.set_resolution_debug(self.resolution_debug_5, 2560, 1600))
        # self.resolution_debug_6 = AppContainerClass.create_qradiobutton(self.h_layout_debug_3, '3840x2160')
        # self.resolution_debug_6.toggled.connect(self.set_resolution_debug(self.resolution_debug_6, 3840, 2160))
        # IMPORTS
        self.h_layout_g_imports = QtWidgets.QHBoxLayout()
        self.v_layout_m.addLayout(self.h_layout_g_imports)
        self.g_imports_set = AppContainerClass.create_qlable('IMPORTS', self.h_layout_g_imports,
                                                             background=True)
        self.h_layout_imports_1 = QtWidgets.QHBoxLayout()
        self.v_layout_m.addLayout(self.h_layout_imports_1)
        self.import_file = AppContainerClass.create_qlable('SETTINGS FILE NAME : settings',
                                                           self.h_layout_imports_1)
        self.set_import_file = AppContainerClass.create_qpushbutton(self.h_layout_imports_1,
                                                                    self.get_settings_file_name)
        self.export_QPushButton = AppContainerClass.create_qpushbutton(self.h_layout_imports_1,
                                                                       self.export_settings_func, 'export')
        self.import_QPushButton = AppContainerClass.create_qpushbutton(self.h_layout_imports_1,
                                                                       self.import_settings_func, 'import')
        # SHOT
        self.h_layout_g_shot = QtWidgets.QHBoxLayout()
        self.v_layout_m.addLayout(self.h_layout_g_shot)
        self.g_shot_set = AppContainerClass.create_qlable('SHOT', self.h_layout_g_shot, background=True)
        self.h_layout_shot_1 = QtWidgets.QHBoxLayout()
        self.v_layout_m.addLayout(self.h_layout_shot_1)
        self.ip_cam_snapshot = AppContainerClass.create_qlable('ip-cam : 15.204', self.h_layout_shot_1)
        self.set_ip_cam_snapshot = AppContainerClass.create_qpushbutton(self.h_layout_shot_1,
                                                                        self.get_ip_cam_snapshot_button)
        self.name_snapshot = AppContainerClass.create_qlable('file name : picture.jpg', self.h_layout_shot_1)
        self.set_name_snapshot = AppContainerClass.create_qpushbutton(self.h_layout_shot_1,
                                                                      self.set_name_snapshot_button)
        self.snapshot_QPushButton = AppContainerClass.create_qpushbutton(self.h_layout_shot_1,
                                                                         self.snapshot_btn_func,
                                                                         'snapshot')

        self.setLayout(self.v_layout_m)
        self.auto_play_func()
        self.auto_import_settings_func()

    def get_speed_analysis_button(self):
        widget = self.speed_analysis
        value, success = QtWidgets.QInputDialog.getDouble(self, f'Set {widget.text().split(":")[0].strip()}',
                                                          f'{widget.text().split(":")[0].strip()} value:',
                                                          1.0, 0.01, 50.0, 2)
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_alarm_level_button(self):
        widget = self.alarm_level
        value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                        f'{widget.text().split(":")[0].strip()} value:',
                                                        text=f'{widget.text().split(":")[1].strip()}')
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_correct_coefficient_button(self):
        widget = self.correct_coefficient
        value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                        f'{widget.text().split(":")[0].strip()} value:',
                                                        text=f'{widget.text().split(":")[1].strip()}')
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_protocol_cam_type_button(self):
        widget = self.protocol_cam_type
        value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                        f'{widget.text().split(":")[0].strip()} value:',
                                                        text=f'{widget.text().split(":")[1].strip()}')
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_port_cam_button(self):
        widget = self.port_cam
        value, success = QtWidgets.QInputDialog.getInt(self, f'Set {widget.text().split(":")[0].strip()}',
                                                       f'{widget.text().split(":")[0].strip()} value:',
                                                       554, 1, 9999, 5)
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_login_cam_button(self):
        widget = self.login_cam
        value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                        f'{widget.text().split(":")[0].strip()} value:',
                                                        text=f'{widget.text().split(":")[1].strip()}')
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_password_cam_button(self):
        widget = self.password_cam
        value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                        f'{widget.text().split(":")[0].strip()} value:',
                                                        text=f'{widget.text().split(":")[1].strip()}')
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_alias_device_button(self):
        widget = self.alias_device
        value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                        f'{widget.text().split(":")[0].strip()} value:',
                                                        text=f'{widget.text().split(":")[1].strip()}')
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_ip_cam_button(self):
        widget = self.ip_cam
        value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                        f'{widget.text().split(":")[0].strip()} value:',
                                                        text=f'{widget.text().split(":")[1].strip()}')
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_mask_cam_button(self):
        widget = self.mask_cam
        value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                        f'{widget.text().split(":")[0].strip()} value:',
                                                        text=f'{widget.text().split(":")[1].strip()}')
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_ip_sql_button(self):
        widget = self.ip_sql
        value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                        f'{widget.text().split(":")[0].strip()} value:',
                                                        text=f'{widget.text().split(":")[1].strip()}')
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_server_sql_button(self):
        widget = self.server_sql
        value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                        f'{widget.text().split(":")[0].strip()} value:',
                                                        text=f'{widget.text().split(":")[1].strip()}')
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_port_sql_button(self):
        widget = self.port_sql
        value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                        f'{widget.text().split(":")[0].strip()} value:',
                                                        text=f'{widget.text().split(":")[1].strip()}')
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_database_sql_button(self):
        widget = self.database_sql
        value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                        f'{widget.text().split(":")[0].strip()} value:',
                                                        text=f'{widget.text().split(":")[1].strip()}')
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_user_sql_button(self):
        widget = self.user_sql
        value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                        f'{widget.text().split(":")[0].strip()} value:',
                                                        text=f'{widget.text().split(":")[1].strip()}')
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_password_sql_button(self):
        widget = self.password_sql
        value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                        f'{widget.text().split(":")[0].strip()} value:',
                                                        text=f'{widget.text().split(":")[1].strip()}')
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_table_now_sql_button(self):
        widget = self.table_now_sql
        value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                        f'{widget.text().split(":")[0].strip()} value:',
                                                        text=f'{widget.text().split(":")[1].strip()}')
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_rows_now_sql_button(self):
        widget = self.rows_now_sql
        value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                        f'{widget.text().split(":")[0].strip()} value:',
                                                        text=f'{widget.text().split(":")[1].strip()}')
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_table_data_sql_button(self):
        widget = self.table_data_sql
        value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                        f'{widget.text().split(":")[0].strip()} value:',
                                                        text=f'{widget.text().split(":")[1].strip()}')
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_rows_data_sql_button(self):
        widget = self.rows_data_sql
        value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                        f'{widget.text().split(":")[0].strip()} value:',
                                                        text=f'{widget.text().split(":")[1].strip()}')
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_settings_file_name(self):
        widget = self.import_file
        value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                        f'{widget.text().split(":")[0].strip()} value:',
                                                        text=f'{widget.text().split(":")[1].strip()}')
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def set_resolution_debug(self, radio, width: int, height: int):
        self.resolution_debug.append([radio, width, height])

    def get_window_resolution(self):
        for radio in self.resolution_debug:
            try:
                if radio[0].isChecked():
                    return [int(radio[1]), int(radio[2])]
            except Exception as ex:
                print(ex)

    def set_window_resolution(self, value):
        for radio in self.resolution_debug:
            try:
                if radio[1] == value[0]:
                    radio[0].setChecked(True)
                else:
                    radio[0].setChecked(False)
            except Exception as ex:
                print(ex)

    def get_process_cores_button(self):
        widget = self.process_cores
        value, success = QtWidgets.QInputDialog.getInt(self, f'Set {widget.text().split(":")[0].strip()}',
                                                       f'{widget.text().split(":")[0].strip()} value:',
                                                       4, 1, 16, 5)
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_ip_cam_snapshot_button(self):
        widget = self.ip_cam_snapshot
        value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                        f'{widget.text().split(":")[0].strip()} value:',
                                                        text=f'{widget.text().split(":")[1].strip()}')
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def set_name_snapshot_button(self):
        widget = self.name_snapshot
        value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                        f'{widget.text().split(":")[0].strip()} value:',
                                                        text=f'{widget.text().split(":")[1].strip()}')
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_string_from_list(self, source: list):
        value = ''
        for x in source:
            value = f'{value} | {x}'
        return value[3::]

    def set_data_func(self, value: str):
        try:
            self.widget_data_value.setText(f"{value}")
        except Exception as ex:
            print(f'set_data_func error : {ex}')

    def create_data_func(self):
        try:
            data = {
                'protocol_cam_type': str(self.protocol_cam_type.text().split(':')[1].strip()),
                'port_cam': int(self.port_cam.text().split(':')[1].strip()),
                'login_cam': str(self.login_cam.text().split(':')[1].strip()),
                'password_cam': str(self.password_cam.text().split(':')[1].strip()),
                'alias_device': list(
                    [x.strip() for x in self.alias_device.text().split(':')[1].strip().split('|')]),
                'ip_cam': list([x.strip() for x in self.ip_cam.text().split(':')[1].strip().split('|')]),
                'mask_cam': list([x.strip() for x in self.mask_cam.text().split(':')[1].strip().split('|')]),
                'sensitivity_analysis': list([int(x.strip()) for x in
                                              self.sensitivity_analysis.text().split(':')[1].strip().split(
                                                  '|')]),
                'alarm_level': list(
                    [int(x.strip()) for x in self.alarm_level.text().split(':')[1].strip().split('|')]),
                'correct_coefficient': list([float(x.strip()) for x in
                                             self.correct_coefficient.text().split(':')[1].strip().split('|')]),

                'sql_write': bool(self.sql_write.isChecked()),
                'ip_sql': str(self.ip_sql.text().split(':')[1].strip()),
                'server_sql': str(self.server_sql.text().split(':')[1].strip()),
                'port_sql': str(self.port_sql.text().split(':')[1].strip()),
                'database_sql': str(self.database_sql.text().split(':')[1].strip()),
                'user_sql': str(self.user_sql.text().split(':')[1].strip()),
                'password_sql': str(self.password_sql.text().split(':')[1].strip()),
                'sql_now_check': bool(self.sql_now_check.isChecked()),
                'table_now_sql': str(self.table_now_sql.text().split(':')[1].strip()),
                'rows_now_sql': list(
                    [x.strip() for x in self.rows_now_sql.text().split(':')[1].strip().split('|')]),
                'sql_data_check': bool(self.sql_data_check.isChecked()),
                'table_data_sql': str(self.table_data_sql.text().split(':')[1].strip()),
                'rows_data_sql': list(
                    [x.strip() for x in self.rows_data_sql.text().split(':')[1].strip().split('|')]),

                'auto_import_check': bool(self.auto_import_check.isChecked()),
                'auto_play_check': bool(self.auto_play_check.isChecked()),
                'speed_analysis': float(self.speed_analysis.text().split(':')[1].strip()),
                'speed_video_stream': float(self.speed_video_stream.text().split(':')[1].strip()),

                'widget_write': bool(self.widget_write.isChecked()),
                'text_write': bool(self.text_write.isChecked()),
                'widget': self.set_data_func,
                'source_type': str(self.source_type.currentText().strip()),
                'compute_debug': str(self.compute_debug.currentText().strip()),
                'process_cores': int(self.process_cores.text().split(':')[1].strip()),
                'render_debug': str(self.render_debug.currentText().strip()),
                'resolution_debug': list(self.get_window_resolution()),

                'import_file': str(self.import_file.text().split(':')[1].strip()),

                'ip_cam_snapshot': str(self.ip_cam_snapshot.text().split(":")[1].strip()),
                'name_snapshot': str(self.name_snapshot.text().split(":")[1].strip()),
            }
            return data
        except Exception as ex:
            print(f'create_data_func error : {ex}')

    def play_btn_func(self):
        try:
            data = self.create_data_func()
            self.play_f(data=data)
        except Exception as ex:
            print(f'play_btn_func error : {ex}')

    def snapshot_btn_func(self):
        try:
            data = self.create_data_func()
            self.snapshot_f(data=data)
        except Exception as ex:
            print(f'snapshot_btn_func error : {ex}')

    def export_settings_func(self):
        try:
            data = self.create_data_func()
            del data['widget']
        except Exception as ex:
            print(f'export_settings_func error : {ex}')

    def import_settings_func(self):
        try:
            data = self.create_data_func()
            self.protocol_cam_type.setText(f'{self.protocol_cam_type.text().split(":")[0].strip()} : '
                                           f'{str(data["protocol_cam_type"])}')
            self.port_cam.setText(f'{self.port_cam.text().split(":")[0].strip()} : '
                                  f'{str(data["port_cam"])}')
            self.login_cam.setText(f'{self.login_cam.text().split(":")[0].strip()} : '
                                   f'{str(data["login_cam"])}')
            self.password_cam.setText(f'{self.password_cam.text().split(":")[0].strip()} : '
                                      f'{str(data["password_cam"])}')
            self.alias_device.setText(f'{self.alias_device.text().split(":")[0].strip()} : '
                                      f'{self.get_string_from_list(data["alias_device"])}')
            self.ip_cam.setText(f'{self.ip_cam.text().split(":")[0].strip()} : '
                                f'{self.get_string_from_list(data["ip_cam"])}')
            self.mask_cam.setText(f'{self.mask_cam.text().split(":")[0].strip()} : '
                                  f'{self.get_string_from_list(data["mask_cam"])}')
            self.sensitivity_analysis.setText(f'{self.sensitivity_analysis.text().split(":")[0].strip()} : '
                                              f'{self.get_string_from_list(data["sensitivity_analysis"])}')
            self.alarm_level.setText(f'{self.alarm_level.text().split(":")[0].strip()} : '
                                     f'{self.get_string_from_list(data["alarm_level"])}')
            self.correct_coefficient.setText(f'{self.correct_coefficient.text().split(":")[0].strip()} : '
                                             f'{self.get_string_from_list(data["correct_coefficient"])}')
            self.sql_write.setChecked(data["sql_write"])
            self.ip_sql.setText(f'{self.ip_sql.text().split(":")[0].strip()} : {str(data["ip_sql"])}')
            self.server_sql.setText(
                f'{self.server_sql.text().split(":")[0].strip()} : {str(data["server_sql"])}')
            self.port_sql.setText(f'{self.port_sql.text().split(":")[0].strip()} : {str(data["port_sql"])}')
            self.database_sql.setText(f'{self.database_sql.text().split(":")[0].strip()} : '
                                      f'{str(data["database_sql"])}')
            self.user_sql.setText(f'{self.user_sql.text().split(":")[0].strip()} : '
                                  f'{str(data["user_sql"])}')
            self.password_sql.setText(f'{self.password_sql.text().split(":")[0].strip()} : '
                                      f'{str(data["password_sql"])}')
            self.sql_now_check.setChecked(data["sql_now_check"])
            self.table_now_sql.setText(f'{self.table_now_sql.text().split(":")[0].strip()} : '
                                       f'{str(data["table_now_sql"])}')
            self.rows_now_sql.setText(f'{self.rows_now_sql.text().split(":")[0].strip()} : '
                                      f'{self.get_string_from_list(data["rows_now_sql"])}')
            self.sql_data_check.setChecked(data["sql_data_check"])
            self.table_data_sql.setText(f'{self.table_data_sql.text().split(":")[0].strip()} : '
                                        f'{str(data["table_data_sql"])}')
            self.rows_data_sql.setText(f'{self.rows_data_sql.text().split(":")[0].strip()} : '
                                       f'{self.get_string_from_list(data["rows_data_sql"])}')
            self.auto_import_check.setChecked(data["auto_import_check"])
            self.auto_play_check.setChecked(data["auto_play_check"])
            self.speed_analysis.setText(f'{self.speed_analysis.text().split(":")[0].strip()} : '
                                        f'{str(data["speed_analysis"])}')
            self.speed_video_stream.setText(f'{self.speed_video_stream.text().split(":")[0].strip()} : '
                                            f'{str(data["speed_video_stream"])}')
            self.widget_write.setChecked(data["widget_write"])
            self.text_write.setChecked(data["text_write"])
            self.source_type.setCurrentText(data["source_type"])
            self.compute_debug.setCurrentText(data["compute_debug"])
            self.process_cores.setText(f'{self.process_cores.text().split(":")[0].strip()} : '
                                       f'{str(data["process_cores"])}')
            self.render_debug.setCurrentText(data["render_debug"])
            self.set_window_resolution(data["resolution_debug"])
            self.import_file.setText(f'{self.import_file.text().split(":")[0].strip()} : '
                                     f'{str(data["import_file"])}')
            self.ip_cam_snapshot.setText(f'{self.ip_cam_snapshot.text().split(":")[0].strip()} : '
                                         f'{str(data["ip_cam_snapshot"])}')
            self.name_snapshot.setText(f'{self.name_snapshot.text().split(":")[0].strip()} : '
                                       f'{str(data["name_snapshot"])}')
        except Exception as ex:
            print(f'import_settings_func error : {ex}')

    def auto_import_settings_func(self):
        try:
            data = self.create_data_func()
            if data['auto_import_check']:
                self.import_settings_func()
        except Exception as ex:
            print(f'auto_import_settings_func error : {ex}')

    def auto_play_func(self):
        pass


def play_func(data: dict):
    global play
    try:
        play = True

        def play_analyze():
            pass

        pass
    except Exception as ex:
        print(ex)
        with open('log.txt', 'a') as log:
            log.write(f'\n{ex}\n')


def stop_func():
    global play
    play = False


def pause():
    global play
    return play


def quit_func():
    stop_func()
    sys.exit(app_container.app.exec())


def snapshot_func(data: dict):
    pass


# MAIN
if __name__ == "__main__":
    multiprocessing.freeze_support()
    play = True
    app_container = AppContainerClass()
    widget = app_container.create_ui(title="analysis", width=300, height=300, icon="icon.ico",
                                     play_f=play_func, stop_f=stop_func, quit_f=quit_func,
                                     snapshot_f=snapshot_func)
    ui_thread = threading.Thread(target=widget.show())
    sys.exit(app_container.app.exec())

########################################################################################################################
