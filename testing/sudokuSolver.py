from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from qt5_file.ui import Ui_MainWindow
from Img2text.decoderClass import Sudoku
from Img2text import img2text
from pathlib import Path
import sys

def error():    
    QMessageBox.about(Qmain,"Error","Please enter valid numbers")

def getitem():
    matrix = [[0 for i in range(9)] for j in range(9)]
    try:
        matrix[0][0] = int(ui.lineEdit_1.text())
    except:
        matrix[0][0]=0
    try:
        matrix[0][1] = int(ui.lineEdit_2.text())
    except:
        matrix[0][1]=0
    try:
        matrix[0][2] = int(ui.lineEdit_3.text())
    except:
        matrix[0][2]=0
    try:
        matrix[0][3] = int(ui.lineEdit_4.text())
    except:
        matrix[0][3]=0
    try:
        matrix[0][4] = int(ui.lineEdit_5.text())
    except:
        matrix[0][4]=0
    try:
        matrix[0][5] = int(ui.lineEdit_6.text())
    except:
        matrix[0][5]=0
    try:
        matrix[0][6] = int(ui.lineEdit_7.text())
    except:
        matrix[0][6]=0
    try:
        matrix[0][7] = int(ui.lineEdit_8.text())
    except:
        matrix[0][7]=0
    try:
        matrix[0][8] = int(ui.lineEdit_9.text())
    except:
        matrix[0][8]=0
    try:
        matrix[1][0] = int(ui.lineEdit_10.text())
    except:
        matrix[1][0]=0
    try:
        matrix[1][1] = int(ui.lineEdit_11.text())
    except:
        matrix[1][1]=0
    try:
        matrix[1][2] = int(ui.lineEdit_12.text())
    except:
        matrix[1][2]=0
    try:
        matrix[1][3] = int(ui.lineEdit_13.text())
    except:
        matrix[1][3]=0
    try:
        matrix[1][4] = int(ui.lineEdit_14.text())
    except:
        matrix[1][4]=0
    try:
        matrix[1][5] = int(ui.lineEdit_15.text())
    except:
        matrix[1][5]=0
    try:
        matrix[1][6] = int(ui.lineEdit_16.text())
    except:
        matrix[1][6]=0
    try:
        matrix[1][7] = int(ui.lineEdit_17.text())
    except:
        matrix[1][7]=0
    try:
        matrix[1][8] = int(ui.lineEdit_18.text())
    except:
        matrix[1][8]=0
    try:
        matrix[2][0] = int(ui.lineEdit_19.text())
    except:
        matrix[2][0]=0
    try:
        matrix[2][1] = int(ui.lineEdit_20.text())
    except:
        matrix[2][1]=0
    try:
        matrix[2][2] = int(ui.lineEdit_21.text())
    except:
        matrix[2][2]=0
    try:
        matrix[2][3] = int(ui.lineEdit_22.text())
    except:
        matrix[2][3]=0
    try:
        matrix[2][4] = int(ui.lineEdit_23.text())
    except:
        matrix[2][4]=0
    try:
        matrix[2][5] = int(ui.lineEdit_24.text())
    except:
        matrix[2][5]=0
    try:
        matrix[2][6] = int(ui.lineEdit_25.text())
    except:
        matrix[2][6]=0
    try:
        matrix[2][7] = int(ui.lineEdit_26.text())
    except:
        matrix[2][7]=0
    try:
        matrix[2][8] = int(ui.lineEdit_27.text())
    except:
        matrix[2][8]=0
    try:
        matrix[3][0] = int(ui.lineEdit_28.text())
    except:
        matrix[3][0]=0
    try:
        matrix[3][1] = int(ui.lineEdit_29.text())
    except:
        matrix[3][1]=0
    try:
        matrix[3][2] = int(ui.lineEdit_30.text())
    except:
        matrix[3][2]=0
    try:
        matrix[3][3] = int(ui.lineEdit_31.text())
    except:
        matrix[3][3]=0
    try:
        matrix[3][4] = int(ui.lineEdit_32.text())
    except:
        matrix[3][4]=0
    try:
        matrix[3][5] = int(ui.lineEdit_33.text())
    except:
        matrix[3][5]=0
    try:
        matrix[3][6] = int(ui.lineEdit_34.text())
    except:
        matrix[3][6]=0
    try:
        matrix[3][7] = int(ui.lineEdit_35.text())
    except:
        matrix[3][7]=0
    try:
        matrix[3][8] = int(ui.lineEdit_36.text())
    except:
        matrix[3][8]=0
    try:
        matrix[4][0] = int(ui.lineEdit_37.text())
    except:
        matrix[4][0]=0
    try:
        matrix[4][1] = int(ui.lineEdit_38.text())
    except:
        matrix[4][1]=0
    try:
        matrix[4][2] = int(ui.lineEdit_39.text())
    except:
        matrix[4][2]=0
    try:
        matrix[4][3] = int(ui.lineEdit_40.text())
    except:
        matrix[4][3]=0
    try:
        matrix[4][4] = int(ui.lineEdit_41.text())
    except:
        matrix[4][4]=0
    try:
        matrix[4][5] = int(ui.lineEdit_42.text())
    except:
        matrix[4][5]=0
    try:
        matrix[4][6] = int(ui.lineEdit_43.text())
    except:
        matrix[4][6]=0
    try:
        matrix[4][7] = int(ui.lineEdit_44.text())
    except:
        matrix[4][7]=0
    try:
        matrix[4][8] = int(ui.lineEdit_45.text())
    except:
        matrix[4][8]=0
    try:
        matrix[5][0] = int(ui.lineEdit_46.text())
    except:
        matrix[5][0]=0
    try:
        matrix[5][1] = int(ui.lineEdit_47.text())
    except:
        matrix[5][1]=0
    try:
        matrix[5][2] = int(ui.lineEdit_48.text())
    except:
        matrix[5][2]=0
    try:
        matrix[5][3] = int(ui.lineEdit_49.text())
    except:
        matrix[5][3]=0
    try:
        matrix[5][4] = int(ui.lineEdit_50.text())
    except:
        matrix[5][4]=0
    try:
        matrix[5][5] = int(ui.lineEdit_51.text())
    except:
        matrix[5][5]=0
    try:
        matrix[5][6] = int(ui.lineEdit_52.text())
    except:
        matrix[5][6]=0
    try:
        matrix[5][7] = int(ui.lineEdit_53.text())
    except:
        matrix[5][7]=0
    try:
        matrix[5][8] = int(ui.lineEdit_54.text())
    except:
        matrix[5][8]=0

    try:
        matrix[6][0] = int(ui.lineEdit_55.text())
    except:
        matrix[6][0]=0
    try:
        matrix[6][1] = int(ui.lineEdit_56.text())
    except:
        matrix[6][1]=0
    try:
        matrix[6][2] = int(ui.lineEdit_57.text())
    except:
        matrix[6][2]=0
    try:
        matrix[6][3] = int(ui.lineEdit_58.text())
    except:
        matrix[6][3]=0
    try:
        matrix[6][4] = int(ui.lineEdit_59.text())
    except:
        matrix[6][4]=0
    try:
        matrix[6][5] = int(ui.lineEdit_60.text())
    except:
        matrix[6][5]=0
    try:
        matrix[6][6] = int(ui.lineEdit_61.text())
    except:
        matrix[6][6]=0
    try:
        matrix[6][7] = int(ui.lineEdit_62.text())
    except:
        matrix[6][7]=0
    try:
        matrix[6][8] = int(ui.lineEdit_63.text())
    except:
        matrix[6][8]=0
    try:
        matrix[7][0] = int(ui.lineEdit_64.text())
    except:
        matrix[7][0]=0
    try:
        matrix[7][1] = int(ui.lineEdit_65.text())
    except:
        matrix[7][1]=0
    try:
        matrix[7][2] = int(ui.lineEdit_66.text())
    except:
        matrix[7][2]=0
    try:
        matrix[7][3] = int(ui.lineEdit_67.text())
    except:
        matrix[7][3]=0
    try:
        matrix[7][4] = int(ui.lineEdit_68.text())
    except:
        matrix[7][4]=0
    try:
        matrix[7][5] = int(ui.lineEdit_69.text())
    except:
        matrix[7][5]=0
    try:
        matrix[7][6] = int(ui.lineEdit_70.text())
    except:
        matrix[7][6]=0
    try:
        matrix[7][7] = int(ui.lineEdit_71.text())
    except:
        matrix[7][7]=0
    try:
        matrix[7][8] = int(ui.lineEdit_72.text())
    except:
        matrix[7][8]=0
    try:
        matrix[8][0] = int(ui.lineEdit_73.text())
    except:
        matrix[8][0]=0
    try:
        matrix[8][1] = int(ui.lineEdit_74.text())
    except:
        matrix[8][1]=0
    try:
        matrix[8][2] = int(ui.lineEdit_75.text())
    except:
        matrix[8][2]=0
    try:
        matrix[8][3] = int(ui.lineEdit_76.text())
    except:
        matrix[8][3]=0
    try:
        matrix[8][4] = int(ui.lineEdit_77.text())
    except:
        matrix[8][4]=0
    try:
        matrix[8][5] = int(ui.lineEdit_78.text())
    except:
        matrix[8][5]=0
    try:
        matrix[8][6] = int(ui.lineEdit_79.text())
    except:
        matrix[8][6]=0
    try:
        matrix[8][7] = int(ui.lineEdit_80.text())
    except:
        matrix[8][7]=0
    try:
        matrix[8][8] = int(ui.lineEdit_81.text())
    except:
        matrix[8][8]=0

    solution_func(matrix)
     
