import sqlite3
import json
from models import Employee


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
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM Employee e
        """)

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])

            employees.append(employee.__dict__)
        return employees

def get_single_employee(id):
    """Handle the GET requests for a single employee"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM Employee e
        WHERE e.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        employee = Employee(data['id'], data['name'], data['address'], data['location_id'])

        return employee.__dict__


def create_employee(employee):
    """Add a new employee to the list of employees and return the new employee."""
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee


def delete_employee(id):
    """Delete an employee by id"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Employee
        WHERE id = ?
        """, (id, ))

def update_employee(id, new_employee):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Employee
            SET
                name = ?,
                address = ?,
                location_id = ?
        WHERE id = ?
        """, (new_employee['name'], new_employee['address'], new_employee['location_id'], id))

        rows_affected = db_cursor.rowcount

        if rows_affected == 0:
            return False
        else:
            return True

def get_employee_by_location(location_id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM Employee e
        WHERE e.location_id = ?
        """, (location_id, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])

            employees.append(employee.__dict__)
        return employees
