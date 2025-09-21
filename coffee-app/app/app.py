import database
from tabulate import tabulate

MENU_PROMPT=""" -- Coffee Bean App --

Please choose one of these option:

1) Add a new bean.
2) See all beans.
3) Find a bean by name.
4) See which preparation method is best for a bean.
5) Exit.

Your selection: """


def menu():
    connection = database.connect()
    database.create_tables(connection)

    while(user_input := input(MENU_PROMPT))!="5":
        match user_input:
            case "1":
                name = input("Enter bean name:  ")
                method = input("Enter how you've prepared it:  ")
                while True:
                    try:
                        rating = int(input("Enter your rating score (0-100):  "))
                        break
                    except ValueError:
                        print("WARNING: Choose a valid rating")
                database.add_bean(connection,name,method,rating)

            case "2":
                listOfAllBeansNoId = [row[1:] for row in database.get_all_beans(connection)]
                print(tabulate(listOfAllBeansNoId,headers = ["NAME", "METHOD","RATING"],tablefmt="rst"))

            case "3":
                name = input("Enter bean name:")
                listOfAllBeansNoId = [row[1:] for row in database.get_beans_by_name(connection, name)]
                print(tabulate(listOfAllBeansNoId,headers = ["NAME", "METHOD","RATING"],tablefmt="rst"))

            case "4":
                name = input("Enter bean name to find the best preparation: ")
                listOfAllBeansNoId = [row[2:] for row in database.get_beans_by_name(connection, name)]
                print(f"For {name} coffee: ")
                print(tabulate(listOfAllBeansNoId,headers = [ "METHOD","RATING"],tablefmt="rst"))
            case _:
                print("\nWARNING: Choose a valid option\n")
    database.close_connection(connection)

if __name__ == "__main__":
    menu()