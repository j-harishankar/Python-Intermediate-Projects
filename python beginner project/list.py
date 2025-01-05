
#python lists example is roll no's

names = ["abi", "adi", "babu", "clement", "dora", "elizabeth", "frank", "gopi", "hari", "irwin", "joseph", "krishna"]
print(names[0])
print(names[2])
#it reads from backwords
print(names[-1])

#some methods on list mainly see and read documentation in video 45 for more reference 
names.append("leo")
names.extend(["manu", "niranjan", "orland"])

#to correct something in the list 
names[8] = "Hari"
print(names)
