# name, dept, salary
import random

names = ['John', 'Sam', 'Dave']
depts = ['Computer Science', 'Physics', 'Music', 'Economics', 'Agriculture']
age_range = (15, 80)
salary_range = (1, 20)
salary_unit = 1000      # in USD 

record_count = 1000

with open('sample.csv', 'w') as f:
    for i in range(record_count):
        name = '{0}-{1}'.format(random.choice(names), random.randint(0,1000))
        dept = random.choice(depts)
        age = random.randint(*age_range)
        salary = random.randint(*salary_range) * salary_unit

        record = '{0},{1},{2},{3}'.format(name, dept, age, salary)

        print record
        
        f.write(record + '\n')

