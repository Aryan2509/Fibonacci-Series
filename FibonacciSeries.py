n=int(input("Enter no. of terms :"))
a=0
b=1
i=1
while i<=n:
    c=a+b
    print(c,end=",")
    a=b
    b=c
    i+=1
        
    
