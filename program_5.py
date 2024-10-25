#Programmer: Mai Lillie
# Date: 10/25/24
# Program: Course Info

# Establishing Variables
course_dictionary = {}
course_list = []
user_input = "Yes"
output_list = []

# Getting the users input
while user_input != "No":
    course_id = input("What's the course ID?: ")
    course_title = input("What's the course title?: ")
    course_list.append(course_id)
    course_dictionary[course_id] = course_title
    user_input = input("Would you like to add another course?: ")

# The function that searches through the dictionary
def search_method(subject_input, main_list):
    new_list = []
    for x in range(0, len(main_list)):
        course = main_list[x]
        if subject_input in course:
            new_list.append(course_dictionary[course])
    return new_list

# Running the main program
subject = input("What subject would you like to search for?: ")
output_list = search_method(subject, course_list)
print(f"These are the subjects that match: {output_list}")