def reset():
    ui.lineEdit_1.setText ("")
    ui.lineEdit_2.setText ("")
    ui.lineEdit_3.setText ("")
    ui.lineEdit_4.setText ("")
    ui.lineEdit_5.setText ("")
    ui.lineEdit_6.setText ("")
    ui.lineEdit_7.setText ("")
    ui.lineEdit_8.setText ("")
    ui.lineEdit_9.setText ("")
    ui.lineEdit_10.setText("")
    ui.lineEdit_11.setText("")
    ui.lineEdit_12.setText("")
    ui.lineEdit_13.setText("")
    ui.lineEdit_14.setText("")
    ui.lineEdit_15.setText("")
    ui.lineEdit_16.setText("")
    ui.lineEdit_17.setText("")
    ui.lineEdit_18.setText("")
    ui.lineEdit_19.setText("")
    ui.lineEdit_20.setText("")
    ui.lineEdit_21.setText("")
    ui.lineEdit_22.setText("")
    ui.lineEdit_23.setText("")
    ui.lineEdit_24.setText("")
    ui.lineEdit_25.setText("")
    ui.lineEdit_26.setText("")
    ui.lineEdit_27.setText("")
    ui.lineEdit_28.setText("")
    ui.lineEdit_29.setText("")
    ui.lineEdit_30.setText("")
    ui.lineEdit_31.setText("")
    ui.lineEdit_32.setText("")
    ui.lineEdit_33.setText("")
    ui.lineEdit_34.setText("")
    ui.lineEdit_35.setText("")
    ui.lineEdit_36.setText("")
    ui.lineEdit_37.setText("")
    ui.lineEdit_38.setText("")
    ui.lineEdit_39.setText("")
    ui.lineEdit_40.setText("")
    ui.lineEdit_41.setText("")
    ui.lineEdit_42.setText("")
    ui.lineEdit_43.setText("")
    ui.lineEdit_44.setText("")
    ui.lineEdit_45.setText("")
    ui.lineEdit_46.setText("")
    ui.lineEdit_47.setText("")
    ui.lineEdit_48.setText("")
    ui.lineEdit_49.setText("")
    ui.lineEdit_50.setText("")
    ui.lineEdit_51.setText("")
    ui.lineEdit_52.setText("")
    ui.lineEdit_53.setText("")
    ui.lineEdit_54.setText("")
    ui.lineEdit_55.setText("")
    ui.lineEdit_56.setText("")
    ui.lineEdit_57.setText("")
    ui.lineEdit_58.setText("")
    ui.lineEdit_59.setText("")
    ui.lineEdit_60.setText("")
    ui.lineEdit_61.setText("")
    ui.lineEdit_62.setText("")
    ui.lineEdit_63.setText("")
    ui.lineEdit_64.setText("")
    ui.lineEdit_65.setText("")
    ui.lineEdit_66.setText("")
    ui.lineEdit_67.setText("")
    ui.lineEdit_68.setText("")
    ui.lineEdit_69.setText("")
    ui.lineEdit_70.setText("")
    ui.lineEdit_71.setText("")
    ui.lineEdit_72.setText("")
    ui.lineEdit_73.setText("")
    ui.lineEdit_74.setText("")
    ui.lineEdit_75.setText("")
    ui.lineEdit_76.setText("")
    ui.lineEdit_77.setText("")
    ui.lineEdit_78.setText("")
    ui.lineEdit_79.setText("")
    ui.lineEdit_80.setText("")
    ui.lineEdit_81.setText("")

