from csv import DictReader, DictWriter

# Exercise 99
# with open("users.csv", "w") as source:
#     headers = ("First", "Last")
#     dict_writer = DictWriter(source, fieldnames=headers)
#     dict_writer.writeheader()
#
#
# def add_user(first, last):
#      with open("users.csv", "a") as source:
#         headers = ("First", "Last")
#         dict_writer = DictWriter(source, fieldnames=headers)
#         dict_writer.writerow({
#             "First": first,
#             "Last": last
#         })
#
#
# add_user("Orlando", "Garcia")
# add_user("Mawi", "Garcia")
# add_user("Sugma", "Polk")

# Exercise 100
#
# def print_users():
#     with open("users.csv") as source:
#         dict_reader = DictReader(source)
#
#         for row in dict_reader:
#             print(f"{row['First']} {row['Last']}")
#
#
# print_users()
# In Colts code, he uses enumerate which can count things (iterations) for us as opposed to tracking index
# def find_user(first, last):
#     index = 0
#     with open("users.csv", "r") as source:
#         dict_reader = DictReader(source)
#         # Enumerate - Gives us two loop vars, count of the current iteration and value of the current iteration
#         for index, name in enumerate(dict_reader):
#             if name['First'] == first and name['Last'] == last:
#                 return index
#
#         return f"{first} {last} not found!"
#
#
# print(find_user("Mawi", "Garcia"))
# print(find_user("Ligma", "Socks"))
# Exercise 102

#
# def update_users(f, l, first, last):
#     changes = 0
#     with open("users.csv", "r") as source:
#         dict_reader = DictReader(source)
#         rows = list(dict_reader)
#
#     print(rows)
#
#     with open("users.csv", "w") as source:
#         headers = ("First", "Last")
#         dict_writer = DictWriter(source, fieldnames=headers)
#         for row in rows:
#             if row["First"] == f and row["Last"] == l:
#                 dict_writer.writerow({
#                     "First": first,
#                     "Last": last
#                 })
#                 changes += 1
#             else:
#                 dict_writer.writerow({
#                     "First": row["First"],
#                     "Last": row["Last"]
#                 })
#         return f"{changes} records updated"
#
#
# print(update_users("Mawi", "Garcia", "True", "Love"))

# Exercise 103

def delete_users(first, last):
    deletes = 0
    with open("users.csv", "r") as source:
        dict_reader = DictReader(source)
        rows = list(dict_reader)

    print(rows)

    with open("users.csv", "w") as source:
        headers = ("First", "Last")

        dict_writer = DictWriter(source, fieldnames=headers)
        dict_writer.writeheader()

        for row in rows:
            if row["First"] == first and row["Last"] == last:
                deletes += 1
                continue        # Dont need this here since it will break out and go to the next loop anyway
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


print(delete_users("Mawi", "Garcia"))