import os
from google.cloud import bigquery

global query
query = ""

def user_interface():
    menu_list = {
        "MENU": print_menu, "PERM": load_permission, "QUERY": run_query,
        "TEST": experimental_query
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
    print("Load permission file: PERM")
    print("Run test query: QUERY")
    print("Run experimental query: TEST")
    print("Exit program: EXIT or QUIT")


def load_permission():
    to_open = input("Which permission file would you like to load: ")
    to_open = to_open + ".txt"
    file = open(to_open, "r")
    global query
    query  = file.read()
    print(query)


def run_query():
    client = bigquery.Client()
    print(query)
    if query == "":
        print("You do not have permission to do this.")
    else:
        # Let user update query here in-line with permissions?
        query_job = client.query(query)
        # User interactivity would begin below this line, if interacting with
        # already retrieved data.
        print("Students")
        for row in query_job:
            print("{}, {}".format(row[0], row[1]))


def experimental_query():
    have_permission = True
    client = bigquery.Client()
    print(query)
    if query == "":
        print("You do not have permission to do this.")
    else:
        user_input = input("Query: ")
        split = user_input.split()
        for i in split:
            if i in query:
                pass
            elif i == "FROM":
                break
            else:
                print("You do not have permission to do this.")
                have_permission = False
                break
        if have_permission == True:
            query_job = client.query(user_input)
            print("Students")
            for row in query_job:
                print("{}, {}".format(row[0], row[1]))
# Passes
# SELECT Last_Name, First_Name FROM `comp690.SampleData.masterlist_table` LIMIT 1000

# Fails
# SELECT Last_Name, First_Name, anything FROM `comp690.SampleData.masterlist_table` LIMIT 1000

# Note: There is no error checking for this function.


user_interface()
