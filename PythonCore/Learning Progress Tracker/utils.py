import re


from errors import InvalidFirstNameError, InvalidLastNameError, InvalidEmailError, InvalidInputFormatError


class Utils:
    @staticmethod
    def parse_credentials(input_string: str):
        """ This function accepts credentials in a certain format (firstname lastname email)
        and splits the input into single data accordingly. """

        credentials = input_string.strip().split()

        if len(credentials) < 3:
            raise ValueError

        if len(credentials) == 3:
            first_name = credentials[0]
            last_name = credentials[1]
            email = credentials[2]
        else:
            first_name = credentials[0]
            last_name = credentials[1]
            email = credentials[-1]

            for x in range(2, len(credentials) - 1):
                last_name += f" {credentials[x]}"

        return first_name, last_name, email

    @staticmethod
    def validate_student_data(first_name, last_name, email,
                              first_name_pattern, last_name_pattern, email_pattern):
        """ This function accepts student data and validates the input, whether it matches
        certain criteria, by matching it to provided regex patterns. This function
        raises proper errors upon pattern mismatches. """

        first_name_valid = re.fullmatch(first_name_pattern, first_name) is not None
        last_name_valid = re.fullmatch(last_name_pattern, last_name) is not None
        email_valid = re.fullmatch(email_pattern, email) is not None

        if not first_name_valid:
            raise InvalidFirstNameError
        if not last_name_valid:
            raise InvalidLastNameError
        if not email_valid:
            raise InvalidEmailError

    @staticmethod
    def parse_points(points):
        """ This function accepts a list of points in raw-input form and validates, whether
        they meet the expected criteria. This function raises an InvalidInputFormatError
        if the criteria is not met. """

        if len(points) != 4:
            raise InvalidInputFormatError

        try:
            python_pts, dsa_pts, databases_pts, flask_pts = map(int, points)
            if any(x < 0 for x in [python_pts, dsa_pts, databases_pts, flask_pts]):
                raise InvalidInputFormatError
        except ValueError:
            raise InvalidInputFormatError

        return python_pts, dsa_pts, databases_pts, flask_pts

    @staticmethod
    def list_to_string(list_of_strings, seperator : str = ", ", with_and : bool = False) -> str:
        """ This function formats a given list of courses into a single print friendly string.
        The function allows custom separators and an optional format, where 'and' is placed between the
        last and second to last value. The with_and-format is off and the separator is ', ' by default.
        If the provided list is empty, the resulting string will be 'n/a'. """

        if not list_of_strings:
            return "n/a"

        if with_and and len(list_of_strings) > 1:
            return f"{seperator.join(list_of_strings[:-1])} and {list_of_strings[-1]}"

        return seperator.join(list_of_strings)

    @staticmethod
    def send_completion_notification(email, first_name, last_name, course_name):
        """ This method imitates sending an email by printing a message to the console. """

        print(f"""To: {email}
Re: Your Learning Progress
Hello, {first_name} {last_name}! You have accomplished our {course_name} course!""")