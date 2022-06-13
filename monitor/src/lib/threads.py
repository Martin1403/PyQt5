import threading
from time import sleep

from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, QCoreApplication, QPoint, QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QMovie

from .data.gathering import start_monitor
from .data.storage import get_storage

data: dict = get_storage()


class IntroProgress(QThread):
    countChanged = pyqtSignal(int)

    def run(self):
        Monitor().start()
        for i in range(101):
            self.countChanged.emit(i)
            sleep(0.05)


class Monitor(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()
        self.name = "Monitor"

    def run(self) -> None:
        while data.get('alive') and not self.event.is_set():
            start_monitor()

    def stop(self) -> None:
        self.event.set()
