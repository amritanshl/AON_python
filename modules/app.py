# app.py
import hr_utils as hr

import config

# Access functions using the 'module.function' syntax
salary = hr.calculate_package(80000, 15000)
status = hr.verify_experience(6)

print(f"Offer: {salary}")
print(f"Status: {status}")
print(f"Motto: {hr.company_motto}")
login_tries = 21
if login_tries > config.MAX_LOGIN_ATTEMPTS:
    print("Account Locked.")