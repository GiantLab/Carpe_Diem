import sys, datetime, time
from PyQt5 import QtWidgets, QtCore, uic, QtTest

# variables (global)

dial_speed=1
input_year=int()
input_gender=int()
life_expectancy=int()

class MeinDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("layout.ui", self)
        
# signals and slots 
        self.ui.pushButtonStart.clicked.connect(self.showData)
        self.ui.pushButtonExit.clicked.connect(self.exit)
        self.ui.dialWheel.valueChanged.connect(self.speed)

# functions
    
        # show data
    def showData(self):
        self.fetchData()
        self.calculateData()
        self.showDateTime()
        self.timer()

        # calculate data
    def calculateData(self):
        global input_year
        global input_gender
        global life_expectancy
        
        # calculate life expectancy // fix numbers for testing, catch if human already dead
        x=datetime.datetime.now()
        year_now=x.strftime("%Y")
        year_now=int(year_now)

        #female
        if input_gender==0: 
            life_expectancy=input_year + 85 # // calculate later 
        #male
        else:               
            life_expectancy=input_year + 80 # // calculate later

        # fetch data      
    def fetchData(self):
        global input_year
        global input_gender
        
        # fetch year of date of birth
        input_year=self.ui.dateEditDateBirth.date().year()
        input_year=int(input_year)

        # fetch gender
        if self.ui.radioButtonW.isChecked():
            input_gender=0
        else:
            input_gender=1

        # control of the counting speed with the dialWheel, global var: dial_speed
    def speed(self):
        global dial_speed
        dial_speed=self.ui.dialWheel.value()

        # shows Date and Time
    def showDateTime(self):
        global life_expectancy
        x=datetime.datetime.now().ctime()
        text=" / life expectancy: "
        z=str(life_expectancy)
        text_final=x+text+z
        y=(text_final)
        self.ui.listWidgetOutput.addItem(y)

        # timer that counts in the future with various speed 
    def timer(self):
        global dial_speed
        global life_expectancy
        #dial from 1-100 (key) => speed QTest: 5000 - 50 (value) via dictionary
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
            if var==life_expectancy:
                break
            else:
                var+=1
                y=x.replace(year=var)
                z=y.strftime("%Y")
                self.ui.labelDateTime.setText(z)
        #combine QTest and dictionary 
                d=dic_speed[dial_speed]
                QtTest.QTest.qWait(d)
        text="life expectancy was: "
        z=str(life_expectancy)
        text_final=text+z
        self.ui.labelDateTime.setText(text_final)

        # exit program  
    def exit(self):
        sys.exit()

# testing output
#print(input_gender)

app = QtWidgets.QApplication(sys.argv)
dialog = MeinDialog()
dialog.show()
sys.exit(app.exec_())