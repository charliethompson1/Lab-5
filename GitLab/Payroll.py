from Employee import Employee

class Payroll():
    def __init__(self):
        self.emp = []

    def __repr__(self):
        return str(self.emp)
    
    def addEmp(self, e):
        self.emp.append(e)

    # New method to calculate total payroll
    def total(self):
        return sum(employee.getPay() for employee in self.emp)