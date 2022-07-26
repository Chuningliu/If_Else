user=int(input("Enter the percentage"))
if user<25:
    print("Grade D")
elif user>25 and user<=45:
    print("Grade C")
elif user>45 and user<=50:
    print("Grade B")
elif user>50 and user<=60:
    print("Grade B+")
elif user>60  and user<=80:
    print("Grade A")
elif user>80:
    print("Grade A+")
# else:
#     print("Absent")
