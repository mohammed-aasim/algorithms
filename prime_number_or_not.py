number = int(input("Enter the input Range : "))
for iter in range(2,number):
    for i in range(2,iter):
        if (iter%i==0):
            break
    else:
        print(iter)