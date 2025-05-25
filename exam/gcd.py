x = int(input("Enter the value for x"))
y = int(input("Enter the value for y"))
w=1
for i in range(abs(y)):
    w*=abs(x)
if y<0:
   w = 1/(w)
print(f"{x}^{y}={w}")