import json
import sqlite3
from models import Customer


CUSTOMERS = [
    {
        "id": 1,
        "name": "Hannah Hall",
    },
    {
        "id": 1,
        "name": "Ryan Tanay"
    }
]


def get_all_customers():
    """ get all customers """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM Customer c
        """)

        customers = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(
                row['id'], row['name'], row['address'], row['email'], row['password'])

            customers.append(customer.__dict__)
        return customers


def get_single_customer(id):
    """get single customer by id"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM Customer c
        WHERE c.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        customer = Customer(data['id'], data['name'],
                            data['address'], data['email'], data['password'])

        return customer.__dict__


def create_customer(customer):
    """create a new customer"""
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1

    customer["id"] = new_id

    CUSTOMERS.append(customer)

    return customer


def delete_customer(id):
    """delete customer"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Customer
        WHERE id = ?
        """, (id, ))


def update_customer(id, new_customer):

    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Customer
        SET
            name = ?,
            address = ?,
            email = ?,
            password = ?
        WHERE id = ?
        """, (new_customer['name'], new_customer['address'],
              new_customer['email'], new_customer['password'], id))

        rows_affected = db_cursor.rowcount

        if rows_affected == 0:
            return False
        else:
            return True


def get_customer_by_email(email):

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, (email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(
                row['id'], row['name'], row['address'], row['email'], row['password'])
            customers.append(customer.__dict__)

    return customers
