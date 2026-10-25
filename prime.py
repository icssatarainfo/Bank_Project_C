n = int(input("Enter Any No = "))
for i in range(2,n+1):
    if n%i==0:
        break

if i==n:
    print("It Is Prime Number")
else:
    print("Not Prime Number")
