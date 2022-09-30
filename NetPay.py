from EmployeeClass import Employee

from PayrollDeductionClass import PayrollDeduction


employee = Employee("Jimmy Smith",58475,"Information Systems","Developer",6800)

deduction_1 = PayrollDeduction("food court","8/14/2022",22.50,39119)
deduction_2 = PayrollDeduction("gift contribution","8/12/2022",25.00,58475)
deduction_3 = PayrollDeduction("food court","8/17/2022",15.25,21547)
deduction_4 = PayrollDeduction("vending machine","8/22/2022",3.00,58475)
deduction_5 = PayrollDeduction("vending machine","8/5/2022",2.75,58475)


#output
print()
print("* * * * Employee Pay * * * *")
print("Name:       ", employee.get_Name())
print("ID Number:  ", employee.get_IDnumber())
print("Department: ", employee.get_Department())
print("Gross Pay   $", float(employee.get_MonthlySalary()), sep= "")
print("Net Pay:    $", employee.get_MonthlySalary() - deduction_2.get_Charge() - deduction_4.get_Charge() - deduction_5.get_Charge(), sep= "")
print()
