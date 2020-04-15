import sys, datetime, time
from PyQt5 import QtWidgets, QtCore, uic
class MeinDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("layout.ui", self)
        
# signals and slots 
        self.ui.pushButtonStart.clicked.connect(self.showDateTime)
        self.ui.pushButtonStart.clicked.connect(self.timer)
        self.ui.pushButtonExit.clicked.connect(self.exit)
# functions

        # exit program // open
    def exit(self):
        pass

        # shows Date and Time
    def showDateTime(self):
        x=datetime.datetime.now().ctime()
        y=("Start at: "+x)
        self.ui.listWidgetOutput.addItem(y)

        # timer that counts in the future with various speed // QTimer possibly better solution, dial lagging
    def timer(self):
        x=datetime.datetime.now()
        z=x.strftime("%Y")
        self.ui.labelDateTime.setText(z)
        var=x.year
        while True:
        #prevent while-loop from freezing the program
            QtCore.QCoreApplication.processEvents()
            if var==2030:
                break
            else:
                var+=1
                y=x.replace(year=var)
                z=y.strftime("%Y")
                self.ui.labelDateTime.setText(z)
                time.sleep(0.5)
        self.ui.labelDateTime.setText("You are dead")

app = QtWidgets.QApplication(sys.argv)
dialog = MeinDialog()
dialog.show()
sys.exit(app.exec_())