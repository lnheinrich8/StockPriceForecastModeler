# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(570, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(570, 600))
        MainWindow.setMaximumSize(QSize(570, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 0, 531, 571))
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.graph_placeholder_widget = QWidget(self.tab1)
        self.graph_placeholder_widget.setObjectName(u"graph_placeholder_widget")
        self.graph_placeholder_widget.setGeometry(QRect(29, 70, 471, 421))
        self.layoutWidget = QWidget(self.tab1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 490, 304, 26))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.window10_button = QPushButton(self.layoutWidget)
        self.window10_button.setObjectName(u"window10_button")
        self.window10_button.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.window10_button)

        self.window50_button = QPushButton(self.layoutWidget)
        self.window50_button.setObjectName(u"window50_button")
        self.window50_button.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.window50_button)

        self.window100_button = QPushButton(self.layoutWidget)
        self.window100_button.setObjectName(u"window100_button")
        self.window100_button.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.window100_button)

        self.window500_button = QPushButton(self.layoutWidget)
        self.window500_button.setObjectName(u"window500_button")
        self.window500_button.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_3.addWidget(self.window500_button)

        self.window1000_button = QPushButton(self.layoutWidget)
        self.window1000_button.setObjectName(u"window1000_button")
        self.window1000_button.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_3.addWidget(self.window1000_button)

        self.windowmax_button = QPushButton(self.layoutWidget)
        self.windowmax_button.setObjectName(u"windowmax_button")
        self.windowmax_button.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_3.addWidget(self.windowmax_button)

        self.cols_combobox = QComboBox(self.tab1)
        self.cols_combobox.setObjectName(u"cols_combobox")
        self.cols_combobox.setGeometry(QRect(56, 50, 72, 20))
        self.choose_ticker_label = QLabel(self.tab1)
        self.choose_ticker_label.setObjectName(u"choose_ticker_label")
        self.choose_ticker_label.setGeometry(QRect(20, 13, 31, 16))
        self.ticker_combobox = QComboBox(self.tab1)
        self.ticker_combobox.setObjectName(u"ticker_combobox")
        self.ticker_combobox.setGeometry(QRect(56, 10, 72, 24))
        self.createmodel_button = QPushButton(self.tab1)
        self.createmodel_button.setObjectName(u"createmodel_button")
        self.createmodel_button.setGeometry(QRect(327, 14, 80, 24))
        self.forecast_button = QPushButton(self.tab1)
        self.forecast_button.setObjectName(u"forecast_button")
        self.forecast_button.setGeometry(QRect(406, 14, 80, 24))
        self.forecast_progress_label = QLabel(self.tab1)
        self.forecast_progress_label.setObjectName(u"forecast_progress_label")
        self.forecast_progress_label.setGeometry(QRect(410, 40, 69, 16))
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.tabWidget.addTab(self.tab2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 570, 21))
        palette = QPalette()
        brush = QBrush(QColor(145, 145, 145, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(111, 111, 111, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.menubar.setPalette(palette)
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(False)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.window10_button.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.window50_button.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.window100_button.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.window500_button.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.window1000_button.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.windowmax_button.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.choose_ticker_label.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.createmodel_button.setText(QCoreApplication.translate("MainWindow", u"Create Model", None))
        self.forecast_button.setText(QCoreApplication.translate("MainWindow", u"Forecast", None))
        self.forecast_progress_label.setText(QCoreApplication.translate("MainWindow", u"Forecasting...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"Model Builder", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

