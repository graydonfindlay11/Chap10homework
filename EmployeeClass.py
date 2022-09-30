class Employee:

    def __init__(self, Name, IDnumber, Department, JobTitle, MonthlySalary):
        self.__Name = Name
        self.__IDnumber = IDnumber
        self.__Department = Department
        self.__JobTitle = JobTitle
        self.__MonthlySalary = MonthlySalary


    def get_Name(self):
        return self.__Name
    def get_IDnumber(self):
        return self.__IDnumber
    def get_Department(self):
        return self.__Department
    def get_JobTitle(self):
        return self.__JobTitle
    def get_MonthlySalary(self):
        return self.__MonthlySalary



