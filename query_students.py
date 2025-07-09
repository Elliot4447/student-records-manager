import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), "my_database.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Ask for a GPA threshold
try:
    gpa_threshold = float(input("Enter GPA threshold: "))
    cursor.execute("""
        SELECT first_name, last_name, gpa
        FROM students
        WHERE gpa >= ?
        ORDER BY gpa DESC
    """, (gpa_threshold,))

    results = cursor.fetchall()
    if results:
        print("\nStudents with GPA ≥", gpa_threshold)
        for row in results:
            print(f"{row[0]} {row[1]} – GPA: {row[2]}")
    else:
        print("No students meet that GPA requirement.")

except ValueError:
    print("❌ Invalid number. Please enter a decimal like 3.5")

cursor.close()
conn.close()