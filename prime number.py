n=14
flag=0
if n==0 or n==1:
    print("Not Prime Number")
elif n==2:
    print("Prime Number")
else:
    for i in range(3,n):
        if n%i==0:
            flag+=1

    if flag==False:
        print("Prime Number")
    else:
        print("Not Prime Number")