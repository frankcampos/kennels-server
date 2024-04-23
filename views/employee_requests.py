EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    },
    {
        "id": 2,
        "name": "Tristan Mcneil"
    },
    {
        "id": 3,
        "name": "Lina Todd"
    }
]


def get_all_employees():
    """return all employees"""
    return EMPLOYEES


def get_single_employee(id):
    """Handle the GET requests for a single employee"""
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee


def create_employee(employee):
    """Add a new employee to the list of employees and return the new employee."""
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee


def delete_employee(id):
    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee['id'] == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee['id'] == id:
            EMPLOYEES[index] = new_employee
            break
