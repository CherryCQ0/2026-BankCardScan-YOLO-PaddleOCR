# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'yoloQt.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSlider, QSplitter, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1197, 777)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(6)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"icon/1000LOGO.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"background-color:white;}\n"
"")
        self.gridLayoutWidget_7 = QWidget(self.centralwidget)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(0, 720, 881, 51))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.progressBar = QProgressBar(self.gridLayoutWidget_7)
        self.progressBar.setObjectName(u"progressBar")
        palette = QPalette()
        brush = QBrush(QColor(142, 197, 252, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(215, 215, 215, 100))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        brush2 = QBrush(QColor(142, 197, 252, 128))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush2)
#endif
        self.progressBar.setPalette(palette)
        self.progressBar.setStyleSheet(u"\n"
"QProgressBar{ \n"
"height:5px;\n"
"color: #8EC5FC; \n"
"text-align:center; \n"
"border:3px solid rgb(255, 255, 255);\n"
"border-radius: 5px; \n"
"background-color: rgba(215, 215, 215,100);\n"
"} \n"
"\n"
"QProgressBar:chunk{ \n"
"border-radius:0px; \n"
"background:  #6BABFA;\n"
"border-radius: 7px;\n"
"}")
        self.progressBar.setValue(0)

        self.gridLayout_7.addWidget(self.progressBar, 0, 1, 1, 1)

        self.pushButton_bofang = QPushButton(self.gridLayoutWidget_7)
        self.pushButton_bofang.setObjectName(u"pushButton_bofang")
        self.pushButton_bofang.setMinimumSize(QSize(32, 32))
        self.pushButton_bofang.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_bofang.setStyleSheet(u"border: none")
        icon1 = QIcon()
        icon1.addFile(u"icon/\u64ad\u653e.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_bofang.setIcon(icon1)
        self.pushButton_bofang.setIconSize(QSize(32, 32))

        self.gridLayout_7.addWidget(self.pushButton_bofang, 0, 0, 1, 1)

        self.pushButton_stop = QPushButton(self.gridLayoutWidget_7)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setMinimumSize(QSize(32, 32))
        self.pushButton_stop.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_stop.setStyleSheet(u"border: none")
        icon2 = QIcon()
        icon2.addFile(u"icon/\u7ec8\u6b62.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_stop.setIcon(icon2)
        self.pushButton_stop.setIconSize(QSize(32, 32))

        self.gridLayout_7.addWidget(self.pushButton_stop, 0, 2, 1, 1)

        self.horizontalFrame = QFrame(self.centralwidget)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setGeometry(QRect(0, 0, 1191, 71))
        self.horizontalFrame.setStyleSheet(u"background:#7B68EE;color:white;")
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_title = QLabel(self.horizontalFrame)
        self.label_title.setObjectName(u"label_title")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(28)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"")
        self.label_title.setTextFormat(Qt.TextFormat.AutoText)
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_title)

        self.frame_left_box = QFrame(self.centralwidget)
        self.frame_left_box.setObjectName(u"frame_left_box")
        self.frame_left_box.setGeometry(QRect(890, 70, 301, 701))
        self.frame_left_box.setStyleSheet(u"QFrame#frame_left_box{\n"
"background:#F1F6FF;\n"
"border: 1px solid #F1F6FF;\n"
"border-radius:8px;}")
        self.frame_left_box.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_left_box.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_weights_box = QFrame(self.frame_left_box)
        self.frame_weights_box.setObjectName(u"frame_weights_box")
        self.frame_weights_box.setGeometry(QRect(10, 10, 281, 121))
        self.frame_weights_box.setStyleSheet(u"QFrame#frame_weights_box{border:2px solid #E6E6FA;\n"
"background:white;\n"
"border-radius:8px;}")
        self.frame_weights_box.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_weights_box.setFrameShadow(QFrame.Shadow.Raised)
        self.line_weights = QLineEdit(self.frame_weights_box)
        self.line_weights.setObjectName(u"line_weights")
        self.line_weights.setGeometry(QRect(10, 60, 211, 41))
        font2 = QFont()
        font2.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53"])
        font2.setPointSize(11)
        self.line_weights.setFont(font2)
        self.line_weights.setStyleSheet(u"padding-left:6px;\n"
"border:1px solid skyblue;\n"
"border-radius:5px;\n"
"\n"
"\n"
"\n"
"")
        self.line_weights.setEchoMode(QLineEdit.EchoMode.Normal)
        self.line_weights.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.Button_select_w_p = QPushButton(self.frame_weights_box)
        self.Button_select_w_p.setObjectName(u"Button_select_w_p")
        self.Button_select_w_p.setGeometry(QRect(230, 60, 41, 41))
        self.Button_select_w_p.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Button_select_w_p.setStyleSheet(u"border: none")
        icon3 = QIcon()
        icon3.addFile(u"icon/model.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_select_w_p.setIcon(icon3)
        self.Button_select_w_p.setIconSize(QSize(32, 32))
        self.frame_11 = QFrame(self.frame_weights_box)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(0, 0, 281, 41))
        self.frame_11.setStyleSheet(u"border:1px solid #E6E6FA;\n"
"background:#E6E6FA;\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8;\n"
"border-bottom-left-radius: 0;\n"
"border-bottom-right-radius: 0px;")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame_11)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 261, 41))
        font3 = QFont()
        font3.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53"])
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setHintingPreference(QFont.PreferFullHinting)
        self.label.setFont(font3)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet(u"background:#E6E6FA;\n"
"border:none;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_source_box = QFrame(self.frame_left_box)
        self.frame_source_box.setObjectName(u"frame_source_box")
        self.frame_source_box.setGeometry(QRect(10, 140, 281, 121))
        self.frame_source_box.setStyleSheet(u"QFrame#frame_source_box{border:2px solid #E6E6FA;\n"
"background:white;\n"
"\n"
"border-radius:8px;}")
        self.frame_source_box.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_source_box.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_13 = QFrame(self.frame_source_box)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(0, 0, 281, 41))
        self.frame_13.setStyleSheet(u"border:1px solid #E6E6FA;\n"
"background:#E6E6FA;\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8;\n"
"border-bottom-left-radius: 0;\n"
"border-bottom-right-radius: 0px;")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.label_3 = QLabel(self.frame_13)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 0, 261, 41))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"background:#E6E6FA;\n"
"border:none;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter = QSplitter(self.frame_source_box)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(20, 60, 261, 38))
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.Button_checkImg = QPushButton(self.splitter)
        self.Button_checkImg.setObjectName(u"Button_checkImg")
        self.Button_checkImg.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Button_checkImg.setStyleSheet(u"border: none;")
        icon4 = QIcon()
        icon4.addFile(u"icon/img.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_checkImg.setIcon(icon4)
        self.Button_checkImg.setIconSize(QSize(38, 38))
        self.splitter.addWidget(self.Button_checkImg)
        self.Button_checkVideo = QPushButton(self.splitter)
        self.Button_checkVideo.setObjectName(u"Button_checkVideo")
        self.Button_checkVideo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Button_checkVideo.setStyleSheet(u"border: none")
        icon5 = QIcon()
        icon5.addFile(u"icon/video.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_checkVideo.setIcon(icon5)
        self.Button_checkVideo.setIconSize(QSize(38, 38))
        self.splitter.addWidget(self.Button_checkVideo)
        self.Button_openCamera = QPushButton(self.splitter)
        self.Button_openCamera.setObjectName(u"Button_openCamera")
        self.Button_openCamera.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Button_openCamera.setStyleSheet(u"border: none")
        icon6 = QIcon()
        icon6.addFile(u"icon/camera.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_openCamera.setIcon(icon6)
        self.Button_openCamera.setIconSize(QSize(38, 38))
        self.splitter.addWidget(self.Button_openCamera)
        self.frame_source_box_2 = QFrame(self.frame_left_box)
        self.frame_source_box_2.setObjectName(u"frame_source_box_2")
        self.frame_source_box_2.setGeometry(QRect(10, 450, 281, 161))
        self.frame_source_box_2.setStyleSheet(u"QFrame#frame_source_box{border:2px solid #E6E6FA;\n"
"background:white;\n"
"\n"
"border-radius:8px;}")
        self.frame_source_box_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_source_box_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_14 = QFrame(self.frame_source_box_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(0, 0, 281, 41))
        self.frame_14.setStyleSheet(u"border:1px solid #E6E6FA;\n"
"background:#E6E6FA;\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8;\n"
"border-bottom-left-radius: 0;\n"
"border-bottom-right-radius: 0px;")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.label_4 = QLabel(self.frame_14)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 0, 261, 41))
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"background:#E6E6FA;\n"
"border:none;")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layoutWidget = QWidget(self.frame_source_box_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 60, 231, 33))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_nums = QLabel(self.layoutWidget)
        self.label_nums.setObjectName(u"label_nums")
        palette1 = QPalette()
        brush3 = QBrush(QColor(255, 0, 0, 255))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush3)
        brush4 = QBrush(QColor(102, 218, 241, 255))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush4)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush5)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush4)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush4)
        brush6 = QBrush(QColor(255, 0, 0, 128))
        brush6.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush3)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush4)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush5)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush4)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush6)
