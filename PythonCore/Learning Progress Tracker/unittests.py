"""import unittest
from utils import Utils
from data import Data
from student import Student
from errors import InvalidFirstNameError, InvalidLastNameError, InvalidEmailError, EmailAlreadyInUseError


class TestStudent(unittest.TestCase):
    pass


class TestMenus(unittest.TestCase):
    def test_main_menu(self):
        pass

    def test_add_student_menu(self):
        pass


class TestUtils(unittest.TestCase):
    def test_parse_credentials(self):
        pos_test_cases = [
            ("john wick john.wick@example.com", "john", "wick", "john.wick@example.com"),
            ("n' _mmoench moench@example.com", "n'", "_mmoench", "moench@example.com"),
            ("Hannah-Lisa o'neil-Bruckner Hager h.l.on.bruckner@example.com", "Hannah-Lisa", "o'neil-Bruckner Hager",
             "h.l.on.bruckner@example.com"),
            ("1Monika kernbauer-Ascher ascher@ascher.at", "1Monika", "kernbauer-Ascher", "ascher@ascher.at"),
            ("Paula-Vicky Kern-Gruber Hausbauer-Aschenwäger Smith Mc'Donalds paula-vicky.kghasm@mail.com",
             "Paula-Vicky", "Kern-Gruber Hausbauer-Aschenwäger Smith Mc'Donalds", "paula-vicky.kghasm@mail.com"),
            ("Mark Tauchlieb tauchlieb.m@example.com", "Mark", "Tauchlieb", "tauchlieb.m@example.com"),
            ("  Susi    Klein-Waeger               waeger.s@example.com     ", "Susi", "Klein-Waeger",
             "waeger.s@example.com")
        ]

        neg_test_cases = [
            "Monika_Hausbauer hausbauer@mail.at",
            "Dominik Streusl:streusl@example.com",
            "annika annika@mail.de",
            "anna_kernreiter_kernreiter@mail.de"
        ]

        for credentials, expected_first_name, expected_last_name, expected_email in pos_test_cases:
            with self.subTest():
                result_first_name, result_last_name, result_email = Utils.parse_credentials(credentials)

                self.assertEqual(result_first_name, expected_first_name,
                                 f"Test failed! Expected first_name = '{expected_first_name}', but got '{result_first_name}'.")
                self.assertEqual(result_last_name, expected_last_name,
                                 f"Test failed! Expected last_name = '{expected_last_name}', but got '{result_last_name}'.")
                self.assertEqual(result_email, expected_email,
                                 f"Test failed! Expected email = '{expected_email}', but got '{result_email}'.")

        for credentials in neg_test_cases:
            with self.subTest(invalid_input=credentials):
                self.assertRaises(ValueError, Utils.parse_credentials, credentials)

    def test_validate_input(self):
        _first_name_pattern = r"^[A-Za-z](((['-][A-Za-z])|[A-Za-z]+)+)$"
        _last_name_pattern = r"^([A-Za-z](((['-][A-Za-z])|[A-Za-z]+)+))( [A-Za-z](((['-][A-Za-z])|[A-Za-z]+)+))*$"
        _email_pattern = r"^[a-z0-9](\.?[a-z0-9_-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*\.[a-z0-9]+$"

        pos_test_cases = [
            ("susi", "kleingeb", "kleingeb@mail.com"),
            ("n'am", "w'w", "w.nam@example.com"),
            ("wi", "Wieser", "wieser@mail.1"),
            ("saraH", "wi-n'aa", "wi-naa@123.123"),
            ("paul-yor'i", "o'neill-shaker", "shaker@shake.0")
        ]

        neg_test_cases = [
            ("_susi", "kleingeb", "kleingeb@mail.com", InvalidFirstNameError),
            ("maxi..", "gauner", "gauner@mail.com", InvalidFirstNameError),
            ("Tom", "'Shaka", "shaka@mail.at", InvalidLastNameError),
            ("ulrikke", "dauner_groß", "daunergroß@example.com", InvalidLastNameError),
            ("1Monika", "Gerber", "1moni1@mailcow.com", InvalidFirstNameError),
            ("Moniiiii", "12er", "12er@0010110.0110", InvalidLastNameError),
            ("KlaudiaAA", "Wissbacher-oller", "__wiesbach@mail.de", InvalidEmailError),
            ("Franzi", "Kaiser", "franzi@kaiser@habsburg.at", InvalidEmailError)
        ]

        for first_name, last_name, email in pos_test_cases:
            with self.subTest():
                try:
                    Utils.validate_student_data(first_name, last_name, email,
                                                _first_name_pattern, _last_name_pattern, _email_pattern)

                except Exception as e:
                    self.fail(f"Raised an unexpected exception for valid input: '{first_name}, {last_name}, {email}'")

        for first_name, last_name, email, expected_error in neg_test_cases:
            self.assertRaises(expected_error, Utils.validate_student_data, first_name, last_name, email,
                              _first_name_pattern, _last_name_pattern, _email_pattern)


class TestData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_data = Data()
        cls.test_students = [
            ("Anna", "Streb", "a.streb@example.com"),
            ("Max", "Traub-Proell", "maxi.t-p@mail.de"),
            ("Tom", "Mc'Thirsty", "tom-thirsty@example.at"),
            ("Bertha", "von Suttner", "bvs@example.com"),
            ("Vicky", "Gross-Allwang", "v.gross-allwand@postfach.de"),
            ("Paula", "Tietz", "paula02@mailwelt.at"),
            ("Louis", "Anger", "l_anger_42@itmail.de"),
            ("Edvin", "Reiter", "edvnrtr@incognitomail.com"),
            ("Olly", "Mars", "ollyisaplanet@mailuniverse.com"),
            ("Rob", "David", "rob.d_v_d@oldie.com")
        ]

        cls.known_ids = []
        for first, last, email in cls.test_students:
            student = Student(first, last, email)
            cls.known_ids.append(student.get_id)
            cls.test_data.add_student(student)

    def test_find_student(self):
        # Positives
        for test_id in self.known_ids:
            with self.subTest(test_id=test_id):
                student = self.test_data.find_student(test_id)
                self.assertIsNotNone(student)
                self.assertTrue(student.get_id == test_id)

        # Negatives
        unknown_ids = [9999, 8888, 7777, 123456]
        for test_id in unknown_ids:
            with self.subTest(test_id=test_id):
                self.assertIsNone(self.test_data.find_student(test_id))

    def test_find_student_by_mail(self):
        # Positives
        for student in self.test_data.all_students_dict.values():
            print(f"Type of student: {type(student)}")

            key_email = student.get_email()

            with self.subTest(key_email):
                student = self.test_data.find_student_by_mail(key_email)
                self.assertIsNotNone(student)
                self.assertTrue(student.get_email() == key_email)

        # Negatives
        unknown_emails = [
            "mayhem@chaosmail.com",
            "deleted@world.com",
            "magician@circusmail.com",
            "anke.engelke@lol.de",
            "angela_merkel@deutsch.de",
            "",
            "12345",
            "Ö#´ü\n BBHMM"
        ]

        for email in unknown_emails:
            with self.subTest(email):
                self.assertIsNone(self.test_data.find_student_by_mail(email))

    def test_add_student(self):
        # Positives
        pos_test_cases = [
            Student("Mirabell", "Perg", "mirabell@sbg-land.at"),
            Student("Larissa", "Bogota", "lara.colombian@example.com"),
            Student("Lucas", "Hansson", "l.hansson@swedemail.se"),
            Student("Ben", "von Leuthen", "b.v.leuthen@royalmail.net")
        ]

        for student in pos_test_cases:
            with self.subTest():
                try:
                    self.test_data.add_student(student)
                except Exception as e:
                    self.fail("Raised an unexpected exception for valid input.")

        # Negatives

        neg_test_cases = [
            (Student("Angie", "Streb", "a.streb@example.com"), EmailAlreadyInUseError),
            (Student("Paula", "Tietz", "paula02@mailwelt.at"), EmailAlreadyInUseError),
            (Student("Bertha", "von Suttner", "bvs@example.com"), EmailAlreadyInUseError)
        ]

        for student, expected_error in neg_test_cases:
            with self.subTest():
                self.assertRaises(expected_error, self.test_data.add_student, student)


if __name__ == '__main__':
    unittest.main()"""
