# this is about dictionary comprehension this is similar to list comprehension
#[q1] Do create the a dictionary that contains random mark of students in the list 
import random
names = ['hari','adithya','vivek','rosh','jydv','bob','raul']
#Dictionary comprehension
mark_dict = {name:random.randint(1,100) for name in names}
#passed_students={name:mark_dict[name] for name in mark_dict if mark_dict[name]>= 50 }
#or 
passed_students = {name:score for (name,score) in mark_dict.items() }
print(passed_students)