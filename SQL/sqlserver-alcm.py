from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

#  Connection string for SQL Server with Windows Authentication
# Replace "SQLEXPRESS" with your instance name if different
engine = create_engine(
    "mssql+pyodbc://@SQLEXPRESS/emp_test?driver=ODBC+Driver+17+for+SQL+Server;Trusted_Connection=yes",
    echo=True
)

Base = declarative_base()

# --- Departments Table ---
class Department(Base):
    __tablename__ = "departments"

    dept_id = Column(Integer, primary_key=True, nullable=False)
    dept_name = Column(String(100), nullable=False)

    # relationships
    employees = relationship("Employee", back_populates="department")
    managers = relationship("Manager", back_populates="department")

# --- Managers Table ---
class Manager(Base):
    __tablename__ = "managers"

    mgr_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    dept_id = Column(Integer, ForeignKey("departments.dept_id"))

    # relationships
    department = relationship("Department", back_populates="managers")
    employees = relationship("Employee", back_populates="manager")

# --- Employees Table ---
class Employee(Base):
    __tablename__ = "employees"

    emp_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    position = Column(String(100))
    mgr_id = Column(Integer, ForeignKey("managers.mgr_id"))
    dept_id = Column(Integer, ForeignKey("departments.dept_id"))

    # relationships
    department = relationship("Department", back_populates="employees")
    manager = relationship("Manager", back_populates="employees")

# --- Create tables in DB ---
Base.metadata.create_all(engine)

# --- Session setup ---
Session = sessionmaker(bind=engine)
session = Session()

# Example: Insert a department
it_dept = Department(dept_id=1, dept_name="IT")
session.add(it_dept)
session.commit()

# Example: Query employees
for emp in session.query(Employee).all():
    print(emp.emp_id, emp.name, emp.position)
