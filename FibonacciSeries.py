"""
TOPIC :FIBONACCI SERIES
DEVELOPED BY:ARYAN VERMA
"""
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
"""
SAMPLE OUTPUT :
Enter no. of terms :7
1,2,3,5,8,13,21,
"""
