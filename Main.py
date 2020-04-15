import sys, datetime, time
from matplotlib import pyplot as plt
from PyQt5 import QtWidgets, QtCore, uic, QtTest
class MeinDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("layout.ui", self)
        
# signals and slots 
        self.ui.pushButtonStart.clicked.connect(self.showDateTime)
        self.ui.pushButtonStart.clicked.connect(self.timer)
        self.ui.pushButtonExit.clicked.connect(self.exit)
# functions

        # exit program  
    def exit(self):
        sys.exit()

        # shows Date and Time
    def showDateTime(self):
        x=datetime.datetime.now().ctime()
        y=("Start at: "+x)
        self.ui.listWidgetOutput.addItem(y)

        # timer that counts in the future with various speed 
    def timer(self):
        x=datetime.datetime.now()
        z=x.strftime("%Y")
        self.ui.labelDateTime.setText(z)
        var=x.year
        while True:
            if var==2050:
                break
            else:
                var+=1
                y=x.replace(year=var)
                z=y.strftime("%Y")
                self.ui.labelDateTime.setText(z)
        #Delay wit QTest
                QtTest.QTest.qWait(500)
        self.ui.labelDateTime.setText("You are dead")

app = QtWidgets.QApplication(sys.argv)
dialog = MeinDialog()
dialog.show()
sys.exit(app.exec_())