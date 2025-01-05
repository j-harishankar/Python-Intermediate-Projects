def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sumprimes(numbers):
    total = 0
    for num in numbers:
        if is_prime(num):
            total += num
    return total

def matched(s):
    j=0
    for i in s:
        if '(' in s:
            if ')' in s:
                return True
                print("")
            else:
                return False
    if j>0:
        print("False")
matched("zb%78") 
matched("(7)(a")
matched("a)*(?")
matched(print("((jkl)78(A)&l(8(dd(FJI:),):)?)"))
  


