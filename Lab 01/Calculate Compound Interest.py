def compound_interest():
    p=float(input("Enter the principal:"))
    r=float(input("Enter the interest rate:"))
    t=float(input("Enter the time in year:"))
    A=p*(1+r/100)**t
    return A
a=compound_interest()
print("Compound interest:",a)
