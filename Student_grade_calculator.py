name=input("Enter the name: ")
mark1=float(input("Enter the marks: "))
mark2=float(input("Enter the marks: "))
mark3=float(input("Enter the marks: "))
mark4=float(input("Enter the marks: "))
mark5=float(input("Enter the marks: "))
Total=mark1+mark3+mark4+mark2+mark5
average=Total/5
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\n----- RESULT -----")
print("Name:", name)
print("Total Marks:", Total)
print("Average:", average)
print("Grade:", grade)
