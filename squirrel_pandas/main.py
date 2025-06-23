import pandas

data = pandas.read_csv("2018_squirrel.csv")
gray = len(data[data["Primary Fur Color"]=='Gray'])
cinnamon = len(data[data["Primary Fur Color"]=='Cinnamon'])
white = len(data[data["Primary Fur Color"]=='Cinnamon']) 

new_dict = {"fur color":['gray','cinnamon','white'],
              "count":[gray,cinnamon,white]  }

df = pandas.DataFrame(new_dict)
df.to_csv("result.csv")