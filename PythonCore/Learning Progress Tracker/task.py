from data import Data
from menus import Menus, Run

# INIT
run_stage = Run.MAIN_MENU
data = Data()
new_students = 0

# RUN PROGRAM
print("Learning progress tracker")
while run_stage != Run.EXIT:

    if run_stage == Run.MAIN_MENU:
        run_stage = Menus.main_menu(data)

    if run_stage == Run.ADD_STUDENT_MENU:
        run_stage, new_students = Menus.add_student_menu(data, new_students)

    if run_stage == Run.ADD_POINTS_MENU:
        run_stage = Menus.add_points_menu(data)

    if run_stage == Run.FIND_STUDENT_MENU:
        run_stage = Menus.find_student_menu(data)

    if run_stage == Run.STATISTICS_MENU:
        run_stage = Menus.statistics_menu(data)
