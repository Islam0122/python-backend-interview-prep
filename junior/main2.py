import sqlite3
import re

DB_NAME = "words.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS words (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT NOT NULL
    )
    """)
    
    cur.execute("CREATE INDEX IF NOT EXISTS idx_word ON words(word)")
    conn.commit()
    conn.close()

def normalize_text(text: str):
    text = text.lower()
    return re.findall(r"[a-zа-яё]+", text)

def insert_words(words):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    
    cur.executemany(
        "INSERT INTO words (word) VALUES (?)",
        [(w,) for w in words]
    )
    
    conn.commit()
    conn.close()

def top_words(limit=5):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    
    cur.execute("""
        SELECT word, COUNT(*) as freq
        FROM words
        GROUP BY word
        ORDER BY freq DESC
        LIMIT ?
    """, (limit,))
    
    result = cur.fetchall()
    conn.close()
    return result

def search_word(word: str):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    
    cur.execute(
        "SELECT COUNT(*) FROM words WHERE word = ?",
        (word.lower(),)
    )
    
    count = cur.fetchone()[0]
    conn.close()
    return count

def main():
    init_db()
    
    text = input("Введи текст: ")
    words = normalize_text(text)
    
    insert_words(words)
    
    print("\nТоп слова:")
    for word, freq in top_words(5):
        print(f"{word}: {freq}")
    
    query = input("\nКакое слово найти? ")
    print(f"Слово '{query}' встречается:", search_word(query))

if __name__ == "__main__":
    main()