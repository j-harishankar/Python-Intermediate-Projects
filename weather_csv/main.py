#with open("weather_data.csv") as fil:
#    line = fil.readlines()
#print(line)


#import csv
#l=[]
#with open("weather_data.csv") as fil:
 #   data = csv.reader(fil)
#    for i,j,z in data:
 #       if j!='temp':
#           l.append(int(j))    
#print(l) 

import pandas 
data = pandas.read_csv("Weather_data.csv")
print(data["temp"])

#data_list = data["temp"].to_list()
#avg_temp = sum(data_list)//len(data_list)
#print(avg_temp)

# using pandas method 

print(data["temp"].max())
#pandas convert the 1st row and column as attribute 
print(5*'*\n')
print(data.temp)
print(5*'*\n')
#print specific row 

print(data[data.day == 'Monday'])
print(5*'*\n')
print(data[data.temp==data.temp.max()])

monday = data[data.day=='Monday'] #this is a series since just one row
l = [monday.temp]
Faren = (l[0]*9/5)+32
print(Faren)


# create a dataframe from scratch

stud_dict = {"students":["Amy","John","Pork"],
             "marks":    [ 76, 56, 55],}

scratch = pandas.DataFrame(stud_dict)

scratch.to_csv("new.csv")