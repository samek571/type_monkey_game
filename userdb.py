import sqlite3
import bcrypt
import json

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

#call just once, make a function call and delete it
def update_database_schema(conn):
    try:
        c = conn.cursor()
        #c.execute("ALTER TABLE users ADD COLUMN owned_stuff TEXT")
    except sqlite3.OperationalError as e:
        print(f"Could not update database schema: {e}")
    finally:
        conn.commit()


def create_table(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (name TEXT NOT NULL, password TEXT UNIQUE NOT NULL, 
                 lvl INTEGER DEFAULT 0, xp INTEGER DEFAULT 0, coins INTEGER DEFAULT 0, 
                 time INTEGER DEFAULT 0, owned_stuff TEXT)''')
    conn.commit()


def add_user(conn, name, password):
    c = conn.cursor()
    owned_stuff = json.dumps({})
    c.execute("INSERT INTO users (name, password, owned_stuff) VALUES (?, ?, ?)",
              (name, password, owned_stuff))
    conn.commit()

def check_user(conn, name, password):
    c = conn.cursor()
    c.execute("SELECT name, password, lvl, xp, coins, time, owned_stuff FROM users WHERE name = ?", (name,))
    user_info = c.fetchone()

    if user_info:
        hashed_password = user_info[1]
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            owned_stuff = json.loads(user_info[6]) if user_info[6] else {}
            print("Login successful.")
            return True, True, *user_info[2:6], owned_stuff
        else:
            print("Incorrect password.")
            return True, False, *[None]*4, {}
    else:
        response = input("No user found with that name. Do you want to add a new user? (yes/no): ").strip()
        if response.lower() in {'yes', 'y', ''}:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            add_user(conn, name, hashed_password)
            print("New user added and logged in.")
            return True, (name, hashed_password, 0, 0, 0, None), {}
        else:
            print("User not added.")
            return False, None, None

def get_highscore(conn, name):
    c = conn.cursor()
    c.execute("SELECT lvl, xp, coins, time, owned_stuff FROM users WHERE name = ?", (name,))
    result = c.fetchone()
    return list(result)

def update_progress(conn, name, lvl, xp, coins, time, owned_stuff):
    c = conn.cursor()

    c.execute("SELECT time FROM users WHERE name = ?", (name,))
    result = c.fetchone()
    current_time_in_db = result[0] if result else None

    owned_stuff_json = json.dumps(owned_stuff)

    if current_time_in_db is None or current_time_in_db < time:
        c.execute("UPDATE users SET lvl = ?, xp = ?, coins = ?, time = ?, owned_stuff = ? WHERE name = ?",
                  (lvl, xp, coins, time, owned_stuff_json, name))
    else:
        c.execute("UPDATE users SET lvl = ?, xp = ?, coins = ?, time = ?, owned_stuff = ? WHERE name = ?",
                  (lvl, xp, coins, current_time_in_db, owned_stuff_json, name))

    conn.commit()