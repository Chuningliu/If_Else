a=int(input("Enter the three sides"))
b=int(input("Enter the three sides"))
c=int(input("Enter the three sides"))
if (a+b>c) and (a+c>b) and (b+c>a):
    print("Triangle is valid")
else:
    print("Triangle is invalid")

