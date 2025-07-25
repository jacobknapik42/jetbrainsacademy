from utils import Utils

cache = ""

# MAIN PROGRAM LOGIC
running = True
while running:
    user_input = input("Choose a formatter: ").strip().lower()

    if user_input == "!done":
        Utils.save_file(cache)
        running = False

    elif user_input == "!help":
        Utils.help_prompt()

    elif user_input in Utils.FORMATTERS_DICT:
        cache = Utils.write_line(user_input, cache)

    else:
        print("Unknown formatting type or command. Type '!help' to view available commands.")
