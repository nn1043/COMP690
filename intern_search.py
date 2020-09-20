global intern_list
intern_list = {}
intern_list["ID Number"] = [
    "Last Name", "First Name", "ID Number", "Major", "Phone Number", "Email",
    "Student LinkedIn URL", "Course Number", "Worked Hours (Logged) ",
    "Total Credits", "Internship Semester ", "Internship Start Date",
    "Internship End Date", "Faculty Advisor ","Internship Site",
    "Mailing Address", "City", "State", '"City, State Zip"',
    "Internship Position Title", "Site Mentor", "Mentor Position",
    "Mentor Email", "Mentor Phone ", " Hourly Pay"
    ]


def user_interface():
    menu_list = {
        "MENU": print_menu, "PREP": prep_csv, "TEST": test_prepped_CSV,
        "SEARCH": search_id
        }
    print("Please choose an operation:")
    print("MENU")
    run_program = True
    while run_program is True:
        user_response = input("Input: ")
        if user_response.upper() in menu_list:
            if type(menu_list[user_response.upper()]) is list:
                for to_do in menu_list[user_response.upper()]:
                    to_do()
            else:
                menu_list[user_response.upper()]()
        elif user_response.upper() in ["EXIT", "QUIT"]:
            print("Goodbye.")
            run_program = False
        else:
            print("Not a valid command.")


def print_menu():
    print("Prep Test CSV: PREP")
    print("Test Prepped CSV: TEST")
    print("Search by Student ID: SEARCH")
    print("Quit Program: QUIT, EXIT")


def prep_csv(filename):
    print("Prepping test CSV...")
    last_name = ""
    first_name = ""
    student_id = ""
    flag_entry = False
    survey = open(filename, "r", encoding = "ISO-8859-1")
    for line in survey.readlines():
        survey_readable = line.split(",")
        for value in survey_readable:
            if survey_readable.index(value) == 0:
                last_name = value
            elif survey_readable.index(value) == 1:
                first_name = value
            elif survey_readable.index(value) == 2: # use student ID for unique
                for char in value:
                    if char.isnumeric() == False:
                        #check_new_sheet(value)
                        flag_entry = True
                student_id = value
                intern_list[student_id] = [last_name, first_name]
            elif value == "":
                if (check_last == True) & (len(intern_list[student_id]) >= 24):
                    break
                    #intern_list[student_id].pop()   <- find way to remove last
                else:
                    value = "N/A"
                    intern_list[student_id].append(value)
                    check_last = True
            else:
                intern_list[student_id].append(value)
                check_last = False
        if flag_entry = True:
            if check_new_sheet(intern_list[student_id]): # returns True, then..
                print("whomp whomp") # what now? continue scraping?
            else:
                print("Error in loading CSV. Please check formatting.")
                # assume error-catching fails, throw response to user
    survey.close()
    print("Test CSV loaded.")


"""
Create a de-facto 'correct' initial column. When index == 2 and char !=
numeric, pull 'correct' columns and compare. Set acceptable typo level, if
fails, either kill program (that script) or create new column, possibly give
user option.
"""

# This requires the full key/value pair. How do I grab the full key/value
# without rewriting the entire script? <- I think I got it.
def check_new_sheet(testing):
    for item in intern_list["ID Number"]
        if item in testing: # if default string is found in new dict, pass
            pass # next need to potentially reindex columns. How?
        else:
            return False: # for right now just break
    return True # every column matches. Will not work with typos at the moment


def test_prepped_CSV():
    print(intern_list["913035402"])


def search_id():
    searching_for = input("Enter Student ID: ")
    if searching_for in intern_list:
        print(intern_list[searching_for])
    else:
        print("Invalid Student ID.")

prep_csv("BS-Analytics.csv")
user_interface()
