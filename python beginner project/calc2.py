def add(n1,n2):
    return(n1+n2)
def sub(n1,n2):
    return(n1-n2)
def div(n1,n2):
    return(n1/n2)
def mul(n1,n2):
    return(n1*n2)
try:
   s = True
   while s:
        cont = True
        a = float(input("Enter the first number"))
        while cont:
            operations = {'+':add,'-':sub,'/':div,'*':mul}
            for key in operations:
                print(key)
            operator = input("choose the operator")
            b = float(input("Enter the second value"))
            c=operations[operator](a,b)
            print(c)
            ch = input("Do you want to continue with result or reset and start yes or no/exit")
            if ch == 'no':
                cont=False
            elif ch == 'e':
                s = False
            else:
                a = c
            
except ValueError:
    print("Enter a valid number ")
