import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (name TEXT NOT NULL, password TEXT UNIQUE NOT NULL, 
                 column1 INTEGER DEFAULT 0, column2 INTEGER DEFAULT 0, column3 INTEGER DEFAULT 0)''')
    conn.commit()


def add_user(conn, name, password):
    c = conn.cursor()
    c.execute("INSERT INTO users (name, password) VALUES (?, ?)", (name, password))
    conn.commit()

def check_user(conn, name):
    c = conn.cursor()
    c.execute("SELECT name, password, column1, column2, column3 FROM users WHERE name = ?", (name,))
    user_info = c.fetchone()

    if user_info:
        print("User found:", user_info)
        return True, user_info, user_info[2], user_info[3], user_info[4]  # Assuming the structure of your user_info
    else:
        response = input("No user found with that name. Do you want to add a new user? (yes/no): ").strip()
        if response.lower() in {'yes', 'y', ''}:
            password = input("Enter the user's password: ").strip()
            add_user(conn, name, password)
            return True, (name, password, 0, 0, 0), 0, 0, 0
        else:
            print("User not added.")
            return False, None, None, None, None

def update_progress(conn, name, column1, column2, column3):
    """
    Update the game progress for a given user.

    Parameters:
    - conn: The database connection object.
    - name: The name of the user.
    - column1, column2, column3: New values for the game progress (e.g., level, XP, coins).
    """
    sql = ''' UPDATE users
              SET column1 = ?, column2 = ?, column3 = ?
              WHERE name = ?'''
    cur = conn.cursor()
    cur.execute(sql, (column1, column2, column3, name))
    conn.commit()
