import sys

A=int(sys.stdin.readline())

if A>=90:
    print("A")
    
elif A>=80 and A<=89:
    print("B")

elif A>=70 and A<=79:
    print("C")

elif A>=60 and A<=69:
    print("D")

else:
    print("F")