def openFile():
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(Qmain, 
        "QFileDialog.getOpenFileName()", 
        options=options)
    if fileName:
        img2text.solver(fileName)
        return
    else:
        return

def additem(solution):
    ui.lineEdit_1.setText (str(solution.matrix[0][0]))
    ui.lineEdit_2.setText (str(solution.matrix[0][1]))
    ui.lineEdit_3.setText (str(solution.matrix[0][2]))
    ui.lineEdit_4.setText (str(solution.matrix[0][3]))
    ui.lineEdit_5.setText (str(solution.matrix[0][4]))
    ui.lineEdit_6.setText (str(solution.matrix[0][5]))
    ui.lineEdit_7.setText (str(solution.matrix[0][6]))
    ui.lineEdit_8.setText (str(solution.matrix[0][7]))
    ui.lineEdit_9.setText (str(solution.matrix[0][8]))
    ui.lineEdit_10.setText(str(solution.matrix[1][0]))
    ui.lineEdit_11.setText(str(solution.matrix[1][1]))
    ui.lineEdit_12.setText(str(solution.matrix[1][2]))
    ui.lineEdit_13.setText(str(solution.matrix[1][3]))
    ui.lineEdit_14.setText(str(solution.matrix[1][4]))
    ui.lineEdit_15.setText(str(solution.matrix[1][5]))
    ui.lineEdit_16.setText(str(solution.matrix[1][6]))
    ui.lineEdit_17.setText(str(solution.matrix[1][7]))
    ui.lineEdit_18.setText(str(solution.matrix[1][8]))
    ui.lineEdit_19.setText(str(solution.matrix[2][0]))
    ui.lineEdit_20.setText(str(solution.matrix[2][1]))
    ui.lineEdit_21.setText(str(solution.matrix[2][2]))
    ui.lineEdit_22.setText(str(solution.matrix[2][3]))
    ui.lineEdit_23.setText(str(solution.matrix[2][4]))
    ui.lineEdit_24.setText(str(solution.matrix[2][5]))
    ui.lineEdit_25.setText(str(solution.matrix[2][6]))
    ui.lineEdit_26.setText(str(solution.matrix[2][7]))
    ui.lineEdit_27.setText(str(solution.matrix[2][8]))
    ui.lineEdit_28.setText(str(solution.matrix[3][0]))
    ui.lineEdit_29.setText(str(solution.matrix[3][1]))
    ui.lineEdit_30.setText(str(solution.matrix[3][2]))
    ui.lineEdit_31.setText(str(solution.matrix[3][3]))
    ui.lineEdit_32.setText(str(solution.matrix[3][4]))
    ui.lineEdit_33.setText(str(solution.matrix[3][5]))
    ui.lineEdit_34.setText(str(solution.matrix[3][6]))
    ui.lineEdit_35.setText(str(solution.matrix[3][7]))
    ui.lineEdit_36.setText(str(solution.matrix[3][8]))
    ui.lineEdit_37.setText(str(solution.matrix[4][0]))
    ui.lineEdit_38.setText(str(solution.matrix[4][1]))
    ui.lineEdit_39.setText(str(solution.matrix[4][2]))
    ui.lineEdit_40.setText(str(solution.matrix[4][3]))
    ui.lineEdit_41.setText(str(solution.matrix[4][4]))
    ui.lineEdit_42.setText(str(solution.matrix[4][5]))
    ui.lineEdit_43.setText(str(solution.matrix[4][6]))
    ui.lineEdit_44.setText(str(solution.matrix[4][7]))
    ui.lineEdit_45.setText(str(solution.matrix[4][8]))
    ui.lineEdit_46.setText(str(solution.matrix[5][0]))
    ui.lineEdit_47.setText(str(solution.matrix[5][1]))
    ui.lineEdit_48.setText(str(solution.matrix[5][2]))
    ui.lineEdit_49.setText(str(solution.matrix[5][3]))
    ui.lineEdit_50.setText(str(solution.matrix[5][4]))
    ui.lineEdit_51.setText(str(solution.matrix[5][5]))
    ui.lineEdit_52.setText(str(solution.matrix[5][6]))
    ui.lineEdit_53.setText(str(solution.matrix[5][7]))
    ui.lineEdit_54.setText(str(solution.matrix[5][8]))
    ui.lineEdit_55.setText(str(solution.matrix[6][0]))
    ui.lineEdit_56.setText(str(solution.matrix[6][1]))
    ui.lineEdit_57.setText(str(solution.matrix[6][2]))
    ui.lineEdit_58.setText(str(solution.matrix[6][3]))
    ui.lineEdit_59.setText(str(solution.matrix[6][4]))
    ui.lineEdit_60.setText(str(solution.matrix[6][5]))
    ui.lineEdit_61.setText(str(solution.matrix[6][6]))
    ui.lineEdit_62.setText(str(solution.matrix[6][7]))
    ui.lineEdit_63.setText(str(solution.matrix[6][8]))
    ui.lineEdit_64.setText(str(solution.matrix[7][0]))
    ui.lineEdit_65.setText(str(solution.matrix[7][1]))
    ui.lineEdit_66.setText(str(solution.matrix[7][2]))
    ui.lineEdit_67.setText(str(solution.matrix[7][3]))
    ui.lineEdit_68.setText(str(solution.matrix[7][4]))
    ui.lineEdit_69.setText(str(solution.matrix[7][5]))
    ui.lineEdit_70.setText(str(solution.matrix[7][6]))
    ui.lineEdit_71.setText(str(solution.matrix[7][7]))
    ui.lineEdit_72.setText(str(solution.matrix[7][8]))
    ui.lineEdit_73.setText(str(solution.matrix[8][0]))
    ui.lineEdit_74.setText(str(solution.matrix[8][1]))
    ui.lineEdit_75.setText(str(solution.matrix[8][2]))
    ui.lineEdit_76.setText(str(solution.matrix[8][3]))
    ui.lineEdit_77.setText(str(solution.matrix[8][4]))
    ui.lineEdit_78.setText(str(solution.matrix[8][5]))
    ui.lineEdit_79.setText(str(solution.matrix[8][6]))
    ui.lineEdit_80.setText(str(solution.matrix[8][7]))
    ui.lineEdit_81.setText(str(solution.matrix[8][8]))

def solution_func(matrix):
    solution = Sudoku(matrix)
    if solution.flag:
        return additem(solution)
    else:
        error()
   


app = QApplication(sys.argv)
Qmain = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(Qmain)
ui.Button.clicked.connect(getitem)
ui.Button_2.clicked.connect(reset)
ui.Button_3.clicked.connect(openFile)

Qmain.show()
sys.exit(app.exec_())




