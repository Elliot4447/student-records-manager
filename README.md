# 🎓 Student Records Manager

A simple Python + SQLite command-line project to manage and query student academic data.

This project demonstrates:
- Reading and parsing `.csv` files
- Writing data into a SQLite database
- Querying data based on user input
- Command-line interaction with user input handling

---

## 📁 Project Structure

```
student-records-manager/
├── import_students.py     # Loads student data from CSV to DB
├── query_students.py      # Queries students by GPA
├── students.csv           # Sample input file
├── .gitignore             # Excludes .db and Python cache
└── README.md              # Project description and usage
```

---

## ⚙️ How to Run

### 1. Import student data into the database

```bash
python3 import_students.py
```

### 2. Query students by GPA

```bash
python3 query_students.py
```

You’ll be prompted to enter a GPA threshold (e.g., `3.5`) and the matching students will be displayed.

---

## 💾 Technologies Used

- Python 3
- SQLite (via `sqlite3`)
- CSV module (`csv.DictReader`)
- Git & GitHub

---

## 🧠 What I Learned

- Managing SQLite tables via Python
- Working with CSV files
- Parameterized queries for safe database interaction
- Clean file structure and version control with Git

---

## ✅ Future Improvements

- Add search by name or email
- Add a Flask web interface
- Export filtered results to CSV or PDF
- Deploy as a web-based form tool

---

## 📜 License

This project is free to use under the [MIT License](https://opensource.org/licenses/MIT).