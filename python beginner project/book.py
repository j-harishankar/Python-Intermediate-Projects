# Dictionary to map accession number to title
books = {}
# Dictionary to map username to fullname
borrowers = {}
# List to store checkout data: accumulate, sort and print
checkouts = [] 

# Find the start of Books data
nextline = input().strip()
while nextline.find("Books") < 0:
    nextline = input().strip()

# Read upto start of Borrowers data
# Skip the line with "Books"
nextline = input().strip()
while nextline.find("Borrowers") < 0:
    (accession_number,title) = nextline.split('~')
    books[accession_number] = title
    nextline = input().strip()

# Read upto Checkout data
# Skip the line with "Borrowers"
nextline = input().strip()
while nextline.find("Checkouts") < 0:
    (username,fullname) = nextline.split('~')
    borrowers[username] = fullname
    nextline = input().strip()

# Process Checkouts
# Skip the line with "Checkouts"
nextline = input().strip()
while nextline.find("EndOfInput") < 0:
    (username,accession_number,due_date) = nextline.split('~')
    checkoutline = due_date+"~"+borrowers[username]+"~"+accession_number+"~"+books[accession_number]
    checkouts.append(checkoutline)
    nextline = input().strip()

# Print the output from checkouts
for checkoutline in sorted(checkouts):
    print(checkoutline)