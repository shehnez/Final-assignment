marks=int(input("Please enter the marks:"))

if(marks >= 80):
    grade="A Grade"
elif(marks >= 60):
    grade = "B Grade"  
elif(marks >= 35):
    grade = "C Grade"
else:
    grade = "Fail"

print("Marks:",marks)
print("Grade:",grade)        


