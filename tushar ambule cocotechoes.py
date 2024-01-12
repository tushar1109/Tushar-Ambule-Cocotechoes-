#Question 1:
#We have a bunch of employees. Each employee gets a commission every month, so 12
#commissions a year.
#You need to create data for about 100 employees, with names like “Employee1”, “Employee2”.
#The commission for each month can be a random amount between 1000 and 5000. Find the
#Top 5 people with the highest average commission
#Hint: Use an array to store commission for each month of the year

import random

def generate_commission():
    return random.uniform(1000, 5000) #I used this for generating random commission

employees = 100 #100 employees
months = 12 #12 months

employees_commissions = {}  #I created a dictionary to store commissions for each employee

for i in range(1, employees + 1):
    employee_name = f"Employee{i}"
    employees_commissions[employee_name] = [generate_commission() for _ in range(months)]  #used to generate data to every employee

average_commissions = {employee: sum(commissions) / months for employee, commissions in employees_commissions.items()} # calculating average commission 

top_5_people = sorted(average_commissions.items(), key=lambda x: x[1], reverse=True)[:5] #finding Top 5 people with the highest average commission

print("Top 5 people with the highest average commission:")
for employee, avg_commission in top_5_people:
    print(f"{employee}: ₹{avg_commission:.2f}")
