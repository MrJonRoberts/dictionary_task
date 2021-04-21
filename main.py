# 07 Dictionary Extension
# Mr Roberts
'''

Using the code at MrJonRoberts/dictionary_task (github.com)
Complete the code following the comments to make it work.

'''

# Python code for a Grade Calculator

# Creating a dictionary which consists of the student name,
# assignment result test results and their respective lab results

# 1. Jack's dictionary
jack = {"name": "Jack Frost",
        "assignment": [80, 50, 40, 20],
        "test": [75, 75],
        "class": [78.20, 77.20]
        }

# 2. James's dictionary
james = {"name": "James Potter",
         "assignment": [82, 56, 44, 30],
         "test": [80, 80],
         "class": [67.90, 78.72]
         }

# 3. Dylan's dictionary
dylan = {"name": "Dylan Rhodes",
         "assignment": [77, 82, 23, 39],
         "test": [78, 77],
         "class": [80, 80]
         }

# 4. Jessica's dictionary
jess = {"name": "Jessica Stone",
        "assignment": [67, 55, 77, 21],
        "test": [40, 50],
        "class": [69, 44.56]
        }

# 5. Tom's dictionary
tom = {"name": "Tom Hanks",
       "assignment": [29, 89, 60, 56],
       "test": [65, 56],
       "class": [50, 40.6]
       }


# Function calculates average
def getAverage(marks):
    avg = 0
    return avg


# Function calculates total average
def calculateTotalAverage(students):
    assignment = getAverage(students["assignment"])
    test = getAverage(students["test"])
    lab = getAverage(students["class"])

    # Return the result based
    # on weightage supplied
    # 10 % from assignments
    # 70 % from test
    # 20 % from lab-works


    weightedMark = 0
    return weightedMark


# Calculate letter grade of each student
def assignLetterGrade(score):
    return "E"


# Function to calculate the total
# average marks of the whole class
def classAverage(studentList):
    average = 0
    return average

# Student list consisting the
# dictionary of all students
students = [jack, james, dylan, jess, tom]

# Iterate through the students list
# and calculate their respective
# average marks and letter grade
for i in students:
    print(i["name"])
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    print(f"Average marks of {i['name']} is : {calculateTotalAverage(i)}")

    print(f"Letter Grade of {i['name']} is : {assignLetterGrade(calculateTotalAverage(i))}")

    print()

    # Calculate the average of whole class
    classAvg = classAverage(students)

    print("Class Average is %s" % (classAvg))
    print("Letter Grade of the class is %s "
          % (assignLetterGrade(classAvg)))
