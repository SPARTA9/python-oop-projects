#Part a(i):
class Employee:
    #self.HourlyPay : REAL
    #self.__EmployeeNumber : STRING
    #self.JobTitle : STRING
    #self.PayYear2022 : ARRAY[0:51]OF REAL
    def __init__(self, pHourlyPay, pEmployeeNumber, pJobtitle):
        self.HourlyPay = pHourlyPay
        self.__EmployeeNumber = pEmployeeNumber
        self.JobTitle = pJobtitle
        self.PayYear2022 = [0.0 for i in range(52)]

    #Part a(ii):
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
    
    #part a(iii):
    def SetPay(self, weekNum, HrsWorked):
        pay = self.HourlyPay * HrsWorked
        self.PayYear2022[weekNum -1] = pay

    #Part a(iv):
    def GetTotalPay(self):
        Total = 0
        for i in range(len(self.PayYear2022)):
            Total = Total + self.PayYear2022[i]
        return Total
    
#Part b(i):
class Manager(Employee):
    # self.BonusValue : REAL
    def __init__(self, pHourlyPay, pEmployeeNumber, pJobtitle, pBonusValue):
        super().__init__(pHourlyPay, pEmployeeNumber, pJobtitle)
        self.BonusValue = pBonusValue

    #Part a(ii):
    def SetPay(self, weekNum, HrsWorked):
        HrsWorked = HrsWorked + (HrsWorked * (self.BonusValue / 100))
        super().SetPay(weekNum, HrsWorked)

#Part c):
EmployeeArray = []
for i in range(8):
    EmployeeArray.append(Employee(0,"",""))
file = open("Employees.txt", 'r')
line = file.readline().strip()
index = 0
while line != "":
    hourlyPay = float(line)
    employeeNum = file.readline().strip()
    #check if next line is bonus value (number) or Job title (String)
    nextline = file.readline().strip()
    try:
        bonusValue = float(nextline) #If its a digit String it will be converted to float, if it isnt then its obviously the jobtitle
        jobTitle = file.readline().strip()
        employee = Manager(hourlyPay, employeeNum, jobTitle, bonusValue)
    except:
        jobTitle = nextline
        employee = Employee(hourlyPay, employeeNum, jobTitle)
    EmployeeArray[index] = employee
    index = index + 1
    line = file.readline().strip()
file.close()

#part d):
def Enterhours():
    file = open("HoursWeek1.txt", 'r')
    line = file.readline().strip()
    while line != "":
        empNum = line
        HrsWrked = float(file.readline().strip())
        for i in range(len(EmployeeArray)):
            if EmployeeArray[i].GetEmployeeNumber() == empNum:
                EmployeeArray[i].SetPay(1,HrsWrked)
                break
        line = file.readline().strip()

#Part e(i):
Enterhours()
for i in range(len(EmployeeArray)):
    TotalPay = EmployeeArray[i].GetTotalPay()
    print("Employee Number: ", EmployeeArray[i].GetEmployeeNumber())
    print("Total Pay: ", TotalPay)




