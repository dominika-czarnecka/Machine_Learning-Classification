from unittest import TestCase
from Frontend import mainWindow

class TestMainWindow(TestCase):
    def test1(self):
        mw = mainWindow()
        self.assertEquals(mw,mainWindow())