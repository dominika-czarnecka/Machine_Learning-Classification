from tkinter import *
import Frontend.errorWindow as error
import Frontend.progressWindow as progress
import Frontend.resultWindow as result
import Frontend.mainView as mv
import Frontend.newClassifierView as ncv


class mainWindow:
    def __init__(self):
        self.tk = Tk()
        self.tk.minsize(width=600,height=100)
        self.tk.title("Machine Learning - Classification")
        # ncV = ncv.newClassifierView(self.tk)
        mV = mv.mainView(self.tk)
        mV.show()
        # self.initComponents()

        self.tk.mainloop()

if __name__ == '__main__':
    # result.resultWindow("Result")
    mw = mainWindow()
    # error.errorWindow("Error !")







