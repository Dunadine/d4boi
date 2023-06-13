import pyfiglet
import os
from class_data import class_options, aspect_names


def get_user_class():
    try:
        with open('user_class.txt', 'r') as file:
            class_choice = file.read().strip()
            if class_choice.isdigit() and int(class_choice) in class_options:
                return class_options[int(class_choice)]
    except FileNotFoundError:
        pass

    return None


def print_aspect_table(aspect_details):
    print("Aspect Table:")
    print("No.  Aspect Name                Dynamic Value 1           Dynamic Value 2")
    print("------------------------------------------------------------------------")
    for index, aspect_detail in enumerate(aspect_details, start=1):
        aspect_name, dynamic_value_1, dynamic_value_2 = aspect_detail
        print(f"{index:<4} {aspect_name.ljust(28)}{dynamic_value_1.ljust(28)}{dynamic_value_2}")


def search_aspect(aspect_details):
    search_term = input("Enter the aspect name to search for: ").lower()
    matching_entries = [entry for entry in aspect_details if search_term in entry[0].lower()]
    if matching_entries:
        print("Matching Entries:")
        print_aspect_table(matching_entries)
        delete_entry = input("Do you want to delete an entry for this aspect? (y/n): ")
        if delete_entry.lower() == 'y':
            delete_input = input("Enter the number of the entry to delete (or 'c' to cancel): ")
            if delete_input == 'c':
                return
            try:
                delete_index = int(delete_input)
                if delete_index in range(1, len(matching_entries) + 1):
                    entry_to_delete = matching_entries[delete_index - 1]
                    aspect_details.remove(entry_to_delete)
                    print("Entry deleted successfully.")
                else:
                    print("Invalid entry number.")
            except ValueError:
                print("Invalid input.")
    else:
        print("No matching entries found.")


