import csv
import sqlite3

# Establish a connection to the SQLite database file
# If the file doesn't exist, it will be created automatically
conn = sqlite3.connect("my_database.db")
# Create a cursor object to interact with the database
cursor = conn.cursor()

# SQL command to create the 'students' table if it doesn't already exist
# Columns: id (auto), first name, last name, email, and GPA
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    gpa REAL
)
""")

# Open the CSV file containing student data for reading
with open("students.csv", newline="") as csvfile:
    # Use DictReader to convert each CSV row into a dictionary
    reader = csv.DictReader(csvfile)  # Automatically maps CSV headers to dictionary keys
    for row in reader:
        # Insert the current student's data into the students table
        cursor.execute("""
            INSERT INTO students (first_name, last_name, email, gpa)
            VALUES (?, ?, ?, ?)
        """, (row['first_name'], row['last_name'], row['email'], row['gpa']))

# Commit the transaction to save all changes to the database
conn.commit()

# Close the cursor and database connection
cursor.close()
conn.close()

print("Students imported into SQLite database.")