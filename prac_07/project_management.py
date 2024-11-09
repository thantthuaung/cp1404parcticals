"""
start date - 9/11/2024
time estimate - 1 hour
"""
from prac_07.project import Project
import datetime

FILE_NAME = "projects.txt"
MENU = """- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"""
LOAD = "l"
SAVE = "s"
DISPLAY = "d"
FILTER = "f"
ADD = "a"
UPDATE = "u"
QUIT = "q"
ZERO = 0
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
HUNDRED = 100


# date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
# date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
# print(f"That day is/was {date.strftime('%A')}")
# print(date.strftime("%d/%m/%Y"))

def main():
    projects = []
    print("Welcome to Pythonic Project Management")
    count = load_txt_file(projects)
    print(f"Loaded {count} projects from {FILE_NAME}\n{MENU}")
    choice = input(">>> ").lower()
    while choice != QUIT:
        if choice == LOAD:
            pass

        elif choice == SAVE:
            pass

        elif choice == DISPLAY:
            complete_project, incomplete_project = group_complete_and_incomplete(projects)
            print("Incomplete projects:")
            display_the_projects(incomplete_project)
            print("Incomplete projects:")
            display_the_projects(complete_project)
            print(f"{MENU}")
            choice = input(">>> ").lower()

        elif choice == FILTER:
            pass

        elif choice == ADD:
            pass

        elif choice == UPDATE:
            pass


def group_complete_and_incomplete(projects):
    complete_project = []
    incomplete_project = []
    for project in projects:
        if project.percentage == HUNDRED:
            complete_project.append(project)
            complete_project.sort()
        else:
            incomplete_project.append(project)
            incomplete_project.sort()
    return complete_project, incomplete_project


def load_txt_file(projects):
    in_file = open(FILE_NAME, "r")
    in_file.readline()
    count = ZERO
    for line in in_file:
        count += ONE
        parts = line.strip().split("\t")
        project = Project(parts[ZERO], parts[ONE], int(parts[TWO]), float(parts[THREE]), int(parts[FOUR]))
        projects.append(project)
    in_file.close()
    return count


def display_the_projects(works):
    for work in works:
        print(f"\t{work}")


main()
