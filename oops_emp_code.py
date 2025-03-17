
class Employee:
    def __init__(self,name,employee_id,hours_worked):
        self.name=name
        self.employee_id=employee_id
        self.hours_worked=hours_worked


    def calculate_salary(self):
        hourly_salary=100
        if self.hours_worked >0:
            hourly_salary*=self.hours_worked

        return hourly_salary


class FullTimeEmployee(Employee):
    def __init__(self, name,employee_id,hours_worked, fixed_salary):
        super().__init__(name,employee_id,hours_worked)  # Corrected the super() call
        self.fixed_salary = fixed_salary

    def calculate_salary(self):
        hours_worked=self.hours_worked
        if hours_worked ==8:
            return self.fixed_salary
        elif hours_worked<8:
            hours_worked *=100

        return hours_worked




emp1=FullTimeEmployee("ramu",1,7,800)
print(emp1.calculate_salary())



