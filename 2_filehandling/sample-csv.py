import csv

data = [
    ['Account_No', 'Customer_Name', 'Balance', 'City'],
    [106, 'Pooja Hegde', 7200.00, 'Bangalore']
]

# with open('hdfc_customers.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     # Technical Note: writerows() takes a list of lists
#     writer.writerows(data)
# with open('hdfc_customers.csv', 'r') as f:
#     writer = csv.reader(f)
#     next(writer)
#     count = sum(1 for row in writer)
#     print(count)
#     # Technical Note: writerows() takes a list of lists
#     for row in writer:
#         print(row[1])
    
# import csv

# new_record = [107, 'Vijay Kumar', 3000.00, 'Pune']

# with open('hdfc_customers.csv', 'a', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(new_record)

 
import csv
data = [['Account no','Customer name','balance','city'],
        [106,'Amritans gupta',100000.00,'ghaziabad']
        ]
with open('customer.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(data)
 