#endif
        brush7 = QBrush(QColor(120, 120, 120, 255))
        brush7.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush7)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush4)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush7)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush4)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush4)
        brush8 = QBrush(QColor(0, 0, 0, 128))
        brush8.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush8)
#endif
        self.label_nums.setPalette(palette1)
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(16)
        font4.setBold(False)
        self.label_nums.setFont(font4)
        self.label_nums.setStyleSheet(u"")
        self.label_nums.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_nums)

        self.layoutWidget1 = QWidget(self.frame_source_box_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 110, 231, 33))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.layoutWidget1)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_3.addWidget(self.label_10)

        self.label_times = QLabel(self.layoutWidget1)
        self.label_times.setObjectName(u"label_times")
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush3)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush4)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush5)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush4)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush6)
#endif
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush3)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush4)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush5)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush4)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush6)
#endif
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush7)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush4)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush7)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush4)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush8)
#endif
        self.label_times.setPalette(palette2)
        self.label_times.setFont(font4)
        self.label_times.setStyleSheet(u"")
        self.label_times.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_times)

        self.frame_iou_box = QFrame(self.frame_left_box)
        self.frame_iou_box.setObjectName(u"frame_iou_box")
        self.frame_iou_box.setGeometry(QRect(10, 360, 281, 81))
        self.frame_iou_box.setStyleSheet(u"QFrame#frame_iou_box{border:2px solid #E6E6FA;\n"
"background:white;\n"
"border-radius:8px;}")
        self.frame_iou_box.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_iou_box.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_16 = QFrame(self.frame_iou_box)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(0, 0, 281, 41))
        self.frame_16.setStyleSheet(u"border:1px solid #CFEBD2;\n"
"background:#CFEBD2;\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8;\n"
"border-bottom-left-radius: 0;\n"
"border-bottom-right-radius: 0px;")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.label_12 = QLabel(self.frame_16)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 0, 281, 41))
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"background:#E6E6FA;\n"
"border:none;")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBox_iou = QDoubleSpinBox(self.frame_iou_box)
        self.doubleSpinBox_iou.setObjectName(u"doubleSpinBox_iou")
        self.doubleSpinBox_iou.setGeometry(QRect(20, 50, 71, 21))
        self.doubleSpinBox_iou.setMaximum(1.000000000000000)
        self.doubleSpinBox_iou.setSingleStep(0.010000000000000)
        self.doubleSpinBox_iou.setValue(0.700000000000000)
        self.horizontalSlider_iou = QSlider(self.frame_iou_box)
        self.horizontalSlider_iou.setObjectName(u"horizontalSlider_iou")
        self.horizontalSlider_iou.setGeometry(QRect(120, 50, 141, 22))
        self.horizontalSlider_iou.setStyleSheet(u"QSlider::groove:horizontal {\n"
"            border: none;\n"
"            height: 5px;\n"
"            background-color: lightgray;\n"
"		 border-radius: 5px;\n"
"        }\n"
"\n"
"        QSlider::handle:horizontal {\n"
"            background-color: #2f77cb;\n"
"            width: 8px;\n"
"            margin: -9px 0px -9px 0px;\n"
"            border-radius: 4px;\n"
"        }\n"
"\n"
"        QSlider::sub-page:horizontal {\n"
"            background-color: #4898ec;\n"
"border-radius: 5px;\n"
"        }\n"
"\n"
"\n"
"")
        self.horizontalSlider_iou.setMaximum(100)
        self.horizontalSlider_iou.setPageStep(10)
        self.horizontalSlider_iou.setValue(70)
        self.horizontalSlider_iou.setSliderPosition(70)
        self.horizontalSlider_iou.setOrientation(Qt.Orientation.Horizontal)
        self.frame_conf_box = QFrame(self.frame_left_box)
        self.frame_conf_box.setObjectName(u"frame_conf_box")
        self.frame_conf_box.setGeometry(QRect(10, 270, 281, 81))
        self.frame_conf_box.setStyleSheet(u"QFrame#frame_conf_box{border:2px solid #E6E6FA;\n"
"background:white;\n"
"border-radius:8px;}")
        self.frame_conf_box.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_conf_box.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_15 = QFrame(self.frame_conf_box)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(0, 0, 281, 41))
        self.frame_15.setStyleSheet(u"border:1px solid #E6E6FA;\n"
"background:#E6E6FA;\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8;\n"
"border-bottom-left-radius: 0;\n"
"border-bottom-right-radius: 0px;")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.label_11 = QLabel(self.frame_15)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 0, 271, 41))
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"background:#E6E6FA;\n"
"border:none;")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalSlider_conf = QSlider(self.frame_conf_box)
        self.horizontalSlider_conf.setObjectName(u"horizontalSlider_conf")
        self.horizontalSlider_conf.setGeometry(QRect(110, 50, 141, 22))
        self.horizontalSlider_conf.setStyleSheet(u"QSlider::groove:horizontal {\n"
"            border: none;\n"
"            height: 5px;\n"
"            background-color: lightgray;\n"
"		 border-radius: 5px;\n"
"        }\n"
"\n"
"        QSlider::handle:horizontal {\n"
"            background-color: #2f77cb;\n"
"            width: 8px;\n"
"            margin: -9px 0px -9px 0px;\n"
"            border-radius: 4px;\n"
"        }\n"
"\n"
"        QSlider::sub-page:horizontal {\n"
"            background-color: #4898ec;\n"
"border-radius: 5px;\n"
"        }\n"
"\n"
"\n"
"")
        self.horizontalSlider_conf.setMaximum(100)
        self.horizontalSlider_conf.setPageStep(10)
        self.horizontalSlider_conf.setValue(25)
        self.horizontalSlider_conf.setSliderPosition(25)
        self.horizontalSlider_conf.setOrientation(Qt.Orientation.Horizontal)
        self.doubleSpinBox_conf = QDoubleSpinBox(self.frame_conf_box)
        self.doubleSpinBox_conf.setObjectName(u"doubleSpinBox_conf")
        self.doubleSpinBox_conf.setGeometry(QRect(20, 50, 71, 21))
        self.doubleSpinBox_conf.setMaximum(1.000000000000000)
        self.doubleSpinBox_conf.setSingleStep(0.010000000000000)
        self.doubleSpinBox_conf.setValue(0.250000000000000)
        self.frame_is_save_box = QFrame(self.frame_left_box)
        self.frame_is_save_box.setObjectName(u"frame_is_save_box")
        self.frame_is_save_box.setEnabled(True)
        self.frame_is_save_box.setGeometry(QRect(10, 620, 281, 61))
        self.frame_is_save_box.setStyleSheet(u"QFrame#frame_is_save_box{\n"
"background:#7B68EE;}")
        self.frame_is_save_box.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_is_save_box.setFrameShadow(QFrame.Shadow.Raised)
        self.checkBox_isSave = QCheckBox(self.frame_is_save_box)
        self.checkBox_isSave.setObjectName(u"checkBox_isSave")
        self.checkBox_isSave.setGeometry(QRect(180, 10, 51, 41))
        font5 = QFont()
        font5.setPointSize(16)
        self.checkBox_isSave.setFont(font5)
        self.checkBox_isSave.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_isSave.setIconSize(QSize(40, 40))
        self.checkBox_isSave.setChecked(True)
        self.label_isSava = QLabel(self.frame_is_save_box)
        self.label_isSava.setObjectName(u"label_isSava")
        self.label_isSava.setGeometry(QRect(0, 0, 171, 61))
        font6 = QFont()
        font6.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53"])
        font6.setPointSize(16)
        font6.setBold(True)
        self.label_isSava.setFont(font6)
        self.label_isSava.setStyleSheet(u"color:white;")
        self.label_isSava.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_result_box = QFrame(self.centralwidget)
        self.frame_result_box.setObjectName(u"frame_result_box")
        self.frame_result_box.setEnabled(True)
        self.frame_result_box.setGeometry(QRect(0, 70, 881, 641))
        self.frame_result_box.setStyleSheet(u"QFrame#frame_result_box{\n"
"border:2px solid #6BABFA;\n"
"}")
        self.frame_result_box.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_result_box.setFrameShadow(QFrame.Shadow.Raised)
        self.label_result = QLabel(self.frame_result_box)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setGeometry(QRect(10, 10, 861, 621))
        self.label_result.setStyleSheet(u"")
        self.label_result.setPixmap(QPixmap(u"icon/zhengshidabian.png"))
        self.label_result.setScaledContents(False)
        self.label_result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
