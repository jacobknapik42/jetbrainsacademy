from formatters import Formatters


class Utils:
    FORMATTERS_DICT = {'plain': Formatters.plain,
                       'bold': Formatters.bold,
                       'italic': Formatters.italic,
                       'header': Formatters.header,
                       'link': Formatters.link,
                       'inline-code': Formatters.inline_code,
                       'new-line': Formatters.new_line,
                       'ordered-list': Formatters.ordered_list,
                       'unordered-list': Formatters.unordered_list}

    @staticmethod
    def help_prompt():
        """ This method prints all available commands to the console. """

        list_formatters = ' '.join(Utils.FORMATTERS_DICT.keys())
        print(f"""Available formatters: {list_formatters}\nSpecial commands: !help !done""")

    @staticmethod
    def write_line(user_input, cache):
        """ This method asks the user via CLI type in a command. If the user chooses a formatter the
          user is asked to type the desired text, which is saved for later output. """

        cache += Utils.FORMATTERS_DICT[user_input]()
        print(cache)
        return cache

    @staticmethod
    def save_file(cache):
        """ This method saves the provided string to a file. It overwrites an existing
        'output.md' file or creates a new one. """

        with open('output.md', 'w') as output_file:
            output_file.write(cache)

        print("Your text has been saved to 'output.md'.")
