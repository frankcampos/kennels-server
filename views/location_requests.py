import json
import sqlite3
from models import Location


LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
]


def get_all_locations():
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        """)
        locations = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            location = Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__)
    return locations


def get_single_location(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address

        FROM animal a
        WHERE a.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        location = Location(data['id'], data['name'], data['address'])

        return location.__dict__


def create_location(location):
    max_id = LOCATIONS[-1]["id"]
    new_id = max_id + 1

    location["id"] = new_id

    LOCATIONS.append(location)
    return location


def delete_location(id):
    """Delete a location by Id"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM location
        WHERE id = ?
        """, (id, ))
    return "you deleted a location successfully"


def update_location(id, new_location):

    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE location
            SET
                name = ?,
                address = ?
        WHERE id = ?
        """, (new_location['name'], new_location['address'], id))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
