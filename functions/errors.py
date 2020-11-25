from PyQt5.QtWidgets import QMessageBox

def error(Qmain):    
    QMessageBox.about(Qmain,"Error","Please enter valid numbers")

def error2(Qmain):    
    QMessageBox.about(Qmain,"Error","Please enter valid file")