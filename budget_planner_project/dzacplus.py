from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QMessageBox


class Ui_Form(QMainWindow):

    def setupUi(self, Form):

        Form.setObjectName("Form")

        Form.resize(400, 300)

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)

        self.verticalLayout.setObjectName("verticalLayout") 

        self.label = QtWidgets.QLabel(Form)

        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.label)

        self.IncometextEdit = QtWidgets.QTextEdit(Form)

        self.IncometextEdit.setObjectName("IncometextEdit")

        self.verticalLayout.addWidget(self.IncometextEdit)

        self.IncomeSubmitButton = QtWidgets.QPushButton(Form)

        self.IncomeSubmitButton.setObjectName("IncomeSubmitButton")

        self.IncomeSubmitButton.clicked.connect(self.submit_income)   # BOTTON

        self.verticalLayout.addWidget(self.IncomeSubmitButton)



        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):

        _translate = QtCore.QCoreApplication.translate

        Form.setWindowTitle(_translate("Form", "Form"))

        self.label.setText(_translate("Form", "New Income"))

        self.IncomeSubmitButton.setText(_translate("Form", "Submit"))


    def submit_income(self):
        pass

    def accepted(self):
        # Handle cleanup actions if needed
        super().accept()

    def reject(self):
        # Handle cleanup actions if needed
        super().reject()


class Ui_BudgetPlannerAlex(QMainWindow):

    def setupUi(self, BudgetPlannerAlex):

        BudgetPlannerAlex.setObjectName("BudgetPlannerAlex")

        BudgetPlannerAlex.setEnabled(True)

        BudgetPlannerAlex.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(BudgetPlannerAlex)

        self.centralwidget.setObjectName("centralwidget")

        self.food = QtWidgets.QLabel(self.centralwidget)

        self.food.setGeometry(QtCore.QRect(20, 140, 111, 111))

        self.food.setText("")

        self.food.setPixmap(QtGui.QPixmap("photos/transparent-diet-icon-healthy-food-icon-healthy-icon-5ff6c06df33df6.1491802516100066379963.jpg"))

        self.food.setScaledContents(True)

        self.food.setWordWrap(False)

        self.food.setObjectName("food")

        self.transport = QtWidgets.QLabel(self.centralwidget)

        self.transport.setGeometry(QtCore.QRect(20, 290, 111, 111))

        self.transport.setText("")

        self.transport.setPixmap(QtGui.QPixmap("photos/taxi.png"))

        self.transport.setScaledContents(True)

        self.transport.setObjectName("transport")

        self.household = QtWidgets.QLabel(self.centralwidget)

        self.household.setGeometry(QtCore.QRect(20, 440, 111, 111))

        self.household.setAutoFillBackground(False)

        self.household.setText("")

        self.household.setPixmap(QtGui.QPixmap("photos/3081990.png"))

        self.household.setScaledContents(True)

        self.household.setWordWrap(False)

        self.household.setObjectName("household")

        self.taxes = QtWidgets.QLabel(self.centralwidget)

        self.taxes.setEnabled(True)

        self.taxes.setGeometry(QtCore.QRect(20, 0, 111, 111))

        self.taxes.setText("")

        self.taxes.setPixmap(QtGui.QPixmap("photos/taxes.png"))

        self.taxes.setScaledContents(True)

        self.taxes.setObjectName("taxes")

        self.house = QtWidgets.QLabel(self.centralwidget)

        self.house.setGeometry(QtCore.QRect(450, 0, 111, 111))

        self.house.setText("")

        self.house.setPixmap(QtGui.QPixmap("photos/house.png"))

        self.house.setScaledContents(True)

        self.house.setObjectName("house")

        self.clothes = QtWidgets.QLabel(self.centralwidget)

        self.clothes.setGeometry(QtCore.QRect(660, 10, 121, 111))

        self.clothes.setText("")

        self.clothes.setPixmap(QtGui.QPixmap("photos/clot.png"))

        self.clothes.setScaledContents(True)

        self.clothes.setObjectName("clothes")

        self.education = QtWidgets.QLabel(self.centralwidget)

        self.education.setGeometry(QtCore.QRect(660, 140, 121, 121))

        self.education.setText("")

        self.education.setPixmap(QtGui.QPixmap("photos/eduuuu.png"))

        self.education.setScaledContents(True)

        self.education.setObjectName("education")

        self.telecom = QtWidgets.QLabel(self.centralwidget)

        self.telecom.setGeometry(QtCore.QRect(660, 290, 111, 111))

        self.telecom.setText("")

        self.telecom.setPixmap(QtGui.QPixmap("photos/telecom.png"))

        self.telecom.setScaledContents(True)

        self.telecom.setObjectName("telecom")

        self.sport = QtWidgets.QLabel(self.centralwidget)

        self.sport.setGeometry(QtCore.QRect(660, 440, 111, 111))

        self.sport.setText("")

        self.sport.setPixmap(QtGui.QPixmap("photos/sport.png"))

        self.sport.setScaledContents(True)

        self.sport.setObjectName("sport")

        self.health = QtWidgets.QLabel(self.centralwidget)

        self.health.setGeometry(QtCore.QRect(250, 440, 111, 111))

        self.health.setText("")

        self.health.setPixmap(QtGui.QPixmap("photos/heal.png"))

        self.health.setScaledContents(True)

        self.health.setObjectName("health")

        self.entertainment = QtWidgets.QLabel(self.centralwidget)

        self.entertainment.setGeometry(QtCore.QRect(450, 440, 111, 111))

        self.entertainment.setText("")

        self.entertainment.setPixmap(QtGui.QPixmap("photos/entertainment.png"))

        self.entertainment.setScaledContents(True)

        self.entertainment.setObjectName("entertainment")

        self.car = QtWidgets.QLabel(self.centralwidget)

        self.car.setGeometry(QtCore.QRect(250, 0, 111, 111))

        self.car.setText("")

        self.car.setPixmap(QtGui.QPixmap("photos/Car.ico"))

        self.car.setScaledContents(True)

        self.car.setObjectName("car")

        self.clothesPush = QtWidgets.QPushButton(self.centralwidget)

        self.clothesPush.setGeometry(QtCore.QRect(660, 10, 111, 111))

        self.clothesPush.setText("")

        self.clothesPush.setFlat(True)

        self.clothesPush.setObjectName("clothesPush")

        self.foodpush = QtWidgets.QPushButton(self.centralwidget)

        self.foodpush.setGeometry(QtCore.QRect(20, 140, 111, 111))

        self.foodpush.setText("")

        self.foodpush.setDefault(False)

        self.foodpush.setFlat(True)

        self.foodpush.setObjectName("foodpush")

        self.carpush = QtWidgets.QPushButton(self.centralwidget)

        self.carpush.setGeometry(QtCore.QRect(250, 0, 111, 111))

        self.carpush.setText("")

        self.carpush.setFlat(True)

        self.carpush.setObjectName("carpush")

        self.transportpush = QtWidgets.QPushButton(self.centralwidget)

        self.transportpush.setGeometry(QtCore.QRect(20, 290, 111, 111))

        self.transportpush.setText("")

        self.transportpush.setFlat(True)

        self.transportpush.setObjectName("transportpush")

        self.HousePush = QtWidgets.QPushButton(self.centralwidget)

        self.HousePush.setGeometry(QtCore.QRect(450, 0, 111, 111))

        self.HousePush.setText("")

        self.HousePush.setFlat(True)

        self.HousePush.setObjectName("HousePush")

        self.TelecomPush = QtWidgets.QPushButton(self.centralwidget)

        self.TelecomPush.setGeometry(QtCore.QRect(660, 290, 111, 111))

        self.TelecomPush.setText("")

        self.TelecomPush.setFlat(True)

        self.TelecomPush.setObjectName("TelecomPush")

        self.EducatioPush = QtWidgets.QPushButton(self.centralwidget)

        self.EducatioPush.setGeometry(QtCore.QRect(660, 140, 111, 111))

        self.EducatioPush.setText("")

        self.EducatioPush.setFlat(True)

        self.EducatioPush.setObjectName("EducatioPush")

        self.EntertainmentPush = QtWidgets.QPushButton(self.centralwidget)

        self.EntertainmentPush.setGeometry(QtCore.QRect(450, 440, 111, 111))

        self.EntertainmentPush.setText("")

        self.EntertainmentPush.setFlat(True)

        self.EntertainmentPush.setObjectName("EntertainmentPush")

        self.taxPush = QtWidgets.QPushButton(self.centralwidget)

        self.taxPush.setEnabled(False)

        self.taxPush.setGeometry(QtCore.QRect(20, 0, 111, 111))

        self.taxPush.setText("")

        self.taxPush.setAutoDefault(False)

        self.taxPush.setDefault(False)

        self.taxPush.setFlat(True)

        self.taxPush.setObjectName("taxPush")

        self.householdPush = QtWidgets.QPushButton(self.centralwidget)

        self.householdPush.setGeometry(QtCore.QRect(20, 440, 111, 111))

        self.householdPush.setText("")

        self.householdPush.setFlat(True)

        self.householdPush.setObjectName("householdPush")

        self.HealthPush = QtWidgets.QPushButton(self.centralwidget)

        self.HealthPush.setGeometry(QtCore.QRect(250, 440, 111, 111))

        self.HealthPush.setText("")

        self.HealthPush.setFlat(True)

        self.HealthPush.setObjectName("HealthPush")

        self.SportPush = QtWidgets.QPushButton(self.centralwidget)

        self.SportPush.setGeometry(QtCore.QRect(660, 440, 111, 111))

        self.SportPush.setText("")

        self.SportPush.setFlat(True)

        self.SportPush.setObjectName("SportPush")

        self.PlusPush = QtWidgets.QPushButton(self.centralwidget)

        self.PlusPush.setGeometry(QtCore.QRect(450, 140, 131, 131))

        self.PlusPush.setText("")

        self.PlusPush.setCheckable(False)

        self.PlusPush.setAutoRepeat(False)

        self.PlusPush.setFlat(True)

        self.PlusPush.setObjectName("PlusPush")

        self.Plus = QtWidgets.QLabel(self.centralwidget)

        self.Plus.setGeometry(QtCore.QRect(450, 140, 131, 131))

        self.Plus.setText("")

        self.Plus.setPixmap(QtGui.QPixmap("photos/plus.png"))

        self.Plus.setScaledContents(True)

        self.Plus.setObjectName("Plus")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)

        self.label_2.setGeometry(QtCore.QRect(220, 140, 121, 121))

        self.label_2.setText("")

        self.label_2.setPixmap(QtGui.QPixmap("photos/minus.png"))

        self.label_2.setScaledContents(True)

        self.label_2.setObjectName("label_2")

        self.MinusPush = QtWidgets.QPushButton(self.centralwidget)

        self.MinusPush.setGeometry(QtCore.QRect(220, 140, 121, 121))

        self.MinusPush.setText("")

        self.MinusPush.setFlat(True)

        self.MinusPush.setObjectName("MinusPush")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)

        self.listWidget.setGeometry(QtCore.QRect(140, 270, 341, 161))

        self.listWidget.setObjectName("listWidget")

        self.BalanceName = QtWidgets.QLabel(self.centralwidget)

        self.BalanceName.setGeometry(QtCore.QRect(490, 390, 71, 31))

        self.BalanceName.setScaledContents(True)

        self.BalanceName.setObjectName("BalanceName")

        self.IncomeReturnText = QtWidgets.QLabel(self.centralwidget)

        self.IncomeReturnText.setGeometry(QtCore.QRect(580, 290, 71, 31))

        self.IncomeReturnText.setText("")

        self.IncomeReturnText.setObjectName("IncomeReturnText")

        self.IncomeName = QtWidgets.QLabel(self.centralwidget)

        self.IncomeName.setGeometry(QtCore.QRect(490, 290, 71, 31))

        self.IncomeName.setScaledContents(True)

        self.IncomeName.setObjectName("IncomeName")

        self.ExpenceName = QtWidgets.QLabel(self.centralwidget)

        self.ExpenceName.setGeometry(QtCore.QRect(490, 340, 71, 31))

        self.ExpenceName.setScaledContents(True)

        self.ExpenceName.setObjectName("ExpenceName")

        self.ExpenciesReturnText = QtWidgets.QLabel(self.centralwidget)

        self.ExpenciesReturnText.setGeometry(QtCore.QRect(580, 340, 71, 31))

        self.ExpenciesReturnText.setText("")

        self.ExpenciesReturnText.setObjectName("ExpenciesReturnText")

        self.BalanceReturnText = QtWidgets.QLabel(self.centralwidget)

        self.BalanceReturnText.setGeometry(QtCore.QRect(580, 390, 55, 16))

        self.BalanceReturnText.setText("")

        self.BalanceReturnText.setObjectName("BalanceReturnText")

        self.PLUSpushButton = QtWidgets.QPushButton(self.centralwidget)

        self.PLUSpushButton.setGeometry(QtCore.QRect(450, 140, 131, 131))

        self.PLUSpushButton.setText("")

        self.PLUSpushButton.setFlat(True)

        self.PLUSpushButton.setObjectName("PLUSpushButton")

        self.PLUSpushButton.clicked.connect(self.open_income_window)      # Plus push botton

        BudgetPlannerAlex.setCentralWidget(self.centralwidget)           



        self.another_window = Ui_Form()

        # self.another_window.setupUi(self.centralwidget)       # central widget@ konkret inchna?

        



        self.retranslateUi(BudgetPlannerAlex)

        QtCore.QMetaObject.connectSlotsByName(BudgetPlannerAlex)



    def retranslateUi(self, BudgetPlannerAlex):
        _translate = QtCore.QCoreApplication.translate

        BudgetPlannerAlex.setWindowTitle(_translate("BudgetPlannerAlex", "MainWindow"))

        self.BalanceName.setText(_translate("BudgetPlannerAlex", "Balance"))

        self.IncomeName.setText(_translate("BudgetPlannerAlex", "Income"))

        self.ExpenceName.setText(_translate("BudgetPlannerAlex", "Expencies"))



    def add_expense(self):
        pass



    def add_income(self):
        pass


    def open_income_window(self):
        self.income_window = Ui_Form()
        self.income_window.setupUi(self.income_window)
        self.income_window.accepted.connect(self.handle_income_window_accepted)
        self.income_window.rejected.connect(self.handle_income_window_rejected)
        self.income_window.show()

    def handle_income_window_accepted(self):
        # Handle actions when the income window is accepted (e.g., user clicked OK)
        del self.income_window

    def handle_income_window_rejected(self):
        # Handle actions when the income window is rejected (e.g., user clicked Cancel)
        del self.income_window

if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)

    BudgetPlannerAlex = QtWidgets.QMainWindow()

    ui = Ui_BudgetPlannerAlex()

    ui.setupUi(BudgetPlannerAlex)

    BudgetPlannerAlex.show()

    sys.exit(app.exec_())