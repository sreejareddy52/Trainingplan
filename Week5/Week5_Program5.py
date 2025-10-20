import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    salary REAL,
    department TEXT
)
""")


employees_data = [
    (1, 'Alice', 72000, 'Engineering'),
    (2, 'Bob', 48000, 'Sales'),
    (3, 'Charlie', 55000, 'Marketing'),
    (4, 'David', 95000, 'Engineering'),
    (5, 'Eve', 51000, 'HR'),
    (6, 'Frank', 45000, 'Support'),
    (7, 'Grace', 87000, 'Engineering'),
    (8, 'Hannah', 62000, 'Finance'),
    (9, 'Ivan', 40000, 'Sales'),
    (10, 'Judy', 77000, 'Marketing')
]
cursor.executemany("INSERT OR REPLACE INTO Employees VALUES (?, ?, ?, ?)", employees_data)
conn.commit()


print("\nAll Employees:")
for row in cursor.execute("SELECT * FROM Employees"):
    print(row)


print("\nEmployees with salary > 50,000:")
for row in cursor.execute("SELECT * FROM Employees WHERE salary > 50000"):
    print(row)


print("\nEmployees sorted by salary (highest to lowest):")
for row in cursor.execute("SELECT * FROM Employees ORDER BY salary DESC"):
    print(row)


conn.close()
