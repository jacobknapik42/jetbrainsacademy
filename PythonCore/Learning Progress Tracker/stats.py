from courses import Courses
from utils import Utils

class Stats:

    @staticmethod
    def _by_popularity(students):
        """ This helping function returns two lists. One consisting of all courses considered most popular
        and one considered least popular. The function will return empty lists, if no students where provided. """

        #TODO ensure no same course can be in both lists

        if not students:
            return [], []

        popularity = {course : 0 for course in Courses}

        all_points = [student.get_points() for student in students]
        for points in all_points:
            for course in Courses:
                if points[course.index] > 0:
                    popularity[course] += 1

        most_students = max(popularity.values())
        least_students = min(popularity.values())

        most_popular = [course.label for course, count in popularity.items() if count == most_students]
        least_popular = [course.label for course, count in popularity.items() if count == least_students]

        if most_popular == least_popular: return most_popular, []

        return most_popular, least_popular

    @staticmethod
    def _by_activity(students):
        """ This helping function returns two lists. One consisting of all courses considered having most active
        students and one of all courses considered having the least active students. The function will return empty lists,
        if no students where provided. """

        # TODO ensure no same course can be in both lists

        if not students:
            return [], []

        activity = {course : 0 for course in Courses}

        all_assignments = [student.get_assignments() for student in students]
        for assignment in all_assignments:
            for course in Courses:
                activity[course] += assignment[course.index]

        most_assignments = max(activity.values())
        least_assignments = min(activity.values())

        highest_activity = [course.label for course, count in activity.items() if count == most_assignments]
        lowest_activity = [course.label for course, count in activity.items() if count == least_assignments]

        if highest_activity == lowest_activity: return highest_activity, []

        return highest_activity, lowest_activity

    @staticmethod
    def _by_difficulty(students):
        """ This helping function returns two lists. One consisting of courses considered most difficult
        and consisting of courses considered least difficult. The function will return empty lists,
        if no students where provided. """

        # TODO ensure no same course can be in both lists

        if not students:
            return [], []

        total_points = {course : 0 for course in Courses}
        total_assignments = {course: 0 for course in Courses}

        for student in students:
            points = student.get_points()
            assignments = student.get_assignments()

            for course in Courses:
                total_points[course] += points[course.index]
                total_assignments[course] += assignments[course.index]

        averages = {course : 0.0 for course in Courses}

        for course in Courses:
            assignments = total_assignments[course]
            points = total_points[course]

            if assignments == 0:
                averages[course] = 0.0
            else:
                averages[course] = points / assignments

        highest_average = max(averages.values())
        lowest_average = min(averages.values())

        easiest = [course.label for course, avg in averages.items() if avg == highest_average]
        hardest = [course.label for course, avg in averages.items() if avg == lowest_average]

        if easiest == hardest: return [], []

        return easiest, hardest

    @staticmethod
    def courses_overview(data):
        """ This function returns a statistic overview for all courses available, by returning a list
        of all suitable courses for each statistic category. The function returns empty lists for
        categories, where statistical data was not retrievable due to missing information. """

        all_stud_ids = data.list_all()
        all_students = [data.find_student(stud_id) for stud_id in all_stud_ids]

        most_popular, least_popular = Stats._by_popularity(all_students)
        highest_activity, lowest_activity = Stats._by_activity(all_students)
        easiest, hardest = Stats._by_difficulty(all_students)

        return most_popular, least_popular, highest_activity, lowest_activity, easiest, hardest

    @staticmethod
    def print_courses_overview(data):
        """ This function uses the existing courses_overview to print the data in a readable format to console. """

        most_popular, least_popular, highest_activity, lowest_activity, easiest, hardest = Stats.courses_overview(data)

        most_popular_str = Utils.list_to_string(most_popular)
        least_popular_str = Utils.list_to_string(least_popular)
        highest_activity_str = Utils.list_to_string(highest_activity)
        lowest_activity_str = Utils.list_to_string(lowest_activity)
        easiest_str = Utils.list_to_string(easiest)
        hardest_str = Utils.list_to_string(hardest)

        print(f"""Most popular: {most_popular_str}
Least popular: {least_popular_str}
Highest activity: {highest_activity_str}
Lowest activity: {lowest_activity_str}
Easiest course: {easiest_str}
Hardest course: {hardest_str}""")

    @staticmethod
    def course_stats(data, course: Courses):
        """ This function returns raw statistical data for the selected course in form of a list of dictionaries.
        The function needs the data and a valid Enum Value from the Courses Class as input, otherwise errors may be risen.
        The result of this function is a list, of dictionaries for easy value access. The list will be empty if there is no data. """

        all_student_ids = data.list_all()
        if not all_student_ids:
            return []

        all_students = [data.find_student(stud_id) for stud_id in all_student_ids]
        course_students = [student for student in all_students if student.get_points()[course.index] > 0]

        course_students_stats = []
        for student in course_students:
            course_points = student.get_points()[course.index]
            course_completion_percentage = round(course_points / course.required_points * 100, 1)

            single_record = {"id" : student.get_id(), "points" : course_points, "completed" : course_completion_percentage}
            course_students_stats.append(single_record)

        return sorted(course_students_stats, key=lambda x: (-x['points'], x['id']))

    @staticmethod
    def print_course_stats(data, course: Courses):
        """ This function uses the existing course_stats to print the data in a readable format to console. """

        print(course.label)
        print(f"id\t\tpoints\tcompleted")

        stats = Stats.course_stats(data, course)

        if stats:
            for record in stats:
                print(f"{record['id']}\t{record['points']}\t\t{record['completed']}%")

    @staticmethod
    def python_stats(data):
        return Stats.course_stats(data, Courses.PYTHON)

    @staticmethod
    def print_python_stats(data):
        Stats.print_course_stats(data, Courses.PYTHON)

    @staticmethod
    def dsa_stats(data):
        return Stats.course_stats(data, Courses.DSA)

    @staticmethod
    def print_dsa_stats(data):
        Stats.print_course_stats(data, Courses.DSA)

    @staticmethod
    def databases_stats(data):
        return Stats.course_stats(data, Courses.DATABASES)

    @staticmethod
    def print_databases_stats(data):
        Stats.print_course_stats(data, Courses.DATABASES)

    @staticmethod
    def flask_stats(data):
        return Stats.course_stats(data, Courses.FLASK)

    @staticmethod
    def print_flask_stats(data):
        Stats.print_course_stats(data, Courses.FLASK)