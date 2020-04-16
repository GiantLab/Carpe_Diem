import sys, datetime, time
from PyQt5 import QtWidgets, QtCore, uic, QtTest

# variables (global)

dial_speed=1

class MeinDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("layout.ui", self)
        
# signals and slots 
        self.ui.pushButtonStart.clicked.connect(self.showDateTime)
        self.ui.pushButtonStart.clicked.connect(self.timer)
        self.ui.pushButtonExit.clicked.connect(self.exit)
        self.ui.dialWheel.valueChanged.connect(self.speed)
# functions
        

        # control of the counting speed with the dialWheel, global var: dial_speed
    def speed(self):
        global dial_speed
        dial_speed=self.ui.dialWheel.value()
        

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
        global dial_speed
        #Dial from 1-100 (key) => speed QTest: 5000 - 50 (value) via dictionary
        dic_speed={}
        x= range(1,101,1)
        xkey=1000
        for i in x:
            dic_speed[i]=xkey 
            xkey-=10

        x=datetime.datetime.now()
        z=x.strftime("%Y")
        self.ui.labelDateTime.setText(z)
        var=x.year
        while True:
            if var==2099:
                break
            else:
                var+=1
                y=x.replace(year=var)
                z=y.strftime("%Y")
                self.ui.labelDateTime.setText(z)
        #combine QTest and dictionary 
                d=dic_speed[dial_speed]
                QtTest.QTest.qWait(d)
        self.ui.labelDateTime.setText("You are dead")

app = QtWidgets.QApplication(sys.argv)
dialog = MeinDialog()
dialog.show()
sys.exit(app.exec_())