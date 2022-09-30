class PayrollDeduction:

    def __init__(self, Description, Date, Charge, EmployeeID):
        self.__Description = Description
        self.__Date = Date
        self.__Charge = Charge
        self.__EmployeeID = EmployeeID


    def get_Description(self):
        return self.__Description
    def get_Date(self):
        return self.__Date
    def get_Charge(self):
        return self.__Charge
    def get_EmployeeID(self):
        return self.__EmployeeID
    
    