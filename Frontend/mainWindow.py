from tkinter import *
import Frontend.errorWindow as error
import Frontend.progressWindow as progress
import Frontend.resultWindow as result
import Frontend.mainView as mv
import Frontend.progressView as pv

class mainWindow:
    def __init__(self):
        self.tk = Tk()
        self.tk.minsize(width=600,height=600)
        self.tk.title("Machine Learning - Classification")
        # ncV = ncv.newClassifierView(self.tk)
        mV = mv.mainView(self.tk)
        mV.show()
        # self.initComponents()
        self.pV = pv.progressView(self.tk)
        # self.pV.show()
        self.tk.mainloop()

if __name__ == '__main__':
    # result.resultWindow("Result\n abc")
    # error.errorWindow("Error !")

    mw = mainWindow()
    # error.errorWindow("Error !")







