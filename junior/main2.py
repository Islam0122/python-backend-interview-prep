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

def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

content = read_file("test.txt")
print(content)

from datetime import datetime
import pytz

# Часовые пояса
moscow_tz = pytz.timezone("Europe/Moscow")
turkey_tz = pytz.timezone("Europe/Istanbul")
london_tz = pytz.timezone("Europe/London")

# Ввод времени
user_time = input("Введите время (формат ЧЧ:ММ): ")

# Преобразуем строку во время (сегодняшняя дата)
now = datetime.now()
dt = datetime.strptime(user_time, "%H:%M")
dt = dt.replace(year=now.year, month=now.month, day=now.day)

# Предположим, что введённое время — локальное (UTC)
utc = pytz.utc.localize(dt)

# Конвертация
moscow_time = utc.astimezone(moscow_tz)
turkey_time = utc.astimezone(turkey_tz)
london_time = utc.astimezone(london_tz)

# Вывод
print("\nВремя в разных странах:")
print("Москва:", moscow_time.strftime("%H:%M"))
print("Турция:", turkey_time.strftime("%H:%M"))
print("Лондон:", london_time.strftime("%H:%M"))