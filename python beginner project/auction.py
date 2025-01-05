import os
auc = '''                                  
( ___ )-----------------------------------------------( ___ )
 |   |                                                 |   | 
 |   |     _   _   _  ____ _____ ___ ___  _   _ _ _ _  |   | 
 |   |    / \ | | | |/ ___|_   _|_ _/ _ \| \ | | | | | |   | 
 |   |   / _ \| | | | |     | |  | | | | |  \| | | | | |   | 
 |   |  / ___ | |_| | |___  | |  | | |_| | |\  |_|_|_| |   | 
 |   | /_/   \_\___/ \____| |_| |___\___/|_| \_(_(_(_) |   | 
 |___|                                                 |___| 
(_____)-----------------------------------------------(_____)'''
def winner(dict):
        '''this is 
        used to 
        find the winner 
        with highest amount of bid'''
        largest=0
        name=''
        for key in dict:
            bid_amt = dict[key]
            if largest<bid_amt:
                largest = bid_amt
                name = key 

        print(f"The winner is {name} and his bid amount is {largest}")
print(auc)
choice = input("Want to start Yes or No").lower()
choice = True
d_b = {}
while choice:
    name = input("Give your name")
    bid = int(input("choose your bid"))
    d_b[name]=bid 
    choice = input("Want to continue Yes or No").lower()
    if choice=='no':
        choice = False
        winner(d_b)
      
    else:
         os.system('cls')
                
            
             

    