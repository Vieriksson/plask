
import sqlite3
from sqlite3 import Error

from data import data


def feck_tuples(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


def create_connection():
    try:
        conn = sqlite3.connect(':memory:')
        conn.row_factory = feck_tuples

        return conn
    except Error as e:
        print(e)

    return None


def select_members(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM members")
    rows = cur.fetchall()
    return rows


def select_member(conn, id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM members WHERE id = %s" % (id))
    row = cur.fetchone()
    return row


def select_users(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    return rows


def create_tables(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE members
             (id integer, name text, title text, description text)''')
    c.execute('''CREATE TABLE users
             (id integer, username text)''')
    conn.commit()


def populate_with_test_members(conn):
    c = conn.cursor()
    for member in data.members:
        query = "INSERT INTO members VALUES (%d, '%s', '%s', '%s')" % (
            member.id, member.name, member.title, member.description)
        c.execute(query)
    conn.commit()


def populate_with_test_users(conn):
    c = conn.cursor()
    for user in data.users:
        query = "INSERT INTO users VALUES (%d, '%s')" % (
            user.id, user.username)
        c.execute(query)
    conn.commit()
