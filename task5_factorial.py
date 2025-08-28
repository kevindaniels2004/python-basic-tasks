def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n-1)
    
n=int(input("enter a  number "))    
result =  fact(n)
print(f"factorial of {n} is ",result)