#if QT_CONFIG(tooltip)
        self.pushButton_bofang.setToolTip(QCoreApplication.translate("MainWindow", u"\u6682\u505c/\u5f00\u542f\u68c0\u6d4b", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_bofang.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_stop.setToolTip(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u68c0\u6d4b", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_stop.setText("")
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u4e8eYOLO12\u94f6\u884c\u5361\u53f7\u68c0\u6d4b\u7cfb\u7edf", None))
        self.line_weights.setInputMask("")
        self.line_weights.setText(QCoreApplication.translate("MainWindow", u"yolov8n.pt", None))
        self.line_weights.setPlaceholderText("")
        self.Button_select_w_p.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6743\u91cd", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u68c0\u6d4b\u8d44\u6e90", None))
#if QT_CONFIG(tooltip)
        self.Button_checkImg.setToolTip(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u5355\u5f20\u56fe\u7247", None))
#endif // QT_CONFIG(tooltip)
        self.Button_checkImg.setText("")
#if QT_CONFIG(tooltip)
        self.Button_checkVideo.setToolTip(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u89c6\u9891\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.Button_checkVideo.setText("")
#if QT_CONFIG(tooltip)
        self.Button_openCamera.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u68c0\u6d4b\u6444\u50cf\u5934</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Button_openCamera.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u7ed3\u679c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">\u76ee\u6807\u603b\u6570\uff1a</span></p></body></html>", None))
        self.label_nums.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">\u82b1\u8d39\u65f6\u95f4\uff1a</span></p></body></html>", None))
        self.label_times.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"IOU", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"conf", None))
#if QT_CONFIG(tooltip)
        self.checkBox_isSave.setToolTip(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u4fdd\u5b58\u5728\u5f53\u524d\u76ee\u5f55runs\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_isSave.setText("")
#if QT_CONFIG(tooltip)
        self.label_isSava.setToolTip(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u4fdd\u5b58\u5728\u5f53\u524d\u76ee\u5f55runs\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
        self.label_isSava.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u4fdd\u5b58\u7ed3\u679c\uff1a", None))
        self.label_result.setText("")
    # retranslateUi

