from csv import DictReader, DictWriter


class CSVExercises:

    # Exercise 99
    def __init__(self):
        """
        Create required CSV file as constructor
        """
        with open("users.csv", "w") as source:
            headers = ("First", "Last")
            dict_writer = DictWriter(source, fieldnames=headers)
            dict_writer.writeheader()

    @staticmethod
    def add_user(first, last):
        """
        Add a users first and last name to the CSV file
        :param first: First name of user
        :param last: Last name of user
        """
        with open("users.csv", "a") as source:
            headers = ("First", "Last")
            dict_writer = DictWriter(source, fieldnames=headers)
            dict_writer.writerow({
                "First": first,
                "Last": last
            })

    # Exercise 100
    @staticmethod
    def print_users():
        """
        Print all users in CSV file
        """
        with open("users.csv") as source:
            dict_reader = DictReader(source)

            for row in dict_reader:
                print(f"{row['First']} {row['Last']}")

    # In Colts code, he uses enumerate which can count things (iterations) for us as opposed to tracking index
    @staticmethod
    def find_user(first, last):
        """
        Find user based on first and last name in CSV
        :param first: First name of target user
        :param last: Last name of target user
        :return: Index in CSV of user or a not found message
        """
        with open("users.csv", "r") as source:
            dict_reader = DictReader(source)
            # Enumerate - Gives us two loop vars, count of the current iteration and value of the current iteration
            for index, name in enumerate(dict_reader):
                if name['First'] == first and name['Last'] == last:
                    return index

            return f"{first} {last} not found!"

    # Exercise 102
    @staticmethod
    def update_users(first, last, first_replacement, last_replacement):
        """
        Update users matching f and l in CSV file, replace with first and last name
        :param f: First name of target user
        :param l: Last name of target user
        :param first: First name of replacement name
        :param last: Last name of replacement name
        :return: # Of changes made to the CSV
        """
        changes = 0
        with open("users.csv", "r") as source:
            dict_reader = DictReader(source)
            rows = list(dict_reader)

        with open("users.csv", "w") as source:
            headers = ("First", "Last")
            dict_writer = DictWriter(source, fieldnames=headers)
            for row in rows:
                if row["First"] == first and row["Last"] == last:
                    dict_writer.writerow({
                        "First": first_replacement,
                        "Last": last_replacement
                    })
                    changes += 1
                else:
                    dict_writer.writerow({
                        'First': row['First'],
                        'Last': row['Last']
                    })

            return f"{changes} records updated"

    # Exercise 103
    @staticmethod
    def delete_users(first, last):
        """
        Delete users in CSV file matching first and last name
        :param first: First name of target user
        :param last: Last name of target user
        :return: # of records deleted
        """
        deletes = 0
        with open("users.csv", "r") as source:
            dict_reader = DictReader(source)
            rows = list(dict_reader)

        with open("users.csv", "w") as source:
            headers = ("First", "Last")

            dict_writer = DictWriter(source, fieldnames=headers)
            dict_writer.writeheader()

            for row in rows:
                if row["First"] == first and row["Last"] == last:
                    deletes += 1
                    continue  # Dont need this here since it will break out and go to the next loop anyway
                else:
                    dict_writer.writerow({
                        "First": row["First"],
                        "Last": row["Last"]
                    })
            # Alernative code for what i wrote
            # for row in rows:
            #     if row["First"] == first and row["Last"] == last:
            #         deletes += 1
            #         continue
            #
            #     dict_writer.writerow({
            #         "First": row["First"],
            #         "Last": row["Last"]
            #     })

            return f"{deletes} records deleted"


CSVExercises()
print('\n' + '*' * 8 + ' Adding users ' + '*' * 8)
CSVExercises.add_user("Orlando", "Garcia")
CSVExercises.add_user("Rob", "Garcia")
CSVExercises.add_user("Sugma", "Polk")

print('\n' + '*' * 8 + ' Finding users ' + '*' * 8)
print(CSVExercises.find_user("Rob", "Garcia"))
print(CSVExercises.find_user("Ligma", "Socks"))

print('\n' + '*' * 8 + ' Deleting users ' + '*' * 8)
print(CSVExercises.delete_users("Rob", "Garcia"))

print('\n' + '*' * 8 + ' Printing users ' + '*' * 8)
CSVExercises.print_users()

print('\n' + '*' * 8 + ' Updating users ' + '*' * 8)

print(CSVExercises.update_users("Rob", "Garcia", "True", "Love"))
