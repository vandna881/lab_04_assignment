class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

def sort_employees(employees, key):
    if key == 1:
        return sorted(employees, key=lambda emp: emp.age)
    elif key == 2:
        return sorted(employees, key=lambda emp: emp.name)
    elif key == 3:
        return sorted(employees, key=lambda emp: emp.salary)
    else:
        raise ValueError("Invalid sorting parameter")

def print_employees(employees):
    print(f"{'Emp ID':<10} {'Name':<10} {'Age':<5} {'Salary (PM)':<10}")
    print("="*40)
    for emp in employees:
        print(f"{emp.emp_id:<10} {emp.name:<10} {emp.age:<5} {emp.salary:<10}")

if __name__ == "__main__":
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000)
    ]

    print("Sorting Options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    sorting_option = int(input("Enter the sorting parameter (1/2/3): "))

    sorted_employees = sort_employees(employees, sorting_option)
    print("\nSorted Employee Data:")
    print_employees(sorted_employees)
