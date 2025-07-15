from errors import EmailAlreadyInUseError


class Data:

    def __init__(self):
        self.all_students_dict = {}
        self.all_student_emails = set()

    def add_student(self, student):
        """ This method adds provided student or raises an EmailAlreadyInUseError
        if a student with the same email already exists. """

        if student.get_email() in self.all_student_emails:
            raise EmailAlreadyInUseError

        self.all_students_dict[student.get_id()] = student
        self.all_student_emails.add(student.get_email())

    def find_student(self, stud_id):
        """ Returns the student with the corresponding student id or None
         if no student with the provided student id was found. """

        try:
            return self.all_students_dict[stud_id]
        except KeyError:
            return None

    def find_student_by_mail(self, email):
        """ Returns the student with the corresponding email address or None
        if no suiting student was found. """

        for student in self.all_students_dict.values():
            if student.get_email() == email: return student

        return None

    def list_all(self):
        """ Returns a list of student ids of all students stored. The
         resulted list will be empty, when no students exist."""

        result = []
        for student in self.all_students_dict.values():
            result.append(student.get_id())

        return result