def create_plain_text_table():
    selected_class = get_user_class()

    if selected_class is None:
        for number, class_name in class_options.items():
            print(f"{number}: {class_name}")

        class_choice = int(input("Enter the number for your class: "))
        selected_class = class_options.get(class_choice)

        with open('user_class.txt', 'w') as file:
            file.write(str(class_choice))
    else:
        print(f"Your current class is: {selected_class}")
        change_class = input("Do you want to change your class? (y/n): ")
        if change_class.lower() == 'y':
            for number, class_name in class_options.items():
                print(f"{number}: {class_name}")

            class_choice = int(input("Enter the number for your class: "))
            selected_class = class_options.get(class_choice)

            with open('user_class.txt', 'w') as file:
                file.write(str(class_choice))

    class_aspects = aspect_names[selected_class]
    general_aspects = aspect_names['General']

    table = ""
    try:
        with open(f'aspects_{selected_class.lower()}.txt', 'r') as file:
            table = file.read().strip()
    except FileNotFoundError:
        pass

    if not table:
        table = "Aspect Name                Dynamic Value 1           Dynamic Value 2\n" \
                "------------------------------------------------------------------------"

    aspect_details = []

    if table:
        rows = table.split('\n')[2:]
        for row in rows:
            aspect_name = row[:28].strip()
            dynamic_value_1 = row[28:56].strip()
            dynamic_value_2 = row[56:].strip()
            aspect_details.append((aspect_name, dynamic_value_1, dynamic_value_2))

    num_aspects_added = len(aspect_details)

    while True:
        print("\nGeneral Aspects:")
        general_aspects_sorted = sorted(general_aspects.values())
        general_aspects_start = 1
        num_general_aspects = len(general_aspects_sorted)
        num_columns = 4
        num_rows = (num_general_aspects + num_columns - 1) // num_columns

        for row in range(num_rows):
            for col in range(num_columns):
                index = row + col * num_rows
                if index < num_general_aspects:
                    aspect_name = general_aspects_sorted[index]
                    number = general_aspects_start + index
                    print(f"{number}: {aspect_name:<25}", end='  ')
            print()

        print()

        print("\nClass Aspects:")
        class_aspects_start = max(general_aspects.keys())
        class_aspects_sorted = sorted(class_aspects.values())
        num_class_aspects = len(class_aspects_sorted)
        num_rows = (num_class_aspects + num_columns - 1) // num_columns

        for row in range(num_rows):
            for col in range(num_columns):
                index = row + col * num_rows
                if index < num_class_aspects:
                    aspect_name = class_aspects_sorted[index]
                    aspect_number = class_aspects_start + index + 1
                    print(f"{aspect_number}: {aspect_name:<25}", end='  ')
            print()

        print('\n')
        aspect_input = input("Enter the number for the aspect (or 's' to search for an aspect, 'd' to delete one of your aspects, 'q' to quit, ): ")
        if aspect_input == 'q':
            break
        elif aspect_input == 'd':
            print_aspect_table(aspect_details)
            delete_input = input("Enter the number of the aspect to delete (or 'c' to cancel): ")
            if delete_input == 'c':
                continue
            try:
                delete_index = int(delete_input)
                if delete_index in range(1, len(aspect_details) + 1):
                    deleted_aspect = aspect_details[delete_index - 1][0]
                    aspect_details = [aspect for aspect in aspect_details if aspect[0] != deleted_aspect]
                    print("Aspect deleted successfully.")
                else:
                    print("Invalid aspect number.")
            except ValueError:
                print("Invalid input.")
            continue
        elif aspect_input == 's':
            search_aspect(aspect_details)
            continue

        aspect_index = int(aspect_input)

        if aspect_index in general_aspects:
            aspect_name = general_aspects[aspect_index]
        elif aspect_index - class_aspects_start in class_aspects:
            aspect_name = class_aspects[aspect_index - class_aspects_start]
        else:
            print("Invalid aspect number. Please try again.")
            continue

        existing_entries = [entry for entry in aspect_details if entry[0] == aspect_name]

        if existing_entries:
            print(f"\nEntries for aspect '{aspect_name}':")
            print_aspect_table(existing_entries)

            delete_entry = input("Do you want to delete an entry for this aspect? (y/n): ")
            if delete_entry.lower() == 'y':
                delete_input = input("Enter the number of the entry to delete (or 'c' to cancel): ")
                if delete_input == 'c':
                    continue
                try:
                    delete_index = int(delete_input)
                    if delete_index in range(1, len(existing_entries) + 1):
                        deleted_entry = existing_entries[delete_index - 1]
                        aspect_details.remove(deleted_entry)
                        print("Entry deleted successfully.")
                    else:
                        print("Invalid entry number.")
                except ValueError:
                    print("Invalid input.")
                continue

        add_new_entry = input(f"Do you want to add a new entry for aspect '{aspect_name}'? (y/n): ")
        if add_new_entry.lower() == 'n':
            continue

        dynamic_value_1 = input(f"Enter the dynamic value for {aspect_name}: ")
        dynamic_value_2 = input("Enter the optional second dynamic value (leave blank if none): ")

        # Validate input as numbers
        if not dynamic_value_1.isdigit():
            print("Invalid input. Dynamic Value 1 must be a number.")
            continue
        if dynamic_value_2 and not dynamic_value_2.isdigit():
            print("Invalid input. Dynamic Value 2 must be a number.")
            continue

        aspect_details.append((aspect_name, dynamic_value_1, dynamic_value_2))

        row = f"{aspect_name.ljust(28)}{dynamic_value_1.ljust(28)}{dynamic_value_2}\n"
        table += row
        num_aspects_added += 1

        if num_aspects_added == 3:
            num_aspects_added = 0

    aspect_details.sort(key=lambda x: x[0])

    sorted_table = "Aspect Name                Dynamic Value 1           Dynamic Value 2\n" \
                   "------------------------------------------------------------------------\n"
    for aspect_detail in aspect_details:
        aspect_name, dynamic_value_1, dynamic_value_2 = aspect_detail
        row = f"{aspect_name.ljust(28)}{dynamic_value_1.ljust(28)}{dynamic_value_2}\n"
        sorted_table += row

    with open(f'aspects_{selected_class.lower()}.txt', 'w') as file:
        file.write(sorted_table)

    print("\nUpdated Table:")
    print(sorted_table)

    return f"aspects_{selected_class.lower()}.txt"


def get_ascii():
    ascii_path = os.path.join(os.path.dirname(__file__), "ascii.txt")
    with open(ascii_path, "r") as file:
        return file.read()


if __name__ == '__main__':
    ascii_art_obj = pyfiglet.Figlet()
    ascii_art = get_ascii()
    print(ascii_art)
    result_file = create_plain_text_table()
    print(f"\nAspect details saved to: {result_file}")
