import sqlite3
import bcrypt

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def update_database_schema(conn):
    try:
        c = conn.cursor()
        c.execute("ALTER TABLE users ADD COLUMN time TIMESTAMP")
    except sqlite3.OperationalError as e:
        print(f"Could not update database schema: {e}")
    finally:
        conn.commit()


def create_table(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (name TEXT NOT NULL, password TEXT UNIQUE NOT NULL, 
                 lvl INTEGER DEFAULT 0, xp INTEGER DEFAULT 0, coins INTEGER DEFAULT 0, time INTEGER DEFAULT 0)''')
    conn.commit()


def add_user(conn, name, password):
    c = conn.cursor()
    c.execute("INSERT INTO users (name, password) VALUES (?, ?)", (name, password))
    conn.commit()


def check_user(conn, name, password):
    c = conn.cursor()
    c.execute("SELECT name, password, lvl, xp, coins, time FROM users WHERE name = ?", (name,))
    user_info = c.fetchone()

    if user_info:
        hashed_password = user_info[1]
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            print("Login successful.")
            return True, user_info, user_info[2], user_info[3], user_info[4], user_info[5]
        else:
            print("Incorrect password.")
            return False, None, None, None, None, None
    else:
        response = input("No user found with that name. Do you want to add a new user? (yes/no): ").strip()
        if response.lower() in {'yes', 'y', ''}:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            add_user(conn, name, hashed_password)
            print("New user added and logged in.")
            return True, (name, hashed_password, 0, 0, 0, None), 0, 0, 0, None
        else:
            print("User not added.")
            return False, None, None, None, None, None


def update_progress(conn, name, lvl, xp, coins, time):
    c = conn.cursor()

    c.execute("SELECT time FROM users WHERE name = ?", (name,))
    result = c.fetchone()
    current_time_in_db = result[0] if result else None

    if current_time_in_db is None or current_time_in_db < time:
        c.execute("UPDATE users SET lvl = ?, xp = ?, coins = ?, time = ? WHERE name = ?", (lvl, xp, coins, time, name))
    else:
        c.execute("UPDATE users SET lvl = ?, xp = ?, coins = ?, time = ? WHERE name = ?", (lvl, xp, coins, current_time_in_db, name))

    conn.commit()
