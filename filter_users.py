import json


def filter_users_by_name(name):
    """function for filtering out users by name"""
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("No users.json found")
        return
    except Exception as error:
        print(f"The error was {error}.")
        return

    try:
        filtered_users = [user for user in users if user["name"].lower() == name.lower()]

        if filtered_users:
            for user in filtered_users:
                print(user)
        else:
            print(f"No user with the name *{name}* found. Check your spelling and try again")

    except Exception as error:
        print(f"The error was {error}")


def filter_users_by_age(age):
    """function for filtering out users by age"""
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("No users.json found")
        return
    except Exception as error:
        print(f"The error was {error}.")
        return

    try:
        filtered_users = [user for user in users if int(user["age"]) >= age]

        if filtered_users:
            for user in filtered_users:
                print(user)
        else:
            print(f"No user with the given age cut-off {age} years and above found")
    except Exception as error:
        print(f"The error was {error}")


def filter_users_by_email(email):
    """function for filtering out users by email"""
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("No users.json found")
        return
    except Exception as error:
        print(f"The error was {error}.")
        return

    try:
        filtered_users = [user for user in users if user["email"].lower() == email.lower()]

        if filtered_users:
            for user in filtered_users:
                print(user)
        else:
            print(f"No user with *{email}* found. Check your spelling and try again")

    except Exception as error:
        print(f"The error was {error}")


if __name__ == "__main__":
    try:
        filter_option = input("What would you like to filter by? (Currently, 'name', 'age' "
                              "and 'email' are supported): ").strip().lower()

        if filter_option == "name":
            name_to_search = input("Enter a name to filter users: ").strip()
            filter_users_by_name(name_to_search)
        elif filter_option == "age":
            age_to_search = int(input("Enter the age (a number: 0 and above) to filter users: ").strip())
            filter_users_by_age(age_to_search)
        elif filter_option == "email":
            email_to_search = input("Enter the email (name@example.com) to filter users: ").strip()
            filter_users_by_email(email_to_search)
        else:
            print("Filtering by that option is not yet supported. Check your input.")

    except ValueError as e:
        print(f"The error was a value-error {e}. Try again.")
    except Exception as e:
        print(f"The error was {e}")
