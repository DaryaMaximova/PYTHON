from view import (get_salary_range, show_menu,
                  no_employee_error)
from model import (read_csv, read_json, write_csv, write_json, find_emp,
                   find_employees_by_salary_range, update_data, add_employee, delete_data,
                   find_employee_by_position)


def run_work():
    employees = read_json()
    print(employees)
    while True:
        choice = show_menu()
        if choice == 1:             # find employee
            employee = find_emp(employees)
            print(employee)
            if employee is None:
                no_employee_error()
        elif choice == 2:           # select employees by position
            position = input("Введите название позиции: ")
            emp_by_position = find_employee_by_position(employees, position)
            print(emp_by_position)
            # if not emp_by_position:
                # no_employee_error()
        elif choice == 3:           # select employees by salary range
            emp_by_salary = find_employees_by_salary_range(employees)
            print(emp_by_salary)
            if not emp_by_salary:
                no_employee_error()
        elif choice == 4:           # add employee
            add_employee(employees)
        elif choice == 5:           # remove employee
            delete_data(employees)
        elif choice == 6:           # update employee data
            update_data(employees)
        elif choice == 7:           # export data to json
            write_json(employees)
        elif choice == 8:           # export data to csv
            write_csv(employees)
        elif choice == 9:
            write_csv(employees)
            break
        else:
            print("Неверный выбор, попробуйте еще раз")
