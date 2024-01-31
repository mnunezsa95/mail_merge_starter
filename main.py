PLACEHOLDER = "[name]"

with open("Inputs/recipients.txt") as names_file:
    list_of_names = names_file.readlines()

with open("Inputs/starting_body.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in list_of_names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        with open(
            f"Outputs/ReadyToSend/letter_for_{stripped_name}.txt",
            mode="w",
        ) as completed_letter:
            completed_letter.write(new_letter)
