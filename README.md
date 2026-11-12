# Employee Management System (Python + Oracle)

A console-based Employee Management System built with Python and Oracle Database. It performs full CRUD operations on an employee table.

## Features
- Add a new employee
- Delete an employee
- Update employee details (checks if the employee number exists first)
- View a single employee
- View all employees
- Search employee
- Menu-driven interface

## Technologies Used
- Python 3
- Oracle Database (orclpdb)
- `oracledb` library
- PyCharm IDE

## Project Structure
| File | Purpose |
|------|---------|
| EmpMainProject.py | Main program, runs the menu |
| EmpMenu.py | Displays the menu |
| EmpAdd.py | Add employee |
| EmpDelete.py | Delete employee |
| EmpUpdate.py | Update employee |
| EmpView.py | View all employees |
| EmpViewSingle.py | View a single employee |
| EmpSearch.py | Search employee |

## Database Table
```sql
CREATE TABLE employee (
  eno NUMBER PRIMARY KEY,
  name VARCHAR2(50),
  sal NUMBER(10,2),
  compname VARCHAR2(50)
);
```

## How to Run
1. Install Oracle Database and create the table above.
2. Install the library: `pip install oracledb`
3. Update the connection string in the code with your own username, password and service name.
4. Run the project: `python EmpMainProject.py`

## Menu Options
1. Add Employee
2. Delete Employee
3. Update Employee
4. View Single Employee
5. View All Employees
6. Search Employee
7. Exit

## Author
Ambar Singh
