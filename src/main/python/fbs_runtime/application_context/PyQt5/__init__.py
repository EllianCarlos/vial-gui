import sys
from PyQt5.QtWidgets import QApplication
from fbs_runtime.application_context import _ApplicationContext

class ApplicationContext(_ApplicationContext):
    def __init__(self):
        self._app = QApplication(sys.argv)
        super().__init__()
