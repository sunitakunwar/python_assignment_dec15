'''Q1. The salary of employees in a software company is stored in a list,
i.e. salary = [15000, 20000, 17000, 18900, 30000].
When annual review was conducted, accounting department made a decision to increase the salary of every employee by 23%.
Now, write a pythonic code to find out how much is the total salary for each employee after the raise.'''

def salary(salary):
    return salary + 0.23*salary


past_salary = [15000, 20000, 17000, 18900, 30000]
print("Total  increase in salary by 23% are : \n")

for each_salary in past_salary:
    constant = salary(each_salary)
    print("{:.3f}\n".format(constant))