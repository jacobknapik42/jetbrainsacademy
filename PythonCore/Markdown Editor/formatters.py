class Formatters:
    BOLD_SYNTAX = "**"
    ITALIC_SYNTAX = '*'
    INLINE_CODE_SYNTAX = '`'
    HEADER_SYNTAX = '#'

    @staticmethod
    def plain():
        """ This method asks the user for text input via CLI and formats the given input as plain
        in valid Markdown syntax. """

        text = input("Text: ")
        return text

    @staticmethod
    def bold():
        """ This method asks the user for text input via CLI and formats the given input as bold
        in valid Markdown syntax. """

        text = input("Text: ")
        return f"{Formatters.BOLD_SYNTAX}{text}{Formatters.BOLD_SYNTAX}"

    @staticmethod
    def italic():
        """ This method asks the user for text input via CLI and formats the given input as italic
        in valid Markdown syntax. """

        text = input("Text: ")
        return f"{Formatters.ITALIC_SYNTAX}{text}{Formatters.ITALIC_SYNTAX}"

    @staticmethod
    def header():
        """ This method asks the user for text and desired header level via CLI and formats the given
        input as a header in valid Markdown syntax. """

        level = input('Level: ').strip()
        while not level.isdigit() or not 1 <= int(level) <= 6:
            print("The level should be within the range of 1 to 6")
            level = input('Level: ').strip()
        else:
            level = int(level)

        text = input('Text: ')
        return f"{Formatters.HEADER_SYNTAX * level} {text}\n"

    @staticmethod
    def link():
        """ This method asks the user for a label and a link via CLI and formats the given
        input as a link in valid Markdown syntax. """

        label = input("Label: ")
        url = input("URL: ")

        return f"[{label}]({url})"

    @staticmethod
    def inline_code():
        """ This method asks the user for text input via CLI and formats the given input as inline-code
        in valid Markdown syntax. """

        text = input("Text: ")
        return f"{Formatters.INLINE_CODE_SYNTAX}{text}{Formatters.INLINE_CODE_SYNTAX}"

    @staticmethod
    def new_line():
        """ This method creates a line break in valid Markdown syntax and takes no input from user.  """

        return "  \n"

    @staticmethod
    def ordered_list():
        """ This method makes uses the create_list method to return an ordered list in valid Markdown syntax. """

        return Formatters._create_list(True)

    @staticmethod
    def unordered_list():
        """ This method makes uses the create_list method to return an unordered list in valid Markdown syntax. """

        return Formatters._create_list(False)

    @staticmethod
    def _create_list(ordered: bool):
        """ This helping method takes the desired number of rows and a text per row as input and creates a list.
        The method takes `ordered` as parameter to determine, whether the created list should be ordered or unordered. """

        no_of_rows = input("Number of rows: ").strip()
        while not no_of_rows.isdigit() or int(no_of_rows) <= 0:
            print("The number of rows should be greater than zero")
            no_of_rows = input("Number of rows: ").strip()
        else:
            no_of_rows = int(no_of_rows)

        rows = []
        for row in range(1, no_of_rows + 1):
            text = input(f"Row #{row}: ")

            if ordered:
                listing = f"{row}. " + text
            else:
                listing = "* " + text

            rows.append(listing)

        resulting_list = f'{Formatters.new_line()}'.join(rows) + Formatters.new_line()
        return resulting_list
