import pyodbc

# 1. Connect to 'master' so the connection doesn't fail if emp_test is missing
conn_str = (
    'DRIVER={SQL Server};'
    'SERVER=Amrit\\SQLEXPRESS;'
    'DATABASE=master;'  # Changed from emp_test to master
    'Trusted_Connection=yes;'
)

# Connect and enable autocommit (required for CREATE DATABASE)
connection = pyodbc.connect(conn_str, autocommit=True)
cursor = connection.cursor()

# 2. Create Database if it doesn't exist
cursor.execute("IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'emp_test') CREATE DATABASE emp_test")

# 3. Switch to the new database
cursor.execute("USE emp_test")

# 4. Create Tables (SQL Server / T-SQL Syntax)
# Note: 'TEXT' is deprecated in SQL Server, use 'NVARCHAR(MAX)' or 'NVARCHAR(50)'
cursor.execute('''
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'departments') AND type in (N'U'))
CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name NVARCHAR(100) NOT NULL
)
''')

cursor.execute('''
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'managers') AND type in (N'U'))
CREATE TABLE managers (
    mgr_id INTEGER PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES departments (dept_id)
)
''')

cursor.execute('''
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'employees') AND type in (N'U'))
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    position NVARCHAR(100),
    mgr_id INTEGER,
    dept_id INTEGER,
    FOREIGN KEY (mgr_id) REFERENCES managers (mgr_id),
    FOREIGN KEY (dept_id) REFERENCES departments (dept_id)
)
''')

# 5. Insert Data Logic (SQL Server does not have "INSERT OR IGNORE")
depts = [(1, 'IT'), (2, 'HR'), (3, 'Sales'), (4, 'Marketing')]
for d in depts:
    cursor.execute("IF NOT EXISTS (SELECT 1 FROM departments WHERE dept_id = ?) INSERT INTO departments VALUES (?,?)", (d[0], d[0], d[1]))

mgrs = [(101, 'Alice Vance', 1), (102, 'Bob Miller', 3), (103, 'Charlie Day', 4)]
for m in mgrs:
    cursor.execute("IF NOT EXISTS (SELECT 1 FROM managers WHERE mgr_id = ?) INSERT INTO managers VALUES (?,?,?)", (m[0], m[0], m[1], m[2]))

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
for e in emps:
    cursor.execute("IF NOT EXISTS (SELECT 1 FROM employees WHERE emp_id = ?) INSERT INTO employees VALUES (?,?,?,?,?)", (e[0], e[0], e[1], e[2], e[3], e[4]))

# 6. Verify by querying the data
print("Employee List from IT Department:")
cursor.execute('SELECT name, position FROM employees WHERE dept_id = 1')
rows = cursor.fetchall()
for row in rows:
    print(f"Name: {row[0]} | Position: {row[1]}")

# 7. Close the connection
connection.close()