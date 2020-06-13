# -------- დავალება 1--------
import sqlite3

conn = sqlite3.connect("book_db.sqlite")
cursor = conn.cursor()

cursor.execute("SELECT title FROM books WHERE author='William Shakespeare'")
print(cursor.fetchall())

cursor.execute("SELECT title FROM books WHERE author='William Shakespeare' OR author='Rowling'")
print(cursor.fetchall())

b = cursor.execute("SELECT title FROM books WHERE price <= 20")
print(b.fetchall())

cursor.execute("SELECT user_id, book_id FROM purchase WHERE purchase_date < '2018-01-01'")
print(cursor.fetchall())

cursor.execute('''SELECT DISTINCT user_id
                  FROM purchase
                  WHERE purchase_date >= '2018-01-01' and purchase_date <= '2018-12-31' ''')

print(cursor.fetchall())

u = cursor.execute("SELECT username FROM users WHERE balance > 100")
for each in u:
    print(each)

cursor.execute("SELECT DISTINCT user_id FROM purchase WHERE book_id IS NOT NULL")
print(cursor.fetchall())

# 8 დავალება ვერ გავაკეთე

cursor.execute('''SELECT users.username, users.balance, books.title
                  FROM users JOIN purchase on (users.id = purchase.user_id)
                  JOIN books on (purchase.book_id = books.id)
                  order by 1''')

print(cursor.fetchall())

conn.close()
