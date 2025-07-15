from enum import Enum

from errors import InvalidFirstNameError, InvalidLastNameError, InvalidEmailError, EmailAlreadyInUseError, \
    InvalidInputFormatError
from student import Student
from utils import Utils
from stats import Stats


class Run(Enum):
    EXIT = 0
    MAIN_MENU = 1
    ADD_STUDENT_MENU = 2
    ADD_POINTS_MENU = 3
    FIND_STUDENT_MENU = 4
    STATISTICS_MENU = 5


class Menus:
    @staticmethod
    def main_menu(data):
        """ This function allows users to start interacting with the program, switch between
         several program menus or exit the application. """

        user_input = input()
        user_input = user_input.strip()

        if user_input == "exit":
            print("Bye!")
            return Run.EXIT

        elif user_input == "back":
            print("Enter 'exit' to exit the program.")

        elif user_input == "add students":
            print("Enter student credentials or 'back' to return:")
            return Run.ADD_STUDENT_MENU

        elif user_input == "list":
            print("Students:")
            students_ids = data.list_all()
            if not students_ids:
                print("No students found")
            else:
                for stud_id in students_ids:
                    print(stud_id)

        elif user_input == "add points":
            print("Enter an id and points or 'back' to return")
            return Run.ADD_POINTS_MENU

        elif user_input == "find":
            print("Enter an id or 'back' to return")
            return Run.FIND_STUDENT_MENU

        elif user_input == "statistics":
            print("Type the name of a course to see details or 'back' to quit:")
            Stats.print_courses_overview(data)
            return Run.STATISTICS_MENU

        elif user_input == "notify":
            Student.notify_students(data)
            return Run.MAIN_MENU

        elif user_input == "":
            print("No input.")

        else:
            print("Unknown command!")

        return Run.MAIN_MENU

    @staticmethod
    def add_student_menu(data, new_students):
        """ This function allows users to add new students to the internal data storage
        via CLI or return to main menu. """

        user_input = input().strip()

        if user_input.lower() == "back":
            print(f"Total of {new_students} students have been added.")
            new_students = 0
            return Run.MAIN_MENU, new_students

        else:
            try:
                first_name, last_name, email = Utils.parse_credentials(user_input)
                student = Student(first_name, last_name, email)
                data.add_student(student)
                new_students += 1
                print("The student has been added.")

            except InvalidFirstNameError:
                print("Incorrect first name.")
            except InvalidLastNameError:
                print("Incorrect last name.")
            except InvalidEmailError:
                print("Incorrect email.")
            except EmailAlreadyInUseError:
                print("This email is already taken.")
            except ValueError:
                print("Incorrect credentials")

        return Run.ADD_STUDENT_MENU, new_students

    @staticmethod
    def add_points_menu(data):
        """ This function allows users to update students' points via CLI. """

        user_input = input().strip().lower()
        if user_input == "back":
            return Run.MAIN_MENU
        else:
            user_and_points = user_input.strip().split()
            stud_id = user_and_points[0]
            points = user_and_points[1:]

            if not stud_id.isnumeric() or data.find_student(int(stud_id)) is None:
                print(f"No student is found for id={stud_id}")
            else:
                try:
                    student = data.find_student(int(stud_id))
                    python_pts, dsa_pts, databases_pts, flask_pts = Utils.parse_points(points)
                    student.update_course_points(python_pts, dsa_pts, databases_pts, flask_pts)
                    print("Points updated")
                except InvalidInputFormatError:
                    print("Incorrect points format")

        return Run.ADD_POINTS_MENU

    @staticmethod
    def find_student_menu(data):
        """ This function allows users to find students stored and display their points. """

        user_input = input().strip().lower()

        if user_input == "back":
            return Run.MAIN_MENU
        else:
            stud_id = user_input
            if not stud_id.isnumeric() or data.find_student(int(stud_id)) is None:
                print(f"No student is found for id={stud_id}")
            else:
                stud_id = int(stud_id)
                student = data.find_student(stud_id)
                python_pts, dsa_pts, databases_pts, flask_pts = student.get_points()
                print(
                    f"{stud_id} points: Python={python_pts}; DSA={dsa_pts}; Databases={databases_pts}; Flask={flask_pts}")

        return Run.FIND_STUDENT_MENU

    @staticmethod
    def statistics_menu(data):
        """ This funktion allows users to receive useful statistics about the offered
        courses via CLI. """

        user_input = input().strip().lower()

        if user_input == "back":
            return Run.MAIN_MENU
        if user_input == "python":
            Stats.print_python_stats(data)
            return Run.STATISTICS_MENU
        if user_input == "dsa":
            Stats.print_dsa_stats(data)
            return Run.STATISTICS_MENU
        if user_input == "databases":
            Stats.print_databases_stats(data)
            return Run.STATISTICS_MENU
        if user_input == "flask":
            Stats.print_flask_stats(data)
            return Run.STATISTICS_MENU
        else:
            print("Unknown course.")
            return Run.STATISTICS_MENU