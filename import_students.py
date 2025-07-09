import csv
import sqlite3

# Connect to local SQLite DB
conn = sqlite3.connect("my_database.db")  # Make sure this .db file exists
cursor = conn.cursor()

with open("students.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute("""
            INSERT INTO students (first_name, last_name, email, gpa)
            VALUES (?, ?, ?, ?)
        """, (row['first_name'], row['last_name'], row['email'], row['gpa']))

conn.commit()
cursor.close()
conn.close()

print("✅ Students imported into SQLite database.")