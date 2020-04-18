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
        self.ui.spinBox_1.valueChanged.connect(self.labelPercentage)
        self.ui.spinBox_2.valueChanged.connect(self.labelPercentage)
        self.ui.spinBox_3.valueChanged.connect(self.labelPercentage)
        self.ui.spinBox_4.valueChanged.connect(self.labelPercentage)
        self.ui.spinBox_5.valueChanged.connect(self.labelPercentage)
        self.ui.spinBox_6.valueChanged.connect(self.labelPercentage)
        self.ui.spinBox_7.valueChanged.connect(self.labelPercentage)

#load data in country-widget from list (0 Country both female male )   
        fhand=open("life_expectancy.txt")
        for line in fhand:
            line=line.rstrip()
            if line.startswith("0") or line=="":
                continue
            line=line.split()
            self.ui.comboBoxCountry.addItem(line[1])
        self.ui.comboBoxCountry.model().sort(0)


# functions 

        # show data
    def showData(self):
        self.fetchData()
        self.calculateData()
        self.showDateTime()
        self.timer()
        self.labelPercentage()

        # check if percentage 100% and comment status in label SystemWaiting funny way // to do
    def labelPercentage(self):
        self.ui.spinBoxes=[self.ui.spinBox_1,self.ui.spinBox_2,self.ui.spinBox_3, \
        self.ui.spinBox_4,self.ui.spinBox_5,self.ui.spinBox_6,self.ui.spinBox_7]
        total=0
        for i in self.ui.spinBoxes:
            total+=i.value()
        self.ui.lcdNumber.display(total)

        # system reaction on user input percentage
        if total <= 5:
            self.ui.labelSystemWaiting.setText("Come on, give me more")
        if total > 5 and total <=10:
            self.ui.labelSystemWaiting.setText("Yes, you can")
        if total > 10 and total <=15:
            self.ui.labelSystemWaiting.setText("A few more please")
        if total > 15 and total <=20:
            self.ui.labelSystemWaiting.setText("Really ?")
        if total > 20 and total <=25:
            self.ui.labelSystemWaiting.setText("I get tired")
        if total > 25 and total <=30:
            self.ui.labelSystemWaiting.setText("Time waste")
        if total > 30 and total <=35:
            self.ui.labelSystemWaiting.setText("The sky is blue")
        if total > 35 and total <=40:
            self.ui.labelSystemWaiting.setText("I want to be drunk")
        if total > 40 and total <=45:
            self.ui.labelSystemWaiting.setText("Are you sleeping ?")
        if total > 45 and total <=50:
            self.ui.labelSystemWaiting.setText("Oh my god")
        if total > 50 and total <=55:
            self.ui.labelSystemWaiting.setText("You are a rocket")
        if total > 55 and total <=60:
            self.ui.labelSystemWaiting.setText("Developers !")  
        if total > 60 and total <=65:
            self.ui.labelSystemWaiting.setText("Winter is coming")
        if total > 65 and total <=70:
            self.ui.labelSystemWaiting.setText("turbocharged")
        if total > 70 and total <=75:
            self.ui.labelSystemWaiting.setText("Go Go Go")
        if total > 75 and total <=80:
            self.ui.labelSystemWaiting.setText("My grandma could do this")
        if total > 80 and total <=80:
            self.ui.labelSystemWaiting.setText("You are fired")
        if total > 85 and total <=80:
            self.ui.labelSystemWaiting.setText("Just joking")
        if total > 90 and total <=80:
            self.ui.labelSystemWaiting.setText("Hmmmm")
        if total > 95 and total <=99:
            self.ui.labelSystemWaiting.setText("Love me, love my dog")
        if total ==100:
            self.ui.labelSystemWaiting.setText("You did it !!")
        if total > 100:
            self.ui.labelSystemWaiting.setText("System crashed")
            self.ui.lcdNumber.display("00000")

        # calculate data
    def calculateData(self):
        global input_year
        global input_gender
        global life_expectancy
        
        # calculate life expectancy // fix numbers for testing, catch if human already dead
        x=datetime.datetime.now()
        year_now=x.strftime("%Y")
        year_now=int(year_now)

        #female // calculate later
        if input_gender==0: 
            life_expectancy=input_year + 85 
        #male // calculate later
        else:               
            life_expectancy=input_year + 80 

        # fetch data      
    def fetchData(self):
        global input_year
        global input_gender
        
        # fetch date of birth (year)
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