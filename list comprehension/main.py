#list
numbers = [1,2,3]
new_list = [item+1 for item in numbers]
print(new_list)
#string
name = "hari"
name_list = [letter for letter in name]
print(name_list)
#range
range_list = [rng*2 for rng in range(1,11)]
print(range_list)

#conditional list comprehension

names = ['hari','adithya','vivek','rosh','jydv','bob','raul']
name_four_list = [name.upper() for name in names if len(name)<=4]
print(name_four_list)