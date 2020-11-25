from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from qt5_file.ui import Ui_MainWindow
from decoder.sudokuClass import Sudoku
from Img2text import img2text
from pathlib import Path
from functions.reset import reset_func
from functions.adding import additem_func
from functions.getting import getValues_func
from functions.errors import error, error2
import sys


def getValues():
    matrix = getValues_func(ui)
    solution_func(matrix)
     
def openFile():
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(Qmain, 
                    "QFileDialog.getOpenFileName()", 
                    options=options)
    if fileName:
        matrix = img2text.solver(fileName)
        if not matrix:
            return error2(Qmain)
        return solution_func(matrix)
    else:
        return

def solution_func(matrix):
    solution = Sudoku(matrix)
    if solution.flag:
        return additem(solution)
    else:
        error(Qmain)

def additem(solution):
    return additem_func(ui,solution)

def mainReset():
    return reset_func(ui)
   
   
app = QApplication(sys.argv)
Qmain = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(Qmain)
ui.Button.clicked.connect(getValues)
ui.Button_2.clicked.connect(mainReset)
ui.Button_3.clicked.connect(openFile)

Qmain.show()
sys.exit(app.exec_())