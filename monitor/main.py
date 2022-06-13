#!usr/bin/python3
# -*- coding: utf-8 -*-
import os
import re
import sys
from PyQt5.QtCore import Qt, QTimer, QCoreApplication, QPoint
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QMovie

from src.untitled import Ui_MainWindow
from src.lib.threads import IntroProgress
from src.lib.data.storage import get_storage

data: dict = get_storage()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.resize(800, 605)
        # REMOVE TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)
        # CENTER WINDOW
        self.center()
        # VARIABLES
        self.m_enable = False
        self.oldPos = self.pos()
        self.translate = QCoreApplication.translate
        # MOVIE
        self.stackedWidget.setCurrentWidget(self.page_1)
        self.movie = QMovie(os.path.join(os.path.dirname(__file__), "data/movies/intro.gif"))
        self.labelMovie.setMovie(self.movie)
        self.movie.start()

        # PUSH BUTTONS
        self.pushButtonClose_1.clicked.connect(self.close_window)
        self.pushButton_minimize_1.clicked.connect(self.minimized)
        self.pushButton_maximize_1.clicked.connect(self.maximized)
        self.pushButton_monitor.clicked.connect(self.monitor)
        self.pushButton_docker.clicked.connect(self.docker)

        # THREADS
        self.count = IntroProgress()
        self.count.countChanged.connect(self.intro_page)
        self.count.start()

        # TIMERS
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(10)

    def mousePressEvent(self, event):
        if event.button() == 1 and event.pos() in self.mouse_frame_1.geometry():
            self.m_enable = True
            self.oldPos = event.globalPos()
        else:
            self.m_enable = False

    def mouseMoveEvent(self, event):
        if self.m_enable:
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    def center(self):
        frame_geometry = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        center_point = QApplication.desktop().screenGeometry(screen).center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())

    def minimized(self):
        self.showMinimized()

    def maximized(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    @staticmethod
    def close_window():
        global data
        data['alive'] = False
        sys.exit(0)

    def intro_page(self, value):
        self.progressBar.setProperty("value", value)
        if value == 100:
            self.resize(1024, 800)
            self.stackedWidget.setCurrentWidget(self.page_2)
            self.monitor()
            self.movie.stop()

    def monitor(self):
        self.stackedWidgetMenu.setCurrentWidget(self.pageMenu)
        self.page_set('monitor')

    def docker(self):
        self.stackedWidgetMenu.setCurrentWidget(self.pageDocker)
        self.page_set('docker')

    def page_set(self, page):
        sheet = "QPushButton {border: 0px solid;border-image:url(:/icons/LABEL_off.png);}" \
                "QPushButton:hover {border: 0px solid;border-image:url(:/icons/LABEL_on.png);}" \
                "QPushButton:focus {border: 0px solid;border-image: url(:/icons/LABEL_on.png);}"
        # RESET BUTTONS:
        for button in ['monitor', 'docker']:
            reset = re.sub('LABEL', button, sheet)
            exec("self.pushButton_{0}.setStyleSheet(reset)".format(button))
        # SET ACTIVE BUTTON:
        sheet = re.sub('LABEL', page, sheet)
        sheet = re.sub('off', 'on', sheet)
        exec("self.pushButton_{0}.setStyleSheet(sheet)".format(page))

    def progress(self):
        global data
        # TRAFFIC
        traffic = data.get('stats').get('traffic')
        if traffic:
            for c, (device, values) in enumerate(traffic.items()):
                item = self.tableWidgetTraffic.item(c, 0)
                item.setText(self.translate("MainWindow", f"  {device}"))
                item = self.tableWidgetTraffic.item(c, 1)
                item.setText(self.translate("MainWindow", f"  {values[0]}"))
                item = self.tableWidgetTraffic.item(c, 2)
                item.setText(self.translate("MainWindow", f"  {values[1]}"))

        # CPU
        cpu = data.get('stats').get('cpu')
        if cpu:
            color = 255 - int(cpu.get('percent') * 2.55)
            self.labelCpuPercent.setStyleSheet(f"border: none;color: rgb(255,{color},{color});")
            self.labelCpuPercent.setText(self.translate("MainWindow", f"{cpu.get('percent')}%"))
            self.frameCpuColor.setStyleSheet(
                re.sub('C', str(color), "QFrame{border: 5px solid rgb(255, C, C);border-radius: 125px;}"))
            self.labelCpuTemp.setStyleSheet(f"border: none;color: rgb(255, {color}, {color});")
            self.labelCpuTemp.setText(self.translate("MainWindow", f"Temp: {cpu.get('temp')} °C"))
            self.labelCpu.setStyleSheet(f"border: none;color: rgb(255, {color}, {color});")
            self.labelCpuCore.setStyleSheet(f"border: none;color: rgb(255, {color}, {color});")
            self.labelCpuCore.setText(self.translate("MainWindow", f"Cores: {cpu.get('cores')}"))
        # MEMO
        memo = data.get('stats').get('memo')
        if memo:
            color = 255 - int(memo.get('percent') * 2.55)
            # memo.percent, memo.free, memo.total
            self.labelMemoPercent.setStyleSheet(f"border: none;color: rgb(255,{color},{color});")
            self.labelMemoPercent.setText(self.translate("MainWindow", f"{memo.get('percent')}%"))
            self.labelMemo.setStyleSheet(f"border: none;color: rgb(255, {color}, {color});")
            self.labelMemoFree.setStyleSheet(f"border: none;color: rgb(255, {color}, {color});")
            self.labelMemoFree.setText(self.translate("MainWindow", f"Free: {memo.get('free')} Gb"))
            self.labelMemoTotal.setStyleSheet(f"border: none;color: rgb(255, {color}, {color});")
            self.labelMemoTotal.setText(self.translate("MainWindow", f"Total: {memo.get('total')}Gb"))
            self.frameMemoColor.setStyleSheet(
                re.sub('C', str(color), "QFrame{border: 5px solid rgb(255, C, C);border-radius: 125px;}"))
        # GPU
        gpu = data.get('stats').get('gpu')
        if gpu:
            color = 255 - int(gpu.get('percent') * 2.55)
            self.labelGpuPercent.setStyleSheet(f"border: none;color: rgb(255,{color},{color});")
            self.labelGpuPercent.setText(self.translate("MainWindow", f"{gpu.get('percent')}%"))
            self.labelGpu.setStyleSheet(f"border: none;color: rgb(255, {color}, {color});")
            self.labelGpuFree.setStyleSheet(f"border: none;color: rgb(255, {color}, {color});")
            self.labelGpuFree.setText(self.translate("MainWindow", f"Free: {gpu.get('free')} Gb"))
            self.labelGpuTotal.setStyleSheet(f"border: none;color: rgb(255, {color}, {color});")
            self.labelGpuTotal.setText(self.translate("MainWindow", f"Total: {gpu.get('total')}Gb"))
            self.frameGpuColor.setStyleSheet(
                re.sub('C', str(color), "QFrame{border: 5px solid rgb(255, C, C);border-radius: 125px;}"))
            self.labelGpu.setText(self.translate("MainWindow", "GPU USAGE"))
        else:
            color = 255
            self.labelGpuPercent.setStyleSheet(f"border: none;color: rgb(255,{color},{color});")
            self.labelGpuPercent.setText(self.translate("MainWindow", "0%"))
            self.labelGpu.setStyleSheet(f"border: none;color: rgb(255, 0, 0);")
            self.labelGpuFree.setStyleSheet(f"border: none;color: rgb(255, {color}, {color});")
            self.labelGpuFree.setText(self.translate("MainWindow", "Free: None"))
            self.labelGpuTotal.setStyleSheet(f"border: none;color: rgb(255, {color}, {color});")
            self.labelGpuTotal.setText(self.translate("MainWindow", "Total: None"))
            self.frameGpuColor.setStyleSheet(
                re.sub('C', str(color), "QFrame{border: 5px solid rgb(255, C, C);border-radius: 125px;}"))
            self.labelGpu.setText(self.translate("MainWindow", "GPU NONE"))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return sys.exit(app.exec_())


if __name__ == '__main__':
    main()


