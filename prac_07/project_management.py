"""
start date - 9/11/2024
time estimate - 1 hour
"""
from prac_07.project import Project
import datetime
from operator import itemgetter

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


def main():
    projects = []
    print("Welcome to Pythonic Project Management")
    count = load_txt_file(projects)
    print(f"Loaded {count} projects from {FILE_NAME}\n{MENU}")
    choice = input(">>> ").lower()
    while choice != QUIT:
        if choice == LOAD:
            projects.clear()
            count = load_txt_file(projects)
            print(f"{MENU}")
            choice = input(">>> ").lower()

        elif choice == SAVE:
            yes_or_no = input("Would you like to save to projects.txt? ")
            if yes_or_no == "yes":
                out_file = save_project(projects)
                out_file.close()
            print(f"{MENU}")
            choice = input(">>> ").lower()

        elif choice == DISPLAY:
            complete_project, incomplete_project = group_complete_and_incomplete(projects)
            print("Incomplete projects:")
            display_the_projects(incomplete_project)
            print("Incomplete projects:")
            display_the_projects(complete_project)
            print(f"{MENU}")
            choice = input(">>> ").lower()

        elif choice == FILTER:
            date_string = input("Show project that start date (d/m/yyyy): ")  # e.g., "30/9/2022"
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            filtered_projects = [project for project in projects if project.start_date >= date]
            filtered_projects = sorted(filtered_projects, key=lambda x: x.start_date)
            for project in filtered_projects:
                print(project)
            print(f"{MENU}")
            choice = input(">>> ").lower()

        elif choice == ADD:
            print("Let's add new project")
            name = input("Name: ")
            date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            priority = int(input("Priority: "))
            cost = float(input("Cost estimate: $"))
            percentage = int(input("Percent complete: "))
            new_project = Project(name, date.strftime("%d/%m/%Y"), priority, cost, percentage)
            projects.append(new_project)
            print(f"{MENU}")
            choice = input(">>> ").lower()

        elif choice == UPDATE:
            display_the_projects(projects)
            project_choice = int(input("Project choice: "))
            print(projects[project_choice])
            new_percentage = input("New Percentage: ")
            if new_percentage != "":
                for project in projects:
                    if projects.index(project) == project_choice:
                        project.update_percentage(int(new_percentage))
                new_priority = input("New Priority: ")
                if new_priority != "":
                    for project in projects:
                        if projects.index(project) == project_choice:
                            project.update_priority(int(new_priority))

            print(f"{MENU}")
            choice = input(">>> ").lower()
    yes_or_no = input("Would you like to save to projects.txt? ")
    if yes_or_no == "yes":
        out_file = save_project(projects)
        out_file.close()
        print("Thank you for using custom-built project management software.")


def save_project(projects):
    out_file = open(FILE_NAME, "w")
    out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
    for project in projects:
        out_file.write(
            f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.percentage}\n")
    return out_file


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
    label = ZERO
    for work in works:
        label += ONE
        print(f"\t{label - ONE} {work}")


main()
