import sqlite3

def setup_database():
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL CHECK(length(name) <= 4),
            score INTEGER NOT NULL,
            time TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
    print("Banco de dados criado com sucesso!")