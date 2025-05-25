fp = open("code.txt",'w')
d = "programming in python"
fp.write(d)
fp.close()
fd = open("code.txt",'r')
w = fd.read()
print(w)
fd.close()
