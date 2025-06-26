# Dictionary Comprehension 2
# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit. 



# To convert temp_c into temp_f use this formula: 

# (temp_c * 9/5) + 32 = temp_f

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {c:round((t*(9/5)+32),1) for (c,t) in weather_c.items()}

print(weather_f)