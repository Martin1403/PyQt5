import sys
from PyQt5.QtCore import Qt, QCoreApplication, QPoint
from PyQt5.QtWidgets import QMainWindow, QApplication

from src.untitled import Ui_MainWindow


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

        # PUSH BUTTONS
        self.pushButtonClose.clicked.connect(self.close_window)
        self.pushButtonMinimize.clicked.connect(self.minimized)
        self.pushButtonMaximize.clicked.connect(self.maximized)

    def mousePressEvent(self, event):
        if event.button() == 1 and event.pos() in self.frame_mouse.geometry():
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

    def close_window(self):
        self.close()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return sys.exit(app.exec_())


if __name__ == '__main__':
    main()
