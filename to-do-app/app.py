import database
from datetime import date
import datetime
from tabulate import tabulate
from colorama import Fore, Style

MENU_PROMPT=""" -- To Do App --

Please choose one of these option:

1) Add a new task.
2) See tasks for a specific day.
3) Check task.
4) Exit.

Your selection: """




def menu():
    connection = database.create_connection()

    database.create_table(connection)

    while (userOption := input(MENU_PROMPT))!="4":
        match userOption:
            case "1":
                task_name = input("Name: ")
                task_priority = input("Priority: ")
                task_date = toDate(input("Date(dd/mm/yyyy): "))
                database.add_job(connection, task_name,task_date, task_priority)
            case "2":
                user_date = toDate(input("Date(dd/mm/yyyy): "))
                listTasks = database.see_job_specific_day(connection, user_date)
                formatted = []
                for task in listTasks:
                    idFromTask, name, date, priority, done = task
                    if done=='S': 
                        name = f"\033[9m{name}\033[0m"  # <-- tachado
                    formatted.append((name, priority))
                print(tabulate(formatted,headers = [ "NAME", "PRIORITY"],tablefmt="rst"))
            case "3":
                task_name = input("Name: ")
                task_date = toDate(input("Date(dd/mm/yyyy): "))
                database.check_done(connection, task_name, task_date)
            case _:
                print("Invalid option")

        
    database.close_connection(connection)




def toDate(dateOfUser):
    while True:
        try:
            day,month,year = dateOfUser.split("/")
            dateOfUser = datetime.date(int(year),int(month),int(day))
            if dateOfUser < date.today():
                dateOfUser = input(f"{Fore.RED}WARNING:{Style.RESET_ALL} Please do not write a date in the past!!\n" \
                         "Date: ")
            else:
                return dateOfUser
        except (ValueError, IndexError):
            dateOfUser = input(f"{Fore.RED}WARNING:{Style.RESET_ALL} Please write the date as dd/mm/yyyy!!\n" \
                                "Date: ")



if __name__ == "__main__":
    menu()