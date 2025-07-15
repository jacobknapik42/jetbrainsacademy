from utils import Utils
from courses import Courses


class Student:
    _first_name_pattern = r"^[A-Za-z](((['-][A-Za-z])|[A-Za-z]+)+)$"
    _last_name_pattern = r"^([A-Za-z](((['-][A-Za-z])|[A-Za-z]+)+))( [A-Za-z](((['-][A-Za-z])|[A-Za-z]+)+))*$"
    _email_pattern = r"^[a-z0-9](\.?[a-z0-9_-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*\.[a-z0-9]+$"
    _next_stud_id = 10000
    _stud_id_pattern = r"^[0-9]+$"

    def __init__(self, first_name, last_name, email):
        first_name = first_name.strip()
        last_name = last_name.strip()
        email = email.strip().lower()

        Utils.validate_student_data(first_name, last_name, email,
                                    self._first_name_pattern, self._last_name_pattern, self._email_pattern)

        self._stud_id = Student._next_stud_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._course_points = {Courses.PYTHON: 0, Courses.DSA: 0, Courses.DATABASES: 0, Courses.FLASK: 0}
        self._course_assignments = {Courses.PYTHON: 0, Courses.DSA: 0, Courses.DATABASES: 0, Courses.FLASK: 0}
        self._completed_courses = []
        self._certificates_sent = []

        Student._next_stud_id += 1

    def __hash__(self):
        return hash(self._stud_id)

    def __eq__(self, other):
        if other is self: return True
        if other is None or not isinstance(other, Student): return False
        return self._stud_id == other._stud_id

    def get_id(self):
        """ This method returns the unique student ID of self. """

        return self._stud_id

    def get_email(self):
        """ This method returns the email address of self. """

        return self._email

    def update_course_points(self, python_pts, dsa_pts, databases_pts, flask_pts):
        """ This method updates the points stored for all available courses for self. """

        self._course_points[Courses.PYTHON] += python_pts
        if self._course_points[Courses.PYTHON] >= Courses.PYTHON.required_points:
            self._completed_courses.append(Courses.PYTHON)
        self._course_points[Courses.DSA] += dsa_pts
        if self._course_points[Courses.DSA] >= Courses.DSA.required_points:
            self._completed_courses.append(Courses.DSA)
        self._course_points[Courses.DATABASES] += databases_pts
        if self._course_points[Courses.DATABASES] >= Courses.DATABASES.required_points:
            self._completed_courses.append(Courses.DATABASES)
        self._course_points[Courses.FLASK] += flask_pts
        if self._course_points[Courses.FLASK] >= Courses.FLASK.required_points:
            self._completed_courses.append(Courses.FLASK)

        self._course_assignments[Courses.PYTHON] += 1 if python_pts > 0 else 0
        self._course_assignments[Courses.DSA] += 1 if dsa_pts > 0 else 0
        self._course_assignments[Courses.DATABASES] += 1 if databases_pts > 0 else 0
        self._course_assignments[Courses.FLASK] += 1 if flask_pts > 0 else 0

    def get_points(self):
        """ This method returns the points stored for all available courses for self. """

        # TODO consider improving this method to ensure indexes for output according to Courses class.
        return self._course_points[Courses.PYTHON], self._course_points[Courses.DSA], self._course_points[Courses.DATABASES], self._course_points[Courses.FLASK]

    def get_assignments(self):
        """ This method returns the number of assignments published per course for all available courses for self. """

        # TODO consider improving this method to ensure indexes for output according to Courses class.
        return self._course_assignments[Courses.PYTHON], self._course_assignments[Courses.DSA], self._course_assignments[Courses.DATABASES], self._course_assignments[Courses.FLASK]

    def notify(self):
        """ This method notifies the student about completed courses by imitating an email by printing a message
         to the console. """

        if self._completed_courses == self._certificates_sent:
            return False

        for course in self._completed_courses:
            if course not in self._certificates_sent:
                self._certificates_sent.append(course)
                Utils.send_completion_notification(self._email, self._first_name, self._last_name, course.label)

        return True

    @staticmethod
    def notify_students(data):
        """ This method notifies all students who have completed courses and have not yet been notified. """

        students_notified = 0

        students = [data.find_student(stud_id) for stud_id in data.list_all()]
        for student in students:
            if student.notify():
                students_notified += 1

        print(f"Total {students_notified} students have been notified.")