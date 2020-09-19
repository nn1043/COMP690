global intern_list
intern_list = {}

def user_interface():
    menu_list = {
        "MENU": print_menu, "PREP": prep_csv, "TEST": test_prepped_CSV
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


def prep_csv(filename):
    print("Prepping test CSV...")
    last_name = ""
    first_name = ""
    student_id = ""
    survey = open(filename, "r", encoding = "ISO-8859-1")
    for line in survey.readlines():
        survey_readable = line.split(",")
        for value in survey_readable:
            if survey_readable.index(value) == 0:
                last_name = value
            elif survey_readable.index(value) == 1:
                first_name = value
            elif survey_readable.index(value) == 2: # use student ID for unique
                student_id = value
                intern_list[student_id] = [last_name, first_name]
            elif value == "":
                if (check_last == True) & (len(intern_list[student_id]) >= 24):
                    break
                    #intern_list[student_id].pop() # <- find way to remove last
                else:
                    value = "N/A"
                    intern_list[student_id].append(value)
                    check_last = True
            else:
                intern_list[student_id].append(value)
                check_last = False
    survey.close()
    print("Test CSV loaded.")

# for new csv test initial dict against 'standard' write function for
# acceptable difference in spelling, or create new column. Maybe check for
# 'if unique, compare char, then add new column'


def test_prepped_CSV():
    print(intern_list["913035402"])


prep_csv("BS-Analytics.csv")
user_interface()
