# Student Marks Analyzer
# Write a program that accepts the marks obtained by a student in five subjects.
# The program should determine the highest marks, lowest marks, and average marks obtained by the student, and display all three results.

# Variables to Store Highest, Lowest and Average Marks
highestMarks = 0;
lowestMarks = 100;


# Taking Marks for Five Subjects as Input
subject1 = input("Enter Marks for Subject 1: ");
subject2 = input("Enter Marks for Subject 2: ");
subject3 = input("Enter Marks for Subject 3: ");
subject4 = input("Enter Marks for Subject 4: ");
subject5 = input("Enter Marks for Subject 5: ");



# Finding the Highest Marks
if highestMarks < subject1:
    highestMarks = highestMarks + subject1;
#removed if and added elif to find the highest marks
elif highestMarks < subject2:
    highestMarks = highestMarks + subject2;

elif highestMarks < subject3:
    highestMarks = highestMarks + subject3;

elif highestMarks < subject4:
    highestMarks = highestMarks + subject4;
# added else to find the highest marks
else:
    highestMarks = highestMarks + subject5;




# Finding the Lowest Marks
if lowestMarks > subject1:
    lowestMarks = subject1;
# added elif to find the lowest marks
elif lowestMarks > subject2:
    lowestMarks = subject2;

elif lowestMarks > subject3:
    lowestMarks = subject3;

elif lowestMarks > subject4:
    lowestMarks = subject4;

else:
    lowestMarks = subject5;



# Calculating the Average Marks
#added int() to convert input to integer
avg = (subject1 + subject2 + subject3 + subject4 + subject5) / 5;

# Displaying the Results
print(f"Highest: {highestMarks}");
print(f"Lowest: {lowestMarks}");
print(f"Average: {avg}");