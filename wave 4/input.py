names = ['Sarah', 'Deji', 'Roli'] # get and process input for a list of names
assignments =  ['Mathematics', 'English', 'Science']# get and process input for a list of the number of assignments
grades = ['B','B', 'C'] # get and process input for a list of grades
highest = 'A'
loop = zip(names, assignments, grades)


message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"



for name, assignment,grade in loop:
    print(message.format(name, assignment, grade, highest))