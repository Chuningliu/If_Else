user=int(input("Enter the number"))
if user<=25:
    print("F")
elif user>=25 and user<45:
    print("E")
elif user>=45 and user<50:
    print("D")
elif user>=50 and user<60:
    print("C")
elif user>=60 and user<80:
    print("B")
elif user>80:
    print("A")
else:
    print("Fail")