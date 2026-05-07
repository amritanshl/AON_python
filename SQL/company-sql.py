import sqlite3 # Import the built-in SQLite library

# 1. Connect to the database (it creates the file if it doesn't exist)
connection = sqlite3.connect('office.db')

# 2. Create a 'cursor' object; think of this as the 'pen' that writes SQL commands
cursor = connection.cursor()

# 3. Create the Tables
# Create Departments table
cursor.execute('''
CREATE TABLE IF NOT EXISTS departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT NOT NULL
)
''')

# Create Managers table
cursor.execute('''
CREATE TABLE IF NOT EXISTS managers (
    mgr_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES departments (dept_id)
)
''')

# Create Employees table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    position TEXT,
    mgr_id INTEGER,
    dept_id INTEGER,
    FOREIGN KEY (mgr_id) REFERENCES managers (mgr_id),
    FOREIGN KEY (dept_id) REFERENCES departments (dept_id)
)
''')

# 4. Insert Data
# Inserting 4 Departments
depts = [(1, 'IT'), (2, 'HR'), (3, 'Sales'), (4, 'Marketing')]
cursor.executemany('INSERT OR IGNORE INTO departments VALUES (?, ?)', depts)

# Inserting 3 Managers
mgrs = [
    (101, 'Alice Vance', 1), # IT Manager
    (102, 'Bob Miller', 3),  # Sales Manager
    (103, 'Charlie Day', 4)  # Marketing Manager
]
cursor.executemany('INSERT OR IGNORE INTO managers VALUES (?, ?, ?)', mgrs)

# Inserting 20 Employees
# Format: (ID, Name, Position, ManagerID, DeptID)
emps = [
    (1, 'James Wilson', 'Developer', 101, 1), (2, 'Mary Smith', 'SysAdmin', 101, 1),
    (3, 'John Doe', 'Developer', 101, 1), (4, 'Patricia Brown', 'QA Engineer', 101, 1),
    (5, 'Robert Jones', 'DevOps', 101, 1), (6, 'Linda Garcia', 'Account Exec', 102, 3),
    (7, 'Michael Miller', 'Sales Rep', 102, 3), (8, 'Barbara Davis', 'Sales Rep', 102, 3),
    (9, 'William Rodriguez', 'Sales Rep', 102, 3), (10, 'Elizabeth Martinez', 'Sales Rep', 102, 3),
    (11, 'David Hernandez', 'Copywriter', 103, 4), (12, 'Susan Lopez', 'Designer', 103, 4),
    (13, 'Joseph Gonzalez', 'SEO Specialist', 103, 4), (14, 'Jessica Wilson', 'Social Media', 103, 4),
    (15, 'Thomas Anderson', 'Analyst', 103, 4), (16, 'Karen Taylor', 'HR Specialist', None, 2),
    (17, 'Nancy Thomas', 'Recruiter', None, 2), (18, 'Steven Moore', 'HR Assistant', None, 2),
    (19, 'Paul Jackson', 'Intern', 101, 1), (20, 'Lisa White', 'Intern', 102, 3)
]
cursor.executemany('INSERT OR IGNORE INTO employees VALUES (?, ?, ?, ?, ?)', emps)

# 5. Commit the changes (Save to disk)
connection.commit()

# 6. Verify by querying the data
print("Employee List from IT Department:")
cursor.execute('SELECT name, position FROM employees WHERE dept_id = 1')
for row in cursor.fetchall():
    print(f"Name: {row[0]} | Position: {row[1]}")
    print(row)


# 7. Close the connection
connection.close()