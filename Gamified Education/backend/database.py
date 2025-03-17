import sqlite3

def create_db():
    conn = sqlite3.connect('education.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS progress (
                    user_id INTEGER PRIMARY KEY,
                    points INTEGER,
                    level INTEGER
                )''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
