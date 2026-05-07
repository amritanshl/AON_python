from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, text
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine('sqlite:///company_orm.db', echo=False)


with engine.connect() as connection:
    # We use .execute() directly on the connection for simple tasks
    result = connection.execute(text("SELECT 'Connection Active!'"))
    print(result.all()) # Should print [('Connection Active!',)]
Base = declarative_base()

class Department(Base):
    __tablename__ = 'departments' # Name of the table in the DB
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    # Relationship: Tells SQLAlchemy this dept has many employees
    employees = relationship("Employee", back_populates="department")

class Manager(Base):
    __tablename__ = 'managers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    # One manager can oversee many employees
    employees = relationship("Employee", back_populates="manager")

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    position = Column(String)
    
    # Foreign Keys: Storing the ID of the linked table
    dept_id = Column(Integer, ForeignKey('departments.id'))
    mgr_id = Column(Integer, ForeignKey('managers.id'))
    
    # Links back to the Classes
    department = relationship("Department", back_populates="employees")
    manager = relationship("Manager", back_populates="employees")

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

it_dept = Department(name="IT")
mgr_alice = Manager(name="Alice Vance")

# Linking objects directly instead of using IDs!
new_emp = Employee(name="James Wilson", position="Dev", department=it_dept, manager=mgr_alice)

# Add to the session and save
session.add_all([it_dept, mgr_alice, new_emp])
session.commit() # Save to disk

# 7. READING DATA (Pythonic Queries)
print("--- Querying with SQLAlchemy ---")
# Find the employee and their department name without writing a JOIN string
emp = session.query(Employee).filter_by(name="James Wilson").first()
print(f"Employee: {emp.name} | Dept: {emp.department.name} | Mgr: {emp.manager.name}")





# (Assuming the models from Example 1 are imported)
Session = sessionmaker(bind=engine)
session = Session()

# 4. INSERT: Adding data using Python Objects
it_dept = Department(name="Information Technology")
boss = Manager(name="Alice Vance", dept_id=1)
new_hire = Employee(name="James Wilson", position="Dev", dept_id=1, mgr_id=1)

session.add_all([it_dept, boss, new_hire]) # Add to 'Waiting Room'
session.commit() # Save to disk

# 5. READ: Querying using method chaining
# Find the first employee whose name is James
james = session.query(Employee).filter(Employee.name == "James Wilson").first()
# selct TOP(1) * from Employee wher ename = "James  Wilson"

# Find all employees in the IT department
it_staff = session.query(Employee).filter_by(dept_id=1).all()

print(f"Found Hire: {james.name} - {james.position}")
print(f"Total IT Staff Count: {len(it_staff)}")
session.close()


try:
    # 3. Create a new employee object
    new_staff = Employee(name="Sarah Connor", position="Security")
    
    # 4. The .add() puts Sarah in the 'Waiting Room'
    session.add(new_staff)
    print("Sarah is added to the session, but NOT yet in the database.")
    
    # 5. The .commit() pushes the changes to the disk
    session.commit()
    print("Changes saved to the database file!")

except Exception as e:
    # If something goes wrong, 'rollback' cancels all unsaved changes in the session
    session.rollback()
    print(f"Error occurred: {e}")
finally:
    # Always close the session to free up resources
    session